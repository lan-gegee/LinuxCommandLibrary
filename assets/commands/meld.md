# TAGLINE

可视化 diff 与合并工具

# TLDR

**比较两个文件**

```meld [file1] [file2]```

**比较三个文件**

```meld [file1] [file2] [file3]```

**比较目录**

```meld [dir1] [dir2]```

**与版本控制进行比较**

```meld [file.txt]```

**开始新的比较**

```meld --newtab [file1] [file2]```

**输出 diff**

```meld --output=[merged.txt] [file1] [file2]```

# SYNOPSIS

**meld** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要比较的文件或目录。

**--newtab**
> 在新标签页中打开。

**--output** _FILE_
> 写入合并结果。

**--diff** _FILES_
> 以 diff 模式启动。

**--help**
> 显示帮助信息。

# DESCRIPTION

**meld** 是一个可视化 diff 与合并工具，用于高亮显示文件或目录之间的差异。

该工具提供三方比较与合并功能，并可与版本控制系统集成。

# CAVEATS

GUI 应用程序。基于 GTK。处理大文件时可能较慢。

# HISTORY

Meld 是为 GNOME 创建的可视化 **diff 与合并**工具，支持文件和目录比较。

# INSTALL

```dnf: sudo dnf install meld```

```pacman: sudo pacman -S meld```

```apk: sudo apk add meld```

```zypper: sudo zypper install meld```

```nix: nix profile install nixpkgs#meld```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [kdiff3](/man/kdiff3)(1), [vimdiff](/man/vimdiff)(1)
