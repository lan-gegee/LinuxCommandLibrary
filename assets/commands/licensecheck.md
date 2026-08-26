# TAGLINE

扫描文件中的许可证信息和版权声明

# TLDR

**检查文件中的许可证**

```licensecheck [file]```

**递归检查目录**

```licensecheck -r [directory]```

**以机器可读格式输出**

```licensecheck --copyright -m [file]```

**检查特定文件类型**

```licensecheck -r --check '*.py' [directory]```

**只显示含许可证的文件**

```licensecheck -r -l [directory]```

# SYNOPSIS

**licensecheck** [_options_] _files_...

# PARAMETERS

**-r**, **--recursive**
> 递归检查目录。

**-l**, **--lines** _n_
> 只检查前 n 行（默认 60）。

**-c**, **--check** _regex_
> 只检查匹配的文件名。

**-i**, **--ignore** _regex_
> 忽略匹配的文件名。

**-m**, **--machine**
> 机器可读输出。

**--copyright**
> 显示版权声明。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**licensecheck** 扫描文件中的许可证信息和版权声明。它检查源代码头部，以识别文件所使用的发布许可证。

该工具能识别许多常见的开源许可证，包括 GPL、MIT、BSD、Apache 等。

# RECOGNIZED LICENSES

```
GPL, LGPL, AGPL (various versions)
MIT, BSD (2/3-clause)
Apache, MPL
Artistic, Perl
Public Domain
```

# CAVEATS

基于启发式的检测可能遗漏或误判许可证。自定义许可证需要人工审查。只检查文件头部。

# HISTORY

licensecheck 起源于 Debian，是一个用于检查软件包源码许可证合规性的工具，帮助维护者核实许可证信息。

# INSTALL

```dnf: sudo dnf install licensecheck```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[license](/man/license)(1), [reuse](/man/reuse)(1)
