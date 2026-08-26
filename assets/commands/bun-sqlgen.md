# TAGLINE

面向 Bun 的类型安全 SQL 代码生成器

# TLDR

**将** bun-sqlgen 添加到项目

```bun add @ilbertt/bun-sqlgen```

**为**一组文件中找到的带标签 SQL 查询**生成**类型定义

```bun bun-sqlgen generate '[src/**/*.ts]' --migrations [db/migrations]```

**通过环境变量指定**用于验证查询的数据库

```DATABASE_URL=[postgres://localhost/app] bun bun-sqlgen generate '[src/**/*.ts]' --migrations [db/migrations]```

# SYNOPSIS

**bun bun-sqlgen generate** _GLOB_ **--migrations** _DIR_

# DESCRIPTION

**bun-sqlgen** 是一个面向 **Bun** 原生 SQL 客户端（**Bun.sql**，即 **bun:sql** 模块）的代码生成工具。它让你在无需 ORM 的情况下编写具有完整类型安全的原始 SQL。

**generate** 子命令扫描与给定 glob 模式匹配的 TypeScript 源文件，提取其中的带标签 SQL 模板字面量，并根据由迁移文件定义模式的真实 **PostgreSQL** 或 **SQLite** 数据库验证每个查询。随后它会写出一个 **src/queries.gen.d.ts** 文件，包含每个查询精确的参数和结果类型，使列名、类型或查询结构上的错误变成编译期错误。

由于检查是针对真实数据库而非解析出的模型进行的，生成的类型始终与实际模式保持一致。不需要 Docker 或独立的类型定义语言。

# PARAMETERS

**generate** _GLOB_

> 处理与加引号的 glob 模式匹配的源文件（例如 **'src/\*\*/\*.ts'**），为其包含的 SQL 查询生成类型定义。请给 glob 加引号，以免被 shell 展开。

**--migrations** _DIR_

> 存放 SQL 迁移文件的目录，作为模式的唯一事实来源。会应用这些迁移来派生出用于校验查询的模式。

# CONFIGURATION

**DATABASE_URL**

> 用于在生成期间验证查询的 PostgreSQL 或 SQLite 数据库的连接字符串。代码生成将针对这个真实数据库实例运行。

# CAVEATS

生成时需要 **Bun** 运行时以及一个可连接的 PostgreSQL 或 SQLite 数据库；它不是独立二进制程序。它只支持 **Bun.sql**，对其他数据库客户端或运行时没有用处。

# HISTORY

由 **ilbertt** 创建，于 **2026 年**首次发布，属于不断壮大的 Bun 生态系统的一部分，为模式感知的查询构建器提供了一种无 ORM 的替代方案。它以 **@ilbertt/bun-sqlgen** 的名义发布在 npm 上，采用 Unlicense 许可证。

# SEE ALSO

[bun](/man/bun)(1), [psql](/man/psql)(1), [sqlite3](/man/sqlite3)(1), [protoc](/man/protoc)(1)

# RESOURCES

```[Source code](https://github.com/ilbertt/bun-sqlgen)```

<!-- verified: 2026-06-24 -->
