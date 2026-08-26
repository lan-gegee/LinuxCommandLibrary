# TAGLINE

在临时单元中运行命令

# TLDR

**启动**临时服务

```sudo systemd-run [command] [arguments]```

以当前用户身份**启动**临时服务

```systemd-run --user [command] [arguments]```

以自定义名称和描述**启动**临时服务

```sudo systemd-run -u [name] --description [string] [command]```

**启动**退出后仍保留的服务并设置自定义环境变量

```sudo systemd-run -r --set-env=[name]=[value] [command]```

**启动**周期性运行的临时定时器

```sudo systemd-run --on-calendar=[calendar_event] [command]```

带终端访问权限**交互式运行**

```systemd-run -r --pty [command]```

**设置**资源限制并等待完成

```systemd-run -p MemoryMax=[bytes] -p CPUQuota=[percentage]% --wait [command]```

在 shell 管道中**使用**

```[command1] | systemd-run -P [command2] | [command3]```

# SYNOPSIS

**systemd-run** [_options_] [_command_] [_arguments_]

# PARAMETERS

**--user**
> 在用户服务管理器下运行

**-u, --unit _name_**
> 临时服务的单元名称

**--description _text_**
> 单元的描述

**-r, --remain-after-exit**
> 进程退出后保留单元

**--set-env _name=value_**
> 设置环境变量

**--on-calendar _spec_**
> 创建定时器单元

**--pty**
> 分配伪终端（PTY）

**-p, --property _name=value_**
> 设置单元属性

**--wait**
> 等待服务完成

**-P, --pipe**
> 启用管道模式以便在管道中使用。

**-t, --pty**
> 附着 PTY 交互式运行（别名变体）。

**-q, --quiet**
> 抑制提示性消息。

**--scope**
> 创建临时的 .scope 单元而非 .service 单元。

**--slice** _NAME_
> 将单元加入指定的 slice。

**--working-directory** _DIR_
> 为被调用的命令设置工作目录。

**--uid** _USER_, **--gid** _GROUP_
> 以给定的用户/组身份运行命令。

**--nice** _N_
> 为被调用的命令设置调度优先级。

# DESCRIPTION

**systemd-run** 在由 systemd 管理的临时 scope 或 service 单元中运行程序。这允许对临时命令应用资源控制、创建定时器并进行规范的服务管理。

该工具适用于以特定资源限制（CPU、内存）运行命令、创建一次性定时器，以及通过 systemd 确保妥善的清理和日志记录。

# CAVEATS

定时器语法遵循 systemd.time 格式。资源属性需要相应的 cgroup 控制器。某些选项需要 root 权限。本命令是 systemd 套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemd-analyze](/man/systemd-analyze)(1), [systemd-cgls](/man/systemd-cgls)(1), [systemd-inhibit](/man/systemd-inhibit)(1)
