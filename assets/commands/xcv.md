# TAGLINE

终端中的文件剪切、复制和粘贴工具

# TLDR

**剪切文件**

```xcv x [file1] [file2]```

**复制文件**

```xcv c [file1] [file2]```

**粘贴文件**

```xcv v```

**列出剪贴板**

```xcv l```

**粘贴到目录**

```xcv v [directory/]```

# SYNOPSIS

**xcv** _x_|_c_|_v_|_l_ [_options_] [_files_]

# PARAMETERS

**x**
> 剪切文件（使用 mv）。

**c**
> 复制文件（使用 cp）。

**v**
> 将文件粘贴到当前目录。

**l**
> 列出剪贴板中的文件。

# DESCRIPTION

**xcv** 在终端中为文件提供类似剪贴板的剪切、复制和粘贴操作。文件被暂存在 ~/.xcv 目录中，作为操作之间的持久化剪贴板。x 命令将文件剪切（移动）到暂存区，c 复制文件，v 将其粘贴到当前或指定目录，l 列出当前剪贴板的内容。

该工具包装了标准的 cp 和 mv 命令，为移动文件提供简单直观的工作流，无需输入完整的源路径和目标路径。

# CAVEATS

文件存储在 ~/.xcv 中。需要 Bash。通过 npm 安装。

# HISTORY

**xcv** 的创建初衷是作为一个简单的 bash 工具，在终端中提供文件的剪切、复制和粘贴功能。

# INSTALL

```brew: brew install xcv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cp](/man/cp)(1), [mv](/man/mv)(1), [xclip](/man/xclip)(1)
