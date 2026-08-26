# TAGLINE

自动安全更新安装器

# TLDR

手动**运行无人值守升级**

```sudo unattended-upgrades```

**模拟升级**而不实际安装（dry run）

```sudo unattended-upgrades --dry-run```

**以详细输出运行**

```sudo unattended-upgrades -v```

**以调试输出运行**

```sudo unattended-upgrades -d```

交互式**配置自动更新**

```sudo dpkg-reconfigure -plow unattended-upgrades```

**检查自动更新是否已启用**

```cat /etc/apt/apt.conf.d/20auto-upgrades```

# SYNOPSIS

**unattended-upgrades** [**-d**] [**-v**] [**--dry-run**] [**--minimal-upgrade-steps**]

# PARAMETERS

**-d**, **--debug**
> 启用额外的调试输出，写入 /var/log/unattended-upgrades/unattended-upgrades.log。

**-v**, **--verbose**
> 运行期间显示详细输出。

**--dry-run**
> 模拟升级过程而不实际安装软件包。

**--apt-debug**
> 启用详细的 APT/LibAPT 输出以便调试。

**--minimal-upgrade-steps**
> 以最小步骤执行升级，允许在软件包之间通过 SIGINT 取消。这是默认行为。

**--no-minimal-upgrade-steps**
> 不使用最小步骤执行升级（一次性升级所有软件包）。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**unattended-upgrades** 在 Debian 和 Ubuntu 系统上自动安装安全更新，也可选择安装其他更新。它每天通过 systemd 定时器（apt-daily.timer 和 apt-daily-upgrade.timer）运行，无需人工干预即可保持系统得到修补。

该工具通过 APT 配置文件进行配置：主要是 /etc/apt/apt.conf.d/50unattended-upgrades 用于配置允许的来源和选项，/etc/apt/apt.conf.d/20auto-upgrades 用于启用自动更新。默认情况下只自动安装安全更新。

配置选项包括电子邮件通知、自动移除不再使用的依赖、需要时自动重启，以及将特定软件包列入黑名单以排除在自动更新之外。该工具将其活动记录到 /var/log/unattended-upgrades/。

**unattended-upgrades** 与 **unattended-upgrade** 两个命令的作用完全相同；其中一个是另一个的符号链接。

# CONFIGURATION

**/etc/apt/apt.conf.d/50unattended-upgrades**
> 主配置文件，指定允许的来源、软件包黑名单、电子邮件通知和重启行为。

**/etc/apt/apt.conf.d/20auto-upgrades**
> 控制是否启用自动更新和无人值守升级。

**/var/log/unattended-upgrades/**
> 日志目录，包含升级历史和调试信息。

# CAVEATS

如果软件包包含破坏性更改或需要手动配置，自动更新可能引发问题。对于生产服务器，应慎重考虑自动重启。某些需要配置提示的软件包可能会被保留不更新。请定期检查日志以确保更新成功应用。

# HISTORY

**unattended-upgrades** 为 **Debian** 和 **Ubuntu** 开发，用于自动化安全补丁管理。它成为 Ubuntu 的默认自动更新机制，至少自 **Ubuntu 16.04** 起默认包含。该工具从基于 cron 的执行演进为 systemd 定时器，以实现更可靠的调度以及与现代 init 系统更好的集成。

# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [dpkg](/man/dpkg)(1), [systemctl](/man/systemctl)(1)
