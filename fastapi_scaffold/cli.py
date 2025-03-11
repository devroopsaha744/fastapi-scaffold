import os
import click
import copy
import subprocess
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
@click.option("--host", default="127.0.0.1", help="Host address")
@click.option("--port", default=8000, help="Port number")
def serve(host, port):
    """Run the API server using uvicorn."""
    cmd = ["uvicorn", "app.main:app", "--host", host, "--port", str(port)]
    click.echo(f"🚀 Starting API server at http://{host}:{port}")
    subprocess.run(cmd)

@cli.command()
def install():
    """Install project dependencies from requirements.txt."""
    requirements = Path("requirements.txt")
    if not requirements.exists():
        click.echo("❌ requirements.txt not found in current directory.")
        return
    click.echo("📦 Installing dependencies...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    click.echo("✅ Dependencies installed successfully!")

@cli.command()
def test():
    """Run the test suite using pytest."""
    click.echo("🔍 Running tests...")
    subprocess.run(["pytest"])

@cli.command()
def info():
    """Display CLI tool information."""
    click.echo("FastAPI CLI Tool")
    click.echo("Version: 1.0.0")
    click.echo("A tool to create and manage FastAPI projects.")

@cli.command()
@click.argument("directory", default=".")
def clean(directory):
    """Clean __pycache__ directories in the specified directory."""
    click.echo(f"🧹 Cleaning __pycache__ in {directory}...")
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            if d == "__pycache__":
                pycache_path = os.path.join(root, d)
                subprocess.run(["rm", "-rf", pycache_path])
    click.echo("✅ Cleaned __pycache__ directories.")

if __name__ == "__main__":
    cli()
