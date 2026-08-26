# TAGLINE

控制和管理 Prosody XMPP 服务器

# TLDR

**启动服务器**

```prosodyctl start```

**停止服务器**

```prosodyctl stop```

**检查状态**

```prosodyctl status```

**添加用户**

```prosodyctl adduser [user@domain.com]```

**删除用户**

```prosodyctl deluser [user@domain.com]```

**更改密码**

```prosodyctl passwd [user@domain.com]```

**检查配置**

```prosodyctl check```

**重载配置**

```prosodyctl reload```

# SYNOPSIS

**prosodyctl** [_options_] _command_ [_args_]

# PARAMETERS

**start**
> 启动 Prosody。

**stop**
> 停止 Prosody。

**restart**
> 重启 Prosody。

**status**
> 显示状态。

**reload**
> 重载配置。

**adduser** _JID_
> 创建用户账户。

**deluser** _JID_
> 删除用户账户。

**passwd** _JID_
> 更改密码。

**check**
> 校验配置。

**about**
> 版本和路径信息。

**cert** _subcommand_ _hosts_
> 证书管理（request、generate、key、import）。

**register** _USER_ _HOST_ _PASSWORD_
> 以非交互方式注册用户。

**unregister** _USER_ _HOST_
> 以非交互方式注销用户。

**shell**
> 打开 Prosody 管理 shell，用于运行时检查。

**--config** _filename_
> 使用指定的配置文件而非默认文件。

**--verbose**
> 提高日志级别以显示调试信息。

**--quiet**
> 降低日志级别，只显示错误。

# DESCRIPTION

**prosodyctl** 是 Prosody XMPP/Jabber 服务器的管理工具，可从命令行进行服务控制、用户管理和配置校验。它可以启动、停止、重启和重载服务器，其中 reload 可在不断开用户连接的情况下应用配置变更。

用户管理命令负责 XMPP 账户的生命周期：用 **adduser** 创建账户、用 **deluser** 移除账户、用 **passwd** 重置密码。所有用户操作都使用 JID（Jabber ID）格式，例如 **user@domain.com**。

**check** 命令在应用更改之前校验 Prosody 配置、DNS 记录和 TLS 证书，捕获常见的设置错误。证书管理命令帮助导入、生成和检查安全 XMPP 连接所需的 TLS 证书。

# CAVEATS

大多数操作需要 root 或相应权限。status、reload 和 shell 等命令要求 Prosody 正在运行。用户管理命令需要 JID 格式（user@domain）。

# HISTORY

**Prosody** 由 **Matthew Wild** 于 **2008 年**启动开发，是一个轻量级 XMPP 服务器。它以模块化、符合标准和内存占用低著称。

# INSTALL

```apt: sudo apt install prosody```

```dnf: sudo dnf install prosody```

```pacman: sudo pacman -S prosody```

```apk: sudo apk add prosody```

```zypper: sudo zypper install prosody```

```nix: nix profile install nixpkgs#prosody```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ejabberdctl](/man/ejabberdctl)(1), [prosody](/man/prosody)(8)
