# TAGLINE

Sequelize ORM 的迁移与模型 CLI

# TLDR

**初始化 sequelize**

```npx sequelize-cli init```

**创建模型**

```npx sequelize-cli model:generate --name [User] --attributes [name:string,email:string]```

**执行迁移**

```npx sequelize-cli db:migrate```

**撤销上一次迁移**

```npx sequelize-cli db:migrate:undo```

**创建种子文件**

```npx sequelize-cli seed:generate --name [demo-user]```

**执行种子数据**

```npx sequelize-cli db:seed:all```

**创建迁移**

```npx sequelize-cli migration:generate --name [add-column]```

# SYNOPSIS

**sequelize-cli** _command_ [_options_]

# PARAMETERS

**init**
> 初始化项目。

**model:generate**
> 创建模型。

**db:migrate**
> 执行迁移。

**db:migrate:undo**
> 回滚迁移。

**seed:generate**
> 创建种子文件。

**db:seed:all**
> 运行所有种子数据。

**migration:generate**
> 创建迁移。

**--name** _NAME_
> 模型/迁移名称。

**--attributes** _ATTRS_
> 模型属性。

# DESCRIPTION

**sequelize-cli** 管理 Sequelize ORM 项目，为模型、迁移和种子文件提供脚手架。**init** 命令会创建标准的项目结构，包含 config、models、migrations 和 seeders 目录。

模型通过带类型的属性定义数据库表映射，CLI 会同时生成模型文件和初始迁移。迁移使用 up 和 down 函数对数据库模式进行版本管理，支持可应用或回滚的增量式模式变更。种子数据用于向表中填充初始或测试数据。

该 CLI 通过 Sequelize 的数据库抽象层支持 PostgreSQL、MySQL、MariaDB、SQLite 和 Microsoft SQL Server。

# CONFIGURATION

**config/config.json**
> 开发、测试和生产环境的数据库连接配置，指定主机、端口、用户名、密码、方言（dialect）和数据库名称。

**.sequelizerc**
> 项目级配置文件，用于覆盖模型、迁移、种子和配置目录的默认路径。

# CAVEATS

Node.js ORM。不同数据库的语法可能有差异。迁移顺序很重要。

# HISTORY

**Sequelize** 是一个 Node.js ORM，支持 PostgreSQL、MySQL、SQLite 等。CLI 提供脚手架和迁移工具。

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1), [knex](/man/knex)(1)
