## [Visão](https://fatequino.com.br/construcao-do-fatequino/visao/)

1.     INTRODUÇÃO
  O ambiente e códigos foram desenvolvidos em linguagem Python3, que é uma das ferramentas referência em programação de Inteligência Artificial. A instalação dessa ferramenta é necessária para garantir o funcionamento de suas respectivas bibliotecas. Para se obter a captura das imagens uma webcam deve estar conectada ao seu dispositivo para a aplicação interagir da forma correta com o uso da biblioteca OpenCV. 
  Os arquivos utilizados na aplicação estão em um repositório no Github Fatequino e no Drive do grupo de Visão do primeiro semestre de 2021. Para garantir um ambiente com menos conflito ao sistema operacional base, é necessária a plataforma de virtualização Anaconda instalada (compatível somente com sistemas operacionais de arquitetura de 64 bits).
  
  Com os requisitos acima atendidos, devemos executar as ações a seguir:
      •	Capturar imagens da face através da webcam;
      •	Fazer o treinamento dessas imagens para fazer o posterior reconhecimento;
      •	Reconhecer a face da pessoa;
      •	Reconhecer os gestos e informar no terminal.
      
 2.      INSTALAÇÃO
 2.1.   ANACONDA PYTHON
  É necessário acessar o terminal de comandos do seu sistema operacional para instalar a plataforma Anaconda Python.
  Acessando o link abaixo, irá identificar a versão adequada para baixar:

     https://www.anaconda.com/products/individual

  Anaconda é solução flexível que fornece os utilitários para criar, distribuir, instalar, atualizar e gerenciar software de maneira multiplataforma. A Anaconda facilita o gerenciamento de vários ambientes de dados que podem ser mantidos e executados separadamente, sem interferência um do outro(Anaconda, 2021).

2.2.   CRIAÇÃO DO AMBIENTE ANACONDA
	A criação deste ambiente é recomendável, pois, evita possíveis problemas de compatibilidades entre sistemas instalados. Dentro do terminal de comandos, no diretório (pasta) o qual deseja manter a aplicação, digite:
  
    conda create --name nomedoseuambiente
      
  Após criado o ambiente, ative-o via terminal:
    
    conda activate nomedoseuambiente
      
  Caso queira encerrar o ambiente, digite:
    
    conda deactivate nomedoseuambiente

2.3.	   DOWNLOAD DO PROJETO
  Você pode clonar o projeto via comando, dentro do diretório desejado, como exibido abaixo:
  
    git clone https://github.com/Fatequino/Fatequino
      
  *Você pode baixar o projeto diretamente acessando o link acima, clicando em Clone ou download
      
  Após baixado, acesse a pasta contendo os arquivos com o seguinte comando:
  
    cd Fatequino/Visão

2.4.	   INSTALANDO BIBLIOTECAS  
    As bibliotecas utilizadas são:
    
    •	OpenCV: Originalmente, desenvolvida pela Intel, em 2000, é uma biblioteca multiplataforma, totalmente livre ao uso acadêmico e comercial, para o desenvolvimento de aplicativos na área de Visão computacional;
    •	Dlib: É uma biblioteca de software multiplataforma de uso geral;
    •	Python Imaging Library (Pillow): É uma biblioteca da linguagem de programação Python que adiciona suporte à abertura e gravação de muitos formatos de imagem diferentes;
    •	Numpy: É um pacote para a linguagem Python que suporta arrays e matrizes multidimensionais, possuindo uma larga coleção de funções matemáticas para trabalhar com estas estruturas;
    •	Imutils: É um pacote baseado em OPenCV para atingir o objetivo de chamar a interface OPenCV de forma mais concisa, podendo facilmente implementar uma série de operações como translação, rotação, dimensionamento e esqueletização de imagens.
  O comando para instalar no terminal, são os cincos comandos abaixo:
  
    conda install -c conda-forge dlib -y
    conda install -c conda-forge opencv -y
    conda install -c conda-forge pillow -y
    conda install -c conda-forge numpy -y
    conda install -c conda-forge imutils –y

3.	   EXECUÇÃO 
3.1.   DETECÇÃO E RECONHECIMENTO
  Para executar, é necessário que você tenha uma webcam conectada a seu dispositivo de execução, ou você pode utilizar um aplicativo que simule em seu smartphone esta funcionalidade. Precisaremos executar três programas em sequência sendo eles, o de captura de rostos, treinamento e reconhecimento da face. Acesse a pasta referente aos arquivos de execução (No projeto é o diretório “Reconhecimento”), digite no terminal:
  
    cd Reconhecimento

3.1.1. CAPTURA DA FACE
  Para captura da face, no terminal, digite o seguinte comando:
      
    python3 capturandoRostos.py
      
  Deverá ser informado o seu nome, seguido do seu RA. Com esses dados o programa criará uma pasta em um diretório de acordo com o que for informado em dataPath (Dentro do código capturandoRostos.py, este poderá ser alterado para seu uso). Direcionando a câmera para sua face, a aplicação irá reconhecer o seu rosto. Ao fazer o reconhecimento do rosto neste momento várias fotos do rosto serão tiradas (procurar fazer expressões diferentes), sendo no total de 300 fotos.
  Mesmo ao mudar o gesto da sua face, seu rosto será reconhecido. Após as capturas feitas ou a tecla “Esc” for pressionada o programa é finalizado.

3.1.2. TREINAMENTO DAS IMAGENS
  Para o treinamento das imagens obtidas, no terminal digite o seguinte comando:
    
    python3 treinandoRF.py
      
  Com as imagens obtidas através do programa anterior, é necessário fazer o treinamento para posterior reconhecimento. O programa irá acessar a pasta criada no programa anterior, onde se encontram as imagens salvas e a leitura das imagens serão feitas. Após a leitura dessas imagens, o programa gera dois arquivos no formato “.xml”, o “modeloEigenFace.xml” e o “modeloLBPHFace.xml”, estes por sua vez, guardam os vetores da face para posterior reconhecimento.

3.1.3. RECONHECIMENTO DA FACE
  Para fazer o reconhecimento da face, no terminal digite o seguinte comando:
    
    python3 ReconhecimentoFacial.py
      
  O programa detectará seu rosto, fazendo a comparação dos arquivos que foram gerados anteriormente (modeloEigenFace e modeloLBPHFace) e mostrará o nome e o RA que foram colocados na hora da captura, assim que o rosto já treinado seja detectado.

3.2.   RECONHECIMENTO DE GESTOS
  Após as configurações de ambiente do Anaconda, feita no diretório base (que já incluem as instalações de algumas das bibliotecas citadas).
  Acesse a pasta referente aos arquivos de execução (No projeto é o diretório “Gestos”), digite no terminal:
  
    cd Gestos
      
  Após acessar, digite o comando para executar a aplicação:
    
	  python3 HandGestureV2.py*
      
  Ao fazer o gesto representando o número dois com a mão na frente da câmera (indicador e dedo médio levantado), no terminal irá aparecer "Olá aluno!". Fazendo o gesto representando o número cinco (com a palma da mão aberta), no terminal irá aparecer “Pare!”. Para finalizar a execução tecle "Esc".

  *É recomendável que se esteja em um local bem iluminado e que sua mão esteja totalmente no quadrante da câmera (sem ultrapassar as linhas).
    
    

