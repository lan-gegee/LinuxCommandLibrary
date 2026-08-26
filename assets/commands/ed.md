# TAGLINE

标准 Unix 行编辑器

# TLDR

**启动 ed 并打开**文件

```ed [file.txt]```

**打印第 5 行**

```5p```

**打印所有行**

```,p```

**替换文本**

```s/old/new/```

**在该行全局替换**

```s/old/new/g```

**在当前行之后追加**

```a```

**保存并退出**

```wq```

**通过管道向 ed 传入命令以非交互方式编辑文件**

```printf '%s\n' ',s/old/new/g' 'w' 'q' | ed -s [file.txt]```

# SYNOPSIS

**ed** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要编辑的文件。

**-p** _STRING_, **--prompt=**_STRING_
> 使用 STRING 作为命令提示符（默认没有提示符）。

**-s**, **--quiet**, **--script**
> 抑制诊断信息、字节数和 '!' 提示：脚本的通常选择。

**-E**, **--extended-regexp**
> 使用扩展正则表达式而非基本正则表达式。

**-G**, **--traditional**
> 以与传统 Unix ed 兼容的模式运行。

**-l**, **--loose-exit-status**
> 即使命令失败也以状态码 0 退出。

**-r**, **--restricted**
> 受限模式：禁止 shell 逃逸和编辑当前目录之外的文件。

**-v**, **--verbose**
> 输出完整的错误消息，而不是单纯的 '?'。

**--help**
> 显示帮助并退出。

**--version**
> 显示版本并退出。

# DESCRIPTION

**ed** 是标准的 Unix 行编辑器。它默认在命令模式下运行，接受单字母命令来导航、查看和修改文本。它是 sed 和 vi 的祖先。

命令通常由一个地址或范围加上一个命令字母组成。地址可以是行号、模式或特殊字符（`.` 表示当前行，`$` 表示最后一行）。

ed 适用于脚本化编辑，因为命令可以通过管道传入。它的极简接口使其在全屏编辑器不可用时对紧急系统恢复很有价值。

# CAVEATS

默认没有可视化反馈。错误仅以 "?" 报告，除非启用 verbose。命令语法有一定学习曲线。不适合日常随意编辑。

# HISTORY

ed 由 **Ken Thompson** 于 **1969 年**在贝尔实验室编写，是最早的 Unix 程序之一。它的设计影响了 sed、ex、vi，并最终影响到现代文本编辑器。

# INSTALL

```apt: sudo apt install ed```

```dnf: sudo dnf install ed```

```pacman: sudo pacman -S ed```

```apk: sudo apk add ed```

```zypper: sudo zypper install ed```

```brew: brew install ed```

```nix: nix profile install nixpkgs#ed```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sed](/man/sed)(1), [vi](/man/vi)(1), [ex](/man/ex)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/ed/)```

```[Documentation](https://www.gnu.org/software/ed/manual/ed_manual.html)```

<!-- verified: 2026-07-14 -->
