# TAGLINE

无模式文本编辑器

# TLDR

**编辑文件**

```moe [file.txt]```

**打开多个文件**

```moe [file1.txt] [file2.txt]```

**只读模式**

```moe -r [file.txt]```

**设置制表符宽度**

```moe -t [4] [file.txt]```

# SYNOPSIS

**moe** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要编辑的文件。

**-r**
> 只读模式。

**-t** _WIDTH_
> 制表符宽度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**moe** 是一个无模式文本编辑器。它为 vi/emacs 提供了一个更简单的替代选择。

该工具使用常见的按键绑定，无需切换模式。

# CAVEATS

功能不如 vim/emacs 强大。学习曲线更平缓。ncurses 界面。

# HISTORY

moe 的诞生是为偏好不做模式切换的用户提供一个简单的**无模式**文本编辑器。

# INSTALL

```dnf: sudo dnf install moe```

```zypper: sudo zypper install moe```

```brew: brew install moe```

```nix: nix profile install nixpkgs#moe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nano](/man/nano)(1), [micro](/man/micro)(1), [joe](/man/joe)(1)
