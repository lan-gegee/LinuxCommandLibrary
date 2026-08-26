# TAGLINE

检查路径名的有效性和可移植性

# TLDR

**检查路径的 POSIX 可移植性**

```pathchk [/path/to/file]```

**检查向旧系统的可移植性**

```pathchk -p [/path/to/file]```

**检查空名称和前导连字符**

```pathchk -P [path]```

**检查完整的 POSIX 可移植性**（结合 -p 和 -P）

```pathchk --portability [path]```

**检查多个路径**

```pathchk [path1] [path2] [path3]```

# SYNOPSIS

**pathchk** [_-p_] [_-P_] _pathname_...

# PARAMETERS

**-p**
> 按 POSIX 可移植文件名字符集和最小路径长度限制检查（组成部分限制为 14 个字符）。

**-P**
> 检查空名称和以连字符开头的名称。

**--portability**
> 检查对所有 POSIX 系统的可移植性（相当于 -p -P）。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**pathchk** 检查路径名的有效性和可移植性。它能找出可能在其他系统上引起问题的名称。

默认检查验证路径在当前系统上是否有效：长度是否合适、字符是否合法、父目录是否可访问。

POSIX 可移植模式（-p）执行更严格的限制。它检查在所有 POSIX 系统上都有效的字符，并将组成部分长度限制为 14 个字符（历史最小值）。

-P 选项增加对空路径组成部分和以连字符开头的名称的检查，这类名称可能干扰命令参数解析。

退出码 0 表示所有路径都通过了检查。非零表示发现问题，并通过错误消息说明具体问题。

该工具有助于确保脚本和归档在不同 Unix 系统之间正常运行，不会因路径名问题而失败。

# CAVEATS

可移植模式的检查较为保守。现代系统接受更长的名称。某些检查对仅在单一系统上使用而言可能过于严格。

# HISTORY

**pathchk** 属于 **GNU coreutils**，由 **POSIX** 规定。它提供了一种标准方式来验证路径名，适用于跨平台脚本和工具。

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

[basename](/man/basename)(1), [dirname](/man/dirname)(1), [realpath](/man/realpath)(1)
