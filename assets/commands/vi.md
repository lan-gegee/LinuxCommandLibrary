# TAGLINE

经典的 Unix 可视化文本编辑器

# TLDR

**打开文件**

```vi [file]```

**在指定行打开**

```vi +[line_number] [file]```

**以只读模式打开**

```vi -R [file]```

**打开多个文件**

```vi [file1] [file2]```

**从交换文件恢复文件**

```vi -r [file]```

# SYNOPSIS

**vi** [**-rR**] [**+**_command_] [_file_...]

# PARAMETERS

**-R**
> 只读模式

**-r** [_file_]
> 恢复模式；列出可恢复的文件或恢复指定文件

**+** _command_
> 加载后执行命令

**+** _line_
> 从指定行号开始

**-c** _command_
> 加载后执行命令（与 + 相同）

# MODES

**Normal**：导航与命令（默认模式）
**Insert**：文本输入（i、a、o）
**Command**：Ex 命令（:）
**Visual**：选择（v）—— 仅 vim 支持

按 **Esc** 返回 Normal 模式。

# ESSENTIAL COMMANDS

**Navigation**：h/j/k/l（左/下/上/右），0/$（行首/行尾），gg/G（文件开头/结尾）
**Insert**：i（光标前），a（光标后），o（下方新行），O（上方新行）
**Delete**：x（字符），dd（行），dw（单词）
**Copy/Paste**：yy（复制行），p（向后粘贴），P（向前粘贴）
**Undo**：u（撤销），Ctrl+r（重做 —— 仅 vim 支持）
**Save/Quit**：:w（保存），:q（退出），:wq（保存并退出），:q!（不保存退出），ZZ（保存并退出）
**Search**：/pattern（向前搜索），?pattern（向后搜索），n/N（下一个/上一个）

# DESCRIPTION

**vi** 是经典的 Unix 可视化文本编辑器，几乎所有类 Unix 系统都有它。它采用模态编辑方式，按键的功能取决于当前所处模式。

在大多数现代 Linux 系统上，**vi** 实际上是以兼容模式运行的 **vim**（Vi IMproved）的链接，或是 **nvi** 之类的极简 vi 克隆。真正的原始 vi 在商业 Unix 系统之外很少见。

模态设计无需修饰键即可进行强大的文本操作，导航时手指不必离开主键位行。虽然学习曲线陡峭，但熟练后编辑效率极高。

传统 vi 的配置存储在 **~/.exrc**，vim 则使用 **~/.vimrc**。

# CAVEATS

Vi 学习曲线陡峭。可使用 **vimtutor**（如果安装了 vim）进行交互式学习。

终端配置不正确时，vi 可能无法正常运行。请正确设置 TERM 环境变量。

在精简系统上，可能只有基础版 vi 而没有 vim 的增强功能。请掌握常用的命令子集。

# HISTORY

Vi 由 **Bill Joy** 于 **1976 年**在加州大学伯克利分校创建，作为 ex 行编辑器的可视化模式。它成为 Unix 的标准编辑器，并影响了无数文本编辑器。其名字代表 "visual"，因为它是 ex 的可视化界面。

# INSTALL

```apk: sudo apk add neatvi-vi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [nvim](/man/nvim)(1), [nano](/man/nano)(1), [emacs](/man/emacs)(1), [ed](/man/ed)(1)
