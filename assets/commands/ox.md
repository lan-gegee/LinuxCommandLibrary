# TAGLINE

简单而灵活的终端文本编辑器

# TLDR

**打开文件**

```ox [path/to/file]```

**打开多个文件**

```ox [file1] [file2]```

# SYNOPSIS

**ox** [_files_...]

# KEY BINDINGS

**Ctrl+Q**：退出当前标签页或编辑器。**Ctrl+S**：保存文件。**Alt+S**：另存为。**Ctrl+N**：新建标签页。**Ctrl+O**：打开文件。**Ctrl+F**：搜索。**Ctrl+A**：查找并全部替换。**Ctrl+Z**：撤销。**Ctrl+Y**：重做。**Ctrl+Left/Right**：切换标签页。**Alt+A**：聚焦命令行。

# DESCRIPTION

**ox** 是一款使用 Rust 编写、在终端中运行的文本编辑器。与模态编辑器不同，你可以直接开始输入。它完全从零构建，不基于任何现有编辑器。

功能包括插件系统、内置终端、用于项目管理的文件树、语法高亮，以及辅助编程的工具。它支持 Linux、macOS 和 Windows。配置通过基于 Lua 的配置文件完成。

# CAVEATS

不像 vim 那样采用模态设计——使用传统的编辑按键绑定。插件生态仍在发展壮大中。需要支持 Unicode 的终端。

# HISTORY

**ox** 由 **curlpipe** 创建，使用 **Rust** 编写。可通过 `cargo install --git https://github.com/curlpipe/ox` 安装。

# INSTALL

```brew: brew install ox```

```nix: nix profile install nixpkgs#ox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nano](/man/nano)(1), [micro](/man/micro)(1), [vim](/man/vim)(1)
