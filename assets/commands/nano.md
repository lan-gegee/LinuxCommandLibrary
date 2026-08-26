# TAGLINE

简易文本编辑器

# TLDR

**打开文件**

```nano [file.txt]```

**在指定行打开**

```nano +[10] [file.txt]```

**以只读方式打开**

```nano -v [file.txt]```

**启用行号**

```nano -l [file.txt]```

**禁用长行折行**

```nano -w [file.txt]```

**开启备份打开**

```nano -B [file.txt]```

**设置制表符宽度**

```nano -T [4] [file.txt]```

# SYNOPSIS

**nano** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要编辑的文件。

**+** _LINE_
> 从指定行号开始。

**-v**
> 查看模式（只读）。

**-l**
> 显示行号。

**-w**
> 不对长行折行。

**-B**
> 创建备份文件。

**-T** _NUM_
> 制表符宽度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nano** 是一个简单的文本编辑器。它提供易于使用的终端编辑环境。

该工具在底部显示快捷键。是对新手友好的 vi/vim 替代品。

# CAVEATS

不如 vim/emacs 强大。基于 Ctrl 的快捷键。配置位于 ~/.nanorc。

# HISTORY

nano 作为 Pico 编辑器的**自由软件替代品**而创建，自 2001 年起成为 GNU 项目的一部分。

# INSTALL

```apt: sudo apt install nano```

```dnf: sudo dnf install nano```

```pacman: sudo pacman -S nano```

```apk: sudo apk add nano```

```zypper: sudo zypper install nano```

```brew: brew install nano```

```nix: nix profile install nixpkgs#nano```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [emacs](/man/emacs)(1), [pico](/man/pico)(1)
