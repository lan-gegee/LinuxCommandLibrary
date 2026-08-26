# TAGLINE

基于 System V IPC 的 fakeroot 守护进程

# TLDR

**启动 fakeroot** 守护进程

```faked-sysv```

使用指定套接字运行

```faked-sysv --socket [/tmp/fakeroot.sock]```

调试模式

```faked-sysv --debug```

# SYNOPSIS

**faked-sysv** [_options_]

# PARAMETERS

**--socket** _PATH_
> 用于通信的 Unix 套接字路径。

**--debug**
> 启用调试输出。

**--foreground**
> 在前台运行（不转为守护进程）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**faked-sysv** 是 fakeroot 中使用 System V IPC 的守护进程组件。它维护一个虚假文件所有者和权限的数据库，让非特权用户也能创建包含 root 属主文件的归档。

该守护进程通过 LD_PRELOAD 拦截文件操作并返回虚假的所有者/权限信息。这使得构建软件包时无需真正的 root 权限即可获得正确的文件属主。

faked-sysv 使用 System V 共享内存通信，而 faked-tcp 则使用 TCP 套接字。

# CAVEATS

只伪造元数据，不伪造真实权限。需要配套的 fakeroot 包装器。SysV IPC 受系统限制约束。并非安全隔离机制。

# HISTORY

faked-sysv 是为 Debian 软件包构建而创建的 **fakeroot** 软件包的一部分。它使构建过程无需 root 权限就能创建具有正确文件属主的 .deb 包。

# INSTALL

```apt: sudo apt install fakeroot```

```dnf: sudo dnf install fakeroot```

```pacman: sudo pacman -S fakeroot```

```zypper: sudo zypper install fakeroot```

```brew: brew install fakeroot```

```nix: nix profile install nixpkgs#fakeroot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fakeroot](/man/fakeroot)(1), [dpkg-buildpackage](/man/dpkg-buildpackage)(1)
