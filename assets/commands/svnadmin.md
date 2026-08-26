# TAGLINE

Subversion 仓库管理工具

# TLDR

**创建新仓库**

```svnadmin create [/path/to/repo]```

**将仓库转储到文件**

```svnadmin dump [/path/to/repo] > [backup.dump]```

**将转储载入仓库**

```svnadmin load [/path/to/repo] < [backup.dump]```

**验证仓库完整性**

```svnadmin verify [/path/to/repo]```

**列出未完成的事务**

```svnadmin lstxns [/path/to/repo]```

**移除失效的事务**

```svnadmin rmtxns [/path/to/repo] [txn-id]```

**升级仓库格式**

```svnadmin upgrade [/path/to/repo]```

**显示仓库信息**

```svnadmin info [/path/to/repo]```

# SYNOPSIS

**svnadmin** _subcommand_ _repos-path_ [_options_] [_args_]

# PARAMETERS

**--revision** _rev_, **-r** _rev_
> 指定修订版或修订版范围。

**--incremental**
> 只转储上一个修订版之后的变更。

**--deltas**
> 在转储输出中使用增量（delta）以获得更小的文件。

**--fs-type** _type_
> 新仓库的文件系统类型：fsfs 或 bdb。

**--force-uuid**
> 使用转储流中的 UUID 设置仓库。

**--ignore-uuid**
> 忽略转储流中的 UUID。

**--quiet**, **-q**
> 抑制常规输出。

**--wait**
> 等待仓库锁而不是直接失败。

**--config-dir** _dir_
> 使用其他配置目录。

**--pre-1.4-compatible**
> 创建与 Subversion 1.4 或更早版本兼容的仓库。

**--pre-1.6-compatible**
> 创建与 Subversion 1.6 或更早版本兼容的仓库。

**--compatible-version** _ver_
> 创建与指定 Subversion 版本兼容的仓库。

**--bypass-hooks**
> 载入期间跳过钩子脚本。

**--bypass-prop-validation**
> 载入期间跳过属性校验。

# SUBCOMMANDS

**create**: 创建新的空仓库。

**dump**: 以可移植格式输出仓库内容。

**load**: 将转储文件载入仓库。

**verify**: 检查仓库是否损坏。

**recover**: 从崩溃中恢复仓库。

**upgrade**: 将仓库升级到最新格式。

**hotcopy**: 制作仓库的热备份副本。

**lstxns**: 列出未完成的事务。

**rmtxns**: 移除指定的事务。

**info**: 显示仓库信息。

**setlog**: 设置某个修订版的日志消息。

**setrevprop**: 设置修订版属性。

**pack**: 优化仓库存储。

**freeze**: 冻结仓库以便备份。

# DESCRIPTION

**svnadmin** 是 Subversion 仓库的管理工具。它提供创建、维护和备份存储在本地文件系统上的仓库的命令。

该工具可以使用 FSFS（默认）或 Berkeley DB 后端创建仓库。它支持用于备份和迁移的完整及增量转储，并可通过可选的增量压缩生成更小的转储文件。

仓库维护包括完整性验证、崩溃恢复、格式升级和事务清理。hotcopy 命令可以在不中断仓库访问的情况下创建一致的备份。

与 svn 客户端不同，svnadmin 只能操作本地仓库路径，无法通过网络访问仓库。

# CAVEATS

只能操作本地仓库，不支持 URL。完整导出时转储文件可能非常大。Berkeley DB 后端已不推荐使用，建议改用 FSFS。绕过钩子的选项应谨慎使用。仓库锁会阻止并发的管理操作。

# HISTORY

**svnadmin** 自 Subversion 2000 年首次发布以来就是其组成部分。Subversion 由 CollabNet 创建，作为 CVS 的替代品。该工具随仓库格式的演进不断变化，陆续增加了对 FSFS（Subversion 1.1）、仓库打包（1.6）以及各种性能改进的支持。

# INSTALL

```apt: sudo apt install subversion```

```dnf: sudo dnf install subversion```

```pacman: sudo pacman -S subversion```

```apk: sudo apk add subversion```

```zypper: sudo zypper install subversion```

```brew: brew install subversion```

```nix: nix profile install nixpkgs#subversion```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[svn](/man/svn)(1), [svnserve](/man/svnserve)(8), [git](/man/git)(1)
