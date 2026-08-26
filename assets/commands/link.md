# TAGLINE

在文件之间创建硬链接

# TLDR

**创建硬链接**

```link [target] [linkname]```

将文件链接到目录中

```link [file.txt] [dir/file.txt]```

# SYNOPSIS

**link** _file1_ _file2_

# PARAMETERS

_FILE1_
> 目标文件（源）。

_FILE2_
> 链接名（目的地）。

# DESCRIPTION

**link** 在文件之间创建硬链接。与 ln 不同，它只创建硬链接，且必须且只能接受两个参数。

该工具会创建一个指向同一 inode 的额外目录项。两个名称引用同一份文件数据。

# CAVEATS

不能创建符号链接。不能链接目录。目标必须存在。只能在同一文件系统内使用。

# HISTORY

link 是一个 **POSIX** 工具，为创建硬链接的 link() 系统调用提供了简单接口。

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

[ln](/man/ln)(1), [unlink](/man/unlink)(1), [readlink](/man/readlink)(1)
