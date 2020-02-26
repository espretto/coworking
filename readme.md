# Co-working Space

This is a showcase project to bring together a number of different technologies in a hexagonal architecture.

## Roadmap

- [ ] develop application features
  - [x] represent offices, reservations and clients
  - [x] design and implement a rest-api for them
  - [ ] connect to kafka/rabbitmq message broker
  - [ ] offload pdf bill generation to worker queue
  - [ ] mount document storage for authenticated uploads
- [ ] frontend views
  - [x] about page presenting the project
  - [ ] registration and authentication functionality
  - [x] map view with markers for local workspaces
  - [x] overview: tabular calendar for office/desk reservations
  - [ ] detailed view: reservation, office
- [ ] setup CI to automate the following tasks
  - [x] linting flake8
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
  - [x] postgresql database
    - [x] generate fixtures with [mockaroo](https://mockaroo.com/)
    - [ ] create indices where necessary
    - [ ] duplicate the instance setup log-sharing
  - [ ] message/task broker
  - [ ] worker instance[s] to offload tasks
    - [ ] automate process restart on error
- [ ] setup storage cluster for data volumes (SCSI)
- [ ] make the number of workers adapt to the number of tasks
- [ ] test behaviour of component outage

## Issues

- [ ] do not expose object ids but, use slugs where available

## Resources
- task queue: https://adamj.eu/tech/2020/02/03/common-celery-issues-on-django-projects/

## Notes
Geographic centre: 47.21627/-1.54936
