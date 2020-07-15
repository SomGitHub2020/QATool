# base image
FROM node:alpine

# set working directory
WORKDIR /app/frontend/

# add `/app/node_modules/.bin` to $PATH
#ENV PATH /app/frontend/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package*.json /app/frontend/

RUN npm install

COPY . /app/frontend/

#COPY . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
#RUN adduser appuser && chown -R appuser /app
RUN adduser -D -g '' admin
USER admin

EXPOSE 3000

CMD ["npm","run","start"]
# start app
#RUN npm start