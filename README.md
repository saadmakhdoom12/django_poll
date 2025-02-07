# Django Polls Application

A simple polls application built with Django, allowing users to create and
vote on polls.

## Setup

1. Clone the repository:

```bash
git clone git@github.com:saadmakhdoom12/django_poll.git
cd django_poll
```

2. Install Poetry (if not already installed):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies using Poetry:

```bash
poetry install
```

4. Activate the Poetry shell:

```bash
poetry shell
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

## Features

- Create and manage polls
- Vote on polls
- View poll results
- Admin interface for poll management

## Project Structure

```bash
django_poll/
├── manage.py
├── polls/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
└── mysite/
    ├── settings.py
    └── urls.py
```

## License

This project is licensed under the MIT License.
