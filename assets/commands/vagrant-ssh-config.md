# TAGLINE

输出 Vagrant 虚拟机的 SSH 配置

# TLDR

**显示 SSH 配置**

```vagrant ssh-config```

**输出指定主机的配置**

```vagrant ssh-config --host [name]```

**追加到 SSH 配置**

```vagrant ssh-config >> ~/.ssh/config```

# SYNOPSIS

**vagrant** **ssh-config** [_options_] [_name_]

# PARAMETERS

**--host** _name_
> 配置中使用的主机名。

# DESCRIPTION

**vagrant ssh-config** 输出用于连接虚拟机的 SSH 配置。显示主机、用户、端口和身份文件设置。可将其追加到 ~/.ssh/config 以便直接使用 ssh 访问。

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-ssh](/man/vagrant-ssh)(1), [ssh](/man/ssh)(1)
