import os
import click
from pathlib import Path
from .templates import TEMPLATE

@click.group()
def cli():
    """FastAPI CLI Tool"""
    pass

@cli.command()
@click.argument("project_name")
@click.option("--ml", is_flag=True, help="Include ML model serving")
@click.option("--db", is_flag=True, help="Include database setup")
@click.option("--auth", is_flag=True, help="Include authentication")
@click.option("--docker", is_flag=True, help="Include Docker support")
def create(project_name, ml, db, auth, docker):
    """Create a FastAPI project with optional components"""

    project_path = Path(project_name)
    if project_path.exists():
        click.echo(f"❌ Directory {project_name} already exists.")
        return
    
    click.echo(f"🚀 Creating FastAPI project: {project_name}")

    # Copy template
    custom_template = TEMPLATE.copy()

    # Remove unwanted files
    if not ml:
        custom_template["app"]["api"].pop("ml.py", None)
        custom_template["app"]["models"].pop("model.pkl", None)
    if not db:
        custom_template["app"].pop("database.py", None)
    if not auth:
        custom_template["app"].pop("auth.py", None)
    if not docker:
        custom_template.pop("Dockerfile", None)
        custom_template.pop("docker-compose.yml", None)

    # Generate project files
    create_structure(project_path, custom_template)

    click.echo(f"✅ FastAPI project '{project_name}' created successfully!")

def create_structure(base_path, template):
    """Recursively creates directories and files from template"""
    for name, content in template.items():
        path = base_path / name
        if isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)

if __name__ == "__main__":
    cli()
