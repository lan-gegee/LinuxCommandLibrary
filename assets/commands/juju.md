# TAGLINE

编排应用的部署与管理

# TLDR

**引导控制器**

```juju bootstrap [cloud] [controller-name]```

**部署应用**

```juju deploy [charm-name]```

**添加机器**

```juju add-machine```

**查看状态**

```juju status```

**添加关系**

```juju add-relation [app1] [app2]```

**SSH 连接到单元**

```juju ssh [unit/0]```

# SYNOPSIS

**juju** _command_ [_options_]

# PARAMETERS

**bootstrap** _CLOUD_ _NAME_
> 创建控制器。

**deploy** _CHARM_
> 部署 charm。

**add-machine**
> 向模型添加机器。

**status**
> 显示模型状态。

**add-relation** _APP1_ _APP2_
> 连接应用。

**ssh** _UNIT_
> SSH 连接到单元。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Juju** 负责编排应用的部署与管理。它将应用封装为 charm，部署到各种云和裸机环境。

该工具可管理复杂的应用拓扑，并处理扩缩容、关系和配置。

# CAVEATS

需要先搭建控制器。需要云凭证。属于 Canonical 产品。

# HISTORY

Juju 由 **Canonical** 开发，用于服务编排，从配置管理方案逐步演进为应用建模方式。

# INSTALL

```brew: brew install juju```

```nix: nix profile install nixpkgs#juju```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lxc](/man/lxc)(1), [snap](/man/snap)(8)
