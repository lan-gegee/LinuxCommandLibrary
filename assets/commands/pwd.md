# TAGLINE

显示当前工作目录路径

# TLDR

**打印工作目录**

```pwd```

**打印物理路径（不含符号链接）**

```pwd -P```

**打印逻辑路径（保留符号链接）**

```pwd -L```

# SYNOPSIS

**pwd** [_options_]

# PARAMETERS

**-L**
> 逻辑路径（跟随符号链接）。

**-P**
> 物理路径（解析符号链接）。

# DESCRIPTION

**pwd** 打印当前工作目录的绝对路径。它是最基础的 Shell 命令之一，用于在目录之间导航时确认你在文件系统中的位置。

**-P** 选项会解析符号链接以显示物理路径，而 **-L**（大多数 shell 的默认值）会在路径中保留符号链接组件。它既有 shell 内建版本，也有来自 GNU coreutils 的独立二进制文件；交互式 shell 中默认使用内建版本。

# CAVEATS

存在 shell 内建版本和外部命令两种形式。行为可能不同。

# HISTORY

pwd 是用于显示目录的 **经典 Unix** 命令。

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

[cd](/man/cd)(1), [dirs](/man/dirs)(1), [basename](/man/basename)(1)
