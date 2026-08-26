# TAGLINE

以可读格式显示 MySQL 二进制日志内容

# TLDR

**读取二进制日志**

```mysqlbinlog [mysql-bin.000001]```

**从指定位置开始读取**

```mysqlbinlog --start-position=[4] [mysql-bin.000001]```

**读取时间范围内的事件**

```mysqlbinlog --start-datetime="[2024-01-01 00:00:00]" --stop-datetime="[2024-01-02 00:00:00]" [mysql-bin.000001]```

**只输出指定数据库**

```mysqlbinlog --database=[mydb] [mysql-bin.000001]```

# SYNOPSIS

**mysqlbinlog** [_options_] _log_file_...

# PARAMETERS

**--start-position** _pos_
> 从给定的字节位置开始读取二进制日志。

**--stop-position** _pos_
> 在给定的字节位置停止读取二进制日志。

**--start-datetime** _datetime_
> 只显示时间戳等于或晚于给定日期时间的事件。

**--stop-datetime** _datetime_
> 在第一个时间戳等于或晚于给定日期时间的事件处停止读取。

**-d** _db_, **--database** _db_
> 只显示属于指定数据库的事件。

**-r** _file_, **--result-file** _file_
> 将输出定向到指定文件而非标准输出。

**--base64-output** _mode_
> 控制基于行事件的 base64 编码（AUTO、NEVER、DECODE-ROWS）。

**-v**, **--verbose**
> 将行事件重建为伪 SQL；重复使用（**-vv**）可包含列元数据注释。

**-R**, **--read-from-remote-server**
> 从远程 MySQL 服务器而非本地文件读取二进制日志。

**-h** _host_, **--host** _host_
> 连接到指定主机（与 **-R** 配合使用）。

**-u** _user_, **--user** _user_
> MySQL 用户名（与 **-R** 配合使用）。

**-p**, **--password**[=_pw_]
> MySQL 密码（与 **-R** 配合使用）。

**--to-last-log**
> 与 **-R** 一起使用时，继续读到服务器上的最后一个二进制日志。

**--disable-log-bin**
> 在输出中写入 SET sql_log_bin=0，使重放的语句不再被记录到日志。

# DESCRIPTION

**mysqlbinlog** 读取 MySQL 的二进制日志（和中继日志）文件，并将其内容显示为 SQL 语句。它常用于基于时间点的恢复（将其输出管道输入 **mysql**）、复制调试以及变更审计。

基于语句的事件直接以 SQL 形式呈现；基于行的事件则以 base64 编码的 BINLOG 语句形式输出，可通过 **--verbose** 选择性解码为伪 SQL。

# CAVEATS

除非经过适当解码，基于行事件的输出并非可直接执行的 SQL。用于恢复时，应将输出管道输入 **mysql**，而不是保存后再作为独立语句重新执行，以保留会话状态（如临时表）。

# INSTALL

```dnf: sudo dnf install mariadb```

```pacman: sudo pacman -S mariadb```

```apk: sudo apk add mariadb```

```zypper: sudo zypper install mariadb```

```brew: brew install mariadb```

```nix: nix profile install nixpkgs#mariadb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [mysqldump](/man/mysqldump)(1)
