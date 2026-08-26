# TAGLINE

直观的命令行查找替换工具

# TLDR

**替换文件中的文本**

```sd '[find]' '[replace]' [path/to/file]```

**按字面字符串替换文本**（不使用正则表达式）

```sd -F '[find]' '[replace]' [path/to/file]```

**预览更改**而不修改文件

```sd -p '[find]' '[replace]' [path/to/file]```

**从 stdin 替换文本**

```echo '[text]' | sd '[find]' '[replace]'```

在替换中**使用捕获组**

```sd '(\w+)@(\w+)' '$1 at $2' [file]```

配合 fd **在多个文件中替换**

```fd --type file --exec sd '[find]' '[replace]'```

**字面替换包含特殊字符的文本**

```sd -F '$.value' 'newValue' [config.json]```

# SYNOPSIS

**sd** [_options_] _find_ _replace-with_ [_files_...]

# PARAMETERS

**-F**, **--fixed-strings**
> 将查找和替换模式视为字面字符串，而非正则表达式

**-p**, **--preview**
> 预览更改而不修改文件

**-f**, **--flags** _FLAGS_
> 正则标志：c（区分大小写）、i（不区分大小写）、m（多行）、s（dotall）

**--**
> 标志结束；允许模式以短横线开头

# DESCRIPTION

**sd** 是一款用 Rust 编写的快速、直观的查找替换命令行工具。它是 sed 的现代化替代品，专注于文本替换，语法更简单、更易读。

与 sed 不同，sd 使用大多数开发者已经熟悉的 JavaScript/Python 风格正则表达式。查找和替换模式作为独立参数提供，而不是组合在一个复杂表达式中，使命令更易编写和理解。

捕获组的使用很直观：使用 **$1**、**$2** 引用索引组，或用 **$name** 引用以 **(?P\<name\>pattern)** 定义的命名组。要在替换中包含字面的美元符号，请将其转义为 **$$**。

未指定文件时，sd 从标准输入读取。配合 **fd** 等工具，可以在整个代码库中进行强大的批量替换。

# CAVEATS

提供了文件参数时，sd 默认就地修改文件。处理重要文件时务必先用 **-p** 预览更改。其正则风格与 sed 不同，从 sed 工作流迁移时可能需要调整模式。

# HISTORY

**sd** 由 **chmln** 创建，约于 **2019 年**首次发布。它以 **Rust** 编写，旨在解决 sed 在日常查找替换任务中的复杂性和不直观语法。该项目作为重新构想传统 Unix 工具的现代 Rust CLI 工具浪潮的一部分而广受欢迎。

# INSTALL

```apt: sudo apt install sd```

```pacman: sudo pacman -S sd```

```apk: sudo apk add sd```

```zypper: sudo zypper install sd```

```brew: brew install sd```

```nix: nix profile install nixpkgs#sd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sed](/man/sed)(1), [awk](/man/awk)(1), [rg](/man/rg)(1), [fd](/man/fd)(1), [perl](/man/perl)(1)
