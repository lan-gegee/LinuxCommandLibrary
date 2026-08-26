# TAGLINE

恢复已挂起的 Vagrant 机器

# TLDR

**恢复**默认的已挂起虚拟机

```vagrant resume```

按**名称**或 **ID****恢复**指定的虚拟机

```vagrant resume [name|id]```

**恢复**并在之后运行**预配置器**

```vagrant resume --provision```

**恢复**并跳过所有**预配置器**

```vagrant resume --no-provision```

# SYNOPSIS

**vagrant** **resume** [_options_] [_name_]

# PARAMETERS

**--provision**
> 运行预配置器。

**--no-provision**
> 跳过预配置器。

# DESCRIPTION

**vagrant resume** 让已挂起的 Vagrant 机器重新上线。它会从使用 **vagrant suspend** 挂起时的状态恢复虚拟机。由于是从保存的内存快照恢复而不是冷启动，恢复比从关机状态完整启动更快。如果机器不处于挂起状态，该命令不会产生任何效果。

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-suspend](/man/vagrant-suspend)(1), [vagrant-halt](/man/vagrant-halt)(1), [vagrant-status](/man/vagrant-status)(1)
