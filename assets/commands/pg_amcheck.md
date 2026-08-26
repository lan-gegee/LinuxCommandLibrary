# TAGLINE

使用访问方法校验功能检查 PostgreSQL 数据库损坏

# TLDR

**检查所有数据库**

```pg_amcheck --all```

**检查特定数据库**

```pg_amcheck -d [database]```

**以详细输出检查特定表**

```pg_amcheck -d [database] -t [table] -v```

**对所有索引值进行堆验证检查**

```pg_amcheck -d [database] --heapallindexed```

**使用多个并行连接进行检查**

```pg_amcheck --all --jobs [4]```

# SYNOPSIS

**pg_amcheck** [_options_] [_dbname_]

# PARAMETERS

**-a**, **--all**
> 检查所有数据库。

**-d**, **--database** _name_
> 要检查的数据库。

**-t**, **--table** _table_
> 检查特定的表。

**-i**, **--index** _index_
> 检查特定的索引。

**-s**, **--schema** _schema_
> 仅检查指定模式中的表和索引。

**-v**, **--verbose**
> 为每个被检查的关系打印一条消息，并提供更详细的错误信息。

**--heapallindexed**
> 验证每个被检查索引中都包含全部堆元组对应的索引元组。

**--parent-check**
> 使用 bt_index_parent_check 做额外的父/子关系校验。

**--checkunique**
> 对带唯一约束的索引，验证不存在重复的可见条目。

**--rootdescend**
> 对每个元组通过根页面搜索在叶子层重新定位。隐含启用 --parent-check。

**--install**
> 安装检查数据库所缺失的必需扩展（目前为 amcheck）。

**-j**, **--jobs** _num_
> 使用 num 个到服务器的并发连接。

**--progress**
> 显示进度信息，包括已完成的关系及其大小。

**-w**, **--no-password**
> 从不提示输入密码。

**-W**, **--password**
> 连接前强制提示输入密码。

# DESCRIPTION

**pg_amcheck** 通过对目标数据库中的所有关系运行 amcheck 的校验函数，来检查一个或多个 PostgreSQL 数据库是否存在损坏。它能检测表和 B-tree 索引中的物理损坏，例如无效的页头、缺失或重复的元组、断裂的内部链接等。自 PostgreSQL 14 起可用。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_checksums](/man/pg_checksums)(1)
