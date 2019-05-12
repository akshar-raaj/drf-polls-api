Run with Docker

    docker build -t django-polls .
    docker run -p 8000:8000 --env-file env.list django-polls
