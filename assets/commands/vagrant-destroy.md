# TAGLINE

删除 Vagrant 虚拟机

# TLDR

**销毁虚拟机**

```vagrant destroy```

**跳过确认强制销毁**

```vagrant destroy -f```

**销毁指定的虚拟机**

```vagrant destroy [name]```

销毁前先**优雅关机**

```vagrant destroy --graceful```

# SYNOPSIS

**vagrant** **destroy** [_options_] [_name_]

# PARAMETERS

**-f**, **--force**
> 不显示确认提示直接销毁。

**-g**, **--graceful**
> 销毁前先优雅地关闭机器。

**--[no-]parallel**
> 启用或禁用多台机器的并行销毁。若提供者支持则默认启用。

# DESCRIPTION

**vagrant destroy** 停止并删除 Vagrant 机器的所有资源。它会移除虚拟机及关联的存储。Vagrantfile 和预配置保持不变。

# CAVEATS

此操作会永久销毁虚拟机数据。共享文件夹和宿主机文件不受影响。destroy 命令不会移除在 `vagrant up` 期间下载的 box。请使用 `vagrant box remove` 来回收那部分磁盘空间。

# INSTALL

```apt: sudo apt install vagrant```

```dnf: sudo dnf install vagrant```

```nix: nix profile install nixpkgs#vagrant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-halt](/man/vagrant-halt)(1), [vagrant-box](/man/vagrant-box)(1), [vagrant-status](/man/vagrant-status)(1)
