# MEUS ANIMES

### PÁGINA INICIAL
![captura1](https://github.com/vitorfigueiredopb/desafio-workshop-fds-2021.1/blob/master/screenshots/screenshot1.png)

### PÁGINA DE ADICONAR UM NOVO ANIME
![captura2](https://github.com/vitorfigueiredopb/desafio-workshop-fds-2021.1/blob/master/screenshots/screenshot2.png)

### PÁGINA DE ATUALIZAR UM ANIME EXISTENTE
![captura3](https://github.com/vitorfigueiredopb/desafio-workshop-fds-2021.1/blob/master/screenshots/screenshot3.png)

### PÁGINA DE CONFIRMAR EXCLUSÃO DE UM ANIME
![captura4](https://github.com/vitorfigueiredopb/desafio-workshop-fds-2021.1/blob/master/screenshots/screenshot4.png)

# COMO RODAR O PROJETO NA SUA MÁQUINA?

### Pré-requesitos para a execução do projeto no Ubuntu
PostgreSQL: https://www.postgresql.org/download/linux/ubuntu/

Configure no arquivo ![settings.py](https://github.com/vitorfigueiredopb/desafio-workshop-fds-2021.1/blob/master/projeto/settings.py)(linha 78) de acordo com as configurações feitas no seu postgres.

LINKS ÚTEIS SOBRE O POSTGRES:
![Como mudar sua senha do postgres](https://stackoverflow.com/questions/12720967/postgresql-how-to-change-postgresql-user-password)
![Como criar um banco de dados no postgres](https://www.postgresql.org/docs/8.4/tutorial-createdb.html)

### Clonando o repositório e mudando para ele

`$ git clone https://github.com/vitorfigueiredopb/desafio-workshop-fds-2021.1.git`
`$ cd desafio-workshop-fds2021.1`

### Comandos para instalar, criar e ativar o ambiente virtual Python

Para instalar:

`$ sudo apt-get install python3-venv`

Para criar o ambiente virtual:
`$ python3 -m venv venv`

Ativando a venv:
`$ source venv/bin/activate`

### Instalando o requirements.txt

`$ pip install -r requirements.txt`

### Criando as tabelas no bando de dados

`$ python3 manage.py migrate`

### Rodando o projeto

`$ python3 manage.py runserver`

## Obrigado pela visita! :D
