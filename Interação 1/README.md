# INTALAÇÃO DO AMBIENTE PARA O CHATBOT

Para iniciar o chatbot do Fatequino em sua máquina, os seguintes softwares são necessários:

* MongoDB, versão 4.x.x
* Python3, versão 3.7.x
* pip, versão 19.x.x
* MONGODB
É possível baixar o MongoDB no link oficial do programa:

https://www.mongodb.com/try/download/community

>No site escolha o MongoDB Community Server, e esolha a opção do seu sistema operacional, nesse caso estamos usando o Windows, mas é aceito Linux e IOS também. >Lembre -se de utilizar a versão mais recente.

>Após o término do download, clique no programa e aceite as condições de uso e escolha a opção complete

Atente-se ao caminho que o MongoDB foi instalado, caso não tenha modificado o caminho de instalação o local que ele foi instalado normalmente é: Disco Local > Arquivos de Programas > MongoDB > Server > “versão baixada” > bin. Dentro da pasta temos dois arquivos importantes o mongo e mongod.

O Mongod é um servidor do banco de dados e o Mongo é uma aplicação shell, utilizado para digitar as linhas de comandos de interação, exclusão, inclusão ou buscar um determinado documento dentro do bando de dados do MongoDB. Para podermos utilizá-lo sem problemas no prompt é preciso criar uma variável de ambiente.

## 1.2 VARIÁVEL DE AMBIENTE

>No caso do Windows basta digitar na caixa de pesquisa “variáveis de ambiente” ou então pode ir pelo caminho “Painel de Controle > Sistemas e Segurança > Sistemas > Configurações Avançadas do Sistema”.

>Ao acessar essas configurações escolha a opção variáveis de ambiente

>Nessa nova janela teremos duas opções variáveis de usuário e variáveis do sistema, a melhor opção é a segunda, para não ter problema em acessá-lo, escolha a variável Path, selecione a e clique em editar.

>Após clicar em editar, uma nova janela irá abrir e clique em Novo

>Acrescente o caminho que está instalado o mongod, normalmente o caminho é: C:\Program Files\MongoDB\Server\4.4\bin

>Lembrando que o 4.4 é a versão, então atente-se qual foi a versão instalada no computador. Após preencher os valores clique em todos os OK, para salvar, caso contrário o caminho não será salvo. Para saber se está correto e o caminho funcionado, use o prompt e digite: mongod -version Se a versão aparecer está correto, caso contrário verifique se o caminho e o nome da variável estão corretos.

Uma dica é abrir outro cmd caso você tenha usado antes de fazer a variável de ambiente. Depois é preciso subir o banco, basta digitar mongod. Caso aja um problema exception in initAndListen: 29 Data directory C:\data\db\not found., terminating Isso siginifica que ele não esta encontrando o diretório data e para isso basta seguir os comandos: • cd.. (para voltar no diretório anterior) digite até ficar no “C:>”; • md data (cria um diretório chamado data); • cd data (para entrar dentro do diretório data); • md db (cria um diretório db); • cd db (entrar dentro do diretório db) • mongod (para inicializar o MongoDB)

A janela não poderá ser fechada, caso contrário é como se estivéssemos encerrando o servidor.

## PYTHON E PIP
>Para instalação do python baixe o no link abaixo: https://www.python.org/downloads/

>Escolha a versão mais atualizada e execute. Antes de clicar em Install Now, selecione a opção Add Python to PATH, isso irá poupar o trabalho de criar uma variável de ambiente. Caso tenha esquecido de selecionar essa opção é só seguir o passo-a-passo no tópico 1.2 VARIÁVEL DE AMBIENTE. Depois de clicar em Install Now, a próxima janela será Optional Feature e deixe tudo selecionado (padrão). A tela Advance Optional, não precisa marcar ou desmarcar nenhum item, deixe padrão. Nessa mesma tela se atente ao caminho que o Python esta sendo instalado, caso não tenha marcado a opção de Add Python to PATH é melhor copiar e colar esse caminho, para utilizar mais tarde. Depois de instalado use o prompt para ver se deu certo com o comando python -V

Caso não apareça verifique nas variáveis de ambiente se foi criado o PATH python.

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

