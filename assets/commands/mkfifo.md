# TAGLINE

创建命名管道

# TLDR

**创建命名管道**

```mkfifo [pipe_name]```

**以指定权限创建**

```mkfifo -m [600] [pipe_name]```

**创建多个管道**

```mkfifo [pipe1] [pipe2] [pipe3]```

**以默认 SELinux 上下文创建 FIFO**

```mkfifo -Z [pipe_name]```

# SYNOPSIS

**mkfifo** [_options_] _name_

# PARAMETERS

_NAME_
> 要创建的 FIFO 的路径。

**-m** _MODE_, **--mode**=_MODE_
> 将文件权限位设置为 MODE（同 chmod），而不是 a=rw 减去 umask。

**-Z**
> 将 SELinux 安全上下文设置为默认类型。

**--context**[=_CTX_]
> 将 SELinux 或 SMACK 安全上下文设置为指定值。

**--help**
> 显示帮助信息。

**--version**
> 输出版本信息。

# DESCRIPTION

**mkfifo** 创建命名管道（FIFO）。命名管道支持进程间通信。

该工具创建用于进程间管道传输的特殊文件。数据按先进先出的顺序流动。

# CAVEATS

默认阻塞。需手动删除。与匿名管道不同。

# HISTORY

mkfifo 是用于创建进程间通信命名管道的 **POSIX** 工具。

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

[mknod](/man/mknod)(1)
