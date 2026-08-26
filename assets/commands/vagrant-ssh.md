# TAGLINE

通过 SSH 连接 Vagrant 虚拟机

# TLDR

**通过 SSH 连接虚拟机**

```vagrant ssh```

**连接指定的虚拟机**

```vagrant ssh [name]```

**通过 SSH 执行命令**

```vagrant ssh -c "[command]"```

**不带 TTY 连接**

```vagrant ssh -- -T```

# SYNOPSIS

**vagrant** **ssh** [_options_] [_name_] [-- _ssh_args_]

# PARAMETERS

**-c**, **--command** _cmd_
> 执行命令。

**-p**, **--plain**
> 不附加额外参数的普通 SSH。

**--**
> 将参数传递给 ssh。

# DESCRIPTION

**vagrant ssh** 打开到 Vagrant 机器的 SSH 会话。它会使用生成的密钥自动完成身份验证。是以交互方式访问 Vagrant 虚拟机的主要途径。

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-ssh-config](/man/vagrant-ssh-config)(1), [ssh](/man/ssh)(1)
