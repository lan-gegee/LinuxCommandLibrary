# TAGLINE

在只读的 nano 编辑器中查看文件

# TLDR

**以只读方式查看文件**

```rnano [file]```

**显示行号查看**

```rnano -l [file]```

**定位到指定行查看**

```rnano +[42] [file]```

**平滑滚动查看**

```rnano -S [file]```

# SYNOPSIS

**rnano** [_-l_] [_+line_] [_options_] _file_

# PARAMETERS

**-l**
> 显示行号。

**-S**
> 平滑滚动。

**+**_LINE_
> 从指定行开始。

**-v**
> 查看模式（默认）。

**-h**
> 显示帮助。

# DESCRIPTION

**rnano** 是 nano 文本编辑器的只读模式，通常实现为一个符号链接，调用 nano 时附带 **-v**（view）标志。它提供熟悉的 nano 界面来查看文件，同时防止任何意外修改，适合用来检查配置文件和日志。

nano 的所有导航功能都保持可用，包括滚动、用 **+LINE** 跳转到指定行、语法高亮、用 **-l** 显示行号，以及用 **-S** 实现平滑滚动。编辑器只是拒绝任何修改命令，因此用户可以安全浏览而不必担心无意间的改动。

这类似于 **vi** 与 **view** 的关系：为熟悉的编辑器提供一个只读变体。

# CAVEATS

只是指向 nano -v 的链接。与 less/more 相比功能有限。没有搜索历史。

# HISTORY

**rnano** 通常是指向 **nano** 的符号链接，以只读（view）模式调用它，类似于 view 之于 vim 的关系。

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

[nano](/man/nano)(1), [less](/man/less)(1), [view](/man/view)(1), [cat](/man/cat)(1)
