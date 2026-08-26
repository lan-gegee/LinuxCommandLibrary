# TAGLINE

管理容器化子系统，实现隔离的软件包安装

# TLDR

交互式**创建**新子系统

```apx subsystems new```

从指定栈**创建**子系统

```apx subsystems new --name [name] --stack [stack]```

**列出**子系统

```apx subsystems list```

**重置**子系统

```apx subsystems reset -n name```

**强制**重置

```apx subsystems reset -n name -f```

**删除**子系统

```apx subsystems rm -n name```

**强制**删除

```apx subsystems rm -n name -f```

# SYNOPSIS

**apx subsystems** _command_ [_OPTIONS_]

# DESCRIPTION

**apx subsystems** 管理 apx 软件包管理器中的容器化子系统。子系统基于现有栈创建的容器，允许使用不同软件包管理器进行隔离的软件包安装。

# PARAMETERS

**new**
> 创建新子系统。未提供 name 和 stack 时为交互式。

**list**
> 列出所有可用的子系统

**reset**
> 将子系统重置到初始状态

**rm**
> 删除子系统

**-n, --name** _name_
> 指定子系统名称（供 new、reset、rm 使用）

**-s, --stack** _stack_
> 指定作为子系统基础的栈（供 new 使用）

**-H, --home** _path_
> 为子系统设置自定义主目录（供 new 使用）

**-i, --init**
> 在子系统容器内使用 systemd（供 new 使用）

**-j, --json**
> 以 JSON 格式输出子系统列表（供 list 使用）

**-f, --force**
> 强制执行操作而不确认（供 reset、rm 使用）

# CAVEATS

子系统需要容器运行时支持。删除或重置子系统会销毁其内容。创建子系统需要有兼容的栈可用。

# HISTORY

**apx** 是 **Vanilla OS** 的软件包管理器，提供基于子系统的软件包管理，支持多种软件包管理器。

# INSTALL

```dnf: sudo dnf install apx```

```aur: yay -S apx```

```nix: nix profile install nixpkgs#apx```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apx](/man/apx)(1), [apx-stacks](/man/apx-stacks)(1), [distrobox](/man/distrobox)(1)

# RESOURCES

```[Source code](https://github.com/Vanilla-OS/apx)```

```[Homepage](https://apx.vanillaos.org/)```

```[Documentation](https://docs.vanillaos.org/docs/en/apx)```

<!-- verified: 2026-06-11 -->
