# TAGLINE

杀死监听指定 TCP/UDP 端口的进程

# TLDR

**杀死**占用某端口的进程

```killport [8080]```

**杀死**多个端口上的进程

```killport [3000] [8000] [5432]```

**试运行**（显示将杀死哪些进程）

```killport -n [8080]```

**同时向绑定该端口的 Docker 容器发送信号**

```killport -s [8080]```

# SYNOPSIS

**killport** [*options*] *port*...

# DESCRIPTION

**killport** 查找绑定到给定端口号的进程（以及可选的容器）并将其终止。这是一款针对本地开发中常见"端口已被占用"问题的小型便利工具，用 Rust 编写，可通过 **cargo**、Homebrew 和发行版二进制文件获取。

# PARAMETERS

*port*...

> 要释放的一个或多个端口号。

**-n**, **--dry-run**

> 打印匹配的进程而不杀死（标志名称可能因版本而异为 **--dry-run**；参见 **killport --help**）。

**-s**, **--signal** *signal* / 与容器相关的标志

> 控制使用的信号以及是否针对容器 —— 已安装版本的具体用法请查阅 **killport --help**。

**-h**, **--help** / **-V**, **--version**

> 帮助与版本信息。

# CAVEATS

需要具有向目标进程发送信号的权限（对于特权端口或其他用户的 PID 通常需要 root）。杀错进程可能中断服务 —— 不确定时优先使用试运行。

# INSTALL

```zypper: sudo zypper install killport```

```brew: brew install killport```

```nix: nix profile install nixpkgs#killport```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsof](/man/lsof)(1), [fuser](/man/fuser)(1), [ss](/man/ss)(8), [kill](/man/kill)(1)

# RESOURCES

```[Source code](https://github.com/jkfran/killport)```

<!-- verified: 2026-07-19 -->
