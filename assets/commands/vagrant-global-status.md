# TAGLINE

列出系统范围内的所有 Vagrant 环境

# TLDR

**显示所有虚拟机**

```vagrant global-status```

**清理无效条目**

```vagrant global-status --prune```

# SYNOPSIS

**vagrant** **global-status** [_options_]

# PARAMETERS

**--prune**
> 移除无效条目。

# DESCRIPTION

**vagrant global-status** 列出系统上的所有 Vagrant 环境。显示虚拟机的 ID、名称、提供者、状态和目录。可以使用 ID 从任意目录控制虚拟机。

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-status](/man/vagrant-status)(1)
