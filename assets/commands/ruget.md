# TAGLINE

用 Rust 编写的替代文件下载器

# TLDR

**下载** URL 内容到文件

```ruget https://example.com/file```

下载到**指定的输出**文件

```ruget -o file_name https://example.com/file```

# SYNOPSIS

**ruget** [_options_] _URL_

# PARAMETERS

**-o**, **--output** _file_
> 指定输出文件名

# DESCRIPTION

**ruget** 是一个用 Rust 编写的下载工具，可作为 wget 的替代品。它通过简单的命令行界面从 URL 下载文件。

该工具专注于简洁性和现代化的 Rust 实现。

# CAVEATS

功能可能少于 wget 或 curl。请查阅项目文档了解支持的协议和选项。

# HISTORY

作为 wget 等传统下载工具的 Rust 替代品而开发。

# INSTALL

```aur: yay -S ruget```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wget](/man/wget)(1), [curl](/man/curl)(1), [aria2c](/man/aria2c)(1)
