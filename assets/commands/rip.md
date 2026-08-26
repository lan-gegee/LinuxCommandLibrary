# TAGLINE

rm 的安全且符合人体工程学的替代品

# TLDR

**安全删除文件**

```rip [file.txt]```

**删除多个文件和目录**

```rip [file1.txt] [file2.txt] [directory/]```

**删除前查看文件信息**（显示大小和前几行内容）

```rip -i [file.txt]```

**列出从当前目录删除的文件**

```rip --seance```

**恢复最近删除的文件**

```rip --unbury```

**从墓地中恢复指定文件**

```rip --unbury [filename]```

**恢复 seance 列出的所有文件**（组合 -s 和 -u）

```rip -su```

**永久删除墓地中的所有文件**

```rip --decompose```

**使用自定义的墓地目录**

```rip --graveyard [path/to/graveyard] [file.txt]```

# SYNOPSIS

**rip** [_FLAGS_] [_OPTIONS_] [_TARGET..._]

# PARAMETERS

**-d**, **--decompose**
> 永久删除（unlink）整个墓地。

**-i**, **--inspect**
> 在提示操作之前打印 TARGET 的信息。

**-s**, **--seance**
> 打印曾从当前目录下删除的文件。

**-u**, **--unbury** _target_
> 撤销当前用户上一次的删除，或指定墓地中的文件。

**--graveyard** _graveyard_
> 设置已删除文件的去处目录。

**-h**, **--help**
> 打印帮助信息。

**-V**, **--version**
> 打印版本信息。

# DESCRIPTION

**rip**（Rm ImProved）是 rm 的更安全替代品，它将被删除的文件移动到"墓地"（graveyard）目录，而不是永久移除。墓地里保留了原始文件系统路径结构，因此需要时可以轻松将文件恢复到原来的确切位置。

**--seance** 标志列出曾从当前目录下删除的文件。**--unbury** 标志用于恢复文件，可以是最近删除的项目，也可以是指定名称的文件。组合使用 **-s** 和 **-u** 可恢复 seance 列出的所有内容。当不再需要墓地中的内容时，可用 **--decompose** 永久移除以回收磁盘空间。

墓地位置默认为 /tmp/graveyard-$USER，可通过 **--graveyard** 标志自定义。不会有数据被覆盖；如果相同路径的文件被多次删除，它们会被重命名为带编号的备份。**--inspect** 选项在提示删除前显示文件的大小和前几行内容，或目录的总大小和前几个条目。

# CAVEATS

墓地会占用磁盘空间。大量删除可能填满 /tmp 存储。这不是安全删除工具；墓地中的文件任何有访问权限的人都可以读取。

# INSTALL

```aur: yay -S rip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rm](/man/rm)(1), [trash-cli](/man/trash-cli)(1), [safe-rm](/man/safe-rm)(1)
