# TAGLINE

可扩展的模态文本编辑器

# TLDR

**打开文件**进行编辑

```ad [path/to/file]```

**打开多个文件**

```ad [file1] [file2]```

对文件**执行编辑脚本**

```ad -e "[script]" [path/to/file]```

从文件**运行编辑脚本**

```ad -f [path/to/script] [path/to/file]```

**列出打开的编辑器会话**

```ad --list-sessions```

# SYNOPSIS

**ad** [_options_] [_files..._]

# PARAMETERS

**-e**, **--expression** _script_
> 内联执行编辑脚本

**-f**, **--script-file** _file_
> 从文件加载并执行编辑脚本

**-c**, **--config** _path_
> 使用自定义配置文件

**--default-config**
> 忽略用户配置并使用默认设置

**-l**, **--list-sessions**
> 显示打开的编辑器会话

**--rm-sockets**
> 清理无响应的套接字文件

**-h**, **--help**
> 显示用法信息

**-v**, **--version**
> 显示版本详情

# DESCRIPTION

**ad** 是一个用 Rust 编写的模态文本编辑器，它将 vim 风格的模态编辑与 Plan 9 Acme 编辑器的可扩展性理念相结合。其特性包括 vim/kakoune 风格的文本导航与选择、借鉴 emacs 的迷你缓冲区次模式、sam/acme 风格的编辑命令，以及通过内置 9P 文件服务器接入外部客户端程序实现扩展。

该编辑器支持基于 tree-sitter 的语法高亮、LSP 补全、鼠标导航与界面缩放、多栏与多缓冲区、临时缓冲区以及可自定义的按键绑定。通过 TOML 文件进行配置。

# CAVEATS

仍处于积极开发阶段，版本之间可能存在破坏性变更。除内置的 **:help** 命令外文档有限。需要熟悉模态编辑概念。

# HISTORY

**ad** 由 **Innes Anderson-Morrison**（sminez）创建，是一款融合 vim、kakoune、emacs 和 Plan 9 acme 理念的实验性编辑器。用 Rust 编写并以 MIT 许可证发布，于 2025 年 12 月达到 0.4.0 版本。

# INSTALL

```aur: yay -S ad```

```brew: brew install ad```

```nix: nix profile install nixpkgs#ad```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[vim](/man/vim)(1), [kakoune](/man/kakoune)(1), [emacs](/man/emacs)(1)
