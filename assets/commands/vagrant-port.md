# TAGLINE

显示 Vagrant 虚拟机的端口转发映射

# TLDR

**显示端口映射**

```vagrant port```

**显示指定虚拟机的映射**

```vagrant port [name]```

**显示指定客户机端口对应的主机端口**

```vagrant port --guest [80]```

使用转发的端口进行 **SSH 连接**

```ssh -p $(vagrant port --guest 22) vagrant@localhost```

# SYNOPSIS

**vagrant** **port** [_options_] [_name_]

# PARAMETERS

**--guest** _port_
> 只显示映射到指定客户机端口的主机端口。若该端口未被转发则返回错误。适合脚本使用。

**--machine-readable**
> 供自动化使用的机器可读输出格式。

# DESCRIPTION

**vagrant port** 显示客户机到主机的端口映射。展示为虚拟机配置的转发端口。用于查找访问客户机中服务所需的主机端口。

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-status](/man/vagrant-status)(1), [vagrant-ssh](/man/vagrant-ssh)(1), [vagrant-ssh-config](/man/vagrant-ssh-config)(1)
