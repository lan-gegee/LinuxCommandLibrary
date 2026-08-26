# TAGLINE

在文本编辑器中编辑文件名

# TLDR

**在编辑器中编辑文件名**

```vidir```

**编辑指定文件**

```vidir [*.txt]```

**编辑目录内容**

```vidir [path/to/directory/]```

**使用指定编辑器**

```EDITOR=[vim] vidir```

**详细模式**

```vidir -v```

# SYNOPSIS

**vidir** [_-v_] [_files_|_directory_]

# PARAMETERS

**-v**, **--verbose**
> 详细输出。

_files_
> 要编辑的文件。

_directory_
> 要编辑的目录。

# ENVIRONMENT

**EDITOR** - 所使用的编辑器
**VISUAL** - 可视化编辑器

# DESCRIPTION

**vidir** 在文本编辑器中打开一个文件名列表，每一行包含一个编号和一个文件名。修改文件名会重命名对应的文件，删除行则会移除相应文件。所有更改在你保存并退出编辑器时生效。

这种方式可以利用编辑器中熟悉的功能，例如查找替换、宏和多光标编辑，完成用单条 **mv** 命令会很繁琐的强大批量重命名操作。

# EXAMPLE

编辑器显示：
```
1	file1.txt
2	file2.txt
3	old_name.doc
```

修改为：
```
1	document1.txt
2	document2.txt
3	new_name.doc
```

# CAVEATS

属于 **moreutils** 软件包的一部分。删除一行将永久移除对应文件。不要更改每行开头的行号。使用 **-v** 可以查看执行了哪些操作。

# HISTORY

**vidir** 是 **Joey Hess** 所写 **moreutils** 的一部分。它借助熟悉的编辑器界面提供直观的文件重命名方式。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qmv](/man/qmv)(1), [rename](/man/rename)(1), [mmv](/man/mmv)(1)
