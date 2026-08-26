# TAGLINE

检查 MATLAB 代码中的问题

# TLDR

**检查 MATLAB 代码**

```mh_lint [file.m]```

**检查目录**

```mh_lint [src/]```

**输出到文件**

```mh_lint [file.m] > [report.txt]```

**启用所有检查**

```mh_lint --all [file.m]```

**显示可用的检查项**

```mh_lint --list```

# SYNOPSIS

**mh_lint** [_options_] _files_

# PARAMETERS

_FILES_
> 要检查的 MATLAB 文件。

**--all**
> 启用所有检查。

**--list**
> 列出可用的检查项。

**--fix**
> 自动修复问题。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mh_lint** 用于检查 MATLAB 代码中的问题，识别风格违规和潜在缺陷。

该工具是 MISS_HIT 的一部分，用于在 MATLAB/Simulink 项目中强制执行编码规范。

# CAVEATS

属于 MISS_HIT。仅针对 MATLAB。基于 Python 的工具。

# HISTORY

mh_lint 是 **MISS_HIT** 的一部分——一套 MATLAB/Simulink 代码质量工具集。

# SEE ALSO

[mh_metric](/man/mh_metric)(1)
