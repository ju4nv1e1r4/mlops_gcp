FROM python:3.11

ARG BASIC_AUTH_USERNAME_ARG
ARG BASIC_AUTH_PASSWORD_ARG

ENV BASIC_AUTH_USERNAME=BASIC_AUTH_USERNAME_ARG
ENV BASIC_AUTH_PASSWORD=BASIC_AUTH_PASSWORD_ARG

COPY ./requirements.txt /usr/requirements.txt

WORKDIR /usr

RUN pip install -r requirements.txt

COPY ./mlops_gcp /usr/mlops_gcp

ENTRYPOINT [ "python3" ]

CMD [ "mlops_gcp/main.py" ]