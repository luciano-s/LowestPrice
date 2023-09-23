# pull official base image
FROM python:3.10.9

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt -y install
RUN apt -y install python3-dev libpq-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000