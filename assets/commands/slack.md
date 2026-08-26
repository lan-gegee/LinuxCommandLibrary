# TAGLINE

Slack 应用开发命令行界面

# TLDR

从模板**创建新的 Slack 应用**

```slack create [app-name]```

在本地**运行应用**进行开发

```slack run```

**将应用部署**到 Slack

```slack deploy```

**列出可用命令**

```slack help```

为应用**创建触发器**

```slack trigger create```

**列出已安装的应用**和工作区

```slack list```

**登录工作区**

```slack login```

**显示版本信息**

```slack version```

# SYNOPSIS

**slack** _command_ [_options_]

# PARAMETERS

**-a**, **--app** _string_
> 使用指定的应用 ID 或环境。

**-w**, **--team** _string_
> 按团队名称或 ID 选择工作区或组织。

**--token** _string_
> 设置与团队关联的访问 token。

**--config-dir** _string_
> 为系统配置目录使用自定义路径。

**-f**, **--force**
> 忽略警告并继续执行命令。

**--no-color**
> 去除输出中的样式和格式。

**-s**, **--skip-update**
> 跳过检查 CLI 最新版本。

**-v**, **--verbose**
> 打印调试日志和附加信息。

**-e**, **--experiment** _strings_
> 在命令中使用实验特性。

**-h**, **--help**
> 显示帮助信息。

# COMMANDS

**create**
> 从模板创建新的 Slack 应用。

**run**
> 在本地运行应用进行开发。

**deploy**
> 将应用部署到 Slack 基础设施。

**trigger** **create**|**list**|**delete**
> 管理工作流触发器。

**datastore** **query**|**put**|**delete**
> 与应用数据存储交互。

**login**
> 向 Slack 工作区进行身份验证。

**logout**
> 移除身份验证。

**list**
> 列出已安装的应用和工作区。

**activity**
> 查看应用活动日志。

**version**
> 显示 CLI 版本信息。

**help**
> 显示任意命令的帮助。

# DESCRIPTION

**slack** 是 Slack 官方用于创建、开发和部署 Slack 应用的命令行界面。它与面向 JavaScript 和 Python 的 Deno Slack SDK 及 Bolt 框架配合，为 Slack 工作区构建工作流自动化、集成和自定义功能。

该 CLI 提供覆盖应用开发全生命周期的命令：从模板搭建新应用、开发期间在本地运行应用、部署到 Slack 的基础设施，以及管理触发器和数据存储。它负责与 Slack 工作区进行身份验证，并提供用于调试的活动日志。

CLI 通过 shell 脚本安装，可用于 Linux 和 macOS。

# CAVEATS

需要向具有应用开发权限的 Slack 工作区进行身份验证。某些功能需要付费的 Slack 计划。如果路径中已存在名为 "slack" 的其他 CLI 工具，请在安装时使用自定义别名。CLI 需要访问 Slack API 的网络连接。

# HISTORY

**Slack CLI** 由 Slack（现属 Salesforce）发布，旨在让开发者基于其平台构建新一代 Slack 应用。它与 Deno Slack SDK 一同推出，是 Slack 简化应用开发举措的一部分。该 CLI 取代了旧的部署方式，并集成了 Slack 的工作流自动化功能。目前仍在持续开发中，定期更新添加新功能。

# INSTALL

```nix: nix profile install nixpkgs#slack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[slack-term](/man/slack-term)(1), [slackcat](/man/slackcat)(1)
