# TAGLINE

以只读 Vim 模式打开文件

# TLDR

**以只读模式打开文件**

```view [file]```

**以只读模式打开多个文件**

```view [file1] [file2]```

**在指定行号打开**

```view +[line_number] [file]```

**打开并跳转到模式匹配处**

```view +/[pattern] [file]```

# SYNOPSIS

**view** [_options_] [_file ..._]

# PARAMETERS

所有 vim 选项均可用。常用的包括：

**+**_num_
> 在指定行号打开文件。

**+/**_pattern_
> 在模式首次出现处打开文件。

**-c** _command_
> 加载文件后执行命令。

**-n**
> 不使用交换文件（适合敏感文件）。

**-o**
> 以水平分割方式打开文件。

**-O**
> 以垂直分割方式打开文件。

**-p**
> 以标签页方式打开文件。

# DESCRIPTION

**view** 是 Vim 的只读模式。它等同于运行 **vim -R**，打开文件时设置 readonly 选项，防止意外修改。

你仍然可以导航、搜索以及使用 vim 的所有查看功能。尝试保存时会出现警告，但如果有权限，可以用 **:w!** 强制写入。

所有标准 vim 命令均可用于导航：**h/j/k/l** 移动、**/** 搜索、**G** 跳到末尾、**gg** 跳到开头、**:q** 退出。

# CAVEATS

虽然 view 能防止意外保存，但并不能完全禁止编辑缓冲区。如需更严格的只读模式，请使用 **vim -M**，它会禁用一切修改。与 less 或 cat 不同，view 会加载整个文件并默认使用交换文件。

# HISTORY

view 自早期起就是 **vi** 和 **vim** 的一部分。最初的 vi 由 **Bill Joy** 于 **1976 年**在加州大学伯克利分校编写。由 **Bram Moolenaar** 开发的 vim（Vi IMproved）于 **1991 年**首次发布，并将 view 作为调用只读模式的标准方式。这种命名遵循 Unix 惯例：同一二进制程序通过不同名称调用时触发不同行为。

# INSTALL

```pacman: sudo pacman -S gvim```

```apk: sudo apk add gvim```

```zypper: sudo zypper install gvim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [less](/man/less)(1), [cat](/man/cat)(1), [more](/man/more)(1)
