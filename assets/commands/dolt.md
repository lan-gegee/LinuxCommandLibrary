# TAGLINE

带 Git 式版本控制的 SQL 数据库

# TLDR

**初始化仓库**

```dolt init```

**克隆仓库**

```dolt clone [owner/repo]```

**查看状态**

```dolt status```

**添加变更**

```dolt add [table_name]```

**提交变更**

```dolt commit -m "[message]"```

**运行 SQL 查询**

```dolt sql -q "[SELECT * FROM table]"```

**启动 SQL 服务器**

```dolt sql-server```

**推送到远程**

```dolt push origin main```

**对比两个提交**或分支

```dolt diff [main] [feature_branch]```

将 CSV **导入**表

```dolt table import -c --pk=[id] [table_name] [data.csv]```

# SYNOPSIS

**dolt** _command_ [_arguments_] [_flags_]

# COMMANDS

**init** / **clone** _owner_/_repo_
> 在当前目录创建新数据库，或从 DoltHub 等远程克隆一个。

**status** / **diff** / **log** / **blame**
> 检查工作集、比较提交或分支、浏览历史，并查看最后修改某一行的是哪个提交。

**add** _table_ / **reset** / **commit** **-m** _msg_
> 暂存、取消暂存并提交表变更。

**branch** / **checkout** / **merge** / **tag**
> 管理分支、切换分支、合并历史以及标记发布。

**remote** / **fetch** / **pull** / **push**
> 管理 remote 并与其交换提交。

**sql** [**-q** _query_]
> 打开 SQL Shell 或运行单条查询。

**sql-server**
> 启动 MySQL 兼容服务器，让普通客户端和 ORM 都能连接。

**table import** / **table export**
> 将 CSV、JSON 或 Parquet 文件载入表中，或把表导出。

**dump**
> 将整个数据库导出为 SQL、CSV、JSON 或 Parquet。

**gc**
> 从不可达的数据中回收磁盘空间。

**version**
> 打印已安装的 Dolt 版本。

# DESCRIPTION

**Dolt** 是一个带 Git 式版本控制的 SQL 数据库。它是真正 MySQL 兼容的关系型数据库，Git 的每一项核心操作——`clone`、`branch`、`diff`、`merge`、`commit`、`push`、`pull`——都能作用于其中的数据和表结构。

版本控制界面有两种用法。CLI 与 Git 命令一一对应，这是多数人入门时的途径。所有操作也可以通过 SQL 完成：`AS OF` 查询能读取任意提交或分支时刻的表；`dolt_log`、`dolt_diff_<table>`、`dolt_status` 等系统表暴露历史；`CALL DOLT_COMMIT()` 和 `CALL DOLT_MERGE()` 这类存储过程则让应用程序无需调用外部命令即可为自己的数据建立版本。

由于合并按单元格而非文本行进行，触及同一行不同列的两个分支可以干净地合并；真正的冲突会作为记录出现在 `dolt_conflicts` 表中，用 SQL 即可解决。**DoltHub** 和 **DoltLab** 提供托管与自托管两种远程仓库，正如 GitHub 之于 Git 的关系。

典型用途包括数据版本管理与审计、共享数据集的协作整理、可回滚到任意历史状态的可复现流水线，以及能为每轮测试单独建分支的测试数据。

# CONFIGURATION

**~/.dolt/config_global.json**
> 全局配置，包含用户名、邮箱和默认远程。

**.dolt/config.json**
> 仓库专属配置，包含远程和分支相关设置。

# CAVEATS

保留全部历史版本并非没有代价：Dolt 数据库比同等的 MySQL 实例更大、通常也更慢，重写入负载需要定期执行 **dolt gc**。MySQL 兼容性很高但并不完备，重度依赖冷门函数或存储引擎行为的应用可能需要调整。通过 `dolt sql` 或 `sql-server` 写入的数据会进入工作集，提交之前不算作历史，这一点常令期待普通数据库的用户意外。冲突不通过文本标记解决，而是借助 `dolt_conflicts` 系统表处理。

# HISTORY

Dolt 由 **Liquidata**（即如今的 DoltHub）创建，于 **2019 年**发布。其存储引擎承袭自 **Noms**——Attic Labs 早前推出的内容寻址版本化数据库，这正是廉价分支和结构性 diff 得以实现的根基。早期版本拥有自己的查询方言；后来转向 MySQL 兼容（基于 DoltHub 接手并维护至今的 **go-mysql-server** 引擎），才让 Dolt 从一个有趣的数据共享工具变成可以直接承载现有应用的数据库。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [mysql](/man/mysql)(1), [sqlite3](/man/sqlite3)(1), [dolt-sql](/man/dolt-sql)(1), [dolt-merge](/man/dolt-merge)(1), [dolt-clone](/man/dolt-clone)(1)

# RESOURCES

```[Source code](https://github.com/dolthub/dolt)```

```[Homepage](https://www.dolthub.com)```

```[Documentation](https://www.dolthub.com/docs/)```

<!-- verified: 2026-07-14 -->
