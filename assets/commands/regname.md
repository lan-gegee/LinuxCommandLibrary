# TAGLINE

基于正则表达式的文件重命名工具

# TLDR

**用正则模式重命名文件**

```regname [pattern] [replacement] [files]```

# SYNOPSIS

**regname** [_options_] _pattern_ _replacement_ [_files_...]

# DESCRIPTION

**regname** 是一款灵活的基于正则表达式的文件重命名工具，同时支持图形界面和命令行界面。它使用带捕获组替换的正则模式，实现强大的批量文件重命名操作。

# HISTORY

**regname** 由 **mobzystems** 创建，使用 **C#** 编写。

# INSTALL

```nix: nix profile install nixpkgs#regname```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rename](/man/rename)(1), [mmv](/man/mmv)(1), [nomino](/man/nomino)(1)
