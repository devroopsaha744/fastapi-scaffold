# fastapi-scaffold

[![PyPI Version](https://img.shields.io/pypi/v/fastapi-scaffold.svg)](https://pypi.org/project/fastapi-scaffold/)
[![Python Version](https://img.shields.io/badge/python-%3E=3.7-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

fastapi-scaffold is a CLI tool that generates a scalable FastAPI project template with advanced features including authentication, machine learning endpoints, background tasks, caching, rate limiting, and more.

## Installation

Install the CLI tool via pip:

```sh
pip install fastapi-scaffold
```

## Usage

### Create a New FastAPI Project

To create a new project, run:

```sh
fastapi-scaffold create my_project
```

This command generates a new project with optional features:

- `--ml` → Includes machine learning endpoints and model setup.
- `--db` → Adds database configuration and ORM setup.
- `--auth` → Includes authentication endpoints.
- `--docker` → Generates Dockerfile and docker-compose.yml for container support.

Example:

```sh
fastapi-scaffold create my_project --ml --db --auth --docker
```

### Install Project Dependencies

After generating your project, navigate into the project directory and install dependencies:

```sh
fastapi-scaffold install
```

Alternatively, run:

```sh
pip install -r requirements.txt
```

### Delete an Existing Project

To delete a project directory, use:

```sh
fastapi-scaffold delete my_project
```

## Project Structure

A generated project will have the following structure:

```
my_project/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── items.py
│   │   ├── admin.py
│   │   ├── ml.py
│   │   └── health.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── item.py
│   │   ├── ml.py
│   │   └── stats.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── item.py
│   │   └── ml_model.pkl
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── item.py
│   │   └── stats.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── tasks.py
│   │   └── ml.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   ├── cache.py
│   │   └── rate_limit.py
│   ├── middleware.py
│   ├── database.py
│   ├── auth.py
│   ├── logger.py
│   ├── config.py
│   └── main.py
├── tests/
│   ├── test_main.py
│   └── test_users.py
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Running the Project

1. Navigate to the project directory:
    ```sh
    cd my_project
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Start the FastAPI server:
    ```sh
    uvicorn app.main:app --reload
    ```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
