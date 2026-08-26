# TAGLINE

挂起正在运行的 Vagrant 机器

# TLDR

**挂起虚拟机**

```vagrant suspend```

**挂起指定的虚拟机**

```vagrant suspend [name]```

# SYNOPSIS

**vagrant** **suspend** [_options_] [_name_]

# DESCRIPTION

**vagrant suspend** 保存虚拟机状态并将其停止。它会保留内存内容以便快速恢复。状态存储会占用磁盘空间。比关机更快，但占用更多存储。

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-resume](/man/vagrant-resume)(1), [vagrant-halt](/man/vagrant-halt)(1)
