# TAGLINE

为指定容器启动一个控制台

# TLDR

**连接**到容器控制台

```sudo lxc-console container_name```

连接到**指定的 tty**

```sudo lxc-console -t 1 container_name```

**退出**控制台

```Ctrl+a q```

显示**帮助**

```lxc-console --help```

# SYNOPSIS

**lxc-console** [_options_] **-n** _container_name_

# DESCRIPTION

**lxc-console** 为指定容器启动一个控制台。它会连接到容器 init 系统提供的 tty 设备，实现交互式访问。

# PARAMETERS

**-n, --name NAME**
> 要连接的容器名称

**-t, --tty N**
> 连接到编号为 N 的 tty，而非任意可用的 tty

**-e, --escape CHAR**
> 设置转义字符（默认为 'a'，即 Ctrl+a）

**-P, --lxcpath PATH**
> 使用替代的容器路径

**-?, --help**
> 显示帮助信息

# CAVEATS

退出控制台的转义序列是先按 Ctrl+a 再按 q（除非已用 -e 更改）。容器必须在其 tty 上运行着相应的 getty 或登录进程。

# HISTORY

**lxc-console** 是 **LXC**（Linux Containers）的一部分，LXC 提供操作系统级虚拟化，可在单一主机上运行多个相互隔离的 Linux 系统。

# INSTALL

```apt: sudo apt install lxc```

```dnf: sudo dnf install lxc```

```pacman: sudo pacman -S lxc```

```apk: sudo apk add lxc```

```zypper: sudo zypper install lxc```

```brew: brew install lxc```

```nix: nix profile install nixpkgs#lxc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lxc-start](/man/lxc-start)(1), [lxc-attach](/man/lxc-attach)(1), [lxc-stop](/man/lxc-stop)(1)
