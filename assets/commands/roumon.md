# TAGLINE

面向 Go 应用程序的 TUI goroutine 监视器

# TLDR

**监视 localhost:6060 上的 goroutine（pprof 默认端口）**

```roumon```

**监视远程主机和端口上的 Go 应用程序**

```roumon -host=[192.168.10.1] -port=[8081]```

**将调试输出写入日志文件**

```roumon -debug=[roumon.log]```

**将远程连接与调试日志结合使用**

```roumon -host=[app.example.com] -port=[6060] -debug=[roumon.log]```

**显示内置帮助**

```roumon -h```

# SYNOPSIS

**roumon** [**-host=**_host_] [**-port=**_port_] [**-debug=**_logfile_]

# PARAMETERS

**-host** _HOST_
> pprof HTTP 服务器的主机名或 IP 地址。默认值：`localhost`。

**-port** _PORT_
> pprof HTTP 服务器的端口。默认值：`6060`。

**-debug** _LOGFILE_
> 启用调试日志记录，并将诊断信息写入指定文件。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**roumon** 是一个用于监控运行中 Go 应用程序 goroutine 的终端用户界面。它连接到 Go 程序的 `net/http/pprof` 端点，实时呈现 goroutine 列表及其堆栈跟踪、状态和标签，因此非常适合排查 goroutine 泄漏和调试并发问题。

在 TUI 内部，按 **F1** 获取帮助，按 **F10** 或 **Ctrl+C** 退出。

# CAVEATS

目标 Go 应用程序必须在 HTTP 监听器上导入并暴露 **net/http/pprof**。同一时间只应有一个 roumon 会话连接到某个 pprof 端点，以免采样噪声过多。

# HISTORY

**roumon** 由 **Armin Becher**（becheran）创建，使用 Go 编写，作为开源项目发布在 GitHub 上。

# INSTALL

```aur: yay -S roumon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pprof](/man/pprof)(1), [dlv](/man/dlv)(1), [go](/man/go)(1), [gotop](/man/gotop)(1), [htop](/man/htop)(1)
