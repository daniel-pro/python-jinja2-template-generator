# Python program to generate code from Jinja2 templates

## Installation

Clone the repo :

```sh
git clone https://github.com/daniel-pro/python-jinja2-template-generator.git
```

Create the Docker container image :

```sh
cd python-jinja2-template-generator/
docker build -t dpro/ptyg:1.0 .
```

Run the Docker container :
```sh
docker run --rm --mount type=bind,source=/tmp,target=/app/wdir dpro/ptyg:1.0 python ptyg.py /app/wdir/input.yaml /app/wdir/input.template /app/wdir/output.out
```

## Dependencies
Although you don't need them if you use the containerized version, these are the script's dependencies:
1. pathlib
2. pyyaml
3. jinja2
