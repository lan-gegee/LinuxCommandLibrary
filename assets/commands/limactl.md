# TAGLINE

管理 Lima Linux 虚拟机

# TLDR

**创建并启动默认虚拟机**

```limactl start```

**从模板创建虚拟机**

```limactl start --name=[myvm] template://ubuntu```

**列出虚拟机**

```limactl list```

**停止一台虚拟机**

```limactl stop [name]```

**删除一台虚拟机**

```limactl delete [name]```

**在虚拟机中打开 shell**

```limactl shell [name]```

**复制文件到虚拟机**

```limactl copy [local-file] [name]:[remote-path]```

# SYNOPSIS

**limactl** _command_ [_options_]

# PARAMETERS

**start** [_name_]
> 创建并启动一台虚拟机。

**stop** _name_
> 停止一台正在运行的虚拟机。

**delete** _name_
> 删除一台虚拟机。

**list**
> 列出所有虚拟机。

**shell** _name_
> 在虚拟机中打开 shell。

**copy** _src_ _dest_
> 与虚拟机之间复制文件。

**edit** _name_
> 编辑实例配置。

**snapshot** _subcommand_
> 管理实例快照（apply、create、delete、list）。

**disk** _subcommand_
> 管理附加磁盘（create、delete、list、resize）。

**protect** _name_
> 保护实例免遭意外删除。

**unprotect** _name_
> 移除对实例的保护。

**factory-reset** _name_
> 将实例恢复出厂设置。

**--name** _name_
> 指定虚拟机名称。

# DESCRIPTION

**limactl** 在 macOS、Linux 和 NetBSD 上管理 Lima（Linux Machines）虚拟机。它创建带有自动文件共享和端口转发功能的 Linux 虚拟机。通过 containerd/nerdctl 支持容器工作负载。

# SEE ALSO

[nerdctl](/man/nerdctl)(1), [docker](/man/docker)(1)
