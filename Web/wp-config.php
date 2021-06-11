<?php
/**
 * As configurações básicas do WordPress
 *
 * O script de criação wp-config.php usa esse arquivo durante a instalação.
 * Você não precisa usar o site, você pode copiar este arquivo
 * para "wp-config.php" e preencher os valores.
 *
 * Este arquivo contém as seguintes configurações:
 *
 * * Configurações do MySQL
 * * Chaves secretas
 * * Prefixo do banco de dados
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/pt-br:Editando_wp-config.php
 *
 * @package WordPress
 */

// ** Configurações do MySQL - Você pode pegar estas informações com o serviço de hospedagem ** //
/** O nome do banco de dados do WordPress */
define( 'DB_NAME', "wordpress_5" );

/** Usuário do banco de dados MySQL */
define( 'DB_USER', "root" );

/** Senha do banco de dados MySQL */
define( 'DB_PASSWORD', "" );

/** Nome do host do MySQL */
define( 'DB_HOST', "localhost" );

/** Charset do banco de dados a ser usado na criação das tabelas. */
define( 'DB_CHARSET', 'utf8mb4' );

/** O tipo de Collate do banco de dados. Não altere isso se tiver dúvidas. */
define('DB_COLLATE', '');

/**#@+
 * Chaves únicas de autenticação e salts.
 *
 * Altere cada chave para um frase única!
 * Você pode gerá-las
 * usando o {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org
 * secret-key service}
 * Você pode alterá-las a qualquer momento para invalidar quaisquer
 * cookies existentes. Isto irá forçar todos os
 * usuários a fazerem login novamente.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         ']4g:F*Y[fQ>D|fJc/dC]9+81bBxHE:j8V2r!iNl(MT`dS?7|mh=|u]O}1]yU{i-}' );
define( 'SECURE_AUTH_KEY',  '52n<R)76:Y9@sOQRd.;y-Z|y(*s)NsLQ|{D6@b1G{05YazQnm~iR})$%I,w8I^E7' );
define( 'LOGGED_IN_KEY',    'E&V-L1[kp&Sttu/+aS_b!q(G:LJd<IgheP~`|^{AG=[cU{<5xRuB0,c]*&NX59y&' );
define( 'NONCE_KEY',        'sl8zrWg;b~u0wnXkm//N0]*=~`V<OB=4Zk$6-[+2`SZ~2od}kJ?F,6<-uB#UqOt1' );
define( 'AUTH_SALT',        '5:0S9NSBH}8X{58JQc^@gZ;i9R~RXzIiKWZkmV[}XF [JQ}Xvzmq*=?uO:c;y_v^' );
define( 'SECURE_AUTH_SALT', '0m5<7[+&G;s49q?:vx uHJ5iK x&%igd%aj,(oYiKI<+ZinW8sc_~+TGg@-XnCs{' );
define( 'LOGGED_IN_SALT',   'ntY=L*=1+{4Dm#@ $N,aPlyrh3~u.}O<2=GK$3kt|>/.wLK8l8Y6DgtdmML(>RqP' );
define( 'NONCE_SALT',       'G0KRbRt+C~(O*!&Ol]|oHE`8{a }H20N23:&?Uj8oT4v[V^[zZMi<?3z#`pc,MY)' );

/**#@-*/

/**
 * Prefixo da tabela do banco de dados do WordPress.
 *
 * Você pode ter várias instalações em um único banco de dados se você der
 * um prefixo único para cada um. Somente números, letras e sublinhados!
 */
$table_prefix = 'wp_';

/**
 * Para desenvolvedores: Modo de debug do WordPress.
 *
 * Altere isto para true para ativar a exibição de avisos
 * durante o desenvolvimento. É altamente recomendável que os
 * desenvolvedores de plugins e temas usem o WP_DEBUG
 * em seus ambientes de desenvolvimento.
 *
 * Para informações sobre outras constantes que podem ser utilizadas
 * para depuração, visite o Codex.
 *
 * @link https://codex.wordpress.org/pt-br:Depura%C3%A7%C3%A3o_no_WordPress
 */
define('WP_DEBUG', false);

/* Isto é tudo, pode parar de editar! :) */

/** Caminho absoluto para o diretório WordPress. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Configura as variáveis e arquivos do WordPress. */
require_once(ABSPATH . 'wp-settings.php');

