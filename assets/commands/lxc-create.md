# TAGLINE

基于模板创建新的 Linux 容器

# TLDR

以**交互方式**创建容器

```sudo lxc-create -n [container_name] -t download```

在**自定义目录**中创建

```sudo lxc-create -P /path/to/dir/ -n [container_name] -t download```

使用**指定发行版**创建

```sudo lxc-create -n [container_name] -t download -- -d [distro] -r [release] -a [arch]```

显示**帮助**

```lxc-create --help```

# SYNOPSIS

**lxc-create** **-n** _name_ **-t** _template_ [_options_]

# DESCRIPTION

**lxc-create** 基于模板创建新的 Linux 容器。它根据指定的模板设置容器的根文件系统和配置。

# PARAMETERS

**-n, --name NAME**
> 容器名称

**-t, --template TEMPLATE**
> 要使用的模板（download、ubuntu、debian 等）

**-P, --lxcpath PATH**
> 容器存储目录

**-B, --bdev TYPE**
> 后端存储类型（dir、lvm、btrfs、zfs）

**-- TEMPLATE_OPTIONS**
> 传递给模板的选项（-d distro、-r release、-a arch）

**-?, --help**
> 显示帮助信息

# CAVEATS

需要 root 权限。默认存储位置为 /var/lib/lxc/。可用模板因发行版而异。

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

[lxc-destroy](/man/lxc-destroy)(1), [lxc-start](/man/lxc-start)(1), [lxc-ls](/man/lxc-ls)(1)
