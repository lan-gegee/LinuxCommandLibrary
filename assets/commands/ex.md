# TAGLINE

面向行的文本编辑器，vi 的前身

# TLDR

**对文件进入 ex 模式**

```ex [file.txt]```

**执行替换命令后退出**

```ex -c "%s/[old]/[new]/g" -c "wq" [file.txt]```

**以只读模式打开文件**

```ex -R [file.txt]```

**依次编辑多个文件**

```ex [file1.txt] [file2.txt]```

# SYNOPSIS

**ex** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要编辑的文件。

**-c** _COMMAND_
> 加载第一个文件后执行命令。

**-s**
> 静默（批处理）模式。抑制所有交互反馈，适合脚本使用。

**-R**
> 只读模式。禁止写入文件。

**-r** _FILE_
> 在崩溃后从交换文件恢复编辑会话。

**-n**
> 不使用交换文件（vim 实现）。

**-t** _TAG_
> 编辑包含指定标签的文件。

**-V**
> 详细模式。显示从标准输入读取的命令。

**-v**
> 以可视模式启动（等同于运行 vi）。

# DESCRIPTION

**ex** 是一个面向行的文本编辑器。它没有可视化界面，通过命令行进行编辑，使用的正是 vi 冒号（:) 命令背后的同一套命令语言。命令在提示符处输入，而非全屏界面中操作。

ex 特别适合批量编辑和脚本化的文件修改，无需交互即可完成查找替换及其他变换。配合 **-s** 静默模式，它可以从 stdin 或脚本读取编辑命令进行处理。

ex 和 vi 实际上是同一个程序在不同模式下的启动方式。运行 **ex -v** 进入可视模式（vi），运行 **vi -e** 则进入行模式（ex）。

# CAVEATS

ex 模式下没有可视化反馈，复杂编辑容易出错。大多数现代系统通过 vim 提供 ex（即 **vim -e**）。POSIX 规范只定义了其中一部分功能；vim 的 ex 模式包含大量扩展。

# HISTORY

ex 由 **Bill Joy** 于 20 世纪 70 年代末在加州大学伯克利分校开发，是 ed 的扩展版本。它后来增加了可视化界面，演变为 vi，而 ex 作为底层命令模式保留下来。ex 首次出现在 **1BSD**（1978 年）中。

# INSTALL

```pacman: sudo pacman -S gvim```

```apk: sudo apk add gvim```

```zypper: sudo zypper install gvim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vi](/man/vi)(1), [vim](/man/vim)(1), [ed](/man/ed)(1), [sed](/man/sed)(1)
