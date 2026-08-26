# TAGLINE

在命令行中批量重命名文件和目录

# TLDR

使用正则表达式**试运行**重命名

```rnr '[pattern]' '[replacement]' [files...]```

**应用**重命名（写入）

```rnr -f '[pattern]' '[replacement]' [files...]```

**递归**重命名目录

```rnr -r '[pattern]' '[replacement]' [dir]```

**交互式**确认

```rnr -i '[pattern]' '[replacement]' [files...]```

# SYNOPSIS

**rnr** [*options*] *from* *to* [*paths*...]

# DESCRIPTION

**rnr** 是一个 Rust 编写的批量重命名工具，支持正则替换、默认试运行（或按版本通过显式标志执行）、递归处理和撤销转储。它专注于为媒体库和代码树提供安全的批量重命名。

请始终先运行一次试运行并检查计划执行的操作。force/apply 的确切标志在不同版本间略有差异——请用 **rnr --help** 确认。

# PARAMETERS

*from* *to*

> 正则模式和替换字符串。

*paths*

> 要处理的文件/目录。

**-r**, **--recursive**

> 递归进入目录。

**-f**, **--force** / apply 标志

> 执行重命名（在默认为试运行时）。

**-i**, **--interactive**

> 对每次重命名进行确认。

**--dry-run**

> 只打印操作而不更改文件系统。

# CAVEATS

如果模式过于宽泛，正则重命名可能破坏文件名。跨文件系统的移动和目标名称冲突需要格外小心。请保留备份或使用版本控制。

# INSTALL

```brew: brew install rnr```

```nix: nix profile install nixpkgs#rnr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rename](/man/rename)(1), [mmv](/man/mmv)(1), [mv](/man/mv)(1)

# RESOURCES

```[Source code](https://github.com/ismaelgv/rnr)```

<!-- verified: 2026-07-19 -->
