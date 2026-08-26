# TAGLINE

在新会话中运行程序

# TLDR

在**新会话中运行**程序

```setsid [program]```

**运行**程序并丢弃输出和错误

```setsid [program] > /dev/null 2>&1```

**运行**程序并创建新进程（fork）

```setsid -f [program]```

**返回**程序的退出码作为 setsid 的退出码

```setsid -w [program]```

以当前终端作为控制终端**运行**程序

```setsid -c [program]```

# SYNOPSIS

**setsid** [_options_] _program_ [_arguments_]

# PARAMETERS

**-c, --ctty**
> 将控制终端设置为当前终端

**-f, --fork**
> 总是 fork，创建新进程

**-w, --wait**
> 等待程序退出并返回其退出状态

**-h, --help**
> 显示帮助信息

**-V, --version**
> 显示版本信息

# DESCRIPTION

**setsid** 在新会话中运行程序。会话是进程组的集合，新会话默认没有控制终端。调用进程会成为会话首进程。

它常用于将程序与终端分离、运行守护进程，或确保进程在注销后继续运行。结合输出重定向使用时，它可以有效地让进程独立地在后台运行。

# CAVEATS

如果调用进程已经是会话首进程，setsid 会失败，除非使用 **-f**。除非指定 **-c**，否则新会话没有控制终端。属于 util-linux 软件包的一部分。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nohup](/man/nohup)(1), [disown](/man/disown)(1), [screen](/man/screen)(1), [tmux](/man/tmux)(1), [setsid](/man/setsid)(2)
