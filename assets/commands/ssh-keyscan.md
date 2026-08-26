# TAGLINE

从服务器收集 SSH 公开主机密钥

# TLDR

**扫描主机获取密钥**

```ssh-keyscan [hostname]```

**扫描指定端口**

```ssh-keyscan -p [port] [hostname]```

**扫描特定密钥类型**

```ssh-keyscan -t ed25519 [hostname]```

**从文件扫描多台主机**

```ssh-keyscan -f [hosts_file]```

**以哈希主机名追加到 known_hosts**

```ssh-keyscan -H [hostname] >> ~/.ssh/known_hosts```

**以 SSHFP DNS 记录格式打印密钥**

```ssh-keyscan -D [hostname]```

# SYNOPSIS

**ssh-keyscan** [_options_] [_host_...]

# PARAMETERS

**-4**
> 仅使用 IPv4 地址。

**-6**
> 仅使用 IPv6 地址。

**-c**
> 向目标主机请求证书而不是普通密钥。

**-D**
> 将找到的密钥以 SSHFP DNS 记录格式输出。

**-f** _file_
> 从文件读取主机列表（`-` 表示 stdin）。

**-H**
> 对输出中的主机名和地址做哈希处理。

**-p** _port_
> 连接远程主机的指定端口。

**-q**
> 静默模式；抑制输出中的注释。

**-t** _type_
> 要获取的密钥类型：rsa、ed25519、ecdsa、ecdsa-sk 或 ed25519-sk。可用逗号分隔多种类型。

**-T** _timeout_
> 连接超时时间，以秒为单位（默认 5）。

**-v**
> 详细模式；打印调试信息。

# DESCRIPTION

**ssh-keyscan** 是一个从远程服务器收集 SSH 公开主机密钥的工具。它连接到每台指定的主机并获取服务器的公钥，以适合追加到 **~/.ssh/known_hosts** 或 **/etc/ssh/ssh_known_hosts** 文件的格式输出。

该工具主要用于在首次连接时人工接受主机密钥不现实的环境中自动化分发主机密钥。它可以并行扫描多台主机、从文件读取主机列表，并按密钥类型（RSA、Ed25519、ECDSA）过滤。**-H** 选项会对输出中的主机名做哈希处理，提供额外的隐私保护。

# INSTALL

```apt: sudo apt install openssh-client```

```apk: sudo apk add openssh-client-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [ssh-keygen](/man/ssh-keygen)(1)
