# derive: https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.6-slim

# position
WORKDIR /backend
COPY ./Pipfile* ./

# provision (do not venv for ease of access to pip-installed executables)
RUN pip install pipenv && \
    pipenv lock --requirements > requirements.txt && \
    pip install -r requirements.txt

# run using `docker-compose up backend`
