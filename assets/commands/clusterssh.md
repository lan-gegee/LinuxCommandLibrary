# TAGLINE

同时 SSH 连接到多台主机

# TLDR

**打开到多台主机的 SSH 连接**

```cssh [host1] [host2] [host3]```

**连接集群标签中定义的主机**

```cssh [cluster_name]```

**以指定用户名连接**

```cssh -l [username] [host1] [host2]```

**从文件读取要连接的主机**

```cssh -f [hosts.txt]```

**使用自定义终端打开连接**

```cssh -T [/usr/bin/xterm] [host1] [host2]```

**列出已配置的集群**

```cssh -L```

# SYNOPSIS

**cssh** [_options_] [_hosts_|_clusters_]

# PARAMETERS

**-l** _username_
> 用于 SSH 连接的用户名。

**-f** _file_
> 从文件读取主机（每行一个）。

**-T** _terminal_
> 要使用的终端应用程序。

**-L**
> 列出已配置的集群。

**-c** _config_
> 使用备用配置文件。

**-o** _options_
> 将选项传递给 SSH。

**-t** _title_
> 设置窗口标题。

**-a** _command_
> 连接后立即在每个会话中运行一条命令。

**-p** _port_
> 覆盖默认的 SSH 端口。

**-Q**
> 最后一个终端退出时不关闭 cssh。

**-q**
> 安静模式，抑制警告信息。

**-d**
> 启用调试输出（最多可重复 4 次）。

# CONFIGURATION

在 **~/.clusterssh/clusters** 中定义的集群：
```
webservers web1 web2 web3
dbservers db1 db2
all webservers dbservers
```

# DESCRIPTION

**ClusterSSH**（cssh）可同时打开多个 SSH 终端窗口，并配有一个控制窗口，将按键广播到所有连接。这使得可以在多台服务器上并行运行相同的命令。

每台主机都有各自的 xterm 窗口，并在屏幕上自动排列。在控制窗口中输入会同时发送到所有终端。也可以单独选中某些终端，执行针对特定主机的命令。

集群可在配置文件中预先定义，按功能对主机分组（Web 服务器、数据库等）。集群还可以包含其他集群，为复杂环境构建层级结构。

# CAVEATS

需要 X11 显示；无法在无头环境中运行。屏幕空间限制了实际可行的并发连接数量（通常为 10-20 台主机）。所有主机接收完全相同的输入；使用破坏性命令时务必小心。网络延迟差异可能导致命令的执行时间略有不同。

# HISTORY

ClusterSSH 由 **Duncan Ferguson** 编写，于 **2000 年代**初期首次发布。它解决了在 Ansible 等配置管理工具普及之前管理多台相似服务器的常见需求。该工具至今仍被广泛用于临时任务和交互式故障排查等需要同时访问多台主机的场景。

# INSTALL

```dnf: sudo dnf install clusterssh```

```zypper: sudo zypper install clusterssh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [pssh](/man/pssh)(1), [ansible](/man/ansible)(1), [ssh](/man/ssh)(1)
