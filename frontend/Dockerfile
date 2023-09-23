FROM node:latest

WORKDIR /app

COPY package*.json ./
RUN apt install curl
RUN apt install unzip
RUN npm install -g bun

RUN bun install

COPY . .

EXPOSE 3000

CMD ["bun", "run", "dev"]
