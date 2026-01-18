# O que é isso?

O Git-Auto-Deploy consiste em um pequeno servidor HTTP que escuta requisições Webhook enviadas por servidores GitHub, GitLab ou Bitbucket. Esta aplicação permite que você implante seus projetos de forma contínua e automática cada vez que você envia novos commits para o seu repositório.</p>

![fluxo de trabalho](https://cloud.githubusercontent.com/assets/1056476/9344294/d3bc32a4-4607-11e5-9a44-5cd9b22e61d9.png)

# Traduções:
- [Português Brasil](#)
- [English](../../README.md)

# Como funciona?

Quando commits são enviados para o seu repositório Git, o servidor Git notificará o ```Git-Auto-Deploy``` enviando uma requisição HTTP POST com um corpo JSON para uma URL pré-configurada (seu-host:8001). O corpo JSON contém informações detalhadas sobre o repositório e qual evento acionou a requisição. O ```Git-Auto-Deploy``` analisa e valida a requisição e, se tudo correr bem, executa um ```git pull```.

Além disso, o ```Git-Auto-Deploy``` pode ser configurado para executar um comando shell após cada ```git pull``` bem-sucedido, o que pode ser usado para acionar ações de build personalizadas ou scripts de teste.</p>

# Começando

Você pode instalar o ```Git-Auto-Deploy``` de várias maneiras. Abaixo estão as instruções para os métodos mais comuns.

## Instalar do repositório (recomendado para outros sistemas)

Ao instalar o ```Git-Auto-Deploy``` a partir do repositório, você precisará garantir que o Python (testado na versão 3.9) e o Git (testado na versão 2.x) estejam instalados no seu sistema.

Clone o repositório.

    git clone https://github.com/CDTeamMods/Git-Auto-Deploy.git

Instale as dependências com o [pip](http://www.pip-installer.org/en/latest/), um gerenciador de pacotes para Python, executando o seguinte comando.

    pip install -r requirements.txt

Se você não tiver o pip instalado, tente instalá-lo executando isto na linha de comando:

    curl https://bootstrap.pypa.io/get-pip.py | python

Copie o exemplo de configuração e modifique-o. Leia mais sobre as opções de configuração. Certifique-se de que o ```pid-file``` seja gravável para o usuário que executa o script, bem como todos os caminhos configurados para seus repositórios.

    cd Git-Auto-Deploy
    cp config.json.sample config.json

Inicie o ```Git-Auto-Deploy``` manualmente usando;

    python run.py --config config.json

Para iniciar o ```Git-Auto-Deploy``` automaticamente na inicialização, abra o crontab no modo de edição usando ```crontab -e``` e adicione a entrada abaixo.

    @reboot /usr/bin/python /path/to/Git-Auto-Deploy/run.py --daemon-mode --quiet --config /path/to/git-auto-deploy.conf.json

Você também pode configurar o ```Git-Auto-Deploy``` para iniciar na inicialização usando um script init.d (para sistemas init como Debian e Sys-V) ou um serviço para systemd. Leia mais sobre como iniciar o Git-Auto-Deploy automaticamente usando init.d ou systemd.

## Opções de linha de comando

Abaixo está uma lista resumida das opções de linha de comando mais comuns. Para uma lista completa das opções de linha de comando disponíveis, invoque a aplicação com o argumento ```--help``` ou leia o artigo da documentação sobre todas as opções de linha de comando disponíveis, variáveis de ambiente e atributos de configuração.

Opção de linha de comando | Variável de ambiente | Atributo de configuração | Descrição
---------------------- | -------------------- | ---------------- | --------------------------
--daemon-mode (-d)     | GAD_DAEMON_MODE      |                  | Executar em segundo plano (modo daemon)
--quiet (-q)           | GAD_QUIET            |                  | Suprimir saída do console
--config (-c) <path>   | GAD_CONFIG           |                  | Arquivo de configuração personalizado
--pid-file <path>      | GAD_PID_FILE         | pidfilepath      | Especificar um arquivo pid personalizado
--log-file <path>      | GAD_LOG_FILE         | logfilepath      | Especificar um arquivo de log
--log-level <level>    |                      | log-level        | Especificar nível de log (padrão: INFO)
--host <host>          | GAD_HOST             | host             | Endereço para vincular
--port <port>          | GAD_PORT             | port             | Porta para vincular

### Níveis de Log
Níveis de log disponíveis (do menos para o mais detalhado):
* `CRITICAL`
* `ERROR`
* `WARNING`
* `INFO` (padrão)
* `DEBUG`
* `NOTSET`

## Recebendo webhooks do git
Para fazer seu provedor git enviar notificações para o ```Git-Auto-Deploy```, você precisará fornecer o nome do host e a porta para sua instância do ```Git-Auto-Deploy```. Instruções para os provedores git mais comuns estão listadas abaixo.

**GitHub**
1. Vá para o seu repositório -> Settings -> Webhooks -> Add webhook</li>
2. Em "Payload URL", digite seu nome de host e porta (seu-host:8001)
3. Clique em "Add webhook"

**GitLab**
1. Vá para o seu repositório -> Settings -> Web hooks
2. Em "URL", digite seu nome de host e porta (seu-host:8001)
3. Clique em "Add Web Hook"

# Interface Web
O Git-Auto-Deploy vem com uma Interface Web integrada que permite monitorar o status de suas implantações.

Para habilitar a Interface Web, atualize seu `config.json`:
```json
{
    "web-ui-enabled": true,
    "web-ui-username": "admin",
    "web-ui-password": "your-password",
    "web-ui-whitelist": ["127.0.0.1"]
}
```
Por padrão, a Interface Web é acessível em `https://seu-host:8001/` (requer configuração HTTPS) ou `http://seu-host:8001/` se HTTPS estiver desabilitado (não recomendado para produção).

## Desenvolvimento (Web UI)

A Interface Web é construída com React e Vite. Para contribuir ou modificar a Interface Web:

1.  **Inicie o backend Python**:
    ```bash
    python -m gitautodeploy
    ```
2.  **Inicie o servidor de desenvolvimento Frontend**:
    ```bash
    cd webui
    npm install
    npm run dev
    ```
    Acesse `http://localhost:3000`. O servidor Vite está configurado para redirecionar requisições de API para o backend Python rodando na porta 8001.

3.  **Compilar para Produção**:
    Para atualizar os arquivos estáticos servidos pelo Python:
    ```bash
    cd webui
    npm install
    npm run build
    ```
    Isso compilará o aplicativo React e colocará a saída em `gitautodeploy/wwwroot`.
