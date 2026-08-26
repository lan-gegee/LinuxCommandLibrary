# TAGLINE

从终端启动 Zed 代码编辑器

# TLDR

**打开文件**

```zeditor [file]```

**在指定行打开**

```zeditor [file]:[line]```

**打开多个文件**

```zeditor [file1] [file2]```

**新建窗口**

```zeditor --new [file]```

# SYNOPSIS

**zeditor** [_--new_] [_options_] [_files_]

# PARAMETERS

**--new**
> 新建窗口。

**--wait**
> 等待窗口关闭。

**--help**
> 显示帮助。

# DESCRIPTION

**zeditor** 是 Zed 的命令行启动器，Zed 是一款用 Rust 编写的现代代码编辑器。它可以在终端中于 Zed 图形编辑器内打开文件和目录。

文件可以使用 **file:line** 语法在指定行号处打开。**--new** 标志会新建一个编辑器窗口而不是复用现有窗口；**--wait** 会阻塞终端直到编辑器窗口关闭，这对 git 提交信息以及其他需要调用编辑器的工具很有用。

Zed 本身是一款高性能编辑器，具有实时协作编辑、集成 AI 代码辅助，以及为速度而设计的极简界面。

# CAVEATS

需要安装 Zed。编辑器较新，各平台支持情况不一。

# HISTORY

**zeditor** 是 **Zed** 的命令行启动器，Zed 是一款用 Rust 构建的现代代码编辑器。

# SEE ALSO

[code](/man/code)(1), [nvim](/man/nvim)(1), [helix](/man/helix)(1)
