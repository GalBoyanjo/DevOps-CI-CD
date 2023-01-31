FROM python:3.7-alpine
COPY project/ /code
WORKDIR /code
RUN pip install project/requirements.txt
RUN chmod 644 rest_app.py
CMD ["python", "rest_app.py"]