# TAGLINE

MATE 计算器的命令行界面，提供交互式

# TLDR

启动**交互式计算器**会话

```mate-calc-cmd```

计算指定表达式（在交互模式下）

```[2 + 5]```

# SYNOPSIS

**mate-calc-cmd**

# DESCRIPTION

**mate-calc-cmd** 是 MATE 计算器的命令行界面，提供一个基于终端的交互式计算器会话。它使用与图形版 **mate-calc** 应用相同的计算引擎。

交互式会话接受数学表达式并立即显示结果。它支持与图形版相同的功能和运算符，包括三角函数、对数和任意精度算术。

输入 **quit** 或按 **Ctrl+D** 可退出交互式会话。

# CAVEATS

与 **mate-calc --solve** 不同，此命令会启动交互式会话而不是计算单个表达式。若要在脚本中进行一次性计算，请改用 **mate-calc --solve**。

# INSTALL

```apt: sudo apt install mate-calc```

```dnf: sudo dnf install mate-calc```

```pacman: sudo pacman -S mate-calc```

```apk: sudo apk add mate-calc```

```zypper: sudo zypper install mate-calc```

```nix: nix profile install nixpkgs#mate-calc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mate-calc](/man/mate-calc)(1), [bc](/man/bc)(1), [calc](/man/calc)(1)
