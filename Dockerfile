# FROM python:3.9 as core
#
# COPY ./core/requirements.txt ./requirements.txt
# RUN pip install -r requirements.txt
#
# WORKDIR /app
#
# COPY ./core .
# RUN python ./initialization.py
#
# FROM python:3.9
#
# COPY ./api/requirements.txt ./requirements.txt
# RUN pip install -r requirements.txt
#
# WORKDIR /app
# COPY ./api .
#
# COPY --from=core /app/engine.pickle /app/engine.pickle
#
# EXPOSE 9999
# ENTRYPOINT ["python", "service_manager.py"]
FROM python:3.9 as build

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

RUN mkdir -p /app/cache && chmod -R 777 /app/cache

ENV TRANSFORMERS_CACHE=/app/cache

EXPOSE 9999
ENTRYPOINT ["python", "run.py"]
