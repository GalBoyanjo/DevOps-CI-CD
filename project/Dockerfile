FROM python:3.7-alpine
COPY . /code
WORKDIR /code/project
RUN pip install -r requirements.txt
RUN chmod 644 rest_app.py
CMD ["python", "rest_app.py"]