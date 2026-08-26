# TAGLINE

显示环境变量的值

# TLDR

**打印所有环境变量**

```printenv```

**打印特定变量**

```printenv [HOME]```

**打印多个变量**

```printenv [PATH] [USER] [SHELL]```

**以 null 分隔符打印**（供 xargs 使用）

```printenv -0```

# SYNOPSIS

**printenv** [_options_] [_variable_...]

# DESCRIPTION

**printenv** 打印环境变量的值。不带参数调用时，打印所有环境变量。给定变量名作为参数时，只打印这些变量的值。

与 `echo $VAR` 不同，printenv 对未定义的变量不输出任何内容（并返回非零值），因此适合在脚本中测试变量是否存在。

printenv 是 GNU coreutils 的一部分，提供了一种检查 shell 环境的直观方式。

# PARAMETERS

**-0**, **--null**
> 用 NUL 而不是换行符结束每一行。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# CAVEATS

只显示已导出的环境变量，不包括 shell 局部变量。要查看 shell 变量，请使用 `echo $VAR` 或 `set` 命令。变量名区分大小写。

# HISTORY

**printenv** 自 **1983 年**的 **BSD 4.2** 起就是 Unix 系统的组成部分。GNU 版本是 **coreutils** 的一部分。它提供了一种跨不同 shell 访问环境变量的可移植方式。

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

[env](/man/env)(1), [export](/man/export)(1), [set](/man/set)(1)
