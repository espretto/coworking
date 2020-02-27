# derive
FROM python:3.6

# position
WORKDIR /backend
COPY ./Pipfile* ./

# provision (do not venv for ease of access to pip-installed executables)
RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

# run using `docker-compose up backend`
