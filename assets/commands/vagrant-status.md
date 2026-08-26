# TAGLINE

显示 Vagrant 机器的状态

# TLDR

**显示虚拟机状态**

```vagrant status```

**显示指定虚拟机的状态**

```vagrant status [name]```

# SYNOPSIS

**vagrant** **status** [_options_] [_name_]

# DESCRIPTION

**vagrant status** 显示 Vagrant 机器的当前状态。展示虚拟机是正在运行、已关停、已挂起还是尚未创建。需在包含 Vagrantfile 的目录中运行。

# INSTALL

```apt: sudo apt install vagrant```

```dnf: sudo dnf install vagrant```

```nix: nix profile install nixpkgs#vagrant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-global-status](/man/vagrant-global-status)(1)
