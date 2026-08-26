# TAGLINE

用于组织服务器连接的简单 SSH 管理器

# TLDR

**列出所有 SSH 配置**

```ssm list```

**添加新的 SSH 配置**

```ssm add```

**编辑现有配置**

```ssm edit [myserver]```

**打印某个 SSH 配置**

```ssm print [myserver]```

# SYNOPSIS

**ssm** [_global options_] _command_ [_command options_]

# PARAMETERS

**list**, **ls**
> 列出可用的 SSH 配置。

**add**
> 以交互方式添加新的 SSH 配置。

**edit**, **e**
> 编辑现有的 SSH 配置。

**print**
> 将 SSH 配置打印到标准输出。

**help**, **h**
> 显示命令列表或某条命令的帮助。

**--help**, **-h**
> 显示帮助。

**--version**, **-v**
> 打印版本号。

# DESCRIPTION

**ssm**（Simple SSH Manager）是一款用于管理多台服务器 SSH 配置的 CLI 工具。它将 SSH 配置以模块化文件的形式组织在 config.d 目录结构中，支持列出、添加、编辑和打印 SSH 配置。

# HISTORY

**ssm** 由 **Elliot**（elliot40404）创建，使用 **Go** 编写。

# SEE ALSO

[ssh](/man/ssh)(1), [sshs](/man/sshs)(1), [sshclick](/man/sshclick)(1)
