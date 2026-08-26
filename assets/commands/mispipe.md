# TAGLINE

将两个命令用管道连接，但返回第一个命令的退出状态

# TLDR

**运行管道并返回第一个命令的退出状态**

```mispipe "[command1]" "[command2]"```

**在 Shell 管道中使用**

```mispipe "cat /nonexistent" "head -n 5"; echo $?```

# SYNOPSIS

**mispipe** _command1_ _command2_

# PARAMETERS

_command1_
> 第一个命令（数据源）。

_command2_
> 第二个命令（数据汇）。

# DESCRIPTION

**mispipe** 将两个命令用管道连接，但返回第一个命令的退出状态而非最后一个。这与常规 Shell 管道返回最终命令退出状态的行为不同。属于 moreutils 工具集。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pee](/man/pee)(1), [sponge](/man/sponge)(1)
