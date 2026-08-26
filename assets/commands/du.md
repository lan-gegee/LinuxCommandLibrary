# TAGLINE

磁盘用量分析器

# TLDR

**显示目录总大小**

```du -sh [directory]```

**以人类可读格式显示大小**

```du -h [directory]```

**显示子目录大小**（仅一层深度）

```du -h --max-depth=1 [directory]```

**优先显示最大的子目录**

```du -h --max-depth=1 [directory] | sort -hr```

**显示所有文件和目录的大小**

```du -ah [directory]```

**不跨文件系统**（不越过挂载点）

```du -shx [directory]```

# SYNOPSIS

**du** [_options_] [_file_...]

# DESCRIPTION

**du**（disk usage）通过递归遍历目录树来估算并报告文件和目录的空间占用情况。与显示文件系统级剩余空间的 df 不同，du 关注的是单个文件和目录，因此对于找出磁盘空间被什么占用、应该从哪里着手清理至关重要。

该工具遍历目录层级并对每个文件占用的磁盘空间求和，在每个目录层级报告大小。默认情况下它会显示树中所有目录的大小，但可以使用 --max-depth 之类的选项将输出限制为较高层级的汇总。-h 标志把原始块数转换为人类可读的格式（KB、MB、GB）。

du 常与 sort 组合使用来找出占用空间最大的对象。"du -h | sort -hr | head" 这类模式可以揭示最大的磁盘空间消耗者，对于排查磁盘写满问题或规划清理操作必不可少。

该命令报告的是磁盘用量（实际分配的块数）而非文件的表面大小，这一点对稀疏文件和支持压缩的文件系统尤为重要。指向同一 inode 的硬链接默认只计一次（用 -l 可对每个链接分别计数）。-x 选项防止跨越文件系统边界，适合在不包含挂载子目录的情况下分析特定文件系统。

# PARAMETERS

**-h**, **--human-readable**
> 人类可读的大小（K、M、G）

**-s**, **--summarize**
> 仅显示总计

**-c**, **--total**
> 生成总计

**-a**, **--all**
> 包含文件，而不仅是目录

**-d** _N_, **--max-depth=**_N_
> 最大目录深度

**-b**, **--bytes**
> 以字节为单位显示大小

**-k**, **--kilobytes**
> 以 KB 为单位显示大小

**-m**, **--megabytes**
> 以 MB 为单位显示大小

**-x**, **--one-file-system**
> 跳过不同的文件系统

**-l**, **--count-links**
> 对硬链接重复计数

**--apparent-size**
> 显示表面大小而非磁盘用量

**--si**
> 类似 -h，但使用 1000 的幂（而非 1024）

**-L**, **--dereference**
> 跟随符号链接

**--exclude=**_pattern_
> 排除匹配模式的文件

**--time**
> 显示最后修改时间

# CAVEATS

在大目录树上可能较慢。报告的是实际磁盘用量（已分配的块数），不是文件的表面大小——要查看文件大小请用 **--apparent-size**。默认会跨越文件系统边界；用 **-x** 可停留在单一文件系统内。硬链接默认只计一次。访问受限目录可能需要 root 权限。

# HISTORY

**du** 自 **20 世纪 70 年代初**起就是 Unix 的一部分，是最早的一批 Unix 磁盘管理工具之一。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[df](/man/df)(1), [ncdu](/man/ncdu)(1), [ls](/man/ls)(1), [find](/man/find)(1)
