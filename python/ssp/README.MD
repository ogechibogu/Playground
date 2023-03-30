Backend
=======

Python APP
---------
Run:
```python
manage.py run
```
Tests:
```python
manage.py test
```
LDAP
----
```bash
cd ssp/ldap
./run_ldap.sh
```

Frontend
========

To avoid instalation node and all dependecies:

Development
```python
cd ssp/ui
docker run --rm --name node -it -w /project -v $(pwd):/project -p8080:8080 node:12.16.2-stretch bash
npm run-script dev
```
Build for production static JS
```bash
cd ssp/ui
docker run --rm --name node -it -w /project -v $(pwd):/project -p8080:8080 node:12.16.2-stretch bash
npm run-script build
```