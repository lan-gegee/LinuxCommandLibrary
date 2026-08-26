# TAGLINE

Vim 的图形界面版本

# TLDR

**在 GUI 版 vim 中打开文件**

```gvim [file]```

**以标签页打开多个文件**

```gvim -p [file1] [file2]```

**以只读模式打开**

```gvim -R [file]```

**以 diff 模式打开**

```gvim -d [file1] [file2]```

**打开并定位到指定行**

```gvim +[42] [file]```

**在前台打开（不 fork）**

```gvim -f [file]```

**打开文件后执行命令**

```gvim -c "[%s/foo/bar/g]" [file]```

# SYNOPSIS

**gvim** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要编辑的文件。

**-p**
> 以标签页方式打开文件。

**-o**
> 以水平分割方式打开文件。

**-O**
> 以垂直分割方式打开文件。

**-R**
> 只读模式。

**-d**
> diff 模式。

**+** _NUM_
> 从指定行号开始。

**-c** _CMD_
> 启动后执行命令。

**-f**, **--nofork**
> 在前台运行，不 fork 并脱离 shell。

**-g**
> 以 GUI 模式启动（用于以 vim -g 方式调用时）。

**-u** _FILE_
> 使用指定的 vimrc 文件而非默认文件进行初始化。

**-U** _FILE_
> 使用指定的 gvimrc 文件进行 GUI 初始化。

**-N**
> 非兼容模式。重置 'compatible' 选项。

**-geometry** _GEOM_
> 设置初始窗口几何尺寸（如 80x25+0+0）。

**--**
> 选项结束标志。此后的参数被视为文件名。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gvim** 是 Vim 的 GUI 版本。它在提供全部 Vim 功能的同时，增加了图形菜单、鼠标支持和系统剪贴板集成。

该编辑器支持与终端 Vim 相同的命令和插件。它提供工具栏、滚动条和可配置字体等视觉特性。默认情况下，gvim 会 fork 并脱离启动它的 shell；使用 -f 或 --nofork 可以在前台运行。

# CAVEATS

需要 X11/Wayland 或 Windows GUI。内存占用比 vim 更大。GUI 特性可在 .gvimrc 中配置。

# HISTORY

gvim 由 **Bram Moolenaar** 作为 **Vim** 的一部分开发而成，用于为该编辑器提供图形界面。

# INSTALL

```pacman: sudo pacman -S gvim```

```apk: sudo apk add gvim```

```zypper: sudo zypper install gvim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [vi](/man/vi)(1), [nvim](/man/nvim)(1), [vimdiff](/man/vimdiff)(1)
