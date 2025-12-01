Introdução

Esse repositório buscar explicar uma prática desenvolvida noas laboratórios de ensino de microprocessadores e sistemas embarcados da elétrica USP São Carlos.


Usarei de exemplo um script .py de escrita de texto em cartões magnéticos, presente nesse repositório
Para adicionar um script, bash, py, cc, ou outro qualquer a lista de serviços do OS Ubuntu da Raspberry PI, basta executar os seguintes comandos no bash:

sudo nano /lib/systemd/system/card_writer_serv.service

Cria-se, primeiramente, um arquivo de serviço para o diretório padrão de serviços do systemd, com o seguinte conteúdo:

[Unit]
Description=Serviço Python - Escritor de cartões
After=multi-user.target

[Service]
Type=simple
User=SEL
ExecStart=/usr/bin/python3 /home/sel/card_writer.py
WorkingDirectory=/home/sel
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target

Assim, adiciounou-se o interpretador Python e o scrpit à lista de serviços do systemd. Na seção [UNIT], apresenta-se a indentificação do serviço em Description, o que facilita saber se esse foi inicializado corretamente quando exibirmos a tela de inicialização do systemd. A seção [SERVICE] descreve o serviço em si, com os arquivos executados, quais usuários receberão o serviço e ainda adicionei um Restart automático a cada 3 segundos, caso a execução do serviço falhe. A seção [Install] descreve a qual estado do sistema o serviço faz parte, nesse caso o grupo multi-usuário. Esse estado consiste em:

-Sistema iniciado sem interface gráfica, mas com rede funcionando.
-Todos os serviços comuns de servidor carregados.
-Múltiplos usuários podem se conectar (SSH, console, etc.).

Para testar o serviço pode-se inicializar o systemd e utilizar:
sudo systemctl start card_writer_serv
sudo systemctl stop card_writer_serv


No entanto, isso apenas faz uma execução instantânea do serviço, para habilitá-lo, ou seja, iniciá-lo no sempre que o boot for feito, basta utilizar:

sudo systemctl enable card_writer_serv
sudo systemctl disable card_writer_serv

Caso queira verificar mensagens de erro, não expostas normalmente:

systemctl status card_writer_serv.service

Assim, pode-se desejar alterar o arquivo de serviço. Após as aterações basta carregá-las com:

sudo systemctl daemon-reload
