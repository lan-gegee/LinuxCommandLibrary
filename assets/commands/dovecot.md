# TAGLINE

安全的 IMAP 和 POP3 邮件服务器

# TLDR

**启动 Dovecot** 守护进程

```dovecot```

**前台运行**（不守护进程化）

```dovecot -F```

**显示非默认的配置**项

```dovecot -n```

**显示完整配置**（所有设置）

```dovecot -a```

**使用其他配置**文件

```dovecot -c [/path/to/dovecot.conf]```

**不重启而重新加载配置**

```dovecot reload```

**停止 Dovecot** 守护进程

```dovecot stop```

**显示版本**

```dovecot --version```

# SYNOPSIS

**dovecot** [_options_] [_command_]

# PARAMETERS

**-F**
> 前台运行，不守护进程化

**-n**
> 打印非默认配置后退出

**-a**
> 打印所有配置设置后退出

**-c** _config_file_
> 使用指定的配置文件替代 /etc/dovecot/dovecot.conf

**-p**
> 启动时提示输入 SSL 密钥密码

**reload**
> 不重启而重新加载配置

**stop**
> 停止正在运行的守护进程

**--build-options**
> 显示构建选项并退出

**--version**
> 显示版本并退出

# CONFIGURATION

**/etc/dovecot/dovecot.conf**
> 主配置文件，包含协议、身份验证和邮件存储设置。

**/etc/dovecot/conf.d/**
> 模块化配置目录，存放各协议及各功能的具体设置。

# DESCRIPTION

**Dovecot** 是面向类 Unix 系统的开源 IMAP 和 POP3 邮件服务器。它对存储在服务器上的电子邮件提供安全、快速且符合标准的访问。

该服务器支持多种身份验证方法、虚拟用户以及 Maildir 和 mbox 等邮箱格式。其设计兼顾小型与大规模部署，提供配额管理和全文检索等功能。

Dovecot 的模块化架构支持 LDAP 身份验证、Sieve 过滤等插件，并可与邮件系统的其他组件集成。**-F** 标志常用于容器环境或配合进程监督器使用。

# CAVEATS

使用前需正确配置。安全连接需要设置 TLS 证书。邮箱访问常见权限问题。部署更改前先用 **dovecot -n** 校验配置。

# HISTORY

Dovecot 由 **Timo Sirainen** 创建，于 **2002 年**首次发布。它的设计目标是成为现有 IMAP 服务器之外一个安全、快速的替代品，强调正确性和标准符合性。

# INSTALL

```apt: sudo apt install dovecot-core```

```dnf: sudo dnf install dovecot```

```pacman: sudo pacman -S dovecot```

```apk: sudo apk add dovecot```

```zypper: sudo zypper install dovecot```

```brew: brew install dovecot```

```nix: nix profile install nixpkgs#dovecot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[postfix](/man/postfix)(1), [doveadm](/man/doveadm)(1)
