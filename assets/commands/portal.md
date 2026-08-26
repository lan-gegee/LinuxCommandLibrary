# TAGLINE

计算机之间端到端加密的命令行文件传输工具

# TLDR

**发送文件**

```portal send [file1] [file2] [folder1]```

**使用密码接收文件**

```portal receive [1-inertia-elliptical-celestial]```

**在自定义端口上运行中继服务器**

```portal serve --port [1337]```

# SYNOPSIS

**portal** _command_ [_options_] [_args_...]

# PARAMETERS

**send** _FILES_...
> 将文件或目录发送到另一台计算机。

**receive** _PASSWORD_
> 使用发送方显示的临时密码接收文件。

**serve**
> 运行中继服务器。

**-r**, **--relay** _ADDRESS_
> 指定自定义的中继服务器地址。

**-y**, **--yes**
> 不提示直接覆盖已有文件（仅限接收方）。

# DESCRIPTION

**portal** 是一款命令行文件传输工具，可使用临时密码在任意两台计算机之间发送文件。它使用 PAKE2 进行端到端加密，并采用并行 gzip 压缩。Portal 会先尝试直接的点对点连接，必要时回退到通过中继服务器路由。

# HISTORY

**portal** 由 **Arvid Gotthard**（mellonnen）和 **Zino Kader**（ZinoKader）创建，使用 **Go** 编写。

# INSTALL

```brew: brew install portal```

```nix: nix profile install nixpkgs#portal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[croc](/man/croc)(1), [scp](/man/scp)(1)
