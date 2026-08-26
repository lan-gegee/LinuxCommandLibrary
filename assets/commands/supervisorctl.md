# TAGLINE

控制由 Supervisor 管理的进程

# TLDR

**查看状态**

```supervisorctl status```

**启动进程**

```supervisorctl start [process_name]```

**停止进程**

```supervisorctl stop [process_name]```

**重启进程**

```supervisorctl restart [process_name]```

**重新加载配置**

```supervisorctl reread && supervisorctl update```

**启动所有进程**

```supervisorctl start all```

**跟踪进程日志**

```supervisorctl tail -f [process_name]```

**交互式 Shell**

```supervisorctl```

# SYNOPSIS

**supervisorctl** [_options_] _command_ [_args_]

# PARAMETERS

**status**
> 显示进程状态。

**start** _NAME_
> 启动进程。

**stop** _NAME_
> 停止进程。

**restart** _NAME_
> 重启进程。

**reread**
> 重新读取配置文件。

**update**
> 应用配置变更。

**tail** _NAME_
> 显示进程输出。用 **-f** 跟踪，加 **stderr** 后缀表示 stderr 流。

**pid** _NAME_
> 显示进程的 PID。

**signal** _SIG NAME_
> 向进程发送信号（如 HUP、TERM）。

**clear** _NAME_
> 清空进程日志文件。

**-c** _FILE_
> supervisord 配置文件的路径。

**-s** _URL_
> Supervisor 服务器 URL（如 unix:///path 或 http://host:port）。

**-u** _USER_ / **-p** _PASSWORD_
> 服务器认证所需的用户名和密码。

# DESCRIPTION

**supervisorctl** 是用于控制 supervisord 守护进程所管理进程的命令行客户端。它提供启动、停止、重启和监控长期运行进程的命令，还可以查看它们的状态和日志输出。

status 命令显示所有受管进程及其状态（RUNNING、STOPPED、FATAL）、PID 和运行时长。可以独立控制单个进程或进程组。reread 命令检测配置文件变更，update 应用这些变更且不重启未受影响的进程。

该工具可以在单命令模式下工作，也可以作为带 Tab 补全的交互式 Shell 运行。tail 命令实时流式输出进程的 stdout/stderr，便于调试应用问题。配置变更通常遵循先 reread 后 update 的工作流程，以安全地应用修改。

# CAVEATS

需要 supervisord 正在运行。可能需要套接字权限。配置变更后需要执行 update。

# HISTORY

**Supervisor** 由 **Chris McDonough** 创建，用于进程管理。它被广泛用于运行应用服务器和后台工作进程。

# INSTALL

```dnf: sudo dnf install supervisor```

```pacman: sudo pacman -S supervisor```

```apk: sudo apk add supervisor```

```zypper: sudo zypper install supervisor```

```brew: brew install supervisor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[supervisord](/man/supervisord)(8), [systemctl](/man/systemctl)(1)
