# TAGLINE

通用 TLS/SSL 隧道代理

# TLDR

**使用配置文件启动 stunnel**

```stunnel [/etc/stunnel/stunnel.conf]```

**从文件描述符读取配置**（例如 stdin）

```stunnel -fd [0]```

**显示版本与编译期默认值**

```stunnel -version```

**显示可用的套接字选项**

```stunnel -sockets```

**显示可用的 TLS 选项**

```stunnel -options```

**显示帮助**

```stunnel -help```

# SYNOPSIS

**stunnel** [_configfile_] | **-fd** _n_ | **-help** | **-version** | **-sockets** | **-options**

# PARAMETERS

**configfile**
> 要使用的配置文件路径

**-fd** _n_
> 从文件描述符 _n_ 读取配置（仅限 Unix）

**-help**
> 显示帮助消息

**-version**
> 显示版本信息和编译期默认值

**-sockets**
> 显示默认套接字选项

**-options**
> 显示 OpenSSL 编译支持的 TLS/SSL 选项

# CONFIGURATION

Stunnel 完全由配置文件驱动。文件采用 INI 风格语法：全局指令位于顶部，之后是一个或多个以 `[service_name]` 块表示的命名服务节区。以 `;` 开头的行是注释。

**全局指令（节选）**

**foreground**
> 让进程保持在前台运行，并将日志输出到 stderr 而不是 syslog。取值：`yes | no`。默认：`no`

**pid**
> PID 文件路径。空值表示不创建 PID 文件。若设置了 `chroot`，路径相对于 `chroot` 目录（仅限 Unix）

**chroot**
> Chroot 监禁目录。Stunnel 在启动后放弃特权并将根目录切换到该目录（仅限 Unix）

**setuid**
> 启动后用于运行进程的 Unix 用户（仅限 Unix）

**setgid**
> 启动后用于运行进程的 Unix 组（仅限 Unix）

**debug**
> 日志详细程度级别。格式：`[FACILITY.]LEVEL`。级别：emerg(0)、alert(1)、crit(2)、err(3)、warning(4)、notice(5)、info(6)、debug(7)。默认：`notice`

**output**
> 将日志消息追加到指定文件而不是 syslog

**syslog**
> 启用或禁用记录到 syslog。取值：`yes | no`。默认：`yes`

**服务级指令（节选）**

**accept**
> 在指定地址上接受连接。格式：`[HOST:]PORT`。inetd 模式下省略 `accept`

**connect**
> 将连接转发到指定地址。格式：`[HOST:]PORT`。默认主机为 `localhost`。支持多条目以实现轮询负载均衡

**client**
> 启用客户端模式——远端应讲 TLS 协议。取值：`yes | no`。默认：`no`（服务器模式）

**cert**
> PEM 或 PKCS#12 证书链文件的路径。服务器模式下必需；客户端模式下可选，除非服务器要求客户端证书

**key**
> 私钥文件路径。省略时默认使用 `cert` 的值。该文件应仅允许所有者读取

**CAfile**
> 从文件加载受信任的 CA 证书。与 `verifyChain` 或 `verifyPeer` 配合使用

**CApath**
> 从目录加载受信任的 CA 证书。证书文件必须按 OpenSSL 哈希格式命名（`XXXXXXXX.0`）

**verifyChain**
> 从受信任的根 CA 开始验证对端证书链。取值：`yes | no`。默认：`no`

**verifyPeer**
> 验证终端实体（叶子）对端证书。取值：`yes | no`。默认：`no`

**checkHost**
> 验证对端证书使用者可选名称中的主机名。允许多条目。需要 OpenSSL 1.0.2+

**sni**
> 服务器名称指示（SNI）。客户端模式：要发送的 SNI 主机名。服务器模式：`SERVICE_NAME:SERVER_NAME_PATTERN`，用于虚拟主机。需要 OpenSSL 1.0.0+

**protocol**
> 用于协商 TLS 的应用层协议。支持：`cifs`、`connect`、`imap`、`ldap`、`nntp`、`pgsql`、`pop3`、`proxy`、`smtp`、`socks`

**exec**
> 执行本地 inetd 风格的程序，而不是连接远程主机。程序的标准输入/标准输出用作隧道未加密一侧

**execArgs**
> 传给 `exec` 的以空白分隔的参数列表，包括作为 `$0` 的程序名

**delay**
> 推迟 `connect` 的 DNS 解析，直到有客户端连接。取值：`yes | no`。默认：`no`

**ciphers**
> 允许使用的 TLS 1.2 及更早版本密码套件的冒号分隔列表

**ciphersuites**
> TLS 1.3 密码套件的冒号分隔列表。默认：`TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_AES_128_GCM_SHA256`。需要 OpenSSL 1.1.1+

**sslVersionMin**
> 最低 TLS 协议版本。需要 OpenSSL 1.1.0+。默认：`TLSv1`

**sslVersionMax**
> 最高 TLS 协议版本。需要 OpenSSL 1.1.0+。默认：`all`

**securityLevel**
> OpenSSL 安全级别（0–5）。级别 2 要求至少 112 位安全强度（默认）。需要 OpenSSL 1.1.0+

**transparent**
> 启用透明代理模式。取值：`none`、`source`、`destination`、`both`。需要内核和路由支持（仅限 Unix）

**socket**
> 设置套接字选项。格式：`a|l|r:OPTION=VALUE[:VALUE]`，其中 `a`=接受套接字、`l`=本地套接字、`r`=远程套接字

# DESCRIPTION

**stunnel** 是一个 TLS/SSL 代理，可为任意 TCP 连接加上加密，而无需修改应用程序代码。它使用 OpenSSL 执行所有加密操作并支持现代 TLS 版本。

在**服务器模式**（默认）下，stunnel 监听传入的 TLS 加密连接，并将其解密后转发给后端服务（例如纯文本的 IMAP 或 SMTP 守护进程）。在**客户端模式**（`client = yes`）下，它接受来自本地客户端的未加密连接，并与远程 TLS 服务器建立 TLS 加密隧道。

Stunnel 读取一个包含全局设置和一个或多个命名服务节区的配置文件。每个服务节区定义一条独立的隧道。单个 stunnel 进程内可以运行多条隧道。

它支持 inetd 风格运行（省略 `accept`；stunnel 继承套接字）、守护进程模式以及由 systemd 启动。Unix 信号控制运行中的守护进程：`SIGHUP` 重新加载配置，`SIGUSR1` 重新打开日志文件，`SIGTERM`/`SIGQUIT`/`SIGINT` 关闭守护进程。

**FTP 限制**：stunnel 无法为 FTP 数据通道建立隧道，因为 FTP 使用动态协商的第二端口。

# EXAMPLES

**用 TLS 包裹纯文本 IMAP 守护进程（服务器模式）**

```
[imapd]
accept  = 993
exec    = /usr/sbin/imapd
execArgs = imapd
cert    = /etc/stunnel/server.pem
```

**将加密 IMAP 转发到本地的明文守护进程（服务器模式）**

```
[imapd]
accept  = 993
connect = 143
cert    = /etc/stunnel/server.pem
```

**包裹发往远程 TLS 服务器的出站连接（客户端模式）**

```
[imap-client]
client  = yes
accept  = 127.0.0.1:143
connect = mail.example.com:993
```

**SOCKS 代理隧道（客户端与服务器配对）**

```
; Server side
[socks-server]
protocol = socks
accept   = 9080
cert     = /etc/stunnel/server.pem

; Client side
[socks-client]
client   = yes
accept   = 127.0.0.1:1080
connect  = vpnserver.example.com:9080
verifyChain = yes
CAfile   = /etc/stunnel/ca.pem
```

# CAVEATS

由于已知的安全漏洞，SSLv2 和 SSLv3 默认被禁用。生产环境的客户端配置应启用证书链验证（`verifyChain = yes`）和主机名检查（`checkHost`），以防中间人攻击。透明代理模式需要特定的内核支持和路由配置。当应用程序允许攻击者控制明文时，`compression` 选项存在安全风险（CRIME 式攻击）。

# HISTORY

stunnel 由 **Michał Trojnara** 于 **1998 年**创建，是面向 TCP 服务的通用 TLS 包装器。它至今仍在积极开发中，支持现代 TLS 1.3 和当前的 OpenSSL API。

# INSTALL

```apt: sudo apt install stunnel4```

```dnf: sudo dnf install stunnel```

```pacman: sudo pacman -S stunnel```

```apk: sudo apk add stunnel```

```zypper: sudo zypper install stunnel```

```brew: brew install stunnel```

```nix: nix profile install nixpkgs#stunnel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [openssl-s_client](/man/openssl-s_client)(1), [certbot](/man/certbot)(1), [socat](/man/socat)(1), [haproxy](/man/haproxy)(1)
