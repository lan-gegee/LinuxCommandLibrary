# TAGLINE

返回成功的退出状态

# TLDR

返回表示成功的退出状态

```true```

用于无限循环

```while true; do [command]; sleep [1]; done```

在条件判断中用作占位符

```if true; then echo "always runs"; fi```

在脚本中忽略命令失败

```command || true```

在 Shell 中充当空操作命令

```true; echo "continues regardless"```

# SYNOPSIS

**true** [_IGNORED_]

# DESCRIPTION

**true** 什么都不做，只返回退出状态 0（成功）。提供的任何参数都会被忽略。

该命令用于 Shell 脚本中语法上要求有命令但实际无需执行任何操作的场合。常见用法包括：

- 无限循环：**while true; do ...; done**
- 忽略失败：**command || true**（防止脚本在 set -e 下退出）
- 逻辑尚未完成时在条件判断中充当占位符
- 用必须成功的命令替换来初始化变量

作为大多数 Shell 的内建命令，true 执行时不会派生子进程，因此在循环中频繁使用也很高效。

# CAVEATS

虽然 true 会忽略所有参数，但它仍会解析它们。某些实现对 **--help** 和 **--version** 做特殊处理。当内建命令不可用或需要 exec 时，可以使用外部二进制 /usr/bin/true。

# HISTORY

自 **1979 年**的 Version 7 Unix 起，true 就已成为 Unix 的一部分。它最初实现为空 shell 脚本或一个仅调用 exit(0) 的程序。配套命令 **false** 返回退出状态 1。两者均由 POSIX 规定，既可作为 shell 内建命令，也以独立二进制形式存在。

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

[false](/man/false)(1), [test](/man/test)(1), [bash](/man/bash)(1)
