FROM python:3.6-jessie

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./src/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -i https://pypi.doubanio.com/simple -r requirements.txt

COPY ./src /usr/src/app

CMD ["celery", "-A", "src", "worker", "-l", "info"]
# CMD ["python"]
# celery -A src worker -l info
