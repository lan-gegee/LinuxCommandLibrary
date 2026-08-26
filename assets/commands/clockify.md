# TAGLINE

Clockify 时间追踪 CLI 客户端

# TLDR

**开始一条计时记录**

```clockify-cli start "[Task description]"```

**连同项目和标签一起开始**

```clockify-cli start "[Task]" -p [project_id] -t [tag1,tag2]```

**停止当前计时记录**

```clockify-cli stop```

**显示当前正在运行的记录**

```clockify-cli show current```

**列出最近的计时记录**

```clockify-cli report```

**列出所有项目**

```clockify-cli project list```

**列出工作区**

```clockify-cli workspace list```

**配置 API 密钥**

```clockify-cli config set api-key [your_api_key]```

# SYNOPSIS

**clockify-cli** _command_ [_options_]

# PARAMETERS

**start** _description_
> 开始一条新的计时记录。

**stop**
> 停止当前计时记录。

**show current**
> 显示当前正在运行的记录。

**report** [_options_]
> 显示计时记录报告。

**project list**
> 列出所有项目。

**workspace list**
> 列出所有工作区。

**config set** _key_ _value_
> 设置配置值。

**-p**, **--project** _id_
> 关联到项目。

**-t**, **--tag** _tags_
> 添加标签（逗号分隔）。

**--task** _id_
> 关联到任务。

**-b**, **--billable**
> 标记为可计费。

**-w**, **--workspace** _id_
> 指定工作区。

# DESCRIPTION

**clockify-cli** 是时间追踪服务 Clockify 的命令行界面。它让你无需离开终端即可启动、停止和管理计时记录。

该工具与 Clockify API 集成，跨项目和工作区追踪时间。计时记录可以打标签、关联到项目和任务，并可标记为可计费。报告功能提供已追踪时间的汇总。

配置（包括 API 密钥和默认工作区）存储在本地。CLI 支持多个工作区，适合需要在不同组织间追踪时间的用户。

# CAVEATS

需要 Clockify 账户以及账户设置中的 API 密钥。某些功能可能需要付费的 Clockify 套餐。所有操作都需要网络连接。该 CLI 是社区项目，可能落后于 Clockify 的官方功能。

# HISTORY

Clockify 由 COING 于 **2017 年**创立，是一款免费的时间追踪解决方案。该服务因免费层提供不限用户数和追踪时长而广受欢迎。社区随后开发了多种 CLI 工具提供命令行访问，其中 **clockify-cli** 是功能较完整的选项之一，适合偏好终端工作流的开发者。

# INSTALL

```nix: nix profile install nixpkgs#clockify```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[watson](/man/watson)(1), [timew](/man/timew)(1)
