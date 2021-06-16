# [Interação](https://fatequino.com.br/construcao-do-fatequino/interacao/)

Este módulo do projeto tem como objetivo desenvolver um chatbot
capaz de fornecer ao usuário informações sobre a Fatec Carapicuíba.
Caso tenha dificuldade em instalar os softwares, leia a documentação README_COMPLEMENTO

## Instalação

Para iniciar o chatbot do Fatequino em sua máquina, os seguintes softwares
são necessários:

- MongoDB, versão 4.x.x
- Python3, versão 3.7.x
- pip, versão 19.x.x

#### Mongo DB

O MongoDb Server é o sistema de banco de dados utilizado pela aplicação.

Para instalação, siga a documentação oficial: [Instalar MongoDb Server Community Edition](https://docs.mongodb.com/manual/administration/install-community/)

#### Python 3 e PIP

Python é a linguagem de programação utilizada para o desenvolvimento do chatbot.

Para instalação, baixe e execute o instalador no site oficial: [Instalar Python](https://www.python.org/downloads/)

Juntamente com o Python, será instalado o utilitário `pip`. Esta ferramenta é utilizada para o gerenciamento de dependências de aplicações escritas em python.

## Execução

Inicie sua instância do MongoDb na porta `27017`.

Baixe ou clone este repositório (utilizando o git) e coloque-o em um diretório de sua preferência. Por exemplo:

Windows:

> c:/fatequino

Linux:

> ~/fatequino

Crie uma variável de ambiente chamada `FLASK_APP` com o valor `my_flask_app.py`.

Utilizando uma ferramente de linha de comando de sua preferência, acesse o caminho do chatbot, por exemplo:

Windows:

> c:/fatequino/Interação 1

Linux:

> ~/fatequino/Interação 1.

Instale as dependências da aplicação rodando o seguinte comando: `pip install -r requirements.txt`
Caso de erro ao instalar com esse comando, é melhor instalar um de cada vez.

```
Atenção: talvez seja necessário executar o comando acima no modo administrador.
```

Execute o comando `python -m flask run` para executar o programa.

Feito isso, a aplicação será iniciada e poderá ser acessada no endereço: `localhost:5000`

## Post da base de dados do ChatBot

* Para a inserção das informações referentes a Fatec implementadas atualmente, será necessário:

>Baixar o Postman ou acessar https://www.postman.com/

* Para inserção de dados de aulas siga os passos abaixo:

>Em WorkSpaces, crie uma nova aba configure para POST e insira a URL http://127.0.0.1:5000/aulasInfo no campo de URL

>Clique em "Body" e altere para o tipo "Raw" e mude o type para "JSON"

>No espaço abaixo insira o apêndice JSON que se encontra no arquivo aulas.json dentro da pasta "Interação 1" do projeto

>Clique no botão "Send" para fazer o envio dos dados para a base do mongoDB.

* Para inserção de dados de horarios siga os passos abaixo:

>Em WorkSpaces, crie uma nova aba configure para POST e insira a URL http://127.0.0.1:5000/horarioLocal no campo de URL

>Clique em "Body" e altere para o tipo "Raw" e mude o type para "JSON"

>No espaço abaixo insira o apêndice JSON que se encontra no arquivo horarios.json dentro da pasta "Interação 1" do projeto

>Clique no botão "Send" para fazer o envio dos dados para a base do mongoDB.

Pronto, seguindo estes passos o bot já terá acesso as informações.
=======
