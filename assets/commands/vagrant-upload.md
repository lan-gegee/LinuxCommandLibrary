# TAGLINE

向 Vagrant 客户机上传文件

# TLDR

**向虚拟机上传文件**

```vagrant upload [source] [destination]```

**上传到指定虚拟机**

```vagrant upload [source] [destination] [name]```

**压缩后上传**

```vagrant upload --compress [source] [destination]```

# SYNOPSIS

**vagrant** **upload** [_options_] _source_ [_destination_] [_name_]

# PARAMETERS

**--compress**
> 上传前先压缩。

**--temporary**
> 上传到临时目录。

# DESCRIPTION

**vagrant upload** 将文件从宿主机复制到客户机。对大文件支持压缩传输。未指定目标位置时默认为主目录。

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-ssh](/man/vagrant-ssh)(1), [scp](/man/scp)(1)
