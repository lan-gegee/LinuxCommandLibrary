# TAGLINE

在指定的 Proxmox LXC 容器内启动命令

# TLDR

在容器中**执行**命令

```pct exec 100 command```

打开 **bash** shell

```pct exec 100 bash```

传递**参数**

```pct exec 100 -- command arguments```

# SYNOPSIS

**pct exec** _vmid_ [--] _command_ [_arguments_...]

# DESCRIPTION

**pct exec** 在指定的 Proxmox LXC 容器内启动命令。它无需以交互方式进入容器即可直接执行命令。

# PARAMETERS

_VMID_
> LXC 容器的数字 ID（100–999999999）。

_COMMAND_
> 要在容器内执行的命令及其参数。

**--**
> 分隔符，阻止 `pct` 解析其后的选项，使其原样传给命令。

# CAVEATS

容器必须处于运行状态才能执行命令。无论调用 `pct exec` 的宿主机用户是谁，命令都会以容器内的 **root** 身份运行。默认不分配 TTY——交互式 shell 请改用 **pct enter**。命令的退出状态会返回给调用者，但执行前的失败（容器未运行等）会产生 Proxmox 特有的错误码。

# HISTORY

**pct exec** 是用于管理 LXC 容器的 **Proxmox VE** 虚拟化平台的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-enter](/man/pct-enter)(1)
