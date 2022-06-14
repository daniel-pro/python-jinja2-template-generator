# Python program to generate code from Jinja2 templates

## Installation

To install the latest stable release (v2.0 as of now):
```sh
wget https://github.com/daniel-pro/python-jinja2-template-generator/archive/v2.0.tar.gz
tar zxvf v2.0.tar.gz
```

Otherwise if you want to use the development branch (at your own risk): 

```sh
git clone https://github.com/daniel-pro/python-jinja2-template-generator.git
```

Create the Docker container image :

```sh
cd python-jinja2-template-generator/
docker build -t dpro/ptyg:2.0 .
```

Run the Docker container :
```sh
docker run --rm --mount type=bind,source=/tmp,target=/app/wdir dpro/ptyg:1.0 python ptyg.py gen /app/wdir/input.yaml /app/wdir/input.template /app/wdir/output.out
```

## Dependencies
Although you don't need them if you use the containerized version, these are the script's dependencies:
1. pathlib
2. pyyaml
3. jinja2
