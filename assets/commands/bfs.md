# TAGLINE

广度优先文件搜索

# TLDR

**查找**所有文件

```bfs [/path]```

**按名称查找**

```bfs [/path] -name ["*.txt"]```

**仅查找**普通文件

```bfs [/path] -type f```

**用 N 个线程并行搜索**

```bfs [/path] -j [8] -name ["*.c"]```

**从搜索中排除**子树

```bfs [/path] -exclude -name [node_modules]```

**执行**命令

```bfs [/path] -name ["*.log"] -delete```

# SYNOPSIS

**bfs** [_options_] [_path_...] [_expression_]

# DESCRIPTION

**bfs** 是 Unix find 命令的广度优先变体。它以广度优先而非深度优先的方式遍历目录，这对某些操作更快，且打印结果时更直观。

该工具与 GNU find 兼容，但采用不同的遍历策略。

# PARAMETERS

**-name** _pattern_
> 匹配文件名模式

**-type** _type_
> 文件类型（f、d、l 等）

**-size** _n_
> 文件大小

**-mtime** _n_
> 修改时间

**-exec** _command_ **;**
> 执行命令

**-delete**
> 删除匹配的文件

**-depth**
> 先处理目录内容再处理目录本身

**-maxdepth** _n_
> 最大下探深度

# BFS-SPECIFIC FLAGS

**-j** _n_
> 用 N 个线程并行搜索（默认：CPU 数量，最多 8）

**-S** _bfs|dfs|ids|eds_
> 选择搜索策略：广度优先（默认）、深度优先、迭代加深或指数加深

**-color** / **-nocolor**
> 开启或关闭彩色输出（输出为终端时默认 -color）

**-hidden** / **-nohidden**
> 包含或排除隐藏文件（以 . 开头的文件）

**-exclude** _expression_
> 从搜索中排除所有匹配表达式的路径

**-unique**
> 跳过已经见过的文件（配合 -L 使用很有用）

**-x**
> 不下探到其他挂载点（与 -xdev 相同）

**-status**
> 搜索时显示状态栏

**-files0-from** _file_
> 从文件中读取以 NUL 分隔的起始路径

**-D** _flag_
> 打开某个调试标志

# DIFFERENCES FROM FIND

- **广度优先**的遍历顺序
- 对 -quit 操作通常更快
- 输出顺序更直观
- 命令行语法兼容

# WORKFLOW

```bash
# Find all PDFs (breadth-first)
bfs /home -name "*.pdf"

# Find large files in top levels first
bfs / -size +100M

# Delete empty directories
bfs /tmp -type d -empty -delete

# Find recently modified
bfs /var/log -mtime -1
```

# CAVEATS

不如 find 普遍可用。不同的遍历顺序可能影响某些操作。大多数系统默认未安装。复杂查询可能出现行为差异。

# HISTORY

**bfs** 由 Tavian Barnes 于 **2015 年**创建，作为传统 find 命令的优化广度优先替代品。

# INSTALL

```apt: sudo apt install bfs```

```dnf: sudo dnf install bfs```

```pacman: sudo pacman -S bfs```

```apk: sudo apk add bfs```

```brew: brew install bfs```

```nix: nix profile install nixpkgs#bfs```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[find](/man/find)(1), [fd](/man/fd)(1), [locate](/man/locate)(1)

# RESOURCES

```[Source code](https://github.com/tavianator/bfs)```

```[Homepage](https://tavianator.com/projects/bfs.html)```

<!-- verified: 2026-06-19 -->
