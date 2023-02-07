FROM python:3.8-alpine
ARG DB_USR
ENV DB_USR=$DB_USR
ARG DB_PASS
ENV DB_PASS=$DB_PASS
COPY . /code
WORKDIR /code/project
RUN pip install -r requirements.txt
RUN chmod 644 rest_app.py
EXPOSE  5000
CMD ["sh", "-c", "python rest_app.py $DB_USR $DB_PASS"]