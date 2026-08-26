# TAGLINE

管理 Linode 云基础设施

# TLDR

**列出 Linode**

```linode-cli linodes list```

**创建 Linode**

```linode-cli linodes create --type [g6-nanode-1] --region [us-east] --image [linode/ubuntu22.04]```

**查看 Linode**

```linode-cli linodes view [linode_id]```

**重启 Linode**

```linode-cli linodes reboot [linode_id]```

**删除 Linode**

```linode-cli linodes delete [linode_id]```

**配置 CLI**

```linode-cli configure```

# SYNOPSIS

**linode-cli** _command_ [_subcommand_] [_options_]

# PARAMETERS

_COMMAND_
> 资源类型（linodes、volumes、domains 等）。

**linodes**
> 管理 Linode 实例。

**volumes**
> 管理块存储卷。

**domains**
> 管理 DNS 域。

**configure**
> 设置身份验证。

**--help**
> 显示帮助信息。

# DESCRIPTION

**linode-cli** 管理 Linode 云基础设施。它提供对所有 Linode API 功能的访问。

该工具可从命令行控制虚拟机、存储、网络和 DNS。

# CAVEATS

需要 API 令牌。某些操作可能产生费用。令牌保存在 ~/.config/linode-cli 中。

# HISTORY

linode-cli 是 **Linode** 官方的命令行界面，用于管理其云基础设施服务。

# INSTALL

```brew: brew install linode-cli```

```nix: nix profile install nixpkgs#linode-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[linode-cli-linodes](/man/linode-cli-linodes)(1), [linode-cli-volumes](/man/linode-cli-volumes)(1), [aws](/man/aws)(1)
