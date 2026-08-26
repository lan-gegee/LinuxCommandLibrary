# TAGLINE

以多重选择为核心概念的模态文本编辑器

# TLDR

**打开文件**

```kak [path/to/file]```

**打开多个文件**

```kak [file1] [file2]```

**在指定行打开**

```kak +[line] [path/to/file]```

**在命名会话中启动**

```kak -s [session_name] [path/to/file]```

**连接到已有会话**

```kak -c [session_name]```

**以过滤模式运行**（对 stdin 应用命令）

```echo "[text]" | kak -f '[commands]'```

# SYNOPSIS

**kak** [**-s** _session_] [**-c** _session_] [**-f** _commands_] [**+**_line_] [_file_...]

# PARAMETERS

**-s** _SESSION_
> 启动一个命名会话

**-c** _SESSION_
> 连接到已有会话

**-f** _COMMANDS_
> 对 stdin 运行命令（过滤模式）

**-e** _COMMANDS_
> 启动后执行命令

**-n**
> 不加载 kakrc 配置

**-l**
> 列出已有的会话

**-d**
> 以守护进程方式运行（无 UI）

# DESCRIPTION

**Kakoune**（调用名为 **kak**）是一个受 Vim 启发的模态文本编辑器，但它的设计围绕**多重选择**这一核心编辑原语。Kakoune 的大多数操作不是在单个光标上进行，而是同时在多个选择上执行，从而能用更少的按键完成强大的文本操作。

Kakoune 遵循**选择 → 操作**模型（与 Vim 的操作 → 移动相反），即先选中文本（用正则表达式、文本对象或其他方法），看到所选内容，然后再施加操作。该编辑器支持用于协作编辑的客户端-服务器架构、内置语法高亮，并可通过其脚本语言进行深度扩展。

# CAVEATS

选择优先的范式不同于 Vim 的肌肉记忆，需要适应。插件生态比 Vim 小。配置使用其自有的脚本语言而非主流语言。

# HISTORY

**Kakoune** 由 **Maxime Coste**（mawww）创建，用 **C++** 编写。开发始于 **2011** 年前后，最初是一项改进 Vim 编辑模型的实验。多重选择的思路启发了后来的编辑器，包括 **Helix**。

# INSTALL

```dnf: sudo dnf install kakoune```

```pacman: sudo pacman -S kakoune```

```zypper: sudo zypper install kakoune```

```brew: brew install kakoune```

```nix: nix profile install nixpkgs#kakoune```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [helix](/man/helix)(1), [neovim](/man/neovim)(1)
