# TAGLINE

受 Sublime Text 启发的开源文本编辑器

# TLDR

**启动 Lime 文本编辑器**

```lime```

**打开文件**

```lime [file.txt]```

**打开多个文件**

```lime [file1.txt] [file2.txt]```

**在指定行打开文件**

```lime [file.txt]:[line_number]```

# SYNOPSIS

**lime** [_options_] [_files_...]

# PARAMETERS

**-h**, **--help**
> 显示帮助消息。

**-v**, **--version**
> 显示版本。

**--debug**
> 启用调试模式。

# DESCRIPTION

**lime**（Lime Text）是一个受 Sublime Text 启发的开源文本编辑器。它旨在以开源代码库提供一个与 Sublime Text 兼容的编辑器。

Lime 支持多重光标、分屏编辑、命令面板，并可通过 Python 插件扩展。后端使用 Go 编写。

# KEY FEATURES

```
- Sublime Text compatibility
- Multiple cursors
- Split editing
- Command palette
- Python plugin system
- Cross-platform
```

# CAVEATS

开发已明显放缓。相比 Sublime Text 功能尚不完整。各前端实现的成熟度不一。

# HISTORY

Lime 由 **Fredrik Ehnbom** 于 **2013 年**发起，试图用 Go 后端创建一个开源的 Sublime Text 克隆。

# INSTALL

```aur: yay -S lime```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [nano](/man/nano)(1), [code](/man/code)(1)
