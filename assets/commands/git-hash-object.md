# TAGLINE

计算对象 ID 值

# TLDR

**计算对象哈希**

```git hash-object [file]```

**计算并存储对象**

```git hash-object -w [file]```

**从 stdin 计算哈希**

```echo "[content]" | git hash-object --stdin```

**指定对象类型**

```git hash-object -t [blob] [file]```

# SYNOPSIS

**git** **hash-object** [_options_] [_file_...]

# PARAMETERS

**-w**
> 将对象写入数据库。

**--stdin**
> 从 stdin 读取。

**-t** _type_
> 对象类型（blob、commit、tree、tag）。

**--path** _path_
> 按照位于指定路径的情形来计算哈希。

**--no-filters**
> 不应用过滤器。

**--stdin-paths**
> 从 stdin 读取文件路径列表，逐个计算哈希。

**--literally**
> 允许对无法构成有效对象的内容进行哈希（用于调试）。

# DESCRIPTION

**git hash-object** 为文件计算对象 ID（SHA-1，采用该格式的仓库则为 SHA-256），并可选地将其存储到 Git 对象数据库中。这个底层 plumbing 命令暴露了 Git 内部的对象存储机制。

该命令通过将文件内容格式化为 Git 对象（带有类型和大小头部），然后对其计算哈希。使用 -w 选项时，它还会把对象写入 .git/objects/，使其成为仓库的一部分，即使尚未被任何提交引用。--stdin 选项支持对来自管道或脚本的内容计算哈希；--stdin-paths 则改为读取文件路径列表。

# CAVEATS

不使用 **-w** 时，只会计算对象的哈希而不会存储。默认会应用过滤器（例如 `.gitattributes` 中的 `clean`），除非给出 **--no-filters**；这可能会改变最终的哈希值。

# HISTORY

**git hash-object** 是自 Git 最早版本就存在的核心 plumbing 命令，暴露了内部用于 blob、树和提交的对象哈希机制。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-cat-file](/man/git-cat-file)(1), [git-write-tree](/man/git-write-tree)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-hash-object)```

<!-- verified: 2026-07-17 -->
