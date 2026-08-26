# TAGLINE

找出正在使用文件或套接字的进程

# TLDR

查找正在访问**文件或目录**的进程

```fuser path/to/file```

显示包含用户和命令的**详细输出**

```fuser -v path/to/file```

查找正在使用 **TCP 端口**的进程

```fuser 80/tcp```

查找正在使用 **UDP 端口**的进程

```fuser 53/udp```

**终止**正在访问文件的进程

```fuser -k path/to/file```

查找正在访问**已挂载文件系统**的进程

```fuser -m /mnt/usb```

终止占用 TCP 端口的进程

```fuser -k 8080/tcp```

# SYNOPSIS

**fuser** [_-fuv_] [_-a_|_-s_] [_-4_|_-6_] [_-c_|_-m_|_-n space_] [_-k_ [_-i_] [_-SIGNAL_]] _name_...

# DESCRIPTION

**fuser** 显示正在使用指定文件或文件系统的进程 PID。它可以识别哪些进程打开了文件、正在运行可执行文件或占用了套接字，并可选择将其终止。

# ACCESS TYPE INDICATORS

**c**: 当前目录
**e**: 正在运行的可执行文件
**f**: 打开的文件
**F**: 以写方式打开的文件
**r**: 根目录
**m**: 内存映射文件或共享库

# PARAMETERS

**-a, --all**
> 显示所有指定的文件，包括未被访问的

**-k, --kill**
> 终止访问该文件的进程（默认发送 SIGKILL）

**-i, --interactive**
> 终止前请求确认

**-m, --mount NAME**
> 针对访问指定已挂载文件系统的进程

**-M, --ismountpoint**
> 仅当目标是挂载点时才匹配

**-n, --namespace SPACE**
> 选择命名空间：file、tcp 或 udp

**-u, --user**
> 附上进程所有者的用户名

**-v, --verbose**
> 以类似 ps 的格式显示进程

**-s, --silent**
> 静默运行

**-4, --ipv4**
> 仅搜索 IPv4 套接字

**-6, --ipv6**
> 仅搜索 IPv6 套接字

**-SIGNAL**
> 发送指定的信号而不是 SIGKILL

**-l, --list-signals**
> 列出可用的信号名称

# CAVEATS

**-k** 选项默认发送 SIGKILL 终止进程，该信号无法被捕获。使用 **-i** 可在终止前确认。查看所有进程可能需要 root 权限。

# HISTORY

**fuser** 属于 **psmisc** 软件包，该包提供了按文件访问管理进程的工具集。

# INSTALL

```apt: sudo apt install psmisc```

```dnf: sudo dnf install psmisc```

```pacman: sudo pacman -S psmisc```

```apk: sudo apk add psmisc```

```zypper: sudo zypper install psmisc```

```nix: nix profile install nixpkgs#psmisc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsof](/man/lsof)(8), [kill](/man/kill)(1), [killall](/man/killall)(1), [ps](/man/ps)(1)

# RESOURCES

```[Source code](https://gitlab.com/psmisc/psmisc)```

<!-- verified: 2026-07-15 -->
