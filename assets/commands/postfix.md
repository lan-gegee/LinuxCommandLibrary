# TAGLINE

控制 Postfix 邮件系统

# TLDR

**检查**配置

```sudo postfix check```

检查**状态**

```sudo postfix status```

**启动** Postfix

```sudo postfix start```

**优雅地停止**

```sudo postfix stop```

**清空**邮件队列

```sudo postfix flush```

**重新加载**配置

```sudo postfix reload```

# SYNOPSIS

**postfix** [**-c** _config_dir_] [**-D**] _command_

# COMMANDS

**check**
> 校验配置是否有错误

**start**
> 启动 Postfix 邮件系统

**stop**
> 停止 Postfix 邮件系统

**abort**
> 立即停止，不等待投递完成

**flush**
> 强制投递队列中的邮件

**reload**
> 不重启而重新加载配置

**status**
> 检查 Postfix 是否正在运行

# PARAMETERS

**-c _config_dir_**
> 备用配置目录

**-D**
> 调试模式

# DESCRIPTION

**postfix** 是 Postfix 邮件传输代理的控制程序。它负责管理邮件系统组件的启动、停止和重新配置。

Postfix 以安全和高性能为设计目标，以最小权限运行多个相互独立的进程。控制程序负责协调这些进程。

# CONFIGURATION

**/etc/postfix/main.cf**
> 主配置文件，定义主机名、域、中继设置、网络限制、TLS 以及所有主要的 Postfix 参数。

**/etc/postfix/master.cf**
> 定义 Postfix 服务组件（smtpd、cleanup、local 等）及其进程数限制、chroot 设置和命令行选项。

**/etc/postfix/virtual**
> 用于电子邮件地址改写的虚拟别名映射。更改后需要用 **postmap** 重建数据库。

**/etc/postfix/transport**
> 按目标域控制邮件路由。编辑后需要用 **postmap** 重建。

# CAVEATS

大多数命令需要 root 权限。邮件队列在重启后仍然保留。重新加载前请先检查配置。abort 可能丢失传输途中的邮件。

# HISTORY

**Postfix** 由 IBM 研究院的 **Wietse Venema** 编写，作为 Sendmail 的安全、快速替代方案。它于 1998 年发布，凭借安全设计和配置简便成为最受欢迎的 MTA 之一。

# INSTALL

```apt: sudo apt install postfix```

```dnf: sudo dnf install postfix```

```pacman: sudo pacman -S postfix```

```apk: sudo apk add postfix```

```zypper: sudo zypper install postfix```

```nix: nix profile install nixpkgs#postfix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[postconf](/man/postconf)(1), [postqueue](/man/postqueue)(1), [sendmail](/man/sendmail)(8)
