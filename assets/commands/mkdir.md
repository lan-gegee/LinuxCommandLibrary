# TAGLINE

以指定名称创建目录

# TLDR

**创建目录**

```mkdir [directory]```

**创建多个目录**

```mkdir [dir1] [dir2] [dir3]```

**按需创建父目录**（已存在时不报错）

```mkdir -p [path/to/nested/directory]```

**以指定权限创建目录**

```mkdir -m [755] [directory]```

**创建目录并为每个显示消息**

```mkdir -v [dir1] [dir2]```

# SYNOPSIS

**mkdir** [_-pv_] [_-m mode_] _directory ..._

# PARAMETERS

**-p**, **--parents**
> 按需创建父目录；已存在时不报错

**-m** _mode_, **--mode**=_mode_
> 为新目录设置文件模式（权限）

**-v**, **--verbose**
> 为每个创建的目录打印一条消息

**-Z**, **--context**
> 设置每个新建目录的 SELinux 安全上下文

**--help**
> 显示帮助信息并退出

**--version**
> 输出版本信息并退出

# DESCRIPTION

**mkdir** 以指定的名称创建目录。默认情况下，它在当前工作目录或指定路径下创建目录。

**-p** 选项对于在单条命令中创建嵌套目录结构特别有用，它会创建所有必要的父目录，并且在目标目录已存在时不报告错误。这使它非常适合目标目录可能存在也可能不存在的脚本场景。

新目录的权限受当前 **umask** 影响，除非用 **-m** 显式设置。默认权限通常为 777 减去 umask 值。

# CAVEATS

创建目录需要对父目录有写权限。在文件名支持有限的文件系统上（如 FAT），目录名中的某些字符可能导致问题。**-p** 标志在目录已存在时会静默成功，这可能掩盖脚本中期望创建新目录时的错误。

# HISTORY

**mkdir** 命令自 **1971 年的第一版 Unix** 起就存在，是最早的 Unix 命令之一。它由贝尔实验室的 **Ken Thompson** 创建。几十年来该命令一直非常稳定，后续版本加入了 **-p** 选项来简化目录树的创建。它由 POSIX 标准定义，在所有类 Unix 操作系统上均可用。

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

[rmdir](/man/rmdir)(1), [rm](/man/rm)(1), [ls](/man/ls)(1), [chmod](/man/chmod)(1), [install](/man/install)(1)
