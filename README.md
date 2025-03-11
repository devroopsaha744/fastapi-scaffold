### Updates to Make:

#### 1. **Version Bump in `setup.py`**
Since you added commands and modified the template, update the version:
```python
version="0.2.0",
```

#### 2. **Update README.md to Reflect New CLI Commands**
Your `cli.py` now includes:
- `serve` (Runs the API)
- `install` (Installs dependencies)
- `test` (Runs tests)
- `info` (Shows CLI details)
- `clean` (Removes `__pycache__`)

Modify the README to mention these commands.

---

### **Updated README.md**
```md
# FastAPI Scaffold

[![PyPI Version](https://img.shields.io/pypi/v/fastapi-scaffold.svg)](https://pypi.org/project/fastapi-scaffold/)
[![Python Version](https://img.shields.io/badge/python-%3E=3.7-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

FastAPI Scaffold is a CLI tool to quickly generate FastAPI project structures with optional features like authentication, database integration, machine learning model setup, and Docker support.

## Installation

To install FastAPI Scaffold, run:

```sh
pip install fastapi-scaffold
```

## Usage

To create a new FastAPI project, use:

```sh
fastapi-scaffold create my_project
```

This generates a FastAPI project in `my_project/`.

### Options

Customize the generated project using:

```sh
fastapi-scaffold create my_project --ml --db --auth --docker
```

- `--ml` → Includes ML model boilerplate  
- `--db` → Adds database setup  
- `--auth` → Includes authentication  
- `--docker` → Adds Docker support  

### Additional Commands

- **Run API server:**  
  ```sh
  fastapi-scaffold serve --host 0.0.0.0 --port 8000
  ```
  
- **Install dependencies:**  
  ```sh
  fastapi-scaffold install
  ```

- **Run tests:**  
  ```sh
  fastapi-scaffold test
  ```

- **View CLI info:**  
  ```sh
  fastapi-scaffold info
  ```

- **Clean `__pycache__`:**  
  ```sh
  fastapi-scaffold clean
  ```

## Project Structure

A generated project follows this structure:

```
my_project/
│── app/
│   ├── main.py
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── db.py (if --db is used)
│   ├── auth.py (if --auth is used)
│── tests/
│── .env
│── Dockerfile (if --docker is used)
│── requirements.txt
│── README.md
```

## Running the Project

```sh
cd my_project
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Contributing

Contributions welcome! Open an issue or PR.

## License

MIT License. See [LICENSE](LICENSE).

