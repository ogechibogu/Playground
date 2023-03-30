#!/usr/bin/env bash

VERSION="0.1.37"

NAME=sr-ssp
REGISTRY=nexus.srinternal.net:9082

docker build --platform=linux/amd64 --pull -t ${REGISTRY}/${NAME}:${VERSION} .
if [ "${1}" = "push" ]
then
  docker push ${REGISTRY}/${NAME}:${VERSION}
fi
