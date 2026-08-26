# TAGLINE

管理 X server 访问控制

# TLDR

**显示**当前访问控制列表

```xhost```

**允许**特定主机连接

```xhost +[hostname]```

**拒绝**特定主机连接

```xhost -[hostname]```

**允许**所有主机连接（禁用访问控制——不安全）

```xhost +```

**拒绝**所有未明确允许的主机

```xhost -```

使用 family 前缀**移除**特定用户或地址

```xhost -[family:name]```

# SYNOPSIS

**xhost** [[**+**|**-**]_name_...]

# PARAMETERS

**+_hostname_**
> 将主机添加到访问列表

**-_hostname_**
> 从访问列表中移除主机

**+**
> 禁用访问控制（允许全部）

**-**
> 启用访问控制（仅限列表内）

**+si:localuser:_user_**
> 允许本地用户

**-si:localuser:_user_**
> 拒绝本地用户

**+inet:_hostname_**
> 按 IP 族允许

# DESCRIPTION

**xhost** 管理 X server 的访问控制列表。它控制哪些主机和用户可以连接到 X 显示服务器。

family 前缀包括：**inet**（IPv4）、**inet6**（IPv6）、**si**（server interpreted，由服务器解释）、**localuser**（本地用户）和 **local**（本地连接）。

# CAVEATS

使用 **xhost +** 存在安全风险，因为它允许任何主机连接。如需安全的远程 X 访问，请改用 SSH X 转发。访问控制的更改不会在 X server 重启后保留。

# HISTORY

**xhost** 是最早的 X Window System 工具之一，自 X11 早期就提供基本的访问控制功能。

# INSTALL

```apt: sudo apt install x11-xserver-utils```

```dnf: sudo dnf install xhost```

```apk: sudo apk add xhost```

```zypper: sudo zypper install xhost```

```nix: nix profile install nixpkgs#xhost```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xauth](/man/xauth)(1), [ssh](/man/ssh)(1)
