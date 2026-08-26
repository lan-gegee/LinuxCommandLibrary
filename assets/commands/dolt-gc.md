# TAGLINE

清理并优化仓库存储

# TLDR

对新代**执行垃圾回收**

```dolt gc```

执行快速但**不完整的**回收

```dolt gc --shallow```

**执行完整回收**，包括旧代

```dolt gc --full```

**回收但不做归档压缩**

```dolt gc --archive-level [0]```

# SYNOPSIS

**dolt gc** [**--shallow**|**--full**]

# PARAMETERS

**-s**, **--shallow**
> 执行一次快速但不完整的垃圾回收。

**-f**, **--full**
> 执行完整的垃圾回收，包括旧代。

**--archive-level** _N_
> 归档压缩级别。默认为 1；传入 0 可禁用归档。

**--incremental-file-size** _BYTES_
> 增量回收所写入表文件的最大字节数。

# DESCRIPTION

**dolt gc** 通过移除不再能从任何分支、标签或工作集访问到的 chunk 来回收磁盘空间。被删除的分支、硬重置以及被放弃的合并都会留下残余数据，只有垃圾回收才能释放它们。

Dolt 将存储划分为保存近期写入的*新代*和存放经受住上一轮回收数据的*旧代*。默认运行只清扫新代，速度很快，足以满足日常维护需要。**--full** 还会重写旧代，能回收更多空间，但代价是读取并重写整个数据库。

新版 Dolt 还会在后台为 `dolt sql-server` 自动运行垃圾回收，因此显式执行 **dolt gc** 主要是在批量导入、大规模删除之后，或者数据库经历过频繁的分支增删时才有必要。

# CAVEATS

回收是破坏性的：一旦 chunk 被清扫，那些只能从已删除分支或被丢弃的工作集访问到的数据便无法恢复，因此在对重要数据库运行 **--full** 之前请先备份。对大型数据库进行完整回收可能耗时很久，且在重写存储期间所需的空闲磁盘空间大致相当于数据库本身的大小。不要中途打断运行；另外可以通过 `dolt sql --disable-auto-gc` 针对单次查询关闭自动后台 GC。

# HISTORY

dolt gc 扮演着与 **git gc** 相同的角色，只不过作用对象是 Dolt 源自 Noms 的内容寻址 chunk 存储，而不是 Git 对象和 packfile。分代划分和归档格式是后来引入的，目的是控制多 GB 级数据库的回收成本；此后又增加了自动后台回收，长期运行的 SQL 服务器从此不再需要专门的维护窗口。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt](/man/dolt)(1), [dolt-sql](/man/dolt-sql)(1), [git-gc](/man/git-gc)(1)

# RESOURCES

```[Source code](https://github.com/dolthub/dolt)```

```[Documentation](https://www.dolthub.com/docs/cli-reference/cli/)```

<!-- verified: 2026-07-14 -->
