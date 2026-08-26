# TAGLINE

小巧可配置的终端文本编辑器

# TLDR

**打开**文件进行编辑

```dte [filename]```

**打开**多个文件

```dte [file1] [file2]```

**打开**文件并定位到指定行

```dte +[line_number] [filename]```

**以只读模式打开**文件

```dte -R [filename]```

# SYNOPSIS

**dte** [_options_] [_files_]

# PARAMETERS

**+**_N_
> 从第 N 行开始

**-R, --read-only**
> 以只读模式打开

**-c, --config** _FILE_
> 使用指定的配置文件

**-h, --help**
> 显示帮助并退出

**-V, --version**
> 显示版本并退出

# DESCRIPTION

**dte** 是一个小巧、快速且可配置的终端文本编辑器，设计目标是轻量而强大。它支持多种语言的语法高亮、多缓冲区、窗口分割，以及一个类似于 vi/vim 但键位不同的简洁命令接口。

该编辑器用 C 语言编写，依赖极少，适合资源受限的环境。它支持宏、正则表达式搜索，并可通过配置文件自定义键位绑定。

# KEYBINDINGS

**Ctrl+S**
> 保存文件

**Ctrl+Q**
> 退出

**Ctrl+F**
> 搜索

**Ctrl+G**
> 跳转到指定行

**Ctrl+W**
> 关闭缓冲区

**Ctrl+N**
> 新建文件

**Ctrl+O**
> 打开文件

**Ctrl+Z**
> 挂起编辑器

**Tab**
> 缩进/自动补全

**Shift+Tab**
> 取消缩进

# CONFIGURATION

配置文件位置：
- ~/.dterc
- ~/.config/dte/dterc

配置示例：

```
set auto-indent true
set tab-width 4
set show-line-numbers true
```

# CAVEATS

与 vi/vim 不同的键位绑定可能需要一段适应期。部分高级功能需要使用特定选项编译。终端兼容性因环境而异。没有像 Vimscript 或 Emacs Lisp 那样的内置脚本语言。

# HISTORY

**dte** 由 Craig Barnes 创建，作为大型编辑器的轻量替代品。它旨在占用极小空间的同时提供核心编辑功能，并且易于配置和扩展。

# INSTALL

```apt: sudo apt install dte```

```nix: nix profile install nixpkgs#dte```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [nano](/man/nano)(1), [micro](/man/micro)(1), [kakoune](/man/kakoune)(1)
