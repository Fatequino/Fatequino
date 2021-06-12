# Testes de Hardware

> Os testes de hardware implementados para o projeto Fatequino consistem na verificação da movimentação do robô.
A Proposta de testes para a movimentação do robô Fatequino consiste na verificação de sua capacidade de locomoção e detecção com base em 6 percursos preestabelecidos, cada um com diferentes objetivos e graus de dificuldade.

* O primeiro percurso tem como objetivo a verificação da capacidade do robô em seguir uma linha guia;

* O segundo percurso tem como objetivo a verificação da capacidade do robô em detectar um obstáculo em seu trajeto e realizar a parada, impedindo a colisão;

* O terceiro percurso tem como objetivo verificar gradualmente a capacidade do robô em realizar curvas exigidas em seu trajeto. Iniciando pela avaliação sobre uma curva em ângulo obtuso (135°)

* O quarto percurso tem como objetivo verificar gradualmente a capacidade do robô em realizar curvas exigidas em seu trajeto. Iniciando pela avaliação sobre uma curva em ângulo obtuso (90°);

* O quinto percurso tem como objetivo verificar gradualmente a capacidade do robô em realizar curvas exigidas em seu trajeto. Iniciando pela avaliação sobre uma curva em ângulo obtuso (45°);

* O primeiro percurso tem como objetivo verificar a capacidade do robô em desviar de um obstáculo em seu caminho, retornar ao trajeto e concluí-lo.

## Plataforma de Registro <img src="https://img.icons8.com/color/48/000000/ms-excel.png" align="right" height="50px"/>


Com o intuito de garantir a padronização dos registros de testes a serem efetuados, foi desenvolvida uma plataforma intermediária, por onde as execuções de testes serão adicionadas a uma planilha única.

Esta plataforma foi desenvolvida na linguagem VBA (Visual Basic for Applications) e está atrelada a uma planilha Excel, na qual serão armazenadas as execuções de testes e pode ser encontrada no arquivo [Execuções de Testes.xlsm](Execuções de Testes.xlsm).

- ### Instalação

Para utilizar a plataforma de registros deve ser reallizado o download do arquivo [Execuções de Testes.xlsm](Execuções de Testes.xlsm). Ao acessar o arquivo pode ser necessária a habilitação do funcionamento das macros (funções prógramadas da planilha excel).
Caso seja exibido o aviso abaixo, deve ser pressionado o botão indicado "Habilitar Conteúdo".

<img src="mdfiles/HabilitarConteudo.png" align="center" height="200px"/> 

