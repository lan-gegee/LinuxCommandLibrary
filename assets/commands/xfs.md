# TAGLINE

X Window System 字体服务器

# TLDR

**启动字体服务器**

```xfs```

**使用指定配置启动**

```xfs -config [/etc/X11/fs/config]```

**在指定端口上启动**

```xfs -port [7100]```

**以守护进程方式运行**

```xfs -daemon```

**以降权用户启动**

```xfs -user [nobody]```

# SYNOPSIS

**xfs** [_options_]

# PARAMETERS

**-config** _file_
> 配置文件（默认：/etc/X11/fs/config）。

**-port** _num_
> 监听的 TCP 端口（默认：7100）。

**-daemon**
> 转入后台运行。

**-droppriv**
> 启动后放弃 root 权限。

**-user** _user_
> 以指定用户运行。

**-ls** _num_
> 监听套接字的队列长度。

# DESCRIPTION

**xfs** 是 X Window System 的字体服务器。它通过网络向 X server 提供字体，从而实现对多个 X 显示器的集中式字体管理。

可以将 X server 配置为向 xfs 请求字体，而不是（或除本地字体目录之外）从本地字体目录获取。这对于瘦客户机和无盘工作站共享服务器上的字体非常有用。

配置文件定义了字体路径、客户端限制和网络设置。服务器默认监听 TCP 端口 7100。

# CONFIGURATION

配置文件：/etc/X11/fs/config

定义 catalogue（字体路径）、client-limit 和 clone-self 等设置。

# CAVEATS

已被客户端字体渲染（fontconfig/FreeType）取代，属于过时方案。大多数现代系统不再使用 xfs。网络字体访问存在安全隐患。仅适用于遗留应用。

# HISTORY

**xfs** 为 X Window System 而开发，用于集中管理字体。随着向基于 fontconfig 和 FreeType 的客户端渲染过渡，xfs 在很大程度上已过时。它仍可用于需要服务器端字体的遗留 X 应用。

# INSTALL

```nix: nix profile install nixpkgs#xfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fc-cache](/man/fc-cache)(1), [xlsfonts](/man/xlsfonts)(1), [xset](/man/xset)(1)
