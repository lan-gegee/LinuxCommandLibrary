# TLDR

**启动 ssh-agent** 并设置环境变量

```eval $(ssh-agent)```

为当前 Shell **在后台启动代理**

```ssh-agent -s```

**以 C-shell 兼容输出**启动

```ssh-agent -c```

**杀死正在运行的代理**

```ssh-agent -k```

在代理环境中**运行命令**

```ssh-agent [command]```

**设置密钥生命周期**（默认永久）

```ssh-agent -t [1h]```

# SYNOPSIS

**ssh-agent** [**-c** | **-s**] [**-Dd**] [**-a** _SOCKET_] [**-t** _LIFE_] [_COMMAND_ [_ARGS_...]]

**ssh-agent** [**-c** | **-s**] **-k**

# PARAMETERS

**-s**
> 在 stdout 上生成 Bourne shell 命令。

**-c**
> 在 stdout 上生成 C-shell 命令。

**-k**
> 杀死当前代理（使用 SSH_AGENT_PID）。

**-d**
> 调试模式（不 fork）。

**-D**
> 前台模式，无调试输出。

**-a** _SOCKET_
> 绑定到指定的 Unix 套接字而非随机套接字。

**-t** _LIFE_
> 所添加密钥的默认最长生命周期（例如 1h、30m）。

# DESCRIPTION

**ssh-agent** 是一个保存用于 SSH 公钥认证的私钥的程序。代理在后台运行，向 SSH 客户端提供密钥，无需重复输入口令。

密钥通过 **ssh-add** 添加到代理。添加后，代理会响应来自 SSH 连接的认证请求，包括从远程主机转发而来的代理连接。

代理会输出设置环境变量（SSH_AUTH_SOCK 和 SSH_AGENT_PID）的 shell 命令。必须用 **eval $(ssh-agent)** 在 shell 中执行这些命令，SSH 客户端才能与代理通信。

# CAVEATS

代理将解密后的私钥保存在内存中。一旦被攻破，所有已加载的密钥都会暴露。请用 **-t** 限制密钥生命周期。代理转发（ssh 的 -A 选项）应谨慎使用，因为远程主机可以借用你的代理。处理完敏感会话后请杀死代理。

# HISTORY

ssh-agent 作为 OpenSSH 的一部分开发而来；OpenSSH 最初由 Tatu Ylönen 创建，后来由 OpenBSD 项目维护。代理模型既能安全存储密钥，又能实现免密 SSH 连接，已成为所有主流平台上管理 SSH 密钥的标准方式。

# INSTALL

```apt: sudo apt install openssh-client```

```apk: sudo apk add openssh-client-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh-add](/man/ssh-add)(1), [ssh](/man/ssh)(1), [ssh-keygen](/man/ssh-keygen)(1), [sshd](/man/sshd)(8)

# RESOURCES

```[Source code](https://github.com/openssh/openssh-portable)```

```[Homepage](https://www.openssh.com/)```

<!-- verified: 2026-06-10 -->
