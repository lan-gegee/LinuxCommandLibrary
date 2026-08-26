# TAGLINE

查找重复文件和文件系统垃圾

# TLDR

**在目录中查找重复文件**

```rmlint [/path/to/directory]```

**查找重复文件并生成删除脚本**

```rmlint [/path/to/directory]```

**只查找重复文件**（不含空文件/空目录）

```rmlint -T df [/path/to/directory]```

**保留最先发现的重复文件**

```rmlint -k [/path/to/directory]```

**比较两个目录**（保留第一个目录中的原件）

```rmlint [/path/to/originals] // [/path/to/duplicates]```

**查找空文件和空目录**

```rmlint -T ef,ed [/path/to/directory]```

**试运行**（仅输出）

```rmlint --dry-run [/path/to/directory]```

**JSON 输出**

```rmlint -o json [/path/to/directory]```

# SYNOPSIS

**rmlint** [_-T types_] [_-k_] [_-o output_] [_options_] _paths_ [**//** _paths_]

# PARAMETERS

**-T**, **--types** _TYPES_
> 查找类型：df（重复文件）、ef（空文件）、ed（空目录）。

**-k**, **--keep-all-tagged**
> 保留带标记的（第一个）路径中的文件。

**-m**, **--must-match-tagged**
> 要求在带标记的路径中存在匹配项。

**-o**, **--output** _FMT_
> 输出格式：sh、csv、json、py。

**-c**, **--config** _FMT:KEY=VALUE_
> 配置输出处理器。

**-s**, **--size** _RANGE_
> 按文件大小过滤。

**-d**, **--max-depth** _N_
> 最大目录深度。

**--dry-run**
> 不写出输出文件。

**-g**, **--progress**
> 显示进度条。

**-p**, **--paranoid**
> 逐字节比较。

**-S** _CRITERIA_, **--sortcriteria** _CRITERIA_
> 用于选择原件的排序标准。

**-n**, **--newer-than-stamp** _FILE_
> 只处理比指定文件新的文件。

**-r**, **--hidden**
> 包含隐藏文件。

**-f**, **--followlinks**
> 跟随符号链接。

# DESCRIPTION

**rmlint** 查找重复文件、空文件、损坏的符号链接以及其他文件系统垃圾。它会生成脚本来删除或管理找到的项目。

重复检测采用渐进式匹配：先比较大小，再比较部分哈希，最后进行完整哈希或偏执的逐字节比较。这样可以最大限度减少处理大型集合时的 I/O。

双斜杠（//）分隔符用于区分原件路径与副本路径。// 之前的路径中的文件被视为首选原件，之后的则被标记为副本。这使得对备份或镜像目录的受控清理成为可能。

输出包括一个包含删除命令的 shell 脚本（rmlint.sh）。该脚本默认很谨慎，需要确认且会保留原件。JSON 和 CSV 输出便于自定义处理。

排序标准（-S）决定保留哪个副本：按创建时间、路径深度、基本名称长度或字母顺序。多个标准可组合使用以实现细粒度控制。

其他 lint 类型包括：空目录、损坏的符号链接、用户/组异常的文件以及未剥离符号的二进制文件。

# CAVEATS

基于哈希的检测存在理论上的碰撞风险。大型文件系统需要大量内存来跟踪状态。跟随符号链接模式可能大幅扩大搜索范围。删除脚本在执行前应仔细检查。某些文件系统不能准确记录修改时间。

# HISTORY

**rmlint** 由 **Christopher Pahl**（SeeSpotRun）于 **2012 年**前后创建，是一款快速、现代的重复文件查找工具。它以 C 语言编写，取代了较慢的 Python 前身。该项目强调安全性（生成可审查的脚本）和性能（并行哈希、增量匹配）。

# INSTALL

```apt: sudo apt install rmlint```

```dnf: sudo dnf install rmlint```

```brew: brew install rmlint```

```nix: nix profile install nixpkgs#rmlint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fdupes](/man/fdupes)(1), [jdupes](/man/jdupes)(1), [duperemove](/man/duperemove)(1), [rdfind](/man/rdfind)(1)
