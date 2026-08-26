# TAGLINE

使用 RPG 记法模拟掷骰子

# TLDR

**掷骰子**

```roll [2d6]```

**带修正值掷骰**

```roll [1d20+5]```

**多次掷骰**

```roll [3x4d6]```

**详细输出，显示每个骰子**

```roll -v [2d6]```

**只输出总和**

```roll -s [2d6]```

**掷百分骰**

```roll [1d100]```

**带负修正值掷骰**

```roll [1d20-2]```

**多个骰子表达式**

```roll [1d20] [2d6+3]```

# SYNOPSIS

**roll** [_-v_] _dice-expression_ ...

# PARAMETERS

**-v**
> 详细输出，显示每个骰子的结果。

**-s**
> 只输出总和。

_NdS_
> N 个 S 面的骰子。

_NdS+M_
> 加上修正值 M。

_TxNdS_
> 掷 T 次。

# DESCRIPTION

**roll** 是一个命令行掷骰工具，解析 **NdS** 格式的标准 RPG 骰子记法，其中 N 是骰子数量，S 是面数。它支持用修正值（**+** 或 **-**）加减固定数值，并支持 **TxNdS** 格式将同一表达式重复掷多次。

可以在一条命令行中指定多个骰子表达式。**-v** 标志在显示总和之外还显示每个骰子的结果，而 **-s** 只输出最终总和。常见的 RPG 骰子如 d4、d6、d8、d10、d12、d20 和 d100（百分骰）都可通过灵活的记法支持。

# CAVEATS

随机源因系统而异。不具备密码学安全性。仅供娱乐用途。

# HISTORY

**roll** 是一个简单的命令行掷骰工具，实现了桌面角色扮演游戏使用的标准 RPG 骰子记法。

# INSTALL

```brew: brew install roll```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rolldice](/man/rolldice)(6), [shuf](/man/shuf)(1)
