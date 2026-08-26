# TAGLINE

统计源代码行数并估算工作量

# TLDR

**统计目录中的行数**

```sloccount [src/]```

**带详细信息统计**

```sloccount --details [src/]```

**重复文件处理**

```sloccount --duplicates [src/]```

**宽输出格式**

```sloccount --wide [src/]```

**添加工作量估算**

```sloccount --effort [1.0] [2.5] [src/]```

# SYNOPSIS

**sloccount** [_options_] _directories_...

# DESCRIPTION

**sloccount** 统计软件项目中物理源代码行数（SLOC）。它识别多种编程语言，并使用 COCOMO 模型提供工作量和成本估算。

该工具有助于度量项目规模、估算开发工作量以及跟踪代码库的增长。

# PARAMETERS

**--details**
> 显示每个文件的详情。

**--duplicates**
> 统计重复文件。

**--crossdups**
> 统计跨目录的重复文件。

**--wide**
> 宽输出格式。

**--effort** _a_ _b_
> COCOMO 工作量参数。

**--schedule** _a_ _b_
> COCOMO 进度参数。

**--personcost** _cost_
> 人均年度成本。

**--overhead** _rate_
> 管理费率。

**--cached**
> 使用上一次运行的缓存结果，而不重新计算。

**--append**
> 追加到现有数据目录而不是清空它。

**--follow**
> 跟随符号链接。

**--autogen**
> 统计自动生成的源文件（通常被排除）。

**--multiproject**
> 将各目录视为独立的项目。

**--filecount**
> 显示文件数量。

**--datadir** _dir_
> 数据目录（默认：~/.slocdata）。

**--addlang** _lang_
> 添加语言。

# CAVEATS

COCOMO 估算只是粗略近似。语言识别可能遗漏部分文件。大型项目分析较慢。生成的代码可能使统计结果失真。

# HISTORY

**SLOCCount** 由 **David A. Wheeler** 创建，用于精确统计源代码行数。它应用软件经济学模型来估算开发工作量，帮助进行项目规划和比较。

# INSTALL

```apt: sudo apt install sloccount```

```dnf: sudo dnf install sloccount```

```pacman: sudo pacman -S sloccount```

```brew: brew install sloccount```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cloc](/man/cloc)(1), [tokei](/man/tokei)(1), [wc](/man/wc)(1), [find](/man/find)(1)
