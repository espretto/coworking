# Hôtel Bleu

This is a showcase project to bring together a number of different technologies in a hexagonal architecture.

## Roadmap

- [ ] develop application features
  - [ ] represent hotel rooms, reservations and guests
  - [ ] design and implement a rest-api for them
  - [ ] connect to kafka message broker
  - [ ] offload pdf bill generation to worker queue
  - [ ] mount document storage for authenticated uploads
- [ ] frontend views
  - [ ] home page presenting the project
  - [ ] registration and authentication functionality
  - [ ] overview: tabular calendar for room reservations
  - [ ] detailed view: reservation, room
- [ ] setup CI to automate the following tasks
  - [ ] linting flake8
  - [ ] quality control with [lumnify](https://lumnify.com/)
  - [ ] unit/integration tests
  - [ ] test coverage reports
  - [ ] performance regression tests
- [ ] dockerize the following containers
  - [ ] production server for django application
  - [ ] nginx front server
    - [ ] reverse-proxy for api-calls
    - [ ] serve static files for client interface
    - [ ] serve file uploads and authenticate using [nginx auth module](http://nginx.org/en/docs/http/ngx_http_auth_request_module.html)
  - [ ] postgresql database
    - [ ] generate fixtures with [mockaroo](https://mockaroo.com/)
    - [ ] create indices where necessary
    - [ ] duplicate the instance setup log-sharing
  - [ ] message/task broker
  - [ ] worker instance[s] to offload tasks
    - [ ] automate process restart on error
- [ ] setup storage cluster for data volumes (SCSI)
- [ ] make the number of workers adapt to the number of tasks
- [ ] test behaviour of component outage


## Resources
- task queue: https://adamj.eu/tech/2020/02/03/common-celery-issues-on-django-projects/