# [Web](https://fatequino.com.br/construcao-do-fatequino/web/)

Baixando e instalando a versão local do site Fatequino

Utilizando o plugin Duplicator, será possível criar uma cópia do site atual e trabalhar livremente com essa cópia de forma local (no próprio computador).
O plugin deve estar atualizado para melhor integridade de suas funcionalidades. Mais informações: https://br.wordpress.org/plugins/duplicator/.
As mudanças feitas localmente não afetaram o site original, portanto, é possível testar diversas funcionalidades sem medo de prejudicar o site.
Dito isso, as mudanças que forem definitivas deverão ser repetidas no site original.

1. Acesse o site https://fatequino.com.br/, clique no botão de login e utilize as credenciais do fatequino.

2. Uma vez logado, acesse o link https://fatequino.com.br/wp-admin/
No manual anterior, esse procedimento foi dito necessário, pois, turmas anteriores retiraram a página normal do WordPress.
Após o login retornará para a página inicial com a barra do WordPress no topo.

3. Clicando em Fatequino ou em Fatequino > Painel, será direcionado ao painel do administrador.
Após o login retornará para a página inicial com a barra do WordPress no topo.

4. Clicando em Fatequino ou em Fatequino > Painel, será direcionado ao painel do administrador.

5. No final da página, localize e clique em “Duplicator”.

6. Clique em Create New para criar um novo restore do site.

7. A recomendação é manter o nome sugerido (20200311_Fatequino), porém se for mudar, mantenha o padrão yyyymmdd_Fatequino para fácil identificação.

8. Nesta página nenhuma outra alteração é necessária. Pode descer até o final e clicar em “Next”.
O Duplicator irá escanear os arquivos do site e prepará-los para download.

9. Clique em “Yes. Continue with the build process!” e em “Build!”

10. Clique em “One-Click Download” para baixar o installer e o Archive de uma vez.

Neste próximo passo, iremos utilizar o xampp, mas se quiser pode usar qualquer outro similar.

11. Abra o Xampp e ligue o Apache e o MySQL.

12. Acesse a pasta do Xampp, procure htdocs, crie uma pasta para os arquivos baixados e os cole lá

13. Digite localhost/nome_da_pasta/installer.php para começar a instalação do ambiente de desenvolvimento. Deixe como na imagem ao lado:

14. Em “Action” altere para “Create new database”
Obs: Pode ser necessário alterar o User para “root” e clique em “Next”

15. Clique em “Next” e aguarde o processamento...
Feche a aba do Duplicator.

16. Com o Xampp ativado e o Apache e MySQL iniciados, abra o navegador e digite http://localhost/nome_da_pasta/ e pronto!

17. Faça login com os mesmos dados e siga com as alterações sem interferir com o site em produção

