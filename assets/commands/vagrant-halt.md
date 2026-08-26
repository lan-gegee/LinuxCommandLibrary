# TAGLINE

关闭正在运行的 Vagrant 机器

# TLDR

**停止虚拟机**

```vagrant halt```

**强制停止**

```vagrant halt -f```

**停止指定的虚拟机**

```vagrant halt [name]```

# SYNOPSIS

**vagrant** **halt** [_options_] [_name_]

# PARAMETERS

**-f**, **--force**
> 强制关机（直接断电）。

# DESCRIPTION

**vagrant halt** 关闭正在运行的 Vagrant 机器。它会向客户机操作系统发送关机信号。使用 --force 可立即断电而不进行优雅关机。

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-suspend](/man/vagrant-suspend)(1), [vagrant-destroy](/man/vagrant-destroy)(1)
