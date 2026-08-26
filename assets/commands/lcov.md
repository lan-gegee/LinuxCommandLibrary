# TAGLINE

处理 gcov 代码覆盖率数据

# TLDR

**捕获覆盖率数据**

```lcov --capture --directory [.] --output-file [coverage.info]```

**生成 HTML 报告**

```genhtml [coverage.info] --output-directory [coverage/]```

**移除匹配模式的文件**

```lcov --remove [coverage.info] '*/test/*' -o [filtered.info]```

**提取特定文件**

```lcov --extract [coverage.info] '*/src/*' -o [src.info]```

**合并跟踪文件**

```lcov --add-tracefile [a.info] --add-tracefile [b.info] -o [combined.info]```

**计数器清零**

```lcov --zerocounters --directory [.]```

# SYNOPSIS

**lcov** [_options_]

# PARAMETERS

**--capture**
> 捕获覆盖率数据。

**--directory** _DIR_
> 源目录。

**--output-file** _FILE_
> 输出跟踪文件。

**--remove** _FILE_ _PATTERN_
> 移除匹配的文件。

**--extract** _FILE_ _PATTERN_
> 提取匹配的文件。

**--add-tracefile** _FILE_
> 添加跟踪文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lcov** 处理 gcov 代码覆盖率数据。它收集并操作覆盖率信息。

该工具从 gcc/gcov 数据生成覆盖率报告。使用 genhtml 可创建 HTML 报告。

# CAVEATS

需要 gcc/gcov。专注于 C/C++。LCOV 软件包的一部分。

# HISTORY

lcov 为 **Linux Test Project** 而创建，用于提供图形化的代码覆盖率分析。

# INSTALL

```dnf: sudo dnf install lcov```

```pacman: sudo pacman -S lcov```

```apk: sudo apk add lcov```

```zypper: sudo zypper install lcov```

```brew: brew install lcov```

```nix: nix profile install nixpkgs#lcov```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcov](/man/gcov)(1), [genhtml](/man/genhtml)(1)
