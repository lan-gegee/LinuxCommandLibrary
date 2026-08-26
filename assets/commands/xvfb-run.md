# TAGLINE

在虚拟 X server 中运行命令

# TLDR

**在虚拟 X server 中运行命令**

```xvfb-run [command]```

**自动选择空闲的服务器编号**

```xvfb-run -a [command]```

**传递用于屏幕分辨率和色深的服务器参数**

```xvfb-run -s "-screen 0 1024x768x24" [command]```

**将 Xvfb 错误记录到文件**

```xvfb-run -e [/tmp/xvfb.log] [command]```

**使用特定的服务器编号**

```xvfb-run -n [44] [command]```

# SYNOPSIS

**xvfb-run** [_OPTIONS_] _COMMAND_

# PARAMETERS

**-a, --auto-servernum**
> 尝试获取空闲的服务器编号，从 99 或 --server-num 的参数值开始

**-s, --server-args** _ARGS_
> 传给 Xvfb 服务器的参数（默认："-screen 0 640x480x8"）

**-n, --server-num** _NUM_
> 使用指定的服务器编号（默认：99）

**-e, --error-file** _FILE_
> 将 xauth 和 Xvfb 的输出保存到文件（默认：/dev/null）

**-f, --auth-file** _FILE_
> 使用指定的 X authority 文件

**-l, --listen-tcp**
> 在 X server 中启用 TCP 端口监听（出于安全考虑默认禁用）

**-p, --xauth-protocol** _PROTO_
> 要使用的 X authority 协议（默认：MIT-MAGIC-COOKIE-1）

**-w, --wait** _DELAY_
> 启动 Xvfb 后等待 delay 秒再启动命令（默认：3）

**-h, --help**
> 显示用法信息并退出

# DESCRIPTION

**xvfb-run** 使用 Xvfb（X Virtual Frame Buffer）在虚拟 X server 环境中运行命令。这让你可以在没有显示器的系统上运行图形应用程序。

该工具适用于自动化测试、CI/CD 流水线和无头服务器环境。

# CAVEATS

必须安装 Xvfb。某些应用程序在虚拟 X 中的行为可能有所不同。GPU 密集型应用的性能可能有差异。

# INSTALL

```apt: sudo apt install xvfb```

```apk: sudo apk add xvfb-run```

```zypper: sudo zypper install xvfb-run```

```nix: nix profile install nixpkgs#xvfb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xinit](/man/xinit)(1), [xauth](/man/xauth)(1)
