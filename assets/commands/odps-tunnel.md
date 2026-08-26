# TAGLINE

与 MaxCompute 之间传输数据

# TLDR

**向表上传数据**

```odps tunnel upload [file] [project.table]```

**下载表数据**

```odps tunnel download [project.table] [output]```

**带分区上传**

```odps tunnel upload [file] [project.table/pt=value]```

**显示隧道状态**

```odps tunnel show```

# SYNOPSIS

**odps** **tunnel** [_command_] [_options_]

# PARAMETERS

**upload** _FILE_ _TABLE_
> 向表上传数据。

**download** _TABLE_ _FILE_
> 下载表数据。

**show**
> 显示隧道状态。

**-fd** _DELIMITER_
> 字段分隔符。

**-rd** _DELIMITER_
> 记录分隔符。

**--help**
> 显示帮助信息。

# DESCRIPTION

**odps tunnel** 在本地与 MaxCompute 之间传输数据，是一条高速数据通道。

该工具提供批量数据操作能力，属于 ODPS CLI 的一部分。

# CAVEATS

支持大文件。属于阿里云 ODPS 工具的一部分。可能受带宽限制。

# HISTORY

odps tunnel 为阿里云 MaxCompute 提供**高速数据传输**功能。

# SEE ALSO

[odps](/man/odps)(1), [odpscmd-tunnel](/man/odpscmd-tunnel)(1)
