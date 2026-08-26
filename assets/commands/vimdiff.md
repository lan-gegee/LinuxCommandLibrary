# TAGLINE

在 Vim 中并排比较文件

# TLDR

**并排比较两个文件**

```vimdiff [file1] [file2]```

**比较三个文件**

```vimdiff [file1] [file2] [file3]```

**以只读模式打开文件**

```vimdiff -R [file1] [file2]```

**使用水平分割**而非垂直分割

```vimdiff -o [file1] [file2]```

**以干净环境启动**（不加载 .vimrc）

```vimdiff --clean [file1] [file2]```

**比较文件并在启动时执行指定命令**

```vimdiff -c "[command]" [file1] [file2]```

# SYNOPSIS

**vimdiff** [_options_] _file1_ _file2_ [_file3_ [_file4_]]

# PARAMETERS

**-O**
> 垂直分割窗口，左右并排（两个文件时的默认方式）。

**-o**
> 水平分割窗口，上下堆叠。

**-R**
> 以只读模式打开所有文件。

**-c** _command_
> 加载第一个文件后执行命令。

**--clean**
> 启动时不加载 .vimrc 或插件。

**-d**
> 显式启用 diff 模式（vimdiff 会自动启用）。

# DESCRIPTION

**vimdiff** 以 diff 模式启动 Vim 并打开两到八个文件，每个文件位于独立窗口中。文件之间的差异会被高亮显示，便于比较和合并更改。

这等同于运行 **vim -d file1 file2**。在 diff 模式下，Vim 自动设置同步滚动（**scrollbind**）、差异高亮以及折叠未变更行等选项。

在 vimdiff 中，使用 **]c** 和 **[c** 在差异之间跳转。使用 **do**（diff obtain）从另一个窗口拉取更改，使用 **dp**（diff put）将更改推送到另一个窗口。编辑后使用 **:diffupdate** 刷新高亮。

# CAVEATS

vimdiff 最适合两个文件的比较；比较超过四个文件时会难以阅读。差异较多的大文件可能出现性能问题。未变更行的折叠行为可通过 **:set diffopt** 调整。

# HISTORY

Diff 模式由 Bram Moolenaar 加入 **Vim**。vimdiff 包装脚本自 **2001 年**发布的 Vim 6.0 起成为 Vim 的一部分。该功能受其他 diff 工具类似功能的启发，但直接集成到了 Vim 强大的编辑环境中。对最多八个文件的支持在后续版本中加入。

# INSTALL

```apk: sudo apk add vimdiff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [diff](/man/diff)(1), [meld](/man/meld)(1), [kdiff3](/man/kdiff3)(1)
