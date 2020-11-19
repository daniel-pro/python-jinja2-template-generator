
FROM python:3.7-alpine


# Labels
LABEL maintainer="daniel.procopio@gmail.com"
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.description="Python script to generate stuff from Jinja2 Templates and YAML files"
LABEL org.label-schema.docker.cmd="docker run --rm --mount type=bind,source=/tmp,target=/app python ptyg.py gen /app/input/input.yaml /app/input/input.template /app/output/generated.out"

COPY app /app

RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD [ "python", "ptyg.py" ]
