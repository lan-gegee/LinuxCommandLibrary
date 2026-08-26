# TAGLINE

删除 Linux 容器及其配置

# TLDR

**删除**已停止的容器

```sudo lxc-destroy -n [container_name]```

**强制删除**运行中的容器（会先停止它）

```sudo lxc-destroy -n [container_name] -f```

**删除容器及其全部快照**

```sudo lxc-destroy -n [container_name] -s```

显示**帮助**

```lxc-destroy --help```

# SYNOPSIS

**lxc-destroy** **-n** _name_ [_options_]

# DESCRIPTION

**lxc-destroy** 删除 Linux 容器及其配置。除非使用 **-f**，否则容器必须先停止才能销毁。

# PARAMETERS

**-n**, **--name** _NAME_
> 要销毁的容器名称。

**-P**, **--lxcpath** _PATH_
> 使用替代的容器存储目录。

**-f**, **--force**
> 强制销毁运行中的容器（会先停止它）。

**-s**, **--snapshots**
> 同时销毁容器的所有快照。

**-l**, **--logpriority** _LEVEL_
> 设置日志优先级（FATAL、CRIT、WARN、ERROR、NOTICE、INFO、DEBUG）。

**-o**, **--logfile** _FILE_
> 输出到其他日志文件。

**-?**, **--help**
> 显示帮助信息。

# CAVEATS

需要 root 权限。将永久删除容器及其根文件系统。除非使用 --force，否则请先停止容器。

# INSTALL

```apt: sudo apt install lxc```

```dnf: sudo dnf install lxc```

```pacman: sudo pacman -S lxc```

```apk: sudo apk add lxc```

```zypper: sudo zypper install lxc```

```brew: brew install lxc```

```nix: nix profile install nixpkgs#lxc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lxc-create](/man/lxc-create)(1), [lxc-stop](/man/lxc-stop)(1), [lxc-ls](/man/lxc-ls)(1)
