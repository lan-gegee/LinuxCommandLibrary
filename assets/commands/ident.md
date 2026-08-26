# TAGLINE

从文件中提取 RCS 关键字

# TLDR

**显示 RCS 关键字**

```ident [file]```

**处理多个文件**

```ident [file1] [file2]```

**安静模式**

```ident -q [file]```

**只显示版本关键字**

```ident -V [file]```

# SYNOPSIS

**ident** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要扫描的文件。

**-q**
> 安静模式。

**-V**
> 只显示版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ident** 从文件中提取 RCS 关键字。它会查找并显示内嵌的版本控制信息，如 $Id$ 和 $Revision$。

该工具在二进制和文本文件中扫描 RCS 关键字模式。它用于在构建过程中识别文件版本。

# CAVEATS

属于 RCS 软件包。关键字必须已被展开。属于历史工具。

# HISTORY

ident 是 **RCS**（Revision Control System）的一部分，早于现代版本控制系统。

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

[rcs](/man/rcs)(1), [ci](/man/ci)(1), [co](/man/co)(1)
