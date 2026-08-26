# TAGLINE

管理 SQLAlchemy 数据库迁移

# TLDR

在项目中**初始化 Alembic**

```alembic init [alembic]```

**创建一个新的迁移**修订版本

```alembic revision -m "[Add users table]"```

根据模型变更**自动生成迁移**

```alembic revision --autogenerate -m "[Add email column]"```

**升级到最新的**迁移

```alembic upgrade head```

**升级到指定的修订版本**

```alembic upgrade [revision_id]```

**回退一个修订版本**

```alembic downgrade -1```

**显示当前修订版本**

```alembic current```

**显示迁移历史**

```alembic history```

# SYNOPSIS

**alembic** [_options_] _command_ [_command_options_]

# PARAMETERS

**init** _directory_
> 在指定目录初始化新的 Alembic 环境。

**revision** [_-m message_] [_--autogenerate_]
> 创建新的迁移修订文件。

**upgrade** _revision_
> 将数据库升级到目标修订版本（使用 'head' 表示最新）。

**downgrade** _revision_
> 将数据库回退到目标修订版本（使用 '-1' 表示后退一步）。

**current**
> 显示数据库当前的修订版本。

**history**
> 列出修订历史。

**heads**
> 显示所有当前的 head 修订版本。

**branches**
> 显示所有分支点。

**stamp** _revision_
> 将修订表设置为特定版本而不实际执行迁移。

**show** _revision_
> 显示某个修订版本的详细信息。

**check**
> 检查 autogenerate 是否会产生新的迁移操作（若模式过期则返回非零退出码）。

**merge** _revisions_ [_-m message_]
> 将多个分支 head 合并为一个。

**-c**, **--config** _file_
> alembic.ini 配置文件路径。

**-n**, **--name** _name_
> 要使用的配置节名称。

**-x** _key=value_
> 向 env.py 传递附加参数。

**--autogenerate**
> 通过比较模型与数据库自动生成迁移。

**--sql**
> 输出 SQL 而不实际应用迁移。

# DESCRIPTION

**Alembic** 是面向 SQLAlchemy（Python 流行 ORM）的数据库迁移工具。它通过纳入版本控制的迁移脚本，管理数据库模式的增量式可逆变更。

迁移是存放在 versions 目录中的 Python 文件。每个迁移都有一个用于应用变更的 upgrade() 函数和一个用于撤销变更的 downgrade() 函数。Alembic 在一个专门的表中跟踪数据库当前状态，从而判断哪些迁移需要执行。

**--autogenerate** 功能会将 SQLAlchemy 模型定义与当前数据库模式进行比较，自动生成迁移脚本。虽然方便，但生成的迁移仍应人工审查，因为 autogenerate 无法检测所有类型的变更。

配置存储在 **alembic.ini** 中，其中指定数据库 URL、迁移脚本位置和其他设置。alembic 目录中的 **env.py** 脚本负责迁移环境的搭建，可以针对复杂场景进行定制。

# CONFIGURATION

**alembic.ini**
> 主配置文件，指定数据库 URL、迁移脚本位置和日志设置。

**alembic/env.py**
> 迁移环境脚本，配置迁移的运行方式并连接数据库。

# CAVEATS

Autogenerate 无法检测所有变更（表重命名、部分数据库上的列类型变更、约束名称变更）。务必审查生成的迁移。对于自动生成的迁移，downgrade 函数必须手动编写或验证。alembic.ini 中的数据库 URL 可能包含不应提交到版本库的凭据。

# HISTORY

**Alembic** 由 SQLAlchemy 作者 Mike Bayer 创建，于 **2011** 年首次发布。它的设计目标是提供一个与 SQLAlchemy 元数据和模型系统自然集成的迁移方案。其名称源自炼金术中用于蒸馏的容器，契合 SQLAlchemy 的命名主题。

# INSTALL

```apk: sudo apk add py3-alembic```

```nix: nix profile install nixpkgs#python3Packages.alembic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[django-admin](/man/django-admin)(1), [psql](/man/psql)(1), [sqlite3](/man/sqlite3)(1)

# RESOURCES

```[Source code](https://github.com/sqlalchemy/alembic)```

```[Documentation](https://alembic.sqlalchemy.org/)```

<!-- verified: 2026-06-11 -->
