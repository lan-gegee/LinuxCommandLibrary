# TAGLINE

管理 Linode 虚拟机实例

# TLDR

**列出所有 Linode**

```linode-cli linodes list```

**创建 Linode**

```linode-cli linodes create --type [g6-nanode-1] --region [us-east] --image [linode/ubuntu22.04] --root_pass "[password]"```

**查看 Linode 详情**

```linode-cli linodes view [linode_id]```

**启动 Linode**

```linode-cli linodes boot [linode_id]```

**关闭 Linode**

```linode-cli linodes shutdown [linode_id]```

**删除 Linode**

```linode-cli linodes delete [linode_id]```

# SYNOPSIS

**linode-cli linodes** _subcommand_ [_options_]

# PARAMETERS

_SUBCOMMAND_
> Linode 操作。

**list**
> 列出所有 Linode。

**create**
> 创建新的 Linode。

**view** _ID_
> 查看 Linode 详情。

**boot** _ID_
> 启动 Linode。

**shutdown** _ID_
> 关闭 Linode。

**delete** _ID_
> 删除 Linode。

**--type** _PLAN_
> 实例类型/套餐。

**--region** _REGION_
> 数据中心所在区域。

**--image** _IMAGE_
> 要部署的操作系统镜像。

**--help**
> 显示帮助信息。

# DESCRIPTION

**linode-cli linodes** 管理 Linode 虚拟机实例，负责创建、配置和生命周期管理。

该工具可控制 Linode 实例的电源状态、调整大小、克隆和备份。

# CAVEATS

需要身份验证。会创建计费资源。删除是永久性的。

# HISTORY

linode-cli linodes 是 **Linode CLI** 的一部分，用于管理 Linode 云上的虚拟机实例。

# INSTALL

```brew: brew install linode-cli```

```nix: nix profile install nixpkgs#linode-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[linode-cli](/man/linode-cli)(1), [linode-cli-volumes](/man/linode-cli-volumes)(1)
