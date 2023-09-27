
FROM ubuntu

COPY ./ ./

RUN ls -lha
 
## install python3

RUN set -xe \
    && apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip

## install rytr api situation

RUN set -xe \
    && pip install flask \
    && pip install flask_cors

## On Container start, run the Python API file

CMD ["python3", "card-players-unite-registration-api.py"]
