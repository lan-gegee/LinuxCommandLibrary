# TAGLINE

Sublime Text 命令行启动器

# TLDR

在 Sublime Text 中**打开文件**

```subl [path/to/file]```

**在指定行列位置打开文件**

```subl [path/to/file]:[line]:[column]```

**将目录作为项目打开**

```subl [path/to/directory]```

**在新窗口中打开文件**

```subl -n [file1] [file2]```

**将文件夹添加到当前窗口**而不是打开新窗口

```subl -a [path/to/directory]```

**等待文件关闭后再返回**（对 git 有用）

```subl -w [path/to/file]```

**从 stdin 打开**

```echo "[text]" | subl -```

# SYNOPSIS

**subl** [_options_] [_files_] [_directories_]

# PARAMETERS

**-n**, **--new-window**
> 打开新窗口而不是复用现有实例。

**-a**, **--add**
> 将文件夹添加到当前窗口，而不是打开新窗口。

**-w**, **--wait**
> 等待文件关闭后再返回。适合作为版本控制的编辑器。

**-b**, **--background**
> 打开文件但不激活应用窗口。

**--project** _project_
> 加载指定的 .sublime-project 或 .sublime-workspace 文件。

**--command** _command_
> 执行 Sublime Text 内部命令（例如 **save_all**、**build**）。

**--safe-mode**
> 在无插件的沙箱化干净环境中启动。

**--launch-or-new-window**
> 仅当应用已在运行时才打开新窗口。

**-v**, **--version**
> 打印版本信息并退出。

**-h**, **--help**
> 显示帮助消息并退出。

# DESCRIPTION

**subl** 是 Sublime Text 的命令行接口，Sublime Text 是一款流行的跨平台文本编辑器。它允许从终端打开文件和目录，并与 git、subversion 等 Unix 工具集成。

文件名可以带 **:line** 或 **:line:column** 后缀，以在特定位置打开（从 1 开始计数）。该工具可通过 **-** 从 stdin 读取内容。配合 **-w** 使用时，它会阻塞直到文件被关闭，因此适合作为版本控制系统的外部编辑器（例如 `EDITOR='subl -w' git commit`）。

# CAVEATS

使用 **subl** 命令需要已安装 Sublime Text。手动安装时，可能需要创建符号链接：**ln -s /opt/sublime_text/sublime_text /usr/local/bin/subl**。通过软件包管理器安装通常会在 /usr/bin/ 中自动创建该符号链接。

# HISTORY

Sublime Text 由 **Jon Skinner** 创建，于 **2008 年 1 月**首次发布。命令行辅助工具 **subl** 自版本 2 起就是 Sublime Text 的一部分，支持基于终端的工作流。Sublime Text 3 发布于 **2013 年**，Sublime Text 4 随后于 **2021 年**发布，带来了 GPU 渲染和更高的性能。

# SEE ALSO

[code](/man/code)(1), [vim](/man/vim)(1), [nano](/man/nano)(1), [emacs](/man/emacs)(1), [atom](/man/atom)(1)
