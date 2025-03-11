import os
import click
import copy
from pathlib import Path
from .templates import TEMPLATE
from .utils import create_structure

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
    """Create a new FastAPI project."""
    project_path = Path(project_name)
    if project_path.exists():
        click.echo(f"❌ Directory {project_name} already exists.")
        return
    click.echo(f"🚀 Creating FastAPI project: {project_name}")
    custom_template = copy.deepcopy(TEMPLATE)
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
    create_structure(project_path, custom_template)
    click.echo(f"✅ FastAPI project '{project_name}' created successfully!")

@cli.command()
def install():
    """Install project dependencies from requirements.txt."""
    requirements = Path("requirements.txt")
    if not requirements.exists():
        click.echo("❌ requirements.txt not found in current directory.")
        return
    click.echo("📦 Installing dependencies...")
    os.system("pip install -r requirements.txt")
    click.echo("✅ Dependencies installed successfully!")

@cli.command()
@click.argument("project_name")
def delete(project_name):
    """Delete an existing FastAPI project."""
    project_path = Path(project_name)
    if not project_path.exists():
        click.echo(f"❌ Directory {project_name} does not exist.")
        return
    click.echo(f"🗑️ Deleting project: {project_name}")
    os.system(f"rm -rf {project_name}")
    click.echo(f"✅ Project '{project_name}' deleted successfully!")

if __name__ == "__main__":
    cli()
