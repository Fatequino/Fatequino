# Reconhecimento de Face

## Requerimentos/Dependências:


**- Sistema Operacional de arquitetura 64 bits**

**- Anaconda 3**

**- Compatibilidade ao Python 2.7 ou superior**

**- Bibliotecas dlib, opencv e Pillow (Podem ser instaladas via conda ou pip)**


- **OpenCV**, originalmente, desenvolvida pela Intel, em 2000, é uma biblioteca multiplataforma, totalmente livre ao uso acadêmico e comercial, para o desenvolvimento de aplicativos na área de Visão computacional;

- **Dlib** é uma biblioteca de software multiplataforma de uso geral;

- **Python Imaging Library (Pillow)** é uma biblioteca da linguagem de programação Python que adiciona suporte à abertura e gravação de muitos formatos de imagem diferentes.

# Execução/Instalação

## Instalação:

Após as configurações de ambiente do Anaconda, que há no arquivo README.md do diretório base da seção (que já incluem as instalações das bibliotecas citadas), acesse a pasta referente aos arquivos de execução (No projeto é o landmarks.py), no terminal:
	
	cd Face

*caso queira conferir se foram instalados com êxito, digite o comando **conda list**

## Execução

Para executar, é necessário que você tenha uma webcam conectada a seu dispositivo de execução, ou você pode utilizar um aplicativo que simule em seu smartphone esta funcionalidade.

Execute o seguinte comando no terminal dentro da pasta **Fatequino\Visão\Face**:

	python landmarks.py

	Direcione a câmera em sua face, então irá aparecer os pontos de referência.

	Para finalizar a execução digite "q"
	

Para mais informações no que diz respeito do código, referências nos links abaixo:

<https://medium.com/@suzana.svm/configurando-o-ambiente-dlib-python-guia-para-iniciantes-81cdcffc937e>

<http://www.paulvangent.com/2016/08/05/emotion-recognition-using-facial-landmarks/>