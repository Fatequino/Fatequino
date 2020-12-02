## [Visão](https://fatequino.com.br/construcao-do-fatequino/visao/)

Aqui você irá encontrar:
- Descrição do Projeto
- Como instalar o ambiente para execução

# Projeto

Atualmente na Fatec Carapicuíba os alunos conseguem informações sobre aulas e
professores somente pelo site disponibilizado (SIGA e site oficial da Fatec Carapicuíba),
entretanto há alunos que possuem dificuldades para realizar consultas sobre horário de aulas e
professores.

Pensando nisso foi iniciado um projeto para que este problema seja solucionado de forma rápida e eficiente. O projeto nomeado “Fatequino”, possui esse propósito de auxiliar tanto alunos que não possuem conhecimento da instituição ex: novatos, novos professores e visitantes. Auxiliando-os e facilitando em suas buscas através de uma informação simples e
rápida.

O projeto está dividido em 6 grupos que realizarão o desenvolvimento de suas
respectivas áreas: Controle, Interação, Mecânica 1 e 2, Visão e Web.

Esta seção abordará a parte de visão, cujo objetivo é realizar
reconhecimento facial de pessoas e gestos, a fim de que seja alcançado também novos resultados estipulados pelo Projeto Fatequino a cada novo semestre.

## Descrição da aplicação

Em cada subdiretório da seção, se encontra aplicações para reconhecimento dos pontos de referência faciais (/Face) e reconhecimento de gestos (/Gestos).

O reconhecimento de face, utiliza um algoritmo cuja ativações de seus módulos importados aplicam a aprendizagem de máquina, para então detectar os pontos de referência faciais a partir de um arquivo de identificação ".dat", junto com os dados obtidos na câmera.

O reconhecimento de gestos marca na visão da câmera uma região marcada em um quadrado, e nessa região, a aplicação poderá  identificar um gesto, sendo ele especificado pelo algoritmo (quantidade de dedos levantados, por exemplo) para depois notificar no terminal.

## Requerimentos/Dependências:

**- Sistema Operacional de arquitetura 64 bits**

**- Anaconda 3**

**- Compatibilidade ao Python 2.7 ou superior**

**- Bibliotecas dlib, opencv e Pillow, numpy, math e time (Podem ser instaladas via conda ou pip)**


## Instalação:

Instale o Anaconda no S.O. pelo seguinte link:
<https://www.anaconda.com/products/individual>

Após o Download (ou clone) do projeto, acesse a pasta **Fatequino\Visão**, crie o ambiente da aplicação:

	conda create --name visao

*caso queira uma versão específica do Python no projeto, especifique no final da linha do comando acima Python="número da versão"

Após instalado:
	
	conda activate visao

	instale as bibliotecas:

	conda install -c conda-forge numpy -y

	conda install -c conda-forge dlib -y

	conda install -c conda-forge opencv -y

	conda install -c conda-forge pillow -y


*caso queira conferir se foram instalados com êxito, digite o comando **conda list**


Na estrutura de diretórios temos duas aplicações:
	
- Para reconhecimento de faces, que se encontra no diretório **Fatequino\Visão\Face**

- Para reconhecimento de gestos, que se encontra no diretório **Fatequino\Visão\Gestos**


*As instruções para execução estão nos arquivos README.md dos respectivos diretórios


Para mais informações à respeito do código, referências nos links abaixo:

<https://medium.com/@suzana.svm/configurando-o-ambiente-dlib-python-guia-para-iniciantes-81cdcffc937e>

<http://www.paulvangent.com/2016/08/05/emotion-recognition-using-facial-landmarks/>

<https://github.com/biankatpas/Libras>


## Arduino & RaspBerry pi3 
O código conta com dois arquivos na raiz do projeto, responsáveis por fazer o teste da comunicação ente o raspberry e o arduino. 
Antes de executar o código python que envia informações ao arduíno é necessário levar em consideração o circuito que foi desenhado para
demonstração dessa `situação-problema` (disponível no drive), além disso, certifique-se de que o id (atual '/dev/ttyACM0' ) do seu arduino esteja correto. 

