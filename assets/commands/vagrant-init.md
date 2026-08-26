# TAGLINE

创建新的 Vagrantfile 配置

# TLDR

**使用默认 box 初始化**

```vagrant init```

**使用指定 box 初始化**

```vagrant init [box_name]```

**生成最小化的 Vagrantfile**

```vagrant init -m [box_name]```

**通过 box URL 初始化**

```vagrant init [name] [url]```

# SYNOPSIS

**vagrant** **init** [_options_] [_name_] [_url_]

# PARAMETERS

**-m**, **--minimal**
> 创建最小化的 Vagrantfile。

**-f**, **--force**
> 覆盖已有的 Vagrantfile。

**--box-version** _version_
> 指定 box 版本。

**-o**, **--output** _file_
> 输出文件路径。

# DESCRIPTION

**vagrant init** 在当前目录创建新的 Vagrantfile。Vagrantfile 定义了虚拟机配置，包括 box、网络和预配置。是每个 Vagrant 项目的起点。

# INSTALL

```apt: sudo apt install vagrant```

```dnf: sudo dnf install vagrant```

```nix: nix profile install nixpkgs#vagrant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-box](/man/vagrant-box)(1)
