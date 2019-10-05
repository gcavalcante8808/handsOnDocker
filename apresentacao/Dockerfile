FROM node:10.15-slim
RUN useradd -m user && \
    apt-get update && apt-get install -y git && \
    apt-get clean && rm -rf /var/lib/apt/*
RUN npm install -g generator-bespoke yo gulp-cli
USER user
CMD ["gulp","serve"]
