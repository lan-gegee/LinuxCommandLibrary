# TAGLINE

管理 TigerGraph Cloud 实例

# TLDR

**登录** TigerGraph Cloud

```tgcloud login```

**列出解决方案**（云实例）

```tgcloud solution list```

以交互方式**创建解决方案**

```tgcloud solution create```

**启动解决方案**

```tgcloud solution start [solution_id]```

**停止解决方案**

```tgcloud solution stop [solution_id]```

**终止（删除）解决方案**

```tgcloud solution terminate [solution_id]```

**备份解决方案**

```tgcloud backup create [solution_id]```

# SYNOPSIS

**tgcloud** _command_ [_subcommand_] [_options_]

# SUBCOMMANDS

**login**
> 使用你的账户凭据或 API 令牌向 TigerGraph Cloud 进行身份验证。

**logout**
> 退出当前会话。

**solution list**
> 列出账户中的所有解决方案（云实例）。

**solution create**
> 创建新的解决方案（配置区域、套餐、版本等）。

**solution start** _id_ / **solution stop** _id_
> 启动或停止解决方案。

**solution terminate** _id_
> 永久删除解决方案及其数据。

**backup create** _id_ / **backup list** _id_ / **backup restore** _id_
> 管理解决方案的备份。

**user list**
> 列出组织中的用户。

# PARAMETERS

**--help**, **-h**
> 显示命令帮助。

**--verbose**
> 详细输出。

# DESCRIPTION

**tgcloud** 是用于管理 TigerGraph Cloud 图数据库实例（即"解决方案"）的命令行界面。它提供对云端托管的 TigerGraph 部署的程序化控制，支持实例生命周期管理（创建、启动、停止、终止）、备份操作以及用户和组织管理。

该工具面向自动化和脚本化工作流设计，让 DevOps 团队可以在终端或 CI/CD 流水线中管理 TigerGraph Cloud 基础设施，而无需使用 Web 控制台。

# CAVEATS

需要有 TigerGraph Cloud 账户和有效订阅。在执行其他命令前必须先通过 **tgcloud login** 进行身份验证。终止操作不可逆，除非已有备份，否则会删除解决方案中的所有数据。

# HISTORY

**tgcloud** 是 **TigerGraph Cloud** 的官方 CLI，后者是 TigerGraph 图数据库平台的托管版本。

# SEE ALSO

[gsql](/man/gsql)(1), [neo4j](/man/neo4j)(1)
