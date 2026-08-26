# TAGLINE

将本地文件复制进 Proxmox LXC 容器

# TLDR

将本地脚本**推送**进容器

```pct push 100 ./bootstrap.sh /root/bootstrap.sh```

推送配置文件并设置**来宾所有权**

```pct push 100 ./nginx.conf /etc/nginx/nginx.conf --user root --group root```

以**可执行权限**推送

```pct push 100 ./setup.sh /usr/local/bin/setup.sh --perms 0755```

# SYNOPSIS

**pct push** _vmid_ _file_ _destination_ [_OPTIONS_]

# PARAMETERS

**vmid**
> 容器的数字 ID（100–999999999）

**file**
> 主机上本地文件的路径

**destination**
> 容器内要写入的目标路径

**--user** _name|id_
> 所有者用户名或 ID。使用名称时，该用户必须存在于容器内

**--group** _name|id_
> 所有者组名或 ID。使用名称时，该组必须存在于容器内

**--perms** _mode_
> 文件权限（默认为八进制；加 **0x** 前缀表示十六进制）

# DESCRIPTION

**pct push** 将单个本地文件从 Proxmox 主机复制进 LXC 容器。常用于安装引导脚本、放置配置文件或暂存软件包，而无需通过 **scp**/SSH 进入来宾系统。

推送后通常使用 **pct exec** 对文件执行 chmod 并运行。当给定名称（而非数字 ID）时，所有权选项指向容器**内部**的用户和组。

# CAVEATS

仅支持单文件；不支持递归目录推送。容器内的父目录必须已存在。如需复制大目录树，请用 **pct mount** 挂载文件系统或改用网络共享。若来宾系统中未定义相应账户，基于名称的 **--user**/**--group** 会失败。

# HISTORY

**pct push** 是 **Proxmox VE** **pct**（Proxmox Container Toolkit）的一部分，用于管理 LXC 容器。

# SEE ALSO

[pct](/man/pct)(1), [pct-pull](/man/pct-pull)(1), [pct-exec](/man/pct-exec)(1), [pct-enter](/man/pct-enter)(1), [pct-mount](/man/pct-mount)(1)

# RESOURCES

```[Documentation](https://pve.proxmox.com/pve-docs/pct.1.html)```

```[Homepage](https://www.proxmox.com)```

<!-- verified: 2026-07-17 -->
