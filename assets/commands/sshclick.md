# TAGLINE

支持分组的基于终端的 SSH 配置管理器

# TLDR

**列出所有已配置的 SSH 主机**

```sshc host list```

**以卡片格式显示主机详情**

```sshc host show [myserver] --style card```

**创建新的主机组**

```sshc group create [mygroup] --desc "[Production servers]"```

**带参数创建主机**

```sshc host create [myserver] --param hostname=[example.com] --param user=[admin] --param port=[22]```

**删除主机**

```sshc host delete [myserver]```

**启动交互式 TUI**

```sshc tui```

# SYNOPSIS

**sshc** _resource_ _action_ [_options_]

# SUBCOMMANDS

**host list**
> 列出配置中的所有 SSH 主机。

**host show** _name_
> 显示单个主机的详细信息。

**host create** _name_
> 添加新的主机条目。

**host set** _name_
> 修改现有主机的参数。

**host delete** _name_
> 移除主机条目。

**group list** / **group show** / **group create** / **group delete**
> 管理主机组。

**tui**
> 启动交互式终端界面。

# PARAMETERS

**-f**, **--file** _PATH_
> 使用特定的 SSH 配置文件（默认 `~/.ssh/config`）。

**--style** _STYLE_
> 输出样式：table、card、json。

**--param** _key=value_
> 在主机上设置 SSH 选项（例如 hostname、user、port、identityfile）。

**--desc** _TEXT_
> 主机或组的描述性元数据。

# DESCRIPTION

**sshclick** 是一个用于管理 SSH 配置文件的 CLI 和 TUI 工具。它解析你的 SSH 配置（默认为 `~/.ssh/config`），提供列出、过滤、修改和查看主机条目的命令。借助额外的元数据注释，它还支持主机分组和描述等抽象，便于更好地组织配置。

TUI 模式提供对主机和分组的交互式导航、搜索和编辑能力。

# CAVEATS

对 SSH 配置文件的编辑可能重排或重写注释。批量操作前务必备份。

# HISTORY

**sshclick** 由 **Karlo Tisaj**（karlot）创建，使用 **Python** 编写。

# SEE ALSO

[ssh](/man/ssh)(1), [sshs](/man/sshs)(1), [ssh-list](/man/ssh-list)(1)
