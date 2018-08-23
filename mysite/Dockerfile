FROM python:2.7
RUN mkdir /code
WORKDIR /code
ADD . /code
EXPOSE 8000:8000
RUN pip install django
CMD ["python", "manage.py", "runserver"]
