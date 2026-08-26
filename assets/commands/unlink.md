# TAGLINE

通过 unlink(2) 系统调用移除单个文件

# TLDR

**移除普通文件**

```unlink [file]```

**移除符号链接（只删除链接本身，不删除目标）**

```unlink [symlink]```

**显示版本信息**

```unlink --version```

# SYNOPSIS

**unlink** _FILE_

**unlink** _OPTION_

# PARAMETERS

_FILE_
> 恰好一个要取消链接的文件路径。

**--help**
> 显示简短帮助信息并退出。

**--version**
> 输出版本信息并退出。

# DESCRIPTION

**unlink** 调用 **unlink(2)** 系统调用来移除单个文件的目录项。它恰好接受一个操作数，没有递归、交互提示或强制行为等选项。

当文件的最后一个链接被移除且没有进程仍打开它时，底层的 inode 和数据块会被释放。对于有多个硬链接的文件，只有指定的链接被移除；数据仍可通过其余链接访问。移除符号链接只会删除链接本身，不会删除目标。

与 **rm** 不同，**unlink** 不能作用于目录、不能接受多个操作数，也不会对 shell 通配符做特殊展开。这种极简设计使它对脚本而言可预测——只需移除恰好一个路径，不会有意外匹配到其他文件的风险。

# CAVEATS

只接受单个操作数；传入两个或更多参数是错误。不能移除目录——请使用 **rmdir(1)** 或 **rm -r**。许多 shell 附带来自 GNU coreutils 的 **unlink** 工具；shell 内建形式（如 ksh 中的）行为可能略有不同。

# HISTORY

**unlink** 是一个历史悠久的 Unix 工具，用于暴露 **unlink(2)** 系统调用。GNU coreutils 的实现遵循 **POSIX.1-2001** 标准。

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

[rm](/man/rm)(1), [rmdir](/man/rmdir)(1), [ln](/man/ln)(1)
