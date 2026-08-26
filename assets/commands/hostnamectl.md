# TAGLINE

查询和更改系统主机名及相关机器元数据

# TLDR

显示当前**主机名**信息

```hostnamectl```

设置**主机名**

```sudo hostnamectl set-hostname "hostname"```

设置**静态与友好**主机名

```sudo hostnamectl set-hostname --static "hostname.example.com" && sudo hostnamectl set-hostname --pretty "My Computer"```

将**友好主机名**重置为默认

```sudo hostnamectl set-hostname --pretty ""```

设置**机箱类型**

```sudo hostnamectl set-chassis desktop```

设置**部署环境**

```sudo hostnamectl set-deployment production```

# SYNOPSIS

**hostnamectl** [_OPTIONS_] [_COMMAND_]

# DESCRIPTION

**hostnamectl** 查询并更改系统主机名及相关机器元数据。它管理三种主机名：静态（持久化）、友好（人类可读）和瞬态（临时）。

# COMMANDS

**status**
> 显示当前的主机名和机器信息

**hostname [NAME]**
> 获取或设置系统主机名

**set-hostname NAME**
> 设置系统主机名

**set-chassis TYPE**
> 设置机箱类型（desktop、laptop、server、vm、container 等）

**set-deployment ENV**
> 设置部署环境（development、production 等）

**set-location LOC**
> 设置机器的物理位置

**set-icon-name NAME**
> 为图形界面设置图标名称

# PARAMETERS

**--static**
> 仅操作静态主机名

**--transient**
> 仅操作瞬态主机名

**--pretty**
> 仅操作友好主机名

**--no-ask-password**
> 不提示输入密码

**-H, --host**
> 在远程主机上执行操作

**-M, --machine**
> 在容器上执行操作

**-j, --json**
> 以 JSON 格式输出

# HOSTNAME TYPES

**Static**: 保存在 /etc/hostname，重启后保留
**Transient**: 临时的，由 DHCP 或 mDNS 设置
**Pretty**: 用于显示的自由格式 UTF-8 名称

# CAVEATS

静态主机名应为单个有效的 DNS 标签（不含空格，只能使用字母数字和连字符）。友好主机名可以包含任意字符，仅用于显示。

# HISTORY

**hostnamectl** 是 **systemd** 的一部分，通过 systemd-hostnamed 提供统一的主机名管理。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hostname](/man/hostname)(1), [systemctl](/man/systemctl)(1)
