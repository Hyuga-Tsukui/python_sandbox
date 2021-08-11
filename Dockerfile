FROM python:latest
RUN apt-get update -qq && apt-get install -y git vim