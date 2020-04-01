# Stop COVID Backend

## Development environment

Install Docker, then run:

    $ docker-compose up --build

This will boot up everything that your app needs to run.

(Note: the `--build` argument is not required, but will ensure the Python and JS dependencies are always up-to-date.)

In another console, run these commands to set up the database and set up a user:

    $ docker-compose run web ./manage.py migrate
    $ docker-compose run web ./manage.py createsuperuser

The local development environment is now running at [http://localhost:8000](http://localhost:8000). The admin interface is at [http://localhost:8000/admin/](http://localhost:8000/admin/), accessible with the user/pass created above.

## Tests

To run the test suite:

    $ docker-compose run web ./manage.py test

## Deployment on Heroku

This app is designed to be deployed on Heroku.

These commands, roughly, will get you set up with an app. Replace `stopcovid-production` with a name for the app:

```
$ heroku update beta
$ heroku plugins:install @heroku-cli/plugin-manifest
$ heroku apps:create --manifest --no-remote --stack=container stopcovid-production
$ heroku config:set -a stopcovid-production SECRET_KEY=$(openssl rand -hex 64)
```

In the Heroku web UI, go to the app, then the "Deploy" tab, then connect it to a GitHub repo. Then, click "Deploy branch" at the bottom to trigger a deploy. `./manage.py migrate` will be run on deploy.

On this page, you can also set up automatic deploys if you want. You probably want to check "Wait for CI to pass before deploy".
