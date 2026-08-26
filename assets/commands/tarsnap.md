# TAGLINE

加密去重的在线备份

# TLDR

**创建备份**

```tarsnap -c -f [backup-name] [/path/to/backup]```

**列出归档**

```tarsnap --list-archives```

**列出归档内容**

```tarsnap -t -f [backup-name]```

**解压归档**

```tarsnap -x -f [backup-name]```

**删除归档**

```tarsnap -d -f [backup-name]```

显示统计信息

```tarsnap --print-stats```

**试运行**（显示将要备份的内容）

```tarsnap -c --dry-run -f [test] [/path/to/backup]```

# SYNOPSIS

**tarsnap** [_-c_] [_-x_] [_-t_] [_-d_] [_-f archive_] [_options_] [_paths_]

# PARAMETERS

**-c**
> 创建归档。

**-x**
> 解压归档。

**-t**
> 列出归档内容。

**-d**
> 删除归档。

**-f** _ARCHIVE_
> 归档名称。

**--list-archives**
> 列出所有归档。

**--print-stats**
> 显示用量统计。

**--dry-run**
> 模拟模式。

**-v**
> 详细输出。

**--keyfile** _FILE_
> 密钥文件的位置。

**--cachedir** _DIR_
> 缓存目录。

**-C** _DIR_
> 先切换到指定目录。

**--include** _PATTERN_
> 包含匹配的文件。

**--exclude** _PATTERN_
> 排除匹配的文件。

# DESCRIPTION

**tarsnap** 提供安全、去重的在线备份。数据在离开你的电脑之前就已加密，然后存储到云端。

去重机制让相同的块只存储一次。增量备份非常高效，只传输新增或变更的数据。

客户端加密确保只有你自己能读取数据。密钥在本地生成，永远不会与服务器共享。

归档名称是任意字符串，常见的命名方式包括主机名、日期或描述性名称。

统计信息展示存储用量和去重效率。计费按存储和传输的字节数计算。

该工具只有命令行界面，专为脚本和自动化设计。定时备份通常由 cron 任务执行。

# CAVEATS

需要付费账户。密钥丢失即意味着数据丢失——无法恢复。首次备份可能耗时较长。按字节计费。

# HISTORY

**Tarsnap** 由 **Colin Percival** 于 **2008 年**前后创建。Percival 曾任 FreeBSD 安全官，他以安全性为首要目标设计了 Tarsnap。该服务强调密码学上的正确性。

# INSTALL

```pacman: sudo pacman -S tarsnap```

```brew: brew install tarsnap```

```nix: nix profile install nixpkgs#tarsnap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tar](/man/tar)(1), [restic](/man/restic)(1), [borg](/man/borg)(1), [duplicity](/man/duplicity)(1)
