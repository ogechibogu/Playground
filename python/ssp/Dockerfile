FROM node:12.16.2-stretch as builder

COPY ui /project/ui

RUN cd /project/ui && npm install && npm run-script build

FROM python:3.7-buster
RUN apt-get clean
RUN apt-get update && apt-get -y upgrade && apt-get -y install vim

COPY app /opt/ssp/app
COPY manage.py /opt/ssp/
RUN pip install -r /opt/ssp/app/requirements.txt

COPY --from=builder /project/ui/dist /opt/ssp/ui/dist

CMD python /opt/ssp/manage.py run
