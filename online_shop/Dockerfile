FROM python

WORKDIR /online_shop

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    && apt-get install netcat-traditional -y
RUN apt-get upgrade -y && apt-get install -y postgresql gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/src/online_shop/entrypoint.sh"]
