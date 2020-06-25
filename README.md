# Django REST API

## Features
###  Django

- Add JWT Authentication to your API.
  - Install needed libraries in project configuration and/or site settings.
- Keep existing authentication so DRF Browsable API still usable.
  - That includes keeping the styling
  - Install needed libraries in project configuration and/or site settings.

### Docker

- Create a boilerplate Dockerfile and docker-compose.yml so you don’t need to start from scratch each time.
- Switch to using Gunicorn instead of Django’s built in development server.
  - mind the number of workers to avoid sluggishness
- Warning You will run into styling issues when you switch over to Gunicorn.
  - On Django side you’ll need to properly handle static files.
- Adjust docker-compose.yml so that data is persisted in a volume outside of container.



# Pull Request
[PR #1](https://github.com/eugenemonnier/drf-auth/pull/1)