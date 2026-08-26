# TAGLINE

计算 MATLAB 代码度量

# TLDR

为单个文件**计算度量**

```mh_metric [file.m]```

递归**分析**整个**目录**

```mh_metric [src/]```

将度量以 **JSON** 报告形式**输出**

```mh_metric --json=[metrics.json] [file.m]```

将度量以 **HTML** 报告形式**输出**

```mh_metric --html=[metrics.html] [file.m]```

将度量以**文本**报告形式**输出**

```mh_metric --text=[metrics.txt] [file.m]```

以 **CI 模式**运行，仅报告违规项

```mh_metric --ci [src/]```

# SYNOPSIS

**mh_metric** [_options_] [_files or directories_]

# PARAMETERS

_FILES_
> 要分析的 MATLAB 文件或目录。未指定时，递归分析整个工作目录。

**--json**=_FILE_
> 将 JSON 格式的度量报告写入指定文件。

**--html**=_FILE_
> 将 HTML 格式的度量报告写入指定文件。

**--text**=_FILE_
> 将纯文本格式的度量报告写入指定文件。

**--ci**
> CI 模式。不输出总体报告，只报告指标违规。

**--ignore-justifications-with-tickets**
> 忽略代码中提到工单编号的任何豁免说明。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mh_metric** 计算 MATLAB 和 Octave 文件的代码度量，并在指标超过可接受水平时报告违规。它测量圈复杂度、行数、函数长度、嵌套深度等代码质量指标。

该工具是 **MISS_HIT** 套件的一部分。若未指定文件或目录，它会分析整个工作目录及所有子目录。可通过项目树中的 **miss_hit.cfg** 文件提供配置。

# CAVEATS

属于 MISS_HIT 套件，通过 pip 安装（`pip install miss_hit`）。只分析 MATLAB（.m）和 Octave 文件。需要 Python 3.6 或更高版本。

# HISTORY

mh_metric 是 **MISS_HIT**（MATLAB Independent, Small & Safe, High Integrity Tools）的一部分，由 **Florian Schanda** 创建，用于度量 MATLAB 和 Simulink 代码质量指标。

# SEE ALSO

[mh_lint](/man/mh_lint)(1)
