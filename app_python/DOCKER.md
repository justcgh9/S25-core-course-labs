# Docker best practices

In this document I will describe the practices applied to the [Dockerfile](/app_python/Dockerfile). Most of these practices can be found on the [Docker official website](https://docs.docker.com/build/building/best-practices/)

## Choosing the right image

I chose python:3.12.7-alpine, which is a lightweight linux distribution with python pre-installed.

## Creating ephemeral containers

This practice states: "Containers should be stateless and ephemeral, meaning they can be stopped, destroyed, and rebuilt with minimal configuration."

The container itself does not store any specific state, which might have been used in the future builds, leaving all the dependencies on the application code and script, which
are explicitly copied in the dockerfile. Moreover, I use a .dockerignore file to avoid copying undesired files.

## Don't install unnecessary packages

I only install the packages listed in requirements.txt, which remains clean.

## Use a non-root user

In a dockerfile i create an appuser account, and then switch to it to minimize the security risks.

## Dockerfile instructions

When composing the dockerfile I used the instructions for FROM, RUN, CMD, EXPOSE, COPY, USER.
