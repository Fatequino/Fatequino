## [Visão](https://fatequino.com.br/construcao-do-fatequino/visao/)

Aqui você irá encontrar:
- Dependências
- Como executar/instalar

# Instalação

Requerimentos/Dependências:

**- Sistema Operacional de arquitetura 64 bits**
**- Anaconda 3**
**- Compatibilidade ao Python 2.7 ou superior**
**- Bibliotecas dlib, opencv e Pillow(Podem ser instaladas via conda ou pip)**

- OpenCV, originalmente, desenvolvida pela Intel, em 2000, é uma biblioteca multiplataforma, totalmente livre ao uso acadêmico e comercial, para o desenvolvimento de aplicativos na área de Visão computacional;

- Dlib é uma biblioteca de software multiplataforma de uso geral;

- Python Imaging Library (Pillow) é uma biblioteca da linguagem de programação Python que adiciona suporte à abertura e gravação de muitos formatos de imagem diferentes.

# Execução/Instalação


## Instalação:

Instale o Anaconda no S.O. pelo seguinte link:
<https://www.anaconda.com/products/individual>

Após o Download (ou clone) do projeto, acesse a pasta **Fatequino\Visão**, crie o ambiente da aplicação:

	conda create --name visao

*caso queira uma versão específica do Python no projeto, especifique no final da linha do comando acima Python="número da versão"

Após instalado:
	
	conda activate visao

instale as bibliotecas (no nosso exemplo estamos usando o Anaconda):

	conda install -c conda-forge dlib

	conda install -c conda-forge opencv

	conda install -c conda-forge pillow

*caso queira conferir se foram instalados com êxito, digite o comando **conda list**

##Execução:

Para executar, é necessário que você tenha uma webcam conectada a seu dispositivo de execução, ou você pode utilizar um aplicativo que simule em seu smartphone esta funcionalidade.

Execute o seguinte comando no terminal dentro da pasta **Fatequino\Visão**:
	python landmarks.py

	Para finalizar a execução digite "q"

Para mais informaçõe à respeito do código, referências nos links abaixo:

<https://medium.com/@suzana.svm/configurando-o-ambiente-dlib-python-guia-para-iniciantes-81cdcffc937e>

<http://www.paulvangent.com/2016/08/05/emotion-recognition-using-facial-landmarks/>