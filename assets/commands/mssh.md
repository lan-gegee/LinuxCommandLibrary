# TAGLINE

基于 GTK+ 的 SSH 客户端，可向多台服务器同时发出命令

# TLDR

连接**多台 SSH 服务器**

```mssh [user@host1] [user@host2] [user@host3]```

连接 ~/.mssh_clusters 中**预定义的分组**

```mssh -a [alias_name]```

连接**特定端口**上的主机

```mssh [user@host1:2222] [user@host2:22]```

# SYNOPSIS

**mssh** [_options_] (**-a** _alias_ | _hosts_[:_port_])

# PARAMETERS

**-a, --alias _alias_**
> 打开配置中与指定别名关联的主机

**-h, --help**
> 显示帮助并退出

**-V, --version**
> 输出版本信息并退出

# KEYBOARD SHORTCUTS

**Modifier + 方向键**
> 在终端窗口之间导航

**Ctrl + Shift + x**
> 切换终端最大化状态

**Ctrl + Shift + n**
> 打开添加新主机的对话框

# CONFIGURATION

配置文件：**~/.mssh_clusters**

别名映射到以空格分隔的主机列表：
```
webservers = web1.example.com web2.example.com web3.example.com
dbservers = db1.example.com db2.example.com
```

花括号中的命令别名映射为发送到终端的文本：
```
{uptime} = uptime
{df} = df -h
```

# DESCRIPTION

**mssh**（MultiSSH）是一款基于 GTK+ 的 SSH 客户端，可同时向多台服务器发出命令。它以网格布局显示多个终端窗口，管理员只需键入一次命令即可在所有已连接的主机上执行。

界面支持在终端之间导航、单独或成组输入，以及通过配置文件预定义服务器分组。

# CAVEATS

需要图形显示（X11 或带 XWayland 的 Wayland）。默认情况下命令会发送到所有终端；用鼠标点击可选择单个终端。主机别名必须先在 ~/.mssh_clusters 中定义才能使用。

# HISTORY

**mssh** 由 **Bradley Smith** 于 2009 年创建，目前由 **Héctor García** 维护。它是 cssh 和 pdsh 等基于文本的多路 SSH 工具的图形化替代方案。

# INSTALL

```apt: sudo apt install mssh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [tmux](/man/tmux)(1)
