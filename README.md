# What is it?

Git-Auto-Deploy consists of a small HTTP server that listens for Webhook requests sent from GitHub, GitLab or Bitbucket servers. This application allows you to continuously and automatically deploy your projects each time you push new commits to your repository.</p>

![workflow](https://cloud.githubusercontent.com/assets/1056476/9344294/d3bc32a4-4607-11e5-9a44-5cd9b22e61d9.png)

# Languages
- [Português Brasil](./docs/pt-BR/README.md)
- [English](#)

# How does it work?

When commits are pushed to your Git repository, the Git server will notify ```Git-Auto-Deploy``` by sending an HTTP POST request with a JSON body to a pre-configured URL (your-host:8001). The JSON body contains detailed information about the repository and what event that triggered the request. ```Git-Auto-Deploy``` parses and validates the request, and if all goes well it issues a ```git pull```.

Additionally, ```Git-Auto-Deploy``` can be configured to execute a shell command upon each successful ```git pull```, which can be used to trigger custom build actions or test scripts.</p>

# Getting started

You can install ```Git-Auto-Deploy``` in multiple ways. Below are instructions for the most common methods.

## Install from repository (recommended for other systems)

When installing ```Git-Auto-Deploy``` from the repository, you'll need to make sure that Python (tested on version 3.9) and Git (tested on version 2.x) is installed on your system.

Clone the repository.

    git clone https://github.com/CDTeamMods/Git-Auto-Deploy.git

Install the dependencies with [pip](http://www.pip-installer.org/en/latest/), a package manager for Python, by running the following command.

    sudo pip install -r requirements.txt

If you don't have pip installed, try installing it by running this from the command
line:

    curl https://bootstrap.pypa.io/get-pip.py | python

Copy of the sample config and modify it. Read more about the configuration options. Make sure that ```pidfilepath``` is writable for the user running the script, as well as all paths configured for your repositories.

    cd Git-Auto-Deploy
    cp config.json.sample config.json

Start ```Git-Auto-Deploy``` manually using;

    python run.py --config config.json

To start ```Git-Auto-Deploy``` automatically on boot, open crontab in edit mode using ```crontab -e``` and add the entry below.

    @reboot /usr/bin/python /path/to/Git-Auto-Deploy/run.py --daemon-mode --quiet --config /path/to/git-auto-deploy.conf.json

You can also configure ```Git-Auto-Deploy``` to start on boot using an init.d-script (for Debian and Sys-V like init systems) or a service for systemd.Read more about starting Git-Auto-Deploy automatically using init.d or systemd.

## Command line options

Below is a summarized list of the most common command line options. For a full list of available command line options, invoke the application with the argument ```--help``` or read the documentation article about all available command line options, environment variables and config attributes.

Command line option    | Environment variable | Config attribute | Description
---------------------- | -------------------- | ---------------- | --------------------------
--daemon-mode (-d)     | GAD_DAEMON_MODE      |                  | Run in background (daemon mode)
--quiet (-q)           | GAD_QUIET            |                  | Supress console output
--config (-c) <path>   | GAD_CONFIG           |                  | Custom configuration file
--pid-file <path>      | GAD_PID_FILE         | pidfilepath      | Specify a custom pid file
--log-file <path>      | GAD_LOG_FILE         | logfilepath      | Specify a log file
--log-level <level>    |                      | log-level        | Specify log level (default: INFO)
--host <host>          | GAD_HOST             | host             | Address to bind to
--port <port>          | GAD_PORT             | port             | Port to bind to

### Log Levels
Available log levels (from least to most verbose):
* `CRITICAL`
* `ERROR`
* `WARNING`
* `INFO` (default)
* `DEBUG`
* `NOTSET`

## Getting webhooks from git
To make your git provider send notifications to ```Git-Auto-Deploy``` you will need to provide the hostname and port for your ```Git-Auto-Deploy``` instance. Instructions for the most common git providers is listed below.

**GitHub**
1. Go to your repository -> Settings -> Webhooks -> Add webhook</li>
2. In "Payload URL", enter your hostname and port (your-host:8001)
3. Hit "Add webhook"

**GitLab**
1. Go to your repository -> Settings -> Web hooks
2. In "URL", enter your hostname and port (your-host:8001)
3. Hit "Add Web Hook"

**Bitbucket**
1. Go to your repository -> Settings -> Webhooks -> Add webhook
2. In "URL", enter your hostname and port (your-host:8001)
3. Hit "Save"

# Web Interface
Git-Auto-Deploy comes with a built-in Web Interface that allows you to monitor the status of your deployments.

To enable the Web Interface, update your `config.json`:
```json
{
    "web-ui-enabled": true,
    "web-ui-username": "admin",
    "web-ui-password": "your-password",
    "web-ui-whitelist": ["127.0.0.1"]
}
```
By default, the Web UI is accessible at `https://your-host:8001/` (requires HTTPS configuration) or `http://your-host:8001/` if HTTPS is disabled (not recommended for production).