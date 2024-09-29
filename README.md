# URL Shortening Service

## Overview

This URL Shortening Service allows users to create shorter aliases for long URLs. It is designed to be simple to use but also powerful enough to handle significant traffic and provide analytics on URL usage. Features include creating, retrieving, updating, destroying, and redirecting URLs based on a shortcode. Additionally, it tracks how many times a URL is accessed via its shortened version.

## Features

- **Create Short URLs**: Generate a short alias for a long URL.
- **Retrieve URLs**: Fetch details about a shortened URL.
- **Update URLs**: Update the URL details.
- **Delete URLs**: Remove a shortened URL.
- **Redirect**: Automatically redirects to the original URL when the short URL is accessed.
- **Analytics**: Track how many times each URL is accessed.

## Prerequisites

Before you can run this project, you'll need the following installed:

- Python (3.8 or newer)
- Django (3.1 or newer)
- Django REST Framework
- A database supported by Django, such as SQLite, MySQL, or PostgreSQL.

## Installation Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Ivan-G0nzalez/UrlShortener
cd your-repository
```

### 2. Set Up a Virtual Environment

```bash
python -m venv env

# Activate the virtual environment
# On Windows
env\Scripts\activate

# On Unix or MacOS
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

Run migrations to set up your database:

```bash
python manage.py migrate
```

### 5. Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

Now, the server should be running at http://localhost:8000/.

<br>

Roadmap from: https://roadmap.sh/projects/url-shortening-service
