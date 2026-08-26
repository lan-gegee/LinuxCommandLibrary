# TAGLINE

系统容器与虚拟机管理器

# TLDR

**初始化 Incus**

```incus admin init```

**启动一个容器**

```incus launch images:ubuntu/22.04 [container-name]```

**启动一个虚拟机**

```incus launch images:ubuntu/22.04 [vm-name] --vm```

**列出实例**

```incus list```

**在实例中执行命令**

```incus exec [name] -- [command]```

**在实例中打开一个 Shell**

```incus shell [name]```

**向实例中复制文件**

```incus file push [local/path] [name]/[remote/path]```

**显示实例详细信息**

```incus info [name]```

**停止一个实例**

```incus stop [name]```

**删除一个实例**

```incus delete [name]```

# SYNOPSIS

**incus** _command_ [_options_]

# SUBCOMMANDS

**admin init**
> 初始化 Incus。

**launch** _image_ _name_
> 创建并启动实例。

**start** _name_
> 启动实例。

**stop** _name_
> 停止实例。

**delete** _name_
> 删除实例。

**exec** _name_ **--** _cmd_
> 在实例中运行命令。

**shell** _name_
> 在实例中打开交互式 Shell。

**info** _name_
> 显示实例的详细配置和状态。

**file** _push|pull|edit_
> 在实例内传输或编辑文件。

**list**
> 列出所有实例。

**image list**
> 列出可用镜像。

**copy**
> 复制实例。

**move**
> 移动实例。

**snapshot**
> 管理快照。

# DESCRIPTION

**incus** 是一个系统容器与虚拟机管理器，是 LXD 的社区分支，由 Linux Containers 项目维护。它通过统一的 CLI 和 REST API，借助 LXC 管理容器、借助 QEMU 管理虚拟机。支持本地和远程访问、profile、存储池以及网络功能。

# INSTALL

```apt: sudo apt install incus-client```

```dnf: sudo dnf install incus-client```

```pacman: sudo pacman -S incus```

```apk: sudo apk add incus-client```

```zypper: sudo zypper install incus```

```brew: brew install incus```

```nix: nix profile install nixpkgs#incus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lxc](/man/lxc)(1), [docker](/man/docker)(1)
