# TAGLINE

在命令行中掷虚拟骰子

# TLDR

掷一个 **20 面**骰子

```rolldice d20```

掷两个六面骰子并**去掉最低的**

```rolldice 2d6s1```

**带修正值**掷骰

```rolldice 2d20+5```

**多次**掷骰

```rolldice 2xd20```

# SYNOPSIS

**rolldice** _dice_specification_

# PARAMETERS

骰子用 **NdS** 格式指定，其中：
> N = 骰子数量，d = 骰子指示符，S = 面数。

**s**_N_
> 去掉最低的 N 次结果。

**+**_N_ 或 **-**_N_
> 加或减修正值。

**x**
> 多次重复掷骰。

# DESCRIPTION

**rolldice** 以各种配置模拟掷骰子。它支持桌面角色扮演游戏使用的标准骰子记法，包括修正值、去掉骰子和多次掷骰。

该工具对桌面 RPG 玩家、游戏开发者或任何需要随机骰子结果的人都很有用。

# CAVEATS

使用系统随机数生成器。结果是伪随机的，不具备密码学安全性。

# HISTORY

作为一个面向桌面游戏和随机数生成的实用工具而创建，使用标准骰子记法。

# INSTALL

```brew: brew install rolldice```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[shuf](/man/shuf)(1), [random](/man/random)(4)
