# TAGLINE

交互式选择并复制终端输出

# TLDR

**选择并复制**

```echo "[text]" | yank```

**自定义分隔符**

```echo "[text]" | yank -d "[\n]"```

**复制到 X 剪贴板**

```echo "[text]" | yank -x```

**指定选择命令**

```echo "[text]" | yank -- xclip```

# SYNOPSIS

**yank** [_-d delim_] [_-x_] [_options_] [_-- command_]

# PARAMETERS

**-d** _DELIM_
> 字段分隔符。

**-x**
> X 剪贴板。

**-l**
> 行分隔符。

**--** _CMD_
> 提取命令。

# DESCRIPTION

**yank** 从管道或文件读取输入，并在终端中呈现一个选择界面。用户可以用方向键浏览各行或各字段，选中所需的文本，然后 yank 会将其复制到剪贴板或传递给指定的命令。

默认情况下输入按行分割。**-d** 选项可设置自定义分隔符，将输入分割成可选择字段，适合从结构化输出中提取特定列。**-l** 选项则强制按行分割，无论内容如何。

剪贴板集成通过外部命令实现，例如 **xclip** 或 **xsel**，在 **--** 之后指定。在有 X11 的系统上，**-x** 标志提供了访问 X 剪贴板的快捷方式。该工具旨在自然地融入 Unix 管道，可以接受任何向标准输出写入内容的命令的输入。

# CAVEATS

需要终端环境。剪贴板的配置因系统而异。这是一个简单的工具。

# HISTORY

**yank** 是为交互式地选择终端输出并复制到剪贴板而创建的。

# INSTALL

```apt: sudo apt install emboss```

```dnf: sudo dnf install yank```

```pacman: sudo pacman -S yank```

```apk: sudo apk add yank```

```zypper: sudo zypper install yank```

```brew: brew install yank```

```nix: nix profile install nixpkgs#emboss```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xclip](/man/xclip)(1), [xsel](/man/xsel)(1), [fzf](/man/fzf)(1)
