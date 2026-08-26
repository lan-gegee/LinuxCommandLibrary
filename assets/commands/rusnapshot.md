# TAGLINE

简单好用的 BTRFS 快照工具

# TLDR

使用配置文件**创建只读快照**

```sudo rusnapshot -c [path/to/config.toml] --create```

**创建可读写快照**

```sudo rusnapshot -c [path/to/config.toml] --create -w```

**列出被跟踪的快照**

```sudo rusnapshot -c [path/to/config.toml] -l```

**按 ID 删除快照**

```sudo rusnapshot -c [path/to/config.toml] --del --id [snapshot_id]```

**清理旧快照，仅保留最近 3 个**

```sudo rusnapshot -c [path/to/config.toml] --clean -k 3 --kind [hourly]```

**按 ID 恢复快照**

```sudo rusnapshot -c [path/to/config.toml] -r --id [snapshot_id]```

# SYNOPSIS

**rusnapshot** [_options_]

# PARAMETERS

**-c**, **--config** _file_
> TOML 配置文件的路径。

**--create**
> 创建一个只读快照。

**-w**, **--rw**
> 创建可读写快照而非只读快照。

**-l**, **--list**
> 列出数据库中跟踪的快照。

**--del**
> 删除快照。需要 **--id**。

**-r**, **--restore**
> 恢复特定快照。需要 **--id**。

**--id** _id_
> 要操作的快照 ID 或名称。

**--clean**
> 启用快照清理，仅保留由 **-k** 指定的最近 X 个快照。

**-k**, **--keep** _count_
> 要保留的快照数量（默认 3）。

**--kind** _type_
> 用于区分相同前缀快照的类别（例如 hourly、daily）。

**-p**, **--prefix** _name_
> 快照名称的前缀（默认 "rusnapshot"）。

**-d**, **--dfile** _path_
> SQLite 数据库文件的路径。

**--from** _dir_
> 创建快照时的源目录。

**--to** _dir_
> 快照的目标目录。

**--timeout** _ms_
> SQLite 忙等待超时时间（毫秒）（默认 10000）。

# DESCRIPTION

**rusnapshot** 是一个用 Rust 编写的简单好用的 BTRFS 快照工具。它为 BTRFS 文件系统提供快照创建、管理、恢复和自动清理功能，并使用 SQLite 跟踪快照。

配置通过 TOML 文件完成，其中指定快照的源路径和目标路径、前缀和类别。也可以完全通过命令行标志配合 **--from** 和 **--to** 来指定快照。

# CONFIGURATION

**config.toml**
> TOML 配置文件，指定快照源路径、目标子卷、保留策略以及快照类别（hourly、daily、weekly、monthly）。

# CAVEATS

需要 BTRFS 文件系统。使用前必须正确配置配置文件。

# HISTORY

由 **Eduard Tolosa**（Edu4rdSHL）用 **Rust** 编写，作为传统 BTRFS 快照管理工具的简单替代品。

# INSTALL

```aur: yay -S rusnapshot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [snapper](/man/snapper)(8)
