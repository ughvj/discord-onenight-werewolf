FROM python:3.5.3

RUN pip install -U pip
RUN pip install -U discord.py

# ENTRYPOINT python run.py
