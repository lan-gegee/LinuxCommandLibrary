# TAGLINE

在 macOS 上打开文件和 URL

# TLDR

**用默认应用打开文件**

```open [file]```

**在浏览器中打开 URL**

```open [https://example.com]```

**用指定应用打开**

```open -a [Safari] [file.html]```

**在 Finder 中打开目录**

```open [directory]```

**打开当前目录**

```open .```

**在 Finder 中显示**

```open -R [file]```

# SYNOPSIS

**open** [_options_] [_file_...]

# PARAMETERS

_FILE_
> 要打开的文件或 URL。

**-a** _APP_
> 用指定应用程序打开。

**-e**
> 在 TextEdit 中打开。

**-t**
> 在默认文本编辑器中打开。

**-R**
> 在 Finder 中显示。

**-n**
> 打开新实例。

**--help**
> 显示帮助信息。

# DESCRIPTION

**open** 在 macOS 上打开文件和 URL。使用默认或指定的应用程序。

该命令通过关联的应用程序启动文件。macOS 特有工具。

# CAVEATS

仅限 macOS。Linux 上请使用 xdg-open。应用名称区分大小写。

# HISTORY

open 一直是 **macOS** 的一部分，用于使用关联的应用程序打开文件。

# INSTALL

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```apk: sudo apk add kbd```

```zypper: sudo zypper install kbd```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-open](/man/xdg-open)(1)
