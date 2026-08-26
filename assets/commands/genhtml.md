# TAGLINE

从 lcov 跟踪文件生成 HTML 覆盖率报告

# TLDR

**生成 HTML 报告**

```genhtml [coverage.info] -o [html_output]```

**添加标题**

```genhtml --title "[Coverage Report]" [coverage.info] -o [html_output]```

**显示分支覆盖率**

```genhtml --branch-coverage [coverage.info] -o [html_output]```

**前缀路径**

```genhtml --prefix [/src] [coverage.info] -o [html_output]```

# SYNOPSIS

**genhtml** [_options_] _tracefile_...

# PARAMETERS

_TRACEFILE_
> lcov 覆盖率数据文件。

**-o** _DIR_, **--output-directory** _DIR_
> 输出目录。

**--title** _TEXT_
> 报告标题。

**--branch-coverage**
> 包含分支覆盖率。

**--prefix** _PATH_
> 移除源码路径前缀。

**--legend**
> 包含覆盖率图例。

**--help**
> 显示帮助信息。

# DESCRIPTION

**genhtml** 从 lcov 跟踪文件创建 HTML 覆盖率报告。它生成可导航的报告，通过源代码高亮显示行、函数和分支覆盖率。

该工具处理覆盖率数据，生成用于审阅测试覆盖情况的可视化报告。多个跟踪文件可以合并到一份报告中。

genhtml 是 lcov 覆盖率工具套件的可视化组件。

# CAVEATS

需要 lcov 跟踪文件。大型代码库会产生很大的报告。查看需要浏览器。

# HISTORY

genhtml 是 **lcov**（Linux Test Project 的覆盖率工具）的一部分。它为 lcov 从 gcov 收集的覆盖率数据提供 HTML 可视化。

# INSTALL

```dnf: sudo dnf install lcov```

```pacman: sudo pacman -S lcov```

```apk: sudo apk add lcov```

```zypper: sudo zypper install lcov```

```brew: brew install lcov```

```nix: nix profile install nixpkgs#lcov```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lcov](/man/lcov)(1), [gcov](/man/gcov)(1)

# RESOURCES

```[Source code](https://github.com/linux-test-project/lcov)```

<!-- verified: 2026-07-15 -->
