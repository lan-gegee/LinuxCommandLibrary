# TAGLINE

面向 AI 代理的 HTTP 凭据代理与保险库

# TLDR

**启动保险库服务器**与凭据代理（HTTP API + TLS 代理）

```agent-vault server -d```

**运行 AI 代理命令**并透明地代管凭据

```agent-vault vault run -- [claude]```

让任意子进程**经过凭据代理运行**

```agent-vault vault run -- [curl https://api.example.com]```

**停止后台**服务器守护进程

```agent-vault server stop```

**检查版本**

```agent-vault --version```

# SYNOPSIS

**agent-vault** _command_ [_subcommand_] [_options_] [**--** _agent_command_]

# PARAMETERS

**server**
> 启动 HTTP API（默认端口 **14321**）和 TLS 加密的透明 HTTPS 代理（默认端口 **14322**）。

**server** **-d**, **--daemon**
> 以守护进程方式在后台运行服务器。

**server stop**
> 停止正在运行的服务器守护进程。

**vault run** **--** _command_
> 执行 _command_ 并启用凭据代管。自动创建一个限定范围的会话，注入 **HTTPS_PROXY** 和 CA 信任环境变量，并透明地代理对外发出的 HTTPS 请求。

**--config** _FILE_
> 使用替代的配置文件。

**--port** _PORT_
> 覆盖 HTTP API 端口（默认 **14321**）。

**--proxy-port** _PORT_
> 覆盖 HTTPS 代理端口（默认 **14322**）。

**--version**
> 打印 Agent Vault 版本并退出。

**--help**
> 显示 Agent Vault 或某个具体子命令的帮助。

# DESCRIPTION

**agent-vault** 是一款 HTTP 凭据代理与保险库，设计目标是让机密远离 AI 代理，同时不妨碍它们调用需要认证的 API。Agent Vault 不是直接把原始 API 密钥或令牌交给 AI 代理进程，而是把代理作为子进程来运行，并将 **HTTPS_PROXY** 指向本地一个 TLS 终结代理。该代理会为获准的目标地址向外发的 HTTPS 请求注入正确的凭据，AI 代理因此永远看不到机密本身。

服务器在端口 **14321** 上开放 HTTP API（凭据、策略和会话通过 Web UI 管理），并在端口 **14322** 上开放透明 HTTPS 代理。**agent-vault vault run -- <command>** 包装器会派生一个短生命周期的受限会话，在子进程的环境中设置 **HTTPS_PROXY** 和代理的 CA 证书，并在命令退出后销毁该会话。

这缩小了代理遭攻陷或行为失控时的波及范围：即使代理被诱骗外传数据，它也泄露不了自己从未持有过的凭据。

# CONFIGURATION

Web UI 位于 **http://localhost:14321**，用于注册凭据、定义代理会话可以访问哪些主机，以及查看会话活动。服务器会把状态持久化到数据目录下（例如位于 **/data** 的 Docker 卷 **agent-vault-data**）。

# CAVEATS

要求 AI 代理遵守 **HTTPS_PROXY** 环境变量并信任代理的 CA 证书；绕过代理的进程（例如直连 TCP 或使用证书固定）享受不到凭据代管的好处。代理在本地终结 TLS，因此代理与 AI 代理之间的流量是由 Agent Vault 重新加密的，并非端到端直达远端主机。

# HISTORY

**agent-vault** 由 **Infisical** 开发，是其面向 AI 工作负载的机密管理布局的一部分，用于化解让自主代理长期持有凭据的风险。

# SEE ALSO

[vault](/man/vault)(1), [mitmproxy](/man/mitmproxy)(1), [curl](/man/curl)(1)
