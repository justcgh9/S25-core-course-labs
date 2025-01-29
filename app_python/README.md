# Moscow Time Web App

This is a python application built with FastAPI and jinja2 to display current time in Moscow.

## Features

- Displays Moscow time
- Renders HTML dynamically using jinja2

## Requirements

- Python 3.12.7 (built and tested on this version)
- `pip` package manager

## Installation

1. Clone the repo:

    ```bash
    git clone https://github.com/justcgh9/S25-core-course-labs.git
    cd S25-core-course-labs/app_python
    ```

2. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the run.sh script:

    ```bash
    bash run.sh
    ```

2. Visit the page in the browser by this url:

    ```bash
    http://localhost:8080/
    ```

## Docker

This is an instruction for running the application in a docker container

First of all, there is a choice: to build or to pull the image.
After that you will be able to run this image in a docker container

### Build the image

There is a [Dockerfile](/app_python/Dockerfile) in this project. To build the image use this script

```bash
docker build -t moscow-time-app .
```

### Pull the image

Alternative approach: pull the image from the dockerhub

```bash
docker pull justcgh/moscow-time-app:latest
```

### Run the image

If you built the image use this script:

```bash
docker run -p 8080:8080 moscow-time-app
```

If you pulled it:

```bash
docker run -p 8080:8080 justcgh/moscow-time-app:latest
```
