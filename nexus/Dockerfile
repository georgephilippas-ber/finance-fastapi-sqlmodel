FROM node:lts-slim

ENV IN_DOCKER=true

WORKDIR /nexus

COPY package.json ./
COPY package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
