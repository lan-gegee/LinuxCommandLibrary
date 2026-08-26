# TAGLINE

读取并重放 MariaDB 二进制日志文件

# TLDR

**显示**二进制日志文件中的**事件**

```mariadb-binlog /var/lib/mysql/mariadb-bin.000003```

**过滤**单个数据库的**事件**

```mariadb-binlog -d mydb /var/lib/mysql/mariadb-bin.000003```

**显示**两个时间戳之间的**事件**

```mariadb-binlog --start-datetime='2026-01-01 00:00:00' --stop-datetime='2026-02-01 00:00:00' /var/lib/mysql/mariadb-bin.000003```

**显示**两个字节位置之间的**事件**

```mariadb-binlog -j 100 --stop-position 200 /var/lib/mysql/mariadb-bin.000003```

将日志输出**重放**到 MariaDB

```mariadb-binlog mariadb-bin.000001 | mariadb -u root -p```

# SYNOPSIS

**mariadb-binlog** [_options_] _log_file_ ...

# PARAMETERS

**-d** _db_name_, **--database** _db_name_
> 只输出修改 _db_name_ 中表的事件

**-j** _N_, **--start-position** _N_
> 从字节位置 _N_ 处或之后的第一个事件开始

**--stop-position** _N_
> 在字节位置 _N_ 处或之后的第一个事件处停止

**--start-datetime** _datetime_
> 从 _datetime_ 处或之后的第一个事件开始

**--stop-datetime** _datetime_
> 在 _datetime_ 处或之后的第一个事件处停止

**-h** _host_, **--host** _host_
> 从远程 MariaDB 服务器读取二进制日志（需配合 **--read-from-remote-server**）

**-R**, **--read-from-remote-server**
> 从服务器获取日志而不是本地文件

**-v**, **--verbose**
> 将行事件解码为带注释的 SQL 语句

**-H**, **--hexdump**
> 在输出中包含每个事件的十六进制转储

**-s**, **--short-form**
> 只打印 SQL 语句，不带额外元数据

**-r** _file_, **--result-file** _file_
> 将输出写入 _file_ 而不是 stdout

**--help**, **-?**
> 显示帮助并退出

**--version**, **-V**
> 显示版本并退出

# DESCRIPTION

**mariadb-binlog** 是一个用于读取二进制日志文件的 MariaDB 客户端工具。服务器以紧凑的二进制格式写入这些日志；**mariadb-binlog** 把这些事件转换为人类可读的 SQL 或元数据，便于 DBA 审计变更、调试复制以及执行基于时间点的恢复。

每个事件前都有一条头注释，包含字节位置、时间戳、服务器 ID 和执行时间。对于基于语句的日志，输出会显示原始 SQL；对于基于行的日志，使用 **--verbose** 可以将被影响的行重建为 SQL 注释。

该工具可以读取本地日志文件，也可以从远程服务器流式获取日志。其输出可以管道给 **mariadb** 以重放语句，可以先编辑再做选择性恢复，也可以保存为文本文件供日后检查。

复制从节点上的中继日志（relay log）采用相同格式，因此 **mariadb-binlog** 同样可以检查它们。

# CAVEATS

通过多个独立的 **mariadb** 连接重放多个日志文件，可能破坏依赖先前文件中创建的临时表的语句。应改为把所有需要的日志通过单个 **mariadb** 进程用管道处理。

使用 **--database** 时，基于语句和基于行的日志的过滤行为有所不同。对于基于行的日志，只显示修改所选数据库中表的事件。

远程读取日志需要服务器处于运行状态且具备相应权限。

# INSTALL

```apt: sudo apt install mariadb-client```

```dnf: sudo dnf install mariadb```

```pacman: sudo pacman -S mariadb```

```apk: sudo apk add mariadb```

```zypper: sudo zypper install mariadb-client```

```brew: brew install mariadb```

```nix: nix profile install nixpkgs#mariadb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysqlbinlog](/man/mysqlbinlog)(1), [mariadb](/man/mariadb)(1)
