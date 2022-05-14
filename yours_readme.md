# Escreva sua Documentação AQUI!!!

## Requisitos:
Docker

Docker-Compose

<br>

## Ambiente de Teste:
Docker version 20.10.14, build a224086

DockerCompose version v2.5.0

<br>

## Realização dos Requisitos:

### Requisito 1: :white_check_mark:
Realizei a criação do Dockerfile no diretório raiz do projeto usando a imagem de Python mais recente e compatível com a versão do Django requisitada.
Segui as recomendações baseadas na documentação oficial do Docker.

### Requisito 2: :white_check_mark:
No utilização do docker-compose dividi o gerenciamento dos conteiners em 3 serviços web para a aplicação Django, db para o banco de dados Postgres e nginx para o servidor nginx.
Para utilização das variáveis de ambientes disponbilizadas no arquivo .env, usei a opção env_file como é recomendado na documentação.

### Requisito 3: :white_check_mark:
Na criação do serviço web no docker-compose utilizei a opção port para alterar a porta do conteiner para 8008 e mantive a porta do Docker Host em 8000.

### Requisito 4: :heavy_exclamation_mark:
Na construção do workflow Django CI optei por utilizar as versões de Python compatíveis com a versão do Django que está sendo utilizada, prossegui com a instalação das dependências da aplicação, migrações da aplicação e testes com pytest.
No entanto ainda não consigo corrigir alguns erros que estão ocorrendo durante a implementação.
:construction: Em construção :construction:

### Requisito 5: :white_check_mark:
No arquivo Setting.py do projeto docker_django alterei os campos de DATABASE para que utilizassem as variáveis de ambiente já adicionadas aos containers durante o requisito 2. A instância db foi criada no Docker-compose.

### Requisito 6: :white_check_mark:
No diretório nginx se encontra o Dockerfile que realiza a criação do container para o nginx em que é realizado o upstream do serviço web na porta 8000 e realizado do redicionamento da para a porta 80.

### Req 7: :white_check_mark:
Feito.

### Req Extra: :heavy_exclamation_mark:
:construction: Em construção :construction:

<br>

## Como Usar:

1° Passo: Realize o clone do projeto

~~~bash
git clone https://github.com/Mateus-Mota/Desafio-Devops.git
~~~

2° Passo: Execute o comando docker-compose up
~~~bash
docker-compose up
~~~

3° Passo: Acesse a página do projeto pelo endereço http://127.0.0.1
