# TAGLINE

删除空目录

# TLDR

**删除一个空目录**

```rmdir [path/to/directory]```

**删除多个空目录**

```rmdir [dir1] [dir2] [dir3]```

**删除目录及其空的父目录**

```rmdir -p [path/to/directory]```

**以详细输出方式删除**

```rmdir -v [path/to/directory]```

对非空目录**忽略错误**

```rmdir --ignore-fail-on-non-empty [path/to/directory]```

**删除嵌套的空目录**

```rmdir -p [parent/child/grandchild]```

# SYNOPSIS

**rmdir** [_OPTION_]... _DIRECTORY_...

# PARAMETERS

**-p**, **--parents**
> 删除目录及其空的祖先目录。

**-v**, **--verbose**
> 为每个被删除的目录打印一条消息。

**--ignore-fail-on-non-empty**
> 忽略仅由目录非空导致的失败。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**rmdir** 用于删除空目录。与 **rm -r** 不同，它不会删除包含文件或子目录的目录，从而提供了一道防止意外数据丢失的安全检查。

使用 **-p** 选项时，rmdir 会先删除指定目录，然后尝试删除路径中的每个父目录，直到遇到非空目录或删除失败为止。

在脚本中，当你想清理空目录又不想冒删除有内容目录的风险时，rmdir 非常有用。

# CAVEATS

rmdir 只能删除空目录。对于有内容的目录，请使用 **rm -r**（需谨慎）。目录必须不含任何文件和子目录，包括隐藏文件（以 . 开头的文件）。-p 选项只有在父目录因子目录被删而变空之后才会将其删除。

# HISTORY

rmdir 是 GNU coreutils 的一部分，自 Unix 最早版本起就是标准 Unix 命令。它遵循 POSIX 规范的目录删除要求。rmdir（仅限空目录）与 rm -r（递归删除）之间的区分是 Unix 设计中有意的安全特性。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rm](/man/rm)(1), [mkdir](/man/mkdir)(1), [find](/man/find)(1)
