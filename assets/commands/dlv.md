# TAGLINE

Go 编程语言调试器

# TLDR

**调试可执行文件**

```dlv exec [./binary]```

**带参数调试**

```dlv exec [./binary] -- [arg1] [arg2]```

**调试 Go 包**

```dlv debug [package]```

**附加到进程**

```dlv attach [pid]```

**调试测试**

```dlv test [package]```

**启动无界面服务器**

```dlv debug --headless --listen=:[2345]```

**连接到远程**

```dlv connect [localhost:2345]```

# SYNOPSIS

**dlv** _command_ [_options_] [_args_]

# PARAMETERS

_COMMAND_
> 操作类型：debug、exec、test、attach、connect 等。

**debug** [_PACKAGE_]
> 构建并调试 Go 包。

**exec** _BINARY_
> 调试已构建的二进制文件。

**test** [_PACKAGE_]
> 调试测试。

**attach** _PID_
> 附加到正在运行的进程。

**connect** _ADDR_
> 连接到无界面服务器。

**--headless**
> 以无界面模式运行。

**--listen** _ADDR_
> 无界面模式的监听地址。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dlv**（Delve）是 Go 编程语言的调试器。它提供源码级调试，支持 goroutine、断点、变量检查和表达式求值。

Delve 了解 Go 的运行时，能正确处理 goroutine 调度、垃圾回收等 Go 特有的机制。它既支持本地调试，也支持通过无界面模式进行远程调试。

该调试器通过调试适配协议（DAP）与编辑器和 IDE 集成，可在 VS Code、GoLand 等编辑器中实现图形化调试。

# CAVEATS

要求 Go 二进制文件包含调试信息（默认包含）。某些优化可能影响调试效果。附加到进程需要相应权限。核心转储调试要求 Go 版本兼容。

# HISTORY

Delve 由 **Derek Parker** 开发并于 **2014 年**发布。其目标是提供一款理解 Go 并发模型和运行时的调试器，以取代 GDB 完成大多数 Go 调试任务。

# INSTALL

```apt: sudo apt install delve```

```dnf: sudo dnf install delve```

```pacman: sudo pacman -S delve```

```apk: sudo apk add delve```

```zypper: sudo zypper install delve```

```brew: brew install delve```

```nix: nix profile install nixpkgs#delve```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [gdb](/man/gdb)(1)

# RESOURCES

```[Source code](https://github.com/go-delve/delve)```

<!-- verified: 2026-07-11 -->
