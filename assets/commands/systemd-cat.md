# TAGLINE

将命令输出接入 systemd 日志

# TLDR

将命令的输出**写入**日志

```systemd-cat [command]```

将管道的输出**写入**日志

```[command] | systemd-cat```

为日志条目**使用**指定标识符

```[command] | systemd-cat -t [id]```

为记录的消息**使用**指定优先级

```systemd-cat -p [emerg|alert|crit|err|warning|notice|info|debug] [command]```

为 stderr 消息**使用**指定优先级

```systemd-cat --stderr-priority [priority] [command]```

# SYNOPSIS

**systemd-cat** [_options_] [_command_] [_arguments_]

# PARAMETERS

**-t, --identifier _name_**
> 日志条目的 syslog 标识符

**-p, --priority _level_**
> stdout 消息的默认优先级

**--stderr-priority _level_**
> stderr 消息的优先级

**--level-prefix** _BOOL_
> 解析日志输出中 sd-daemon(3) 风格的优先级前缀（默认：true）

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**systemd-cat** 将命令或管道的输出流连接到 systemd 日志。它适用于记录 cron 作业、脚本或任何原生不支持 journal 日志的命令的输出。

直接运行命令时会同时捕获 stdout 和 stderr。作为管道目标使用时，只捕获 stdin（即管道内容），stderr 仍连接到终端。

# CAVEATS

在管道中使用时只捕获管道传入的输出。标识符默认为被调用程序的名称，在管道模式下默认为 "cat"。优先级遵循 syslog 约定（0=emerg 到 7=debug）。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[journalctl](/man/journalctl)(1), [logger](/man/logger)(1), [systemctl](/man/systemctl)(1)
