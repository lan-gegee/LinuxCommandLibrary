# TAGLINE

快速的源代码行数统计工具

# TLDR

**统计当前目录的行数**

```scc```

**统计指定目录**

```scc [path/to/dir]```

**统计特定语言**

```scc --include-ext [py]```

**排除目录**

```scc --exclude-dir [vendor,node_modules]```

**按行数排序**

```scc --sort lines```

**以 JSON 输出**

```scc --format json```

**显示复杂度估计**

```scc -w```

**按文件显示**

```scc --by-file```

# SYNOPSIS

**scc** [_--include-ext ext_] [_--exclude-dir dirs_] [_--format fmt_] [_options_] [_paths_]

# PARAMETERS

**--include-ext** _EXT_
> 只包含指定扩展名。

**--exclude-dir** _DIRS_
> 排除目录。

**--sort** _FIELD_
> 按字段排序（files、lines、blanks、code、comments）。

**--format** _FMT_
> 输出格式（default、json、csv、html 等）。

**-w**, **--wide**
> 显示复杂度和加权行数。

**--by-file**
> 显示每个文件的明细。

**--no-duplicates**
> 忽略重复文件。

**--no-gen**
> 忽略生成的文件。

**--no-min**
> 忽略压缩过的文件。

**--cocomo**
> 显示 COCOMO 估计。

**-f** _PATTERN_
> 匹配文件名。

**-M** _SIZE_
> 最大文件大小。

# DESCRIPTION

**scc**（Succinct Code Counter）统计多种语言的代码行数。它借助并行处理和优化的解析，速度极快。

输出会按语言展示文件数、总行数、空行数、注释行数和代码行数。wide 模式还会基于分支情况添加复杂度估计。

语言检测结合文件扩展名和内容检查。它能识别数百种语言，从常见到冷门一应俱全。

生成文件和压缩文件的检测可避免统计样板代码。忽略重复文件则可以避免把引入的第三方代码重复计算多次。

COCOMO 估算提供粗略的工作量指标。这些数字是理论值，但用于比较仍有参考价值。

多种输出格式便于与其他工具集成。JSON 和 CSV 可供脚本和仪表盘进一步处理。

# CAVEATS

复杂度估计是启发式的。语言检测可能误判某些文件。非常大的代码库可能需要较多内存。

# HISTORY

**scc** 由 **Ben Boyter** 于 **2018 年**前后创建，作为 cloc 及其他行数统计工具的更快替代品。它使用 Go 编写，通过并行化和高效算法强调速度。

# INSTALL

```pacman: sudo pacman -S sc-controller```

```apk: sudo apk add sc-controller```

```zypper: sudo zypper install sc-controller```

```brew: brew install scc```

```nix: nix profile install nixpkgs#sc-controller```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cloc](/man/cloc)(1), [tokei](/man/tokei)(1), [loc](/man/loc)(1), [wc](/man/wc)(1)
