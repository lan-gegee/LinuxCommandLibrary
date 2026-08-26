# TAGLINE

受 Vim 启发的模态文本编辑器

# TLDR

**打开文件**

```kak [file.txt]```

**打开多个文件**

```kak [file1] [file2]```

**定位到某行打开**

```kak +[50] [file.txt]```

**执行命令**

```kak -e "[command]" [file.txt]```

**客户端-服务器模式**

```kak -c [session-name]```

**作为服务器启动**

```kak -d -s [session-name]```

# SYNOPSIS

**kak** [_options_] [_file_...]

# PARAMETERS

_FILE_
> 要编辑的文件。

**+**_LINE_
> 跳转到指定行号。

**-e** _CMD_
> 启动后执行命令。

**-c** _SESSION_
> 连接到会话。

**-d**
> 守护进程模式。

**-s** _NAME_
> 会话名称。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Kakoune** 是一个受 Vim 启发的模态文本编辑器。它采用"选择优先"的编辑方式，支持多重光标。

该编辑器提供即时可视化反馈。它将选择与操作分离，使编辑更直观。

# CAVEATS

与 Vim 范式不同。有学习曲线。采用客户端-服务器架构。

# HISTORY

Kakoune 由 **Maxime Coste** 创建，是一个受 Vim 启发的编辑器，专注于交互性和正交性。

# INSTALL

```apt: sudo apt install kakoune```

```dnf: sudo dnf install kakoune```

```pacman: sudo pacman -S kakoune```

```apk: sudo apk add kakoune```

```zypper: sudo zypper install kakoune```

```brew: brew install kakoune```

```nix: nix profile install nixpkgs#kakoune```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [nvim](/man/nvim)(1), [helix](/man/helix)(1)
