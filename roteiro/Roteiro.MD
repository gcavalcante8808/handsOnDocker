## Slide - Objeto de Investigação OK

Falar sobre imutabilidade;
Falar sobre diferenças entre ambientes;

## Slide - O que é o Docker? OK

- Fazer a instalação do Docker
    - Docker for Linux
    - Docker for Mac

## Slide - O que é uma Imagem? OK

Mostrar alguns serviços rodando e alguns Dockerfiles

Por conta dessa estrutura (que na verdade é um CoW - Copy On Write) inicialmente só o espaço relacionado a imagem será gasto no sistema de arquivos; diferentemente do que acontece na virtualização convencional, 5 contêineres inicializados incorrem em uso total de espaço igual ao total da imagem (230MB por exemplo) e não 5 x 230MB. A medida que os arquivos dos contêineres forem mudando, aí sim, espaço adicional será utilizado.

Curiosidade: Copy on Write

## Slide - Onde Procurar uma imagem OK

- Falar sobre as imagens stock disponibilizadas
    - Python
    - NodeJS
    - .NetCore

## Slide - O que é um "Container"? OK

Explicar sobre processos, visualizar com CTOP e ps aux.

Fazer Exemplo 1, considerando os seguintes passos:

- Rodar o `docker build`;
- Rodar `docker images` e `docker history image --no-trunc`;
- `docker run -it --rm -v $(pwd)/app.py:/app.py exemplo python /app.py` e `docker ps`; 
- Docker run para funcionamento usando as portas: `docker run -it --rm -p 8000:8000 -v $(pwd):/app.py:/app.py exemplo python app.py`;
- Mostrar a importância de rodar em todas as portas disponíveis;
- Rodar os exemplos através do VisualStudioCode Insiders;
- Criar um arquivo grande na pasta e rodar o docker build para ensinar sobre o contexto e `.dockerignore` usando `mkfile -n 1g bigfile`

## Slide - Ciclo de vida de Contêineres

- Exemplo 2
    - Adicionar acesso a um banco de dados local usando sqlalchemy-core, usando variáveis de ambiente;
    - Rodar o banco de dados via `docker run -d -e POSTGRES_DB=mydb -e POSTGRES_PASSWORD=mypwd postgres:12.0-alpine`;
    - Tentar fazer a aplicação conectar no Banco pegando o IP via `docker inspect`.

Builds automáticas com DockerHub.

## Slide - Volumes e Logs
- Exemplo 3
    - Adiciona a geração de Logs na jogada, falando sobre jogar em arquivos ou jogar em `stdout`;
    - Adiciona o cache na jogada, inicialmente usando `docker run -d redis`;

- Mostrar banco e cache usando sistemas de arquivos COW e falar sobre volumes.
    - `docker diff`
    - `docker volume create db-data`
    - `docker volume create cache-data`
    - `docker run -d -e POSTGRES_DB=mydb -e POSTGRES_PASSWORD=mypwd -v db-data:/var/lib/postgres postgres:12.0-alpine`
    - `docker run -d -v cache-data:/data redis:alpine`

Recriar o banco e cache usando um volume docker ou mesmo uma pasta local.

## Slide - Redes e interações entre serviços

- Exemplificar o funcionamento da rede e das portas do Docker: nome internos e forwards de portas.
- Criar uma rede dedicada para os serviços e subir os serviços conectados a essas redes.
    - `docker network create handson`
    - `docker run -d --name db --network handson -v db-data:/var/lib/postgres -e POSTGRES_DB=mydb -e POSTGRES_PASSWORD=mypwd postgres:12.0-alpine`
    - `docker run -d --name cache --network handson -v cache-data:/data redis:alpine`
    - `docker run -d --name app --network handson -e DB_HOST=db -e DB_NAME=mydb -e DB_USER=postgres -e DB_PASSWORD=mypwd -p 8000:8000 -v $(pwd):/app.py:/app.py exemplo python app.py`

## Slide - Docker-Compose

- Instalar se necessário
- Migrar todos os serviços do modo imperativo para o Docker-Compose
