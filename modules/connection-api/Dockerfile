FROM python:3.9.9-alpine3.15

WORKDIR .

RUN apk add --no-cache gcc g++ musl-dev libffi-dev linux-headers geos libc-dev postgresql-dev librdkafka-dev
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]