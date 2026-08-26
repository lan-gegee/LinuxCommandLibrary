# TAGLINE

快速的重复文件查找与删除工具

# TLDR

在目录中**查找重复文件**

```jdupes [path/to/directory]```

**递归查找重复文件**

```jdupes -r [path/to/directory]```

**交互式删除重复文件**

```jdupes -r -d [path/to/directory]```

**自动删除重复文件**（保留第一个）

```jdupes -r -dN [path/to/directory]```

**显示重复文件的大小**

```jdupes -r -S [path/to/directory]```

用**硬链接代替删除**

```jdupes -r -L [path/to/directory]```

**汇总重复统计信息**

```jdupes -r -m [path/to/directory]```

**跨多个目录比较**

```jdupes -r [dir1] [dir2] [dir3]```

# SYNOPSIS

**jdupes** [_options_] _directory_ [_directory ..._]

# PARAMETERS

**-r**, **--recurse**
> 对所有给定目录递归进入子目录。

**-R**, **--recurse:**
> 仅对该标志之后给出的目录递归进入子目录。

**-d**, **--delete**
> 提示选择要删除哪些重复项。

**-N**, **--noprompt**
> 与 -d 配合时，不提示直接删除（保留第一个）。

**-D**, **--debug**
> 显示调试/诊断输出。

**-S**, **--size**
> 显示重复文件的大小。

**-m**, **--summarize**
> 打印重复统计摘要。

**-L**, **--linkhard**
> 用硬链接替换重复文件。

**-s**, **--symlinks**
> 跟随符号链接。

**-H**, **--hardlinks**
> 将硬链接视为重复项。

**-n**, **--noempty**
> 排除零长度文件。

**-A**, **--nohidden**
> 排除隐藏文件。

**-f**, **--omitfirst**
> 在每组重复项中忽略第一个文件。

**-1**, **--sameline**
> 将每组重复项列在同一行。

**-0**, **--printnull**
> 使用空字符作为行终止符。

**-q**, **--quiet**
> 隐藏进度指示器。

**-T**, **--partial-only**
> 仅根据部分哈希匹配，忽略其余部分。

**-Q**, **--quick**
> 跳过逐字节校验（仅使用哈希）。

**-X**, **--xsize** _[+-=]SIZE_
> 按大小条件排除文件。

**-o**, **--order** _by_
> 文件排序依据：name、time、none。

# DESCRIPTION

**jdupes** 是一款快速的重复文件查找与删除工具。它通过先比较文件大小、再比较部分哈希、再比较完整哈希的方式识别内容完全相同的文件，还可以选择进行逐字节比较以确保准确。

该工具是较早的 **fdupes** 程序的分支和增强版，性能更好（通常快 7 倍）且功能更多。它采用优化的比较算法，能够高效处理数百万个文件。

处理重复项有多种方式：交互式删除（-d）会针对每组给出选项；自动删除（-dN）保留第一个文件；硬链接（-L）则用链接替换重复文件，既节省空间又保留所有文件名。

扫描多个目录时，jdupes 会跨所有目录比较文件，适合在备份和主存储之间查找重复内容。摘要模式（-m）可以快速概览可节省的空间。

排序选项（-o）控制自动操作中哪个文件被视为"第一个"，从而可以选择保留较新的或按字母顺序靠前的文件。

# CAVEATS

硬链接只能在同一文件系统上使用。对多个目录使用自动删除（-dN）时可能无法保留预期文件。极大量的文件可能需要大量内存。快速模式（-Q）跳过校验，理论上可能出现误报。

# HISTORY

**jdupes** 由 Jody Bruchon 于 **2015 年**前后基于 fdupes 的增强分支开始开发。其主要目标是在保持兼容性的同时提升性能并增加功能。名称由 "Jody's" 和 "dupes" 组合而成。它已成为管理重复文件的热门选择，可在多数 Linux 发行版仓库中找到。

# INSTALL

```apt: sudo apt install jdupes```

```dnf: sudo dnf install jdupes```

```zypper: sudo zypper install jdupes```

```brew: brew install jdupes```

```nix: nix profile install nixpkgs#jdupes```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fdupes](/man/fdupes)(1), [rdfind](/man/rdfind)(1), [duperemove](/man/duperemove)(8), [rmlint](/man/rmlint)(1)
