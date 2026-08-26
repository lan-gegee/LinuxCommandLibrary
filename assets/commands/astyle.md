# TAGLINE

面向 C、C++、C# 和 Java 的源代码格式化工具

# TLDR

**格式化** C++ 代码

```astyle [file.cpp]```

用**指定风格**格式化

```astyle --style=google [file.cpp]```

**原地**格式化（覆盖原文件）

```astyle --suffix=none [file.cpp]```

**递归**格式化

```astyle --recursive "*.cpp,*.h"```

用**自定义选项**格式化

```astyle --indent=spaces=4 --style=kr [file.cpp]```

# SYNOPSIS

**astyle** [_--style=name_] [_--indent=type_] [_options_] _files_

# DESCRIPTION

**astyle**（Artistic Style）是一款面向 C、C++、C++/CLI、Objective-C、C# 和 Java 的源代码缩进与格式化工具。它按照统一的风格规范重排代码，提升可读性和可维护性。

该工具支持多种预定义风格（Google、Mozilla、GNU 等），并支持大量自定义选项。

# PARAMETERS

**--style=**_name_
> 预定义风格：allman、java、kr、stroustrup、whitesmith、vtk、ratliff、gnu、linux、horstmann、1tbs、google、mozilla、webkit、pico、lisp。

**--indent=**_type_
> 缩进方式：spaces=n、tab、force-tab=n。

**--attach-braces** / **--break-braces**
> 将左大括号附着到语句头或从语句头断开（取代较旧的 **--brackets** 选项）。

**--indent-classes**
> 缩进 class 块

**--indent-switches**
> 缩进 switch 块

**--pad-oper**
> 在运算符两侧填充空格

**--pad-header**
> 在关键字头（if、for、while）后填充空格

**--unpad-paren**
> 移除括号内的填充空格

**--suffix=**_suffix_
> 备份文件后缀（none 表示覆盖原文件）

**--recursive**
> 递归处理目录

**-n**, **--suffix=none**
> 不创建备份文件

**--dry-run**
> 仅显示更改而不实际应用

# CONFIGURATION

**~/.astylerc**
> 用户级默认选项文件。每行包含一个选项（如 --style=google）。

**.astylerc**
> 当前目录下的项目级选项文件，优先于用户默认值。

# CAVEATS

格式化整个项目之前务必备份代码。可能与版本控制的 diff 产生冲突。团队应在应用前就代码风格达成一致。某些风格可能与现有代码约定相冲突。

# HISTORY

**Artistic Style** 由 Tal Davidson 和 Jim Pattee 创建，于 **1998** 年首次发布，如今已成为 C 系语言的标准代码格式化工具之一。

# INSTALL

```apt: sudo apt install astyle```

```dnf: sudo dnf install astyle```

```pacman: sudo pacman -S astyle```

```apk: sudo apk add astyle```

```zypper: sudo zypper install astyle```

```brew: brew install astyle```

```nix: nix profile install nixpkgs#astyle```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[clang-format](/man/clang-format)(1), [indent](/man/indent)(1), [uncrustify](/man/uncrustify)(1)
