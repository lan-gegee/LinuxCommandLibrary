# TAGLINE

使用 Linux 命名空间管理轻量级 NixOS 容器

# TLDR

**列出**正在运行的容器

```sudo nixos-container list```

使用指定的配置文件**创建** NixOS 容器

```sudo nixos-container create [container_name] --config-file [path/to/nix_config_file]```

对指定容器执行**启动、停止、强制终止或销毁**

```sudo nixos-container [start|stop|terminate|destroy|status] [container_name]```

在运行中的容器内**运行命令**

```sudo nixos-container run [container_name] -- [command] [arguments]```

**更新**容器配置

```sudo nixos-container update [container_name]```

进入运行中容器的**交互式 Shell** 会话

```sudo nixos-container root-login [container_name]```

# SYNOPSIS

**nixos-container** _command_ [_options_] [_container_name_]

# PARAMETERS

**list**
> 列出所有容器。

**create _name_**
> 创建一个新容器。

**start _name_**
> 启动一个已停止的容器。

**stop _name_**
> 停止一个正在运行的容器。

**terminate _name_**
> 强制终止一个容器。

**destroy _name_**
> 移除容器及其配置。

**status _name_**
> 显示容器状态。

**run _name_ -- _command_**
> 在容器内执行命令。

**root-login _name_**
> 在容器中打开交互式 root Shell。

**update _name_**
> 配置变更后重新构建容器。

**--config-file _path_**
> 容器的 Nix 配置文件。

# DESCRIPTION

**nixos-container** 使用 Linux 命名空间（systemd-nspawn）管理轻量级 NixOS 容器。每个容器都运行一个精简的 NixOS 系统，拥有自己的配置、服务和网络命名空间。

容器通过标准的 NixOS 配置文件进行配置，从而以声明式方式管理容器化服务。容器共享主机的内核，但拥有隔离的文件系统、进程树，网络也可以选择隔离。

配置文件存储在 **/var/lib/container/<name>/etc/nixos/** 中，可以直接编辑，然后运行 **update** 来应用更改。

# CAVEATS

需要 root 权限。为 NixOS 特有，在其他发行版上不可用。容器共享主机内核，因此内核模块和版本会被继承。若要连接外部网络，需要显式配置网络。

# INSTALL

```nix: nix profile install nixpkgs#nixos-container```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nixos-rebuild](/man/nixos-rebuild)(8), [systemd-nspawn](/man/systemd-nspawn)(1), [machinectl](/man/machinectl)(1)
