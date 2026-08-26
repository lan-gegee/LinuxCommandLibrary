# TAGLINE

高度可配置的模态文本编辑器

# TLDR

**在 vim 中打开文件**

```vim [file]```

**在指定行打开文件**

```vim +[line_number] [file]```

**以只读模式打开**

```vim -R [file]```

**以标签页方式打开多个文件**

```vim -p [file1] [file2]```

**以分割窗口打开多个文件**

```vim -o [file1] [file2]```

**打开并执行命令**

```vim -c "[command]" [file]```

**比较两个文件**（diff 模式）

```vim -d [file1] [file2]```

# SYNOPSIS

**vim** [_options_] [_file_...]

# PARAMETERS

**+** _line_
> 从指定行号开始

**+** _command_
> 加载文件后执行命令

**-c** _command_
> 加载文件后执行命令

**-R**
> 只读模式

**-r**
> 恢复模式（从交换文件恢复）

**-p**
> 以标签页方式打开文件

**-o**
> 以水平分割方式打开文件

**-O**
> 以垂直分割方式打开文件

**-d**
> diff 模式

**-b**
> 二进制模式

**-x**
> 编辑加密文件

**-u** _vimrc_
> 使用指定的 vimrc 文件

**-N**
> 非 compatible 模式（使用 Vim 默认行为）

# NORMAL MODE COMMANDS

**Movement**：h/j/k/l（左/下/上/右），w/b（单词），0/$（行首/行尾），gg/G（文件开头/结尾）
**Editing**：i（插入），a（追加），o（下方新行），x（删除字符），dd（删除行），yy（复制行），p（粘贴）
**Save/Quit**：:w（保存），:q（退出），:wq（保存并退出），:q!（不保存退出），ZZ（保存并退出）
**Search**：/pattern（向前搜索），?pattern（向后搜索），n/N（下一个/上一个匹配）
**Undo/Redo**：u（撤销），Ctrl+r（重做）

# SYSTEM CLIPBOARD

**"+** 寄存器映射到系统剪贴板，因此你可以在 Vim 与其他应用程序之间复制粘贴。这需要编译时带剪贴板支持的 Vim；运行 **vim --version** 并查看是否有 **+clipboard**（Debian/Ubuntu 上安装 **vim-gtk3**）。

**Copy**："+y（复制 Visual 选区）、"+yy（复制当前行）、"+d（剪切到剪贴板）
**Paste**："+p（在光标后粘贴）、"+P（在光标前粘贴）

**"* 寄存器在 X11 上访问主选择区（中键粘贴），在其他平台上行为与 "+ 寄存器相同。

# SELECT ALL

**ggVG**：选择整个文件（gg 到顶部，V 进入按行 Visual，G 到底部）
**ggVGy**：全选并复制到 Vim 默认寄存器
**ggVG"+y**：全选并复制到系统剪贴板
**ggVGd**：全选并删除（剪切）文本

# MODES

**Normal**：用于导航和命令的默认模式
**Insert**：文本输入（i、a、o 等）
**Visual**：选择（v 按字符，V 按行，Ctrl+v 按块）
**Command**：Ex 命令（:）
**Replace**：覆盖文本（R）

在任何其他模式下按 **Esc** 返回 Normal 模式。

# DESCRIPTION

**vim**（Vi IMproved）是一个高度可配置的文本编辑器，专为高效文本编辑而设计。它在经典 vi 编辑器的基础上扩展了语法高亮、Visual 模式、多缓冲区和丰富的插件支持等特性。

Vim 主要通过不同模式下的键盘命令操作，无需离开主键位行即可完成强大的文本操作。虽然学习曲线陡峭，但熟练后编辑速度极快。

配置存放在 **~/.vimrc**（或 ~/.vim/vimrc）。插件可用 vim-plug、Vundle 等包管理器或原生包功能（Vim 8+）管理。

# CAVEATS

Vim 的模态编辑与大多数编辑器不同。新用户常被各种模式困扰；记住 **Esc** 可返回 Normal 模式。

配置可能变得复杂。从简单开始，按需添加功能。多用 **:help** —— Vim 有出色的内置文档。

如果因 Ctrl+S（XOFF）导致终端假死，按 **Ctrl+Q** 恢复。

# HISTORY

Vim 由 **Bram Moolenaar** 开发，于 **1991 年**首次发布，是 vi 的增强克隆。Vi 本身由 Bill Joy 于 **1976 年**创建。Vim 在保持 vi 兼容性的同时增加了许多特性，成为开发者中最流行的文本编辑器之一。

# INSTALL

```pacman: sudo pacman -S gvim```

```apk: sudo apk add gvim```

```zypper: sudo zypper install gvim```

```brew: brew install vim```

```nix: nix profile install nixpkgs#vim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vi](/man/vi)(1), [nvim](/man/nvim)(1), [nano](/man/nano)(1), [emacs](/man/emacs)(1), [vimtutor](/man/vimtutor)(1)
