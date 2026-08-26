# TAGLINE

与 Box 云存储交互的官方 CLI

# TLDR

**认证**（根据配置选择 JWT、OAuth 或 CCG）

```box login```

**列出文件夹中的项目**

```box folders:items [folder_id]```

**上传文件**到文件夹

```box files:upload [file.txt] --parent-id [folder_id]```

按 id **下载文件**

```box files:download [file_id]```

**创建子文件夹**

```box folders:create [parent_id] "[folder_name]"```

**搜索**内容

```box search "[query]"```

为文件**创建共享链接**

```box shared-links:create [file_id] --type file```

从 CSV **执行批量操作**

```box [command] --bulk-file-path [commands.csv]```

**代表其他用户执行操作**（仅限管理员）

```box users:get [user_id] --as-user [user_id]```

**以 JSON 格式输出**

```box files:get [file_id] --json```

# SYNOPSIS

**box** _topic_**:**_command_ [_arguments_] [_options_]

# DESCRIPTION

**box**（即 **@box/cli** 软件包）是 Box API 的官方 Node.js 命令行工具。它封装了 Box Content API，让技术人员和非技术人员无需编写代码即可执行文件、文件夹、用户和管理员操作。

命令按主题分组，例如 `files:upload`、`folders:items`、`users:list`、`collaborations:add`。大多数命令接受 Box 标识符（ID）而不是路径；`box folders:items 0` 列出根文件夹的内容。该 CLI 通过 `--bulk-file-path` 支持由 CSV 驱动的批量执行，每一行触发一次 API 调用。

# SUBCOMMAND TOPICS

**files** — upload、download、get、update、delete、copy、move、rename、lock、unlock、versions
**folders** — create、get、items、delete、update、copy、move、rename
**search** — 在整个企业范围内按查询条件搜索
**users** — list、get、create、update、delete、terminate-session
**groups** — list、create、update、delete、memberships
**shared-links** — 针对文件、文件夹和网页链接的 create/get/update/delete
**collaborations** — add、list、update、remove
**tasks**, **comments**, **web-links**, **metadata**, **legal-holds**, **retention-policies**, **events**, **webhooks**, **terms-of-service**
**configure** — 创建、切换、导入或设置环境（认证配置）

# COMMON OPTIONS

**-h**, **--help**
> 显示 CLI 或特定命令的帮助。

**-q**, **--quiet**
> 抑制发往 stderr 的非错误输出。

**-v**, **--verbose**
> 详细的调试输出。

**--as-user** _USER_ID_
> 代表指定用户发起请求（需要具备 App User 或企业认证的管理员权限）。

**--token** _TOKEN_
> 使用给定的 OAuth/JWT 访问令牌代替已保存的环境。

**--json**
> 以 JSON 输出。

**--csv**
> 以 CSV 输出。

**--save** / **--save-to-file-path** _PATH_
> 将命令输出保存到文件。

**--fields** _LIST_
> 要包含在响应中的字段列表，以逗号分隔。

**--bulk-file-path** _FILE_
> 读取包含输入行的 CSV/JSON 文件，并对每行运行一次命令。

**--no-color**
> 禁用彩色输出。

# CONFIGURATION

**~/.box**
> 保存的环境和应用认证配置的默认目录。

**box configure:environments:add** _FILE_
> 从 JWT 配置 JSON 文件添加新的认证环境。

**box configure:environments:switch** _NAME_
> 切换活动环境。

# CAVEATS

需要 Node.js 18+ 以及一个 Box 开发者应用（JWT、OAuth 2.0 或客户端凭据授权），并具备目标操作所需的权限范围。许多管理员命令需要企业访问令牌。API 有速率限制。

# HISTORY

**Box CLI** 由 **Box, Inc.** 维护，是 Box Content API 的官方开源命令行界面。它通过 npm 以 `@box/cli` 的名称分发（旧名 `box-cli`）。仓库地址：github.com/box/boxcli。

# SEE ALSO

[rclone](/man/rclone)(1), [gsutil](/man/gsutil)(1)
