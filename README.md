# Instructions:

- On first run, make sure you run django migrations (`python manage.py makemigrations` `python manage.py migrate`)
- Replace placeholders in `.env.example` with your API keys and rename to `.env`
- Run `python manage.py sync-action-network` to pull the events
- Run local server with `python manage.py runserver`
- View calendar at http://localhost:8000/events