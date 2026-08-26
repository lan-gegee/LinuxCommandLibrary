# TAGLINE

获取字符串、URL 和文件的字节大小

# TLDR

获取字符串的字节大小

```sizeof "[hello world]"```

获取网页的大小

```sizeof "[https://example.com]"```

获取本地文件的大小

```sizeof [/path/to/file.html]```

# SYNOPSIS

**sizeof** _input_

# DESCRIPTION

**sizeof** 是一个命令行工具，以字节和人类可读的单位告诉你字符串、URL 和文件的大小。传入任意字符串、URL 或文件路径，它就会返回大小的明细。

# HISTORY

**sizeof** 由 **Zachary Proser**（zackproser）创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S sizeof```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wc](/man/wc)(1), [du](/man/du)(1), [stat](/man/stat)(1)
