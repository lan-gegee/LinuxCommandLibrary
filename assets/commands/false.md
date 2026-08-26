# TAGLINE

返回失败退出状态

# TLDR

**返回失败状态**

```false```

在条件判断中使用

```if false; then echo "never"; fi```

与 or 连用

```false || echo "false returned failure"```

无限循环惯用法（until 永不成功）

```until false; do :; done```

# SYNOPSIS

**false**

# PARAMETERS

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**false** 不做任何事情，返回失败的退出状态（1）。它是 true 的对应物，在 shell 脚本中用于流程控制、测试和占位。

该命令不接受操作数，总是以状态码 1（表示失败）退出。这使它适用于条件语句、永不执行的循环以及错误处理测试。

false 是 POSIX 标准命令，同时也是 shell 内建命令，提供保证失败的退出状态。

# CAVEATS

作为内建命令，行为在不同 shell 之间可能略有差异。退出状态始终为 1（或非零）。除此之外什么也不做。

# HISTORY

false 自 **Version 7**（1979 年）起就是 Unix 的一部分。它是最简单的 Unix 命令之一，存在的唯一目的就是返回失败状态。由 POSIX 规定，既有独立工具实现也有 shell 内建实现。

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

[true](/man/true)(1), [test](/man/test)(1), [bash](/man/bash)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/coreutils.git)```

```[Homepage](https://www.gnu.org/software/coreutils/)```

<!-- verified: 2026-07-15 -->
