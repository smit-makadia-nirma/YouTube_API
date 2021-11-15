
# YouTube API

Django based API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.
## Features

- Cronjob setup that calls the API every 5 mins.
- GET API that shows the entries in a paginated form
- Interface to search and filter the responses/ db entries.
- Multiple API keys to automatically use the next available key.
- Admin dashboard to view cron logs and stored API responses in Video model.
## Run Locally

- Clone the project

```bash
  git clone https://github.com/smitmakadia/YouTube_API.git
```

- To install Requirements

```bash
  pip install -r requirements.txt
```

- Personalize your search query and add your API key to API_KEYS in settings.py file.  

- In order to create and apply migration run :

```bash
  python manage.py makemigrations
  python manage.py migrate
```

- Start the server

```bash
  python manage.py runserver
```

- Put Following link in browser

```bash
  http://127.0.0.1:8000/
```

- To run cronjob in console

```bash
  python manage.py runcrons
```




## Screenshots

![920](https://github.com/smitmakadia/YouTube_API/blob/main/Screenshots/920.png)

![921](https://github.com/smitmakadia/YouTube_API/blob/main/Screenshots/921.png)

![917](https://github.com/smitmakadia/YouTube_API/blob/main/Screenshots/917.png)

![918](https://github.com/smitmakadia/YouTube_API/blob/main/Screenshots/918.png)

![919](https://github.com/smitmakadia/YouTube_API/blob/main/Screenshots/919.png)


## Tech Stack

**Technologies:** Django-REST framework, YouTube data v3 API. 
**Language:** Python 3.8.2

## References

 - [YouTube API Documentaion](https://developers.google.com/youtube/v3/docs/search/list)
 - [YouTube data v3 API](https://developers.google.com/youtube/v3/getting-started)
 - [Django REST Framework](https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-generic-class-based-views) for the interface.
 - [Django-cron](https://django-cron.readthedocs.io/en/latest/installation.html) lets you run Django/Python code on a recurring basis proving basic plumbing to track and execute tasks.
 - [Django filter](https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html#quickstart) for search and filtering features.
