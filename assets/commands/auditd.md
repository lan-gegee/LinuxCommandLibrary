# TAGLINE

用于追踪安全相关事件的 Linux 审计守护进程。

# TLDR

**启动**审计守护进程

```sudo auditd```

在前台运行以便调试

```sudo auditd -f```

**不 fork**（供 systemd 或 inittab 使用）

```sudo auditd -n```

使用**备用配置目录**

```sudo auditd -c [/path/to/config_dir]```

启动时不修改内核的**启用标志**

```sudo auditd -s nochange```

# SYNOPSIS

**auditd** [_-f_] [_-l_] [_-n_] [_-s disable|enable|nochange_] [_-c config_dir_]

# DESCRIPTION

**auditd** 是 Linux 审计守护进程，它从内核收集审计事件并写入磁盘。它是 Linux 审计框架的一部分，用于追踪安全相关事件。

守护进程根据配置的规则记录文件访问、系统调用、认证事件及其他活动。

# PARAMETERS

**-f**
> 让守护进程保持在前台运行以便调试。消息同时输出到 stderr 而非审计日志。

**-l**
> 允许守护进程在读取配置文件时跟随符号链接。

**-n**
> 不 fork。适合从 inittab 或 systemd 运行。

**-s** _disable|enable|nochange_
> 在启动时设置内核审计启用标志的状态。默认行为是启动时启用该标志、终止时禁用它。该标志也可通过 **auditctl** 在运行时更改。

**-c** _config_dir_
> 使用备用配置目录。同一目录也会传递给分发器（默认：/etc/audit/）。

# CONFIGURATION

**/etc/audit/auditd.conf**
> 主配置文件，控制日志文件位置、保留策略、磁盘空间处理和分发器设置。

**/etc/audit/rules.d/**
> 存放审计规则文件的目录，由 **augenrules** 编译成生效的规则集。规则定义要监控哪些系统调用和文件访问。

**/etc/audit/plugins.d/**
> 插件（分发器）配置文件目录，用于将事件路由到外部程序。

# CAVEATS

需要 root 权限。高强度的审计会影响性能，且详细规则会让日志快速增长。在现代系统上，应通过服务管理器（例如 **systemctl** 或 **service auditd rotate**）来启动、停止和重载守护进程，而不是直接发送信号。

# HISTORY

**auditd** 作为 Linux Audit 项目的一部分开发，旨在满足 Common Criteria 安全要求，并于 **2.6.6**（2004 年）进入主线内核。

# INSTALL

```apt: sudo apt install auditd```

```dnf: sudo dnf install audit```

```pacman: sudo pacman -S audit```

```apk: sudo apk add audit```

```zypper: sudo zypper install audit```

```nix: nix profile install nixpkgs#audit```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[auditctl](/man/auditctl)(8), [ausearch](/man/ausearch)(8), [aureport](/man/aureport)(8)

# RESOURCES

```[Source code](https://github.com/linux-audit/audit-userspace)```

<!-- verified: 2026-06-17 -->
