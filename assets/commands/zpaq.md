# TAGLINE

高压缩比的日志式归档器

# TLDR

**创建归档**

```zpaq add [archive.zpaq] [files...]```

**解压归档**

```zpaq extract [archive.zpaq]```

**列出归档内容**

```zpaq list [archive.zpaq]```

**以最大压缩添加**

```zpaq add [archive.zpaq] [files] -method 5```

**解压到指定目录**

```zpaq extract [archive.zpaq] -to [/output/dir]```

**增量备份**

```zpaq add [backup.zpaq] [directory] -all```

# SYNOPSIS

**zpaq** _command_ _archive_[**.zpaq**] [_files_...] [_options_]

# COMMANDS

**add**
> 向归档添加或更新文件

**extract**
> 从归档解压文件

**list**
> 列出归档内容

**compare**
> 将归档与文件系统进行比较

**test**
> 测试归档完整性

# PARAMETERS

**-method** _level_
> 压缩级别（0-5，越高压缩越好）

**-to** _path_
> 解压的目标目录

**-all**
> 包含隐藏文件和空目录

**-not** _pattern_
> 排除匹配模式的文件

**-only** _pattern_
> 只包含匹配的文件

**-until** _date_
> 解压截至某一日期时的版本

**-threads** _n_
> 使用的线程数

**-key** _password_
> 使用密码加密/解密

# DESCRIPTION

**zpaq** 是一个兼具高压缩比和日志（journaling）能力的归档器。它使用上下文混合和基于神经网络的预测进行压缩，压缩比优于大多数传统归档器。

ZPAQ 的日志特性使其非常适合增量备份。每次 **add** 都会创建一个新版本，之前的版本仍然可以访问。**-until** 标志可以按特定时间点提取当时的文件。

归档默认是只追加的——新版本追加进归档，不修改先前的数据。这提供了一定的防损坏保护，并支持带版本历史的备份。

压缩级别范围从 0（仅存储）到 5（最大压缩，速度慢）。

# CAVEATS

高压缩级别非常消耗 CPU 且缓慢。级别 5 可能比级别 1 慢上几个数量级。

ZPAQ 格式在 zpaq 工具之外的支持并不广泛。请考虑兼容性需求。

日志式归档会随时间不断增大。可用 **zpaq add -method 0** 来整合。

加密是可选的，且必须在创建归档时指定。

# INSTALL

```apt: sudo apt install zpaq```

```dnf: sudo dnf install zpaq```

```zypper: sudo zypper install zpaq```

```brew: brew install zpaq```

```nix: nix profile install nixpkgs#zpaq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tar](/man/tar)(1), [7z](/man/7z)(1), [gzip](/man/gzip)(1), [zstd](/man/zstd)(1)
