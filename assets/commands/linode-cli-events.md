# TAGLINE

管理 Linode 账户事件

# TLDR

**列出事件**

```linode-cli events list```

**查看特定事件**

```linode-cli events view [event_id]```

**将事件标记为已读**

```linode-cli events mark-read [event_id]```

**将事件标记为已见**

```linode-cli events mark-seen [event_id]```

**以 JSON 格式列出事件**

```linode-cli events list --json```

**按操作过滤**

```linode-cli events list --action [linode_boot]```

# SYNOPSIS

**linode-cli events** _subcommand_ [_options_]

# PARAMETERS

_SUBCOMMAND_
> 事件操作。

**list**
> 列出所有事件。

**view** _ID_
> 查看特定事件。

**mark-read** _ID_
> 将事件标记为已读。

**mark-seen** _ID_
> 将事件标记为已见。

**--action** _TYPE_
> 按事件操作过滤（例如 linode_boot、linode_create、linode_reboot）。

**--json**
> 以 JSON 格式输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**linode-cli events** 管理 Linode 账户事件。事件会跟踪基础设施中的操作和变更。

该工具显示有关实例创建、重启、调整大小及其他活动的通知。

# CAVEATS

需要身份验证。事件有保留期限限制。是 linode-cli 的一部分。

# HISTORY

linode-cli events 是 **Linode CLI** 的一部分，用于监控账户活动和审计轨迹。

# INSTALL

```brew: brew install linode-cli```

```nix: nix profile install nixpkgs#linode-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[linode-cli](/man/linode-cli)(1), [linode-cli-linodes](/man/linode-cli-linodes)(1)
