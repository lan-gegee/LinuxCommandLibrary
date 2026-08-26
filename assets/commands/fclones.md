# TAGLINE

高性能重复文件查找工具

# TLDR

**查找重复文件**

```fclones group [directory]```

**交互式删除重复文件**

```fclones group [directory] | fclones remove```

**限制扫描深度**

```fclones group --depth [2] [directory]```

**用硬链接替换重复文件**

```fclones group [directory] | fclones link```

**显示重复文件统计**

```fclones group [directory] --format fdupes```

**将重复文件移动到**目录

```fclones group [directory] | fclones move [trash_dir]```

# SYNOPSIS

**fclones** _command_ [_options_] [_paths_...]

# PARAMETERS

_COMMAND_
> 操作：group、remove、link、move。

_PATHS_
> 要扫描的目录或文件。

**--depth** _N_
> 最大目录深度。

**--min** _SIZE_
> 最小文件大小。

**--max** _SIZE_
> 最大文件大小。

**--format** _FORMAT_
> 输出格式：default、fdupes、csv、json。

**-R**, **--follow-links**
> 跟随符号链接。

**--threads** _N_
> 线程数。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fclones** 是一款用 Rust 编写的高性能重复文件查找工具。它使用多种算法，包括基于哈希的比较和并行处理，可快速扫描大型文件系统。

该工具分两个阶段工作：先用 'group' 找出重复文件，再用 remove、link 或 move 对其处理。输出可在命令间通过管道传递，也可保存下来在操作前进行审查。

fclones 通过部分哈希、缓存和 SIMD 加速等技术优化速度。

# CAVEATS

删除前需仔细审查。硬链接会影响所有副本。大型目录可能占用大量内存。

# HISTORY

fclones 作为 fdupes 等工具的现代替代品而创建，借助 Rust 的速度和内存安全特性强调性能。它通过并行化和优化的哈希算法实现了显著的加速。

# INSTALL

```pacman: sudo pacman -S fclones```

```apk: sudo apk add fclones```

```zypper: sudo zypper install fclones```

```brew: brew install fclones```

```nix: nix profile install nixpkgs#fclones```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fdupes](/man/fdupes)(1), [rmlint](/man/rmlint)(1), [jdupes](/man/jdupes)(1)
