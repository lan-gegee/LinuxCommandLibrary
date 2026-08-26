# TAGLINE

Chef 基础设施自动化的命令行工具

# TLDR

**引导节点**

```knife bootstrap [host] -x [user] -P [password]```

**列出节点**

```knife node list```

**查看节点信息**

```knife node show [node_name]```

**上传 cookbook**

```knife cookbook upload [cookbook]```

**搜索节点**

```knife search node "role:[webserver]"```

**SSH 到节点**

```knife ssh "role:[webserver]" "[command]"```

# SYNOPSIS

**knife** _command_ [_subcommand_] [_options_]

# PARAMETERS

**bootstrap** _HOST_
> 在节点上引导安装 Chef。

**node** _CMD_
> 节点管理。

**cookbook** _CMD_
> Cookbook 操作。

**search** _TYPE_ _QUERY_
> 搜索 Chef 服务器。

**ssh** _QUERY_ _CMD_
> 通过 SSH 执行命令。

**-x** _USER_
> SSH 用户名。

**--help**
> 显示帮助信息。

# DESCRIPTION

**knife** 是 Chef 基础设施自动化的命令行工具。它管理节点、cookbook 和 Chef 服务器。

该工具用于引导节点进行配置管理、上传配方以及查询基础设施。

# CAVEATS

需要 Chef Workstation。需要能访问 Chef 服务器。基于 Ruby 实现。

# HISTORY

knife 是 **Chef**（由 **Opscode** 创建的基础设施自动化平台，现为 Progress Chef）的组成部分。

# SEE ALSO

[chef](/man/chef)(1), [berkshelf](/man/berks)(1)
