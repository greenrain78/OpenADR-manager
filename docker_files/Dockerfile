# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONUNBUFFERED=1

# install ssh
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y openssh-server

# install vim
RUN apt-get install -y vim

# install src
WORKDIR /home
RUN git clone https://$GIT_ID:$GIT_PASSWORD@github.com/greenrain78/OpenADR-model.git
RUN git config --global user.name "$GIT_USERNAME"
RUN git config --global user.email "$GIT_EMAIL"

# 파이썬 라이브러리 설치
WORKDIR /home/OpenADR-model
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /home/OpenADR-model/requirements.txt

# entrypoint
ENTRYPOINT ["sh", "/home/OpenADR-model/entrypoint.sh" ]

