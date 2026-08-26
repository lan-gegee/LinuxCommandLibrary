# TAGLINE

以 Unix 守护进程方式运行命令

# TLDR

以守护进程方式**运行命令**

```daemonize [command] [arguments]```

将 PID 写入**指定文件**

```daemonize -p [path/to/pidfile] [command] [arguments]```

使用**锁文件**保证单实例

```daemonize -l [path/to/lockfile] [command] [arguments]```

以**指定用户**身份运行

```sudo daemonize -u [user] [command] [arguments]```

# SYNOPSIS

**daemonize** [_options_] _command_ [_arguments_]

# DESCRIPTION

**daemonize** 以 Unix 守护进程的方式运行命令。它负责标准的守护化流程：两次 fork、创建新会话、切换到根目录并关闭标准文件描述符。

适用于那些自身不会守护化、但需要作为后台服务运行的程序。

# PARAMETERS

**-p** _pidfile_
> 将守护进程的 PID 写入文件

**-l** _lockfile_
> 使用锁文件保证单实例

**-u** _user_
> 以指定用户身份运行

**-c** _directory_
> 运行前切换到指定目录

**-o** _file_
> 将 stdout 重定向到文件

**-e** _file_
> 将 stderr 重定向到文件

# CAVEATS

命令必须使用绝对路径指定。在现代系统上通常更推荐 systemd 服务。锁文件可防止多实例，但崩溃后需要手动清理。

# INSTALL

```apt: sudo apt install daemonize```

```dnf: sudo dnf install daemonize```

```zypper: sudo zypper install daemonize```

```brew: brew install daemonize```

```nix: nix profile install nixpkgs#daemonize```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[daemon](/man/daemon)(1), [nohup](/man/nohup)(1)
