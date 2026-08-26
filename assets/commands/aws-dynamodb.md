# TAGLINE

管理 Amazon DynamoDB 中的表和项目。

# TLDR

**创建带分区键的表**

```aws dynamodb create-table --table-name [my-table] --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH --billing-mode PAY_PER_REQUEST```

**向表中写入项目**

```aws dynamodb put-item --table-name [my-table] --item '{"id": {"S": "[item-id]"}, "name": {"S": "[value]"}}'```

**按主键获取项目**

```aws dynamodb get-item --table-name [my-table] --key '{"id": {"S": "[item-id]"}}'```

**按分区键查询项目**

```aws dynamodb query --table-name [my-table] --key-condition-expression "id = :id" --expression-attribute-values '{":id": {"S": "[item-id]"}}'```

**扫描表中的所有项目**

```aws dynamodb scan --table-name [my-table]```

**更新项目的属性**

```aws dynamodb update-item --table-name [my-table] --key '{"id": {"S": "[item-id]"}}' --update-expression "SET #n = :val" --expression-attribute-names '{"#n": "name"}' --expression-attribute-values '{":val": {"S": "[new-value]"}}'```

**按键删除项目**

```aws dynamodb delete-item --table-name [my-table] --key '{"id": {"S": "[item-id]"}}'```

# SYNOPSIS

**aws dynamodb** _command_ [_options_]

# DESCRIPTION

**aws dynamodb** 是 Amazon DynamoDB 的 AWS CLI 接口。DynamoDB 是一项全托管的 NoSQL 键值和文档数据库，可在任意规模下提供个位数毫秒级性能，并内置安全性、备份和内存缓存功能。

表通过主键（分区键，或分区键 + 排序键）标识其中的项目。DynamoDB 支持按需容量模式和预置容量模式、用于多区域复制的全局表，以及满足 ACID 要求的事务操作。

# COMMANDS

**create-table**
> 创建新的 DynamoDB 表

**delete-table**
> 删除表

**describe-table**
> 获取表的元数据和状态

**put-item**
> 插入或替换项目

**get-item**
> 按主键检索项目

**update-item**
> 修改项目属性

**delete-item**
> 按主键删除项目

**query**
> 按分区键检索项目，可选择附加过滤条件

**scan**
> 读取表中的所有项目

**batch-write-item**
> 跨表写入或删除多个项目（每次请求最多 25 个）

**batch-get-item**
> 跨表按键检索多个项目（每次请求最多 100 个）

**transact-write-items**
> 以原子方式执行多个写入操作

**list-tables**
> 列出当前区域的表名

# CAVEATS

项目大小上限为 400 KB。Scan 操作会读取整张表，在大表上开销可能很高。出于性能考虑，应优先使用 Query 而非 Scan。预置容量超限会导致限流。默认为最终一致读取；强一致读取的成本更高。

# HISTORY

Amazon DynamoDB 于 **2012 年 1 月** 作为 SimpleDB 的后继者推出。用于多区域复制的全局表于 **2017 年** 推出，按需容量模式于 **2018 年** 推出，PartiQL 查询语言支持于 **2020 年** 加入。它至今仍是 AWS 使用最广泛的数据库服务之一。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-dynamodbstreams](/man/aws-dynamodbstreams)(1), [aws-rds](/man/aws-rds)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/dynamodb/index.html)```

<!-- verified: 2026-06-18 -->
