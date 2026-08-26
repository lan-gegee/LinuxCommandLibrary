# TAGLINE

解析符号链接和规范路径

# TLDR

**打印符号链接的目标**

```readlink [symlink]```

**获取绝对路径**（解析所有符号链接）

```readlink -f [path]```

**获取绝对路径**（除最后一个组件外都必须存在）

```readlink -e [path]```

**获取规范路径**（不要求路径存在）

```readlink -m [path]```

**每个解析后的路径单独占一行输出**

```readlink -f [path1] [path2]```

# SYNOPSIS

**readlink** [_option_]... _file_...

# PARAMETERS

**-f**, **--canonicalize**
> 递归跟随所有符号链接进行规范化；所有组件必须存在

**-e**, **--canonicalize-existing**
> 规范化，但所有组件必须存在

**-m**, **--canonicalize-missing**
> 规范化，不要求组件存在

**-n**, **--no-newline**
> 不输出末尾换行符

**-q**, **--quiet**
> 抑制错误消息

**-s**, **--silent**
> 抑制错误消息（与 -q 相同）

**-v**, **--verbose**
> 报告错误消息

**-z**, **--zero**
> 每个输出行以 NUL 而不是换行符结尾

**--help**
> 显示帮助并退出

**--version**
> 输出版本信息并退出

# DESCRIPTION

**readlink** 打印符号链接的值或文件的规范路径。不带选项时，它只显示符号链接的直接目标（仅一层）。

规范化选项（**-f**、**-e**、**-m**）会跟随所有符号链接、解析 /./ 和 /../ 引用，返回完整的绝对路径。它们的区别在于如何处理不存在的组件：
- **-f**：除最后一个组件外，其余组件必须存在
- **-e**：所有组件必须存在（最严格）
- **-m**：不要求存在（最宽松）

脚本中常用它来查找文件的真实位置，或把相对路径转换为绝对路径。

# CAVEATS

不带规范化选项时，readlink 只显示符号链接的直接目标。对于链式符号链接，请使用 **-f** 解析最终目标。

在 macOS 上，readlink 行为不同且可能缺少 GNU 选项。可使用 coreutils 提供的 **greadlink** 或 **realpath** 进行可移植的规范化。

需要可移植性的脚本可考虑使用 POSIX 规范中的 **realpath**，尽管它并非处处可用。

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

[ln](/man/ln)(1), [realpath](/man/realpath)(1), [stat](/man/stat)(1), [ls](/man/ls)(1)
