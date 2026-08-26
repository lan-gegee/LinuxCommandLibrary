# TAGLINE

退出用户级或容器服务管理器

# TLDR

退出**用户**服务管理器

```systemctl exit --user```

以指定的**退出码**退出

```systemctl exit [code] --user```

退出**容器**服务管理器

```systemctl exit```

# SYNOPSIS

**systemctl exit** [_EXIT_CODE_]

# PARAMETERS

**--user**
> 退出用户服务管理器

_EXIT_CODE_
> 可选的返回退出码（整数）

# DESCRIPTION

**systemctl exit** 请求服务管理器退出。配合 `--user` 使用时，它会终止每用户的 systemd 实例及所有用户服务。在容器中不带 `--user` 使用时，它会干净地关闭容器。

在常规系统上不带 `--user` 时，等价于 `systemctl poweroff`。

# CAVEATS

退出用户服务管理器时，所有用户服务都会被终止。退出码会传递给启动服务管理器的进程。在容器之外的裸机系统上通常用处不大。

# HISTORY

**exit** 子命令支持容器化 systemd 实例和用户服务管理器的干净关闭，实现正常的服务终止而非强制杀死。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-poweroff](/man/systemctl-poweroff)(1)
