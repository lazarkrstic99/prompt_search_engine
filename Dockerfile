FROM python:3.9 AS install
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

COPY ./api/requirements.txt ./api/requirements.txt
RUN pip install --user -r ./api/requirements.txt

COPY ./core/requirements.txt ./core/requirements.txt
RUN pip install --user -r ./core/requirements.txt

##################################################################
FROM python:3.9 AS setup
COPY --from=install /root/.local /root/.local

WORKDIR /app
COPY ./core .
RUN python ./run.py

##################################################################
FROM python:3.9

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

COPY --from=install --chown=user /root/.local /home/user/.local

WORKDIR $HOME/app

COPY --chown=user ./core ./core
COPY --chown=user ./api ./api

COPY --from=setup --chown=user /app/engine.pickle ./engine.pickle

EXPOSE 7860
ENTRYPOINT ["python", "api/run.py"]
