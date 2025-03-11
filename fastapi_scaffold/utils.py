import os
from pathlib import Path

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
