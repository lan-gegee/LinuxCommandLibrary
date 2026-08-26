# TAGLINE

以免疫挂断信号的方式运行命令

# TLDR

**以免疫挂断的方式运行命令**

```nohup [command] &```

**将输出重定向到文件运行**

```nohup [command] > [output.log] 2>&1 &```

**在后台运行脚本**

```nohup [./script.sh] &```

**以自定义输出运行**

```nohup [command] > [custom.out] &```

# SYNOPSIS

**nohup** _command_ [_arguments_]

**nohup** _option_

# PARAMETERS

_COMMAND_
> 要运行的命令。

_ARGUMENTS_
> 命令参数。

**--help**
> 显示帮助信息。

**--version**
> 输出版本信息。

# DESCRIPTION

**nohup** 运行 _command_ 时忽略 SIGHUP 信号，因此在控制终端关闭或用户注销后进程仍会继续运行。

如果标准输出是终端，输出会被追加到当前目录的 **nohup.out**；若该位置不可写，则追加到 **$HOME/nohup.out**。如果标准错误是终端，则被重定向到标准输出。如果标准输入是终端，则从一个不可读的文件重定向。

注意：**nohup** 本身不会把进程放入后台；需要配合 **&**（或 shell 的作业控制机制）来使其脱离终端。

# EXIT STATUS

**125** nohup 本身失败。**126** 找到了命令但无法调用。**127** 未找到命令。否则返回 _command_ 的退出状态。

# CAVEATS

配合 **&** 使用可在后台运行。输出是追加（而不是覆盖）到 **nohup.out**。许多 shell 提供内置的 **nohup**，可能与 GNU coreutils 版本有所不同。要将进程完全脱离 shell，可考虑使用 **disown** 或 **setsid**。

# HISTORY

nohup 是经典的 **Unix** 命令，用于让进程在终端断开后继续存活。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[screen](/man/screen)(1), [tmux](/man/tmux)(1), [disown](/man/disown)(1), [setsid](/man/setsid)(1)
