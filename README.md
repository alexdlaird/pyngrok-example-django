[![Build](https://img.shields.io/github/actions/workflow/status/alexdlaird/pyngrok-example-django/build.yml)](https://github.com/alexdlaird/pyngrok-example-django/actions/workflows/build.yml)
![GitHub License](https://img.shields.io/github/license/alexdlaird/pyngrok-example-django)

# pyngrok Example - Django

This is an example project that shows how to easily integrate [`pyngrok`](https://github.com/alexdlaird/pyngrok)
with [Django](https://docs.djangoproject.com/en/), as [summarized in the docs](https://pyngrok.readthedocs.io/en/latest/integrations.html#django).

## Running

To run the example locally, install its dependencies, then start the dev server with `USE_NGROK` set to open a
tunnel. The tunnel's public URL is printed when the server starts.

```sh
make install
USE_NGROK=True NGROK_AUTHTOKEN=$NGROK_AUTHTOKEN venv/bin/python manage.py runserver
```

To run the tests, use `make test`.