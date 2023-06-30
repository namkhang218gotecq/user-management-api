FROM python:3.9

RUN mkdir backend

COPY submission/user-management backend/app/user-management
COPY lib backend/lib
COPY make backend/app/user-management/.makelib
COPY env/develop backend/app/user-management/env

WORKDIR /backend/app/user-management

RUN pip install --upgrade pip
RUN pip install -r requirements.txt -r requirements.dev.txt
RUN pip install coloredlogs



CMD ["make", "run"]