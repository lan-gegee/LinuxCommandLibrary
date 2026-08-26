# TAGLINE

列出系统上的 Linux 容器

# TLDR

列出**所有**容器

```sudo lxc-ls```

列出**活动**容器

```sudo lxc-ls --active```

列出**冻结**的容器

```sudo lxc-ls --frozen```

列出**已停止**的容器

```sudo lxc-ls --stopped```

以**精美格式**列出

```sudo lxc-ls --fancy```

以**自定义的精美列**列出

```sudo lxc-ls --fancy -F [NAME,STATE,IPV4,IPV6]```

按**正则表达式过滤**列出容器

```sudo lxc-ls --filter ['^web.*']```

# SYNOPSIS

**lxc-ls** [_options_]

# DESCRIPTION

**lxc-ls** 列出系统上的 Linux 容器。它可以按状态过滤，并以多种格式显示详细信息。

# PARAMETERS

**--active**
> 显示运行中和冻结的容器

**--frozen**
> 仅显示冻结的容器

**--running**
> 仅显示运行中的容器

**--stopped**
> 仅显示已停止的容器

**-f, --fancy**
> 以列格式输出详细信息

**-F, --fancy-format COLS**
> 精美输出的自定义列

**-1**
> 每行一个容器

**--filter** _regex_
> 按正则表达式过滤容器名称

**-?, --help**
> 显示帮助信息

# FANCY OUTPUT COLUMNS

NAME, STATE, AUTOSTART, GROUPS, IPV4, IPV6, UNPRIVILEGED

# CAVEATS

对于系统容器，需要 root 或相应的 LXC 权限。如果非特权容器已针对当前用户配置，则无需 root 即可列出。

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

[lxc-info](/man/lxc-info)(1), [lxc-start](/man/lxc-start)(1), [lxc-stop](/man/lxc-stop)(1), [lxc-create](/man/lxc-create)(1), [lxc-destroy](/man/lxc-destroy)(1)
