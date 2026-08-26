# TAGLINE

以更新后的配置重启 Vagrant 机器

# TLDR

**重载虚拟机**

```vagrant reload```

**带预配置重载**

```vagrant reload --provision```

**重载指定的虚拟机**

```vagrant reload [name]```

# SYNOPSIS

**vagrant** **reload** [_options_] [_name_]

# PARAMETERS

**--provision**
> 运行预配置器。

**--no-provision**
> 跳过预配置器。

**-f**, **--force**
> 强制重载。

# DESCRIPTION

**vagrant reload** 关停并重启 Vagrant 机器。应用需要重启才能生效的 Vagrantfile 变更。等价于先执行 vagrant halt 再执行 vagrant up。

# INSTALL

```apt: sudo apt install vagrant```

```dnf: sudo dnf install vagrant```

```nix: nix profile install nixpkgs#vagrant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-halt](/man/vagrant-halt)(1)
