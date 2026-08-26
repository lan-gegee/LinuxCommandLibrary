# TAGLINE

Entity Framework Core 数据库迁移工具

# TLDR

**添加迁移**

```dotnet ef migrations add [MigrationName]```

**更新数据库**

```dotnet ef database update```

**列出迁移**

```dotnet ef migrations list```

**移除最后一个迁移**

```dotnet ef migrations remove```

**生成幂等的 SQL 脚本**供 DBA 执行

```dotnet ef migrations script --idempotent -o [script.sql]```

**回滚到较早的迁移**（0 表示回滚全部）

```dotnet ef database update [MigrationName]```

**从现有数据库反向生成 DbContext**

```dotnet ef dbcontext scaffold "[connection_string]" [Microsoft.EntityFrameworkCore.SqlServer] -o [Models]```

**检查尚未纳入迁移的模型变更**

```dotnet ef migrations has-pending-model-changes```

**将迁移打包**为独立可执行文件用于部署

```dotnet ef migrations bundle --self-contained -r [linux-x64]```

# SYNOPSIS

**dotnet ef** _area_ _command_ [_arguments_] [_options_]

先将其作为全局工具安装，并把 design 包添加到项目中：

```dotnet tool install --global dotnet-ef```

```dotnet add package Microsoft.EntityFrameworkCore.Design```

# COMMANDS

**migrations add** _NAME_
> 添加新迁移。**-o** 设置输出目录（默认为 `Migrations`）。

**migrations list**
> 列出可用的迁移。**--no-connect** 可避免触碰数据库。

**migrations remove**
> 移除最后一个迁移。**-f**, **--force** 还会同时在数据库中回滚该迁移。

**migrations script** [_FROM_] [_TO_]
> 从迁移生成 SQL。**-i**, **--idempotent** 生成的脚本可以安全地在任意迁移状态的数据库上运行；**--no-transactions** 省略事务语句。

**migrations bundle**
> 构建一个应用迁移的自包含可执行文件，供部署流水线使用。

**migrations has-pending-model-changes**
> 若自上次迁移后模型有变化则以非零码退出。EF Core 8 新增。

**database update** [_MIGRATION_]
> 应用迁移至 _MIGRATION_，省略时应用到最新。特殊值 **0** 回滚所有迁移。

**database drop**
> 删除数据库。**-f** 跳过确认提示，**--dry-run** 只报告将要删除的内容。

**dbcontext scaffold** _CONNECTION_ _PROVIDER_
> 从现有数据库反向工程出 DbContext 和实体类型。

**dbcontext list** / **dbcontext info**
> 列出项目中的 DbContext 类型，或描述其中一个。

**dbcontext optimize**
> 生成编译模型及可选的预编译查询，以缩短启动时间。

**dbcontext script**
> 直接从模型生成 SQL 脚本，完全绕过迁移。

# PARAMETERS

**-c**, **--context** _DBCONTEXT_
> 使用哪个 DbContext。项目中有多个时必填。

**-p**, **--project** _PATH_
> *目标*项目，即文件写入的项目。默认为当前目录。

**-s**, **--startup-project** _PATH_
> *启动*项目，工具会构建并运行它来读取配置和连接字符串。默认为当前目录。

**--connection** _STRING_
> 覆盖来自 `AddDbContext` 或 `OnConfiguring` 的连接字符串。

**--framework** _TFM_ / **--configuration** _CONFIG_ / **--runtime** _RID_
> 当项目提供多种选择时，指定目标框架、构建配置和运行时。

**--no-build**
> 不先构建项目。仅在构建已是最新的情况下才安全。

**-d**, **--data-annotations**
> 反向生成的模型尽量使用特性而非流式 API 进行配置。

**-t**, **--table** _NAME_ / **--schema** _NAME_
> 将反向生成限制于特定的表或架构。每个表/架构重复一次该选项。

**--use-database-names**
> 保持表名和列名原样不变，而不改写成 C# 命名约定。

**--json** / **-v**, **--verbose**
> 输出 JSON 格式，或输出详细的诊断信息。

# DESCRIPTION

**dotnet ef** 是 Entity Framework Core 的设计期工具。它不属于 SDK：作为 .NET 工具单独安装，且其操作的项目必须引用 `Microsoft.EntityFrameworkCore.Design`。

它的核心任务是**迁移**。当 C# 模型发生变化时，`migrations add` 会将模型与上一次的快照做差异比较，并生成一个以 `Up` 和 `Down` 操作描述差异的迁移类。随后 `database update` 应用待处理的迁移，并将每个迁移记录在 `__EFMigrationsHistory` 表中，因此同一条命令可以安全地重复执行。

这些工具要区分两个项目，这一点常让人困惑。**目标项目**是文件写入的地方；**启动项目**才是工具实际构建并执行的项目，因为 EF 必须运行应用程序的配置代码才能发现 DbContext 及其连接字符串。两者通常相同，但当模型位于被 web 或控制台应用引用的类库中时就会分开。

**dbcontext scaffold** 则反其道而行，从已存在的数据库生成 DbContext 和实体类。每张表都必须有主键，才能从中生成实体类型。

# CAVEATS

生产部署应使用迁移脚本，而不是 `database update`。`--idempotent` 脚本或 `migrations bundle` 可执行文件可以由 DBA 审核，并且在服务器上无需 SDK 或源代码即可运行。

反向生成是一次性的生成器，不是同步器：带 **--force** 重新运行会覆盖生成的文件并丢弃你做过的所有修改，因此应把输出当作起点，把自定义内容放在 partial 类或单独的配置中。

工具版本应与 EF Core 运行时版本匹配；`dotnet-ef` 版本低于项目中的包时会报出令人费解的错误。`database drop` 会直接删除数据库。最后，迁移的 `Down` 方法是自动生成的，往往是整个迁移中最薄弱的部分：在依赖回滚之前务必验证它，对任何删除列的操作尤其如此。

# HISTORY

**Entity Framework Core** 随 .NET Core 于 **2016 年**发布，是对 Entity Framework 的彻底重写，跨平台且明显更精简。其 CLI 工具经历过不止一次重构：EF Core 1.x 通过每个项目引用的 `dotnet-ef` 包驱动工具，这种方式颇为别扭，后来才重塑为今天使用的全局工具。`migrations bundle` 和 `has-pending-model-changes` 是面向 CI/CD 流水线的新增功能——在那样的场景下，从开发者的机器上应用迁移从来都不是好主意。

# INSTALL

```nix: nix profile install nixpkgs#dotnet-ef```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotnet](/man/dotnet)(1), [dotnet-build](/man/dotnet-build)(1), [dotnet-publish](/man/dotnet-publish)(1), [sqlcmd](/man/sqlcmd)(1)

# RESOURCES

```[Source code](https://github.com/dotnet/efcore)```

```[Documentation](https://learn.microsoft.com/en-us/ef/core/cli/dotnet)```

<!-- verified: 2026-07-14 -->
