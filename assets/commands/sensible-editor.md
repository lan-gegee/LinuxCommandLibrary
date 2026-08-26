# TAGLINE

打开用户偏好的文本编辑器

# TLDR

在默认编辑器中打开**文件**

```sensible-editor path/to/file```

打开文件并将光标定位到**文件末尾**

```sensible-editor + path/to/file```

打开文件并将光标定位到**第 10 行**

```sensible-editor +10 path/to/file```

以分屏窗口打开**多个文件**

```sensible-editor -O3 path/to/file1 path/to/file2 path/to/file3```

# SYNOPSIS

**sensible-editor** [_options_] [_file_...]

# PARAMETERS

**+**
> 将光标定位到文件末尾

**+**_N_
> 将光标定位到第 N 行

**-O**_N_
> 以垂直分屏方式打开 N 个文件

# DESCRIPTION

**sensible-editor** 在用户偏好的文本编辑器中打开文件。它通过检查环境变量（VISUAL、EDITOR）和系统默认设置来确定要启动的编辑器。

选项会透传给底层编辑器（通常是 vim、nano 或 emacs）。

# CAVEATS

行为取决于环境配置以及哪个编辑器是默认值。某些选项可能并非对所有编辑器都有效。

# HISTORY

属于 **sensible-utils** 软件包的一部分，提供符合 Debian 政策的默认应用启动器。

# SEE ALSO

[editor](/man/editor)(1), [update-alternatives](/man/update-alternatives)(8)
