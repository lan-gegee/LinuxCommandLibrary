# TAGLINE

接收逻辑复制变更

# TLDR

**启动逻辑复制**

```pg_recvlogical -d [database] -S [slot] --start -f -```

**创建槽**

```pg_recvlogical -d [database] -S [slot] --create-slot -P [plugin]```

**删除槽**

```pg_recvlogical -d [database] -S [slot] --drop-slot```

# SYNOPSIS

**pg_recvlogical** [_options_]

# PARAMETERS

**-d**, **--dbname** _name_
> 数据库名称。

**-S**, **--slot** _name_
> 复制槽。

**--start**
> 启动复制。

**--create-slot**
> 创建槽。

**--drop-slot**
> 删除槽。

**-P**, **--plugin** _name_
> 输出插件。

**-f**, **--file** _file_
> 输出文件（- 表示 stdout）。

# DESCRIPTION

**pg_recvlogical** 接收逻辑复制变更。以流的方式获取从逻辑复制槽解码出来的变更。可用于变更数据捕获（CDC）和调试。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_receivewal](/man/pg_receivewal)(1)
