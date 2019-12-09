FROM nikolaik/python-nodejs
RUN npm install -g serverless
COPY ./ /usr/src/app
WORKDIR /usr/src/app
RUN sls plugin install --name serverless-offline-python
EXPOSE 3000
CMD ["sls", "offline", "start"]
