# TAGLINE

管理相互隔离的基础设施环境

# TLDR

**显示当前堆栈**

```pulumi stack```

**列出所有堆栈**

```pulumi stack ls```

**选择堆栈**

```pulumi stack select [stack]```

**创建新堆栈**

```pulumi stack init [name]```

**删除堆栈**

```pulumi stack rm [name]```

**导出堆栈状态**

```pulumi stack export > state.json```

# SYNOPSIS

**pulumi** **stack** [_command_] [_options_]

# PARAMETERS

**ls**
> 列出堆栈。

**select** _name_
> 切换到指定堆栈。

**init** _name_
> 创建堆栈。

**rm** _name_
> 删除堆栈。

**export**
> 将状态导出为 JSON。

**import**
> 从 JSON 导入状态。

**output** _name_
> 获取堆栈输出。

**history**
> 显示部署历史。

**rename** _name_
> 重命名堆栈。

**tag** _cmd_
> 管理堆栈标签。

# DESCRIPTION

**pulumi stack** 管理堆栈。堆栈是基础设施的隔离实例（如 dev、staging、prod）。每个堆栈都有自己的状态、配置和资源。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-up](/man/pulumi-up)(1), [pulumi-config](/man/pulumi-config)(1)
