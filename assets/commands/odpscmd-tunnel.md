# TAGLINE

MaxCompute 表的批量数据传输工具

# TLDR

**将文件上传到表**

```odpscmd tunnel upload [file.csv] [project.table]```

**将表下载到文件**

```odpscmd tunnel download [project.table] [output.csv]```

**上传到指定分区**

```odpscmd tunnel upload [file.csv] [table/pt=value]```

**恢复失败的上传会话**

```odpscmd tunnel resume [session_id]```

**使用自定义分隔符和多线程上传**

```odpscmd tunnel upload [file.csv] [table] -fd [,] -rd [\n] -t [4]```

**下载指定数量的记录**

```odpscmd tunnel download [project.table] [output.csv] -limit [1000]```

# SYNOPSIS

**odpscmd** **tunnel** [_command_] [_options_]

# PARAMETERS

**upload** _FILE_ _TABLE_
> 将本地文件数据上传到 MaxCompute 表。

**download** _TABLE_ _FILE_
> 将表数据下载到本地文件。

**resume** _ID_
> 恢复被中断的上传会话。

**-fd** _CHAR_
> 字段分隔符（默认：逗号）。

**-rd** _CHAR_
> 记录分隔符（默认：换行符）。

**-t** _NUM_
> 并行传输的线程数（默认：1）。

**-bs** _SIZE_
> 块大小，单位 MiB（默认：100）。

**-cp** _BOOL_
> 启用压缩（默认：true）。

**-cf** _BOOL_
> 将文件按 CSV 格式处理。

**-h** _BOOL_
> 在输出中包含表头行。

**-limit** _NUM_
> 限制要下载的记录数量。

**-dbr** _BOOL_
> 丢弃坏记录而不是直接失败。

**-mbr** _NUM_
> 允许的最大坏记录数（默认：1000）。

**-acp** _BOOL_
> 若分区不存在则自动创建。

**-te** _ENDPOINT_
> 指定自定义的 Tunnel 端点。

# DESCRIPTION

**odpscmd tunnel** 提供本地文件与 MaxCompute（前身为 ODPS）表之间的高速批量数据传输。它支持上传和下载大型数据集，并可配置并行度、压缩和分隔符。

每块数据对应一个 HTTP 请求。多个块可以并行且原子地上传——某一块的成功或失败不影响其他块。传输速度通常在 1 MB/s 到 20 MB/s 之间，取决于网络状况。

# CAVEATS

断点续传需要原上传会话的会话 ID。可能受 MaxCompute 项目配置带来的带宽限制。该工具属于 MaxCompute 控制台（odpscmd）套件。

# HISTORY

**odpscmd tunnel** 是**阿里云**提供的 MaxCompute 控制台的组成部分，用于对 MaxCompute（原名 ODPS）执行批量数据操作。

# INSTALL

```aur: yay -S odpscmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[odpscmd](/man/odpscmd)(1), [odps-tunnel](/man/odps-tunnel)(1)
