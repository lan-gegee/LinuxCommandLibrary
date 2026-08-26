# TAGLINE

joe's Own Editor，一款终端文本编辑器

# TLDR

**打开文件**

```joe [file.txt]```

**从指定行号打开**

```joe +[100] [file.txt]```

**只读模式**

```joe -rdonly [file.txt]```

**启用语法高亮**

```joe -syntax [c] [file.c]```

**禁用自动换行**

```joe -wordwrap [file.txt]```

# SYNOPSIS

**joe** [_options_] [_file_...]

# PARAMETERS

_FILE_
> 要编辑的文件。

**+**_LINE_
> 跳转到指定行号。

**-rdonly**
> 只读模式。

**-syntax** _NAME_
> 语法高亮模式。

**-wordwrap**
> 启用自动换行。

**-help**
> 显示帮助信息。

# DESCRIPTION

**joe** 即 Joe's Own Editor，是一款终端文本编辑器。它支持多种编辑模式，包括 WordStar 和 Emacs 模式。

该编辑器具备语法高亮、宏和分屏窗口等功能，按键绑定也可自行配置。

# CAVEATS

默认使用 WordStar 按键绑定。通过 joerc 进行配置。提供多种个性化变体（jmacs、jstar）。

# HISTORY

joe 由 **Joseph H. Allen** 于 1991 年开发，是一款无模式文本编辑器，采用了广为人知的 WordStar 按键绑定。

# INSTALL

```apt: sudo apt install joe```

```dnf: sudo dnf install joe```

```pacman: sudo pacman -S joe```

```apk: sudo apk add joe```

```zypper: sudo zypper install joe```

```brew: brew install joe```

```nix: nix profile install nixpkgs#joe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nano](/man/nano)(1), [vim](/man/vim)(1), [emacs](/man/emacs)(1)
