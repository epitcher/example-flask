# example-flask

A simple Flask web application

## Prerequisites

- Python 3+
- Docker (optional)
- pyenv (optional)

## Getting Started

There are two ways to set up and run this project:

### Option 1: Using Docker Compose

1. Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/), if not already installed.

2. Clone the repository:
```bash
git clone https://github.com/epitcher/example-flask.git
```

3. Change to the project directory:
```bash
cd simple-flask-project
```

4. Run the application with Docker Compose:
```bash
docker-compose up
```


### Option 2: Running Locally

1. Ensure you have Python 3+ installed. You can check the Python version by running:

```bash
python --version
```


If you don't have Python 3, you can download it from the [official website](https://www.python.org/downloads/).

2. Clone the repository:
```bash
git clone https://github.com/epitcher/example-flask.git
```

3. Change to the project directory:
```bash
cd example-flask
```

4. Install the required packages:
```bash
python -m pip install -r requirements.txt
```


5. Run the application:
```
python run.py
```


## Usage

Open your web browser and navigate to `http://localhost:5000`. You should see the homepage with an "Upload file" button. Click the button to upload a file.

## Helpful

### Coverage
- `python -m coverage run -m pytest && python -m coverage report`
- `python -m coverage report`

## License

This project is licensed under the MIT License. <!--- See the [LICENSE](LICENSE) file for details. -->



