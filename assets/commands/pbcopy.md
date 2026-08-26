# TAGLINE

将标准输入复制到 macOS 剪贴板

# TLDR

**复制文本到剪贴板**

```echo "[text]" | pbcopy```

**复制文件内容**

```pbcopy < [file.txt]```

**复制命令输出**

```ls -la | pbcopy```

**从剪贴板粘贴**

```pbpaste```

**粘贴到文件**

```pbpaste > [file.txt]```

# SYNOPSIS

**pbcopy** [_options_]

**pbpaste** [_options_]

# DESCRIPTION

**pbcopy** 将标准输入复制到 macOS 剪贴板（pasteboard）。它的搭档 **pbpaste** 将剪贴板内容输出到标准输出。

这些工具将命令行与图形化剪贴板连接起来，支持脚本化的剪贴板操作。

# PARAMETERS

**-pboard** _name_
> Pasteboard 名称（general、ruler、find、font）。

**-Prefer** _type_
> 首选数据类型（txt、rtf、ps）。

# USAGE EXAMPLES

复制输出并在其他地方粘贴：
```
cat file.txt | pbcopy
# Cmd+V in any application
```

处理剪贴板内容：
```
pbpaste | grep pattern
```

# CAVEATS

仅限 macOS。富文本可能无法按预期复制。二进制数据需谨慎处理。Pasteboard 的更改会影响系统剪贴板。

# HISTORY

**pbcopy** 和 **pbpaste** 是 **Apple** 提供的 macOS 工具。它们自早期版本起就是 macOS 的一部分，为系统 pasteboard（剪贴板）提供命令行访问。

# SEE ALSO

[xclip](/man/xclip)(1), [xsel](/man/xsel)(1), [wl-copy](/man/wl-copy)(1)
