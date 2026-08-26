# TAGLINE

将文件从 Proxmox LXC 容器复制到主机

# TLDR

将文件从容器**拉取**到本地主机

```pct pull 100 /var/log/app.log ./app.log```

拉取配置文件并设置**宿主所有权**

```pct pull 100 /etc/myapp/config.yml ./config.yml --user root --group root```

以**显式权限**拉取

```pct pull 100 /tmp/report.pdf ./report.pdf --perms 0644```

# SYNOPSIS

**pct pull** _vmid_ _path_ _destination_ [_OPTIONS_]

# PARAMETERS

**vmid**
> 容器的数字 ID（100–999999999）

**path**
> 容器内要拉取的文件路径

**destination**
> 本地（宿主）系统上的目标路径

**--user** _name|id_
> 写入的宿主文件的所有者用户名或 ID

**--group** _name|id_
> 写入的宿主文件的所有者组名或 ID

**--perms** _mode_
> 文件权限（默认为八进制；加 **0x** 前缀表示十六进制）

# DESCRIPTION

**pct pull** 将单个文件从 Proxmox VE LXC 容器复制到宿主文件系统。它是 **pct push** 的反向操作：源路径位于容器内，目标路径位于运行 **pct** 的节点上。

适用于在不挂载容器根文件系统或打开交互式 shell 的情况下获取日志、配置或构建产物。可通过 **--user**、**--group** 和 **--perms** 设置宿主侧副本的所有者和权限模式。

# CAVEATS

一次只能复制一个文件（不支持递归目录）。容器必须可从本地节点访问；没有单独的网络/远程拉取模式。路径按容器的文件系统命名空间解析。对于非特权容器，请确保宿主进程能通过常规的 LXC 文件复制途径读取来宾路径。

# HISTORY

**pct pull** 是 **Proxmox VE** **pct**（Proxmox Container Toolkit）的一部分，用于管理 LXC 容器。

# SEE ALSO

[pct](/man/pct)(1), [pct-push](/man/pct-push)(1), [pct-exec](/man/pct-exec)(1), [pct-enter](/man/pct-enter)(1), [pct-mount](/man/pct-mount)(1)

# RESOURCES

```[Documentation](https://pve.proxmox.com/pve-docs/pct.1.html)```

```[Homepage](https://www.proxmox.com)```

<!-- verified: 2026-07-17 -->
