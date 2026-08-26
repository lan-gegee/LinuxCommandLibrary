# TAGLINE

删除未更改的 RCS 工作文件

# TLDR

**删除未更改的工作文件**

```rcsclean```

**删除目录内未更改的工作文件**

```rcsclean [path/to/directory]```

**删除未更改的工作文件**并解锁

```rcsclean -u```

**预览哪些文件会被删除**（演练运行）

```rcsclean -n```

**删除特定的未更改文件**

```rcsclean [filename]```

# SYNOPSIS

**rcsclean** [_options_] [_file_...]

# PARAMETERS

**-n**
> 演练运行；显示将要进行的操作但不实际执行

**-q**
> 安静模式；抑制诊断输出

**-u** [_rev_]
> 若修订由调用者锁定则将其解锁

**-r** _rev_
> 与指定的修订比较，而不是默认修订

**-T**
> 保留 RCS 文件的修改时间

**-V**
> 打印版本号

# DESCRIPTION

**rcsclean** 删除自检出以来未被修改的工作文件。它会将每个工作文件与对应的 RCS 修订进行比较并删除未更改的文件，从而清理工作目录。

这个实用工具适合清理那些只为阅读而检出却从未修改过的文件，减少工作目录中的杂物。配合 **-u** 时，如果工作文件未发生变化，它还会解锁调用者拥有的任何已锁定修订。

默认情况下，rcsclean 处理当前目录中所有受 RCS 管理的文件。指定文件名则只处理特定文件。

# CAVEATS

只删除与其检出版本完全一致的文件。任何修改，包括空白字符的变化，都会阻止删除。

**-u** 选项只会解锁当前用户锁定的修订。它无法解锁其他用户锁定的文件。

请先用 **-n**（演练运行）预览哪些文件将被删除，在整目录上运行时尤其如此。

# INSTALL

```apt: sudo apt install rcs```

```dnf: sudo dnf install rcs```

```pacman: sudo pacman -S rcs```

```apk: sudo apk add rcs```

```zypper: sudo zypper install rcs```

```brew: brew install rcs```

```nix: nix profile install nixpkgs#rcs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rcs](/man/rcs)(1), [ci](/man/ci)(1), [co](/man/co)(1), [rcsdiff](/man/rcsdiff)(1)
