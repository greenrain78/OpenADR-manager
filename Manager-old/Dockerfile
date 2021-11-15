# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONUNBUFFERED=1

ARG GIT_ID
ARG GIT_PASSWORD
ARG GIT_USERNAME
ARG GIT_EMAIL

# install ssh
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y openssh-server

# install vim
RUN apt-get install -y vim

# install docker 
RUN apt-get update
RUN apt-get -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"


# install src

WORKDIR /home
RUN git clone http://$GIT_ID:$GIT_PASSWORD@github.com/greenrain78/OpenADR-manager.git
RUN git config --global user.name "$GIT_USERNAME"
RUN git config --global user.email "$GIT_EMAIL"

WORKDIR /home/OpenADR-manager
RUN git fetch --all
RUN git pull origin main
RUN python -m pip install -r /home/OpenADR-manager/requirements.txt

# pass id and password
ENV GIT_ID=${GIT_ID}
ENV GIT_PASSWORD=${GIT_PASSWORD}

ENTRYPOINT sh /home/OpenADR-manager/entrypoint.sh "$GIT_ID" "$GIT_PASSWORD" 