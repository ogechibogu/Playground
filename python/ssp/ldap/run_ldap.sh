#!/usr/bin/env bash
docker build -t ldap .
docker run --rm -it --name ldap-server -p 389:389 ldap