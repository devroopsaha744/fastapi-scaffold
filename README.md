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

To create a new FastAPI project, use the following command:

```sh
fastapi-scaffold create my_project
```

This will generate a basic FastAPI project structure inside the `my_project` directory.

### Options

You can customize the generated project using the following flags:

```sh
fastapi-scaffold create my_project --ml --db --auth --docker
```

- `--ml` → Includes boilerplate for integrating ML models
- `--db` → Adds database configuration and ORM setup
- `--auth` → Includes authentication (OAuth, JWT, etc.)
- `--docker` → Generates a `Dockerfile` and `docker-compose.yml`

## Project Structure

A generated FastAPI project will follow this structure:

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

After creating the project, navigate to your project directory and install dependencies:

```sh
cd my_project
pip install -r requirements.txt
```

Then, start the FastAPI application:

```sh
uvicorn app.main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Contributing

Contributions are welcome! If you find a bug or want to request a feature, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

