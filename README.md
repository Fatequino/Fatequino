# [Fatequino](https://fatequino.com.br/)

![Projeto Fatequino](https://raw.githubusercontent.com/Fatequino/Fatequino/master/Controle/Imagens/Anota%C3%A7%C3%A3o%202020-05-11%20121530.png)

Robô com inteligência artificial baseado em Arduino e Rapberry elaborado pela Fatec Carapicuíba.

Disponível no repositório:
* Divisão e fluxo de trabalho
* Todos os arquivos e informações necessárias para construir um Fatequino
* Código fonte do Arduino, Raspberry e Website.
* Documentação

## Fluxo de Trabalho
A equipe de controle do projeto planeja, coordena e controla as reuniões quinzenais. A cada quinzena será realizada uma reunião em que serão relatados os avanços em cada tarefa de cada equipe e são atribuídas novas tarefas. Cada time deverá eleger um Scrum Master, que ficará responsável pela equipe. O professor é o Product Owner. As tarefas cumpridas no prazo serão contabilizadas para a composição da nota.
Cada equipe terá uma branch para desenvolvimento e documentação do que foi executado.

>Englobamos o projeto inteiro em um repositório chamado Fatequino, nele temos 7 pastas uma para **cada equipe**. Nessa nova versão da organização do uso do GitHub, escolhemos por separar melhor o motivo para uso da plataforma: Aqui, no GitHub, só serão armazenados códigos desenvolvidos pelas diferentes equipes do projeto, divididas entre:

* Interação I
* Interação II
* Visão
* Web
* Mecânica
* Estrutura do Robô
* Testes

## Divisão de Trabalho

### Mecânica do Movimento
Equipe responsável por pesquisar e desenvolver a solução básica de movimentação, alimentação e construção do Fatequino.

>As funções previstas para o projeto demandam uma gama de peças e tecnologias diferentes trabalhando em conjunto para que tudo o que está previsto se tornar realidade. O desenho básico prevê um robô que possui 4 rodas acopladas em uma base, um braço robótico preso sobre a base e uma câmera com movimentação na ponta do braço. 

### Visão
Equipe responsável por pesquisar e desenvolver a solução de identificação e reconhecimento visual de alunos, professores, funcionários e visitantes.

>Será utilizado uma biblioteca do Python para fazer o reconhecimento facial com redes neurais.

### [Interação](/Interação%201)
Equipe responsável por pesquisar e desenvolver a solução de interação do Fatequino com alunos, professores, funcionários e visitantes.

>Para fazer a interação com os usuários será utilizado um bot com inteligência artificial.

### Presença na WEB
Equipe responsável por pesquisar e desenvolver a solução de presença na web do Fatequino.

>No domínio https://fatequino.com.br será feito cadastro dos alunos e professores para subirem as imagens que serão utilizadas na Equipe de Visão.

### Estrutura do Robô
Equipe responsável por realizar as implementações de modelagens estruturais, compilações de fotos e especificação dos componentes do robô.

>Para modelar o robô virtualmente, será utilizado o software Inventor.

### Testes
Equipe responsável por realizar os testes manuais e automatizados em todas as partes do projeto Fatequino, incluindo o software e o hardware (site e robô).

>Para testar o site, será utilizado o framework Selenium.

## O que subir no GitHub

>Para otimizarmos o uso da plataforma GitHub e facilitar as futuras passagens de conhecimento, o GitHub do fatequino deve armazenar apenas e exclusivamente CÓDIGO desenvolvido pelos integrantes das equipes. Artigos, slides e arquivos de mídia no geral devem ser mantidos em suas respectivas pastas no Google Drive disponibilizado pelo professor.

OBS: Os únicos arquivos de mídia permitidos no GitHub serão somente os pertinentes a estrutura do site, como banners, logos, mascote, etc.

## Padronização de uso do GitHub
    A proposta de  padronização do github, foi feita através de uma conversa com o grupo de teste e tem as seguinte sugestões.

-Versionamento do Fatequino
        Utilizando os padrões de versionamento e adquirindo uma cultura de implementação de correção de bugs e melhorias que podem ser feitos a cada semestre acompanhando a nomenclatura adaptada da semantic versioning (ex. 1.2.4)  a seguir o padrão sugerido: 

X.Y.Z =  

“X” corresponde ao ano do versionamento.        
“Y”  corresponde ao semestre de desenvolvimento.
“Z”  corresponde ao patch de correção.

## Padrão de Commit

Os commits devem ser atômicos, se duas correções distintas são realizadas, elas devem ser implementadas em dois commits diferentes. As mensagens de correção de issue devem descrever o que mudou e fazer referência ao número da issue associada à mudança. 

As sete regras de uma ótima mensagem de commit do Git 
⦁    Separe o assunto do corpo com uma linha em branco
⦁    Limite a linha de assunto a 50 caracteres
⦁    Coloque a linha de assunto em maiúscula
⦁    Não termine a linha de assunto com um ponto
⦁    Use o humor imperativo na linha de assunto
⦁    Envolva o corpo em 72 caracteres (Quebrar linha em 72) 
⦁    Use o corpo para explicar o que e por quê vs. como
