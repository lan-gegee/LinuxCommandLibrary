# TAGLINE

基于文本的纸牌接龙游戏

# TLDR

**开始一局 Canfield 接龙**

```canfield```

**查看**你的 canfield 得分历史

```cfscores```

**查看其他用户**的 canfield 得分

```cfscores [username]```

**查看所有用户**的 canfield 得分

```cfscores -a```

# SYNOPSIS

**canfield**

**cfscores** [**-a**] [_user_]

# PREVIEW

```
 [Kh] [  ] [  ] [  ]
 [Ac] [2d] [3c]
 [##] [##] [##] [##]
```

# DESCRIPTION

**canfield** 是 BSD 游戏合集中 Canfield 纸牌接龙（又称 Demon Solitaire）的文本版实现。卡牌以 ASCII 字符显示在终端中。

**玩法：** 按红黑交替的颜色规则将牌堆向下叠放。整叠牌必须作为一个整体移动。顶牌可用于基础堆，但不能填入空置的牌列位置，空位必须从库存牌补入。手牌每次三张一组发到弃牌堆。

**游戏中的命令：**
- 输入 **ht** 将手牌发到弃牌堆
- 单字母命令加数字表示移动

**计分：** 观察牌面花费 $13，最终结算花费 $26。每张进入基础堆的牌赢得 $5。第一次之后每过一遍手牌花费 $5。游玩时间每分钟花费 $1。

# PARAMETERS

**cfscores** 选项：

**-a**
> 显示所有用户的 canfield 账户

**user**
> 显示指定用户名的得分

# CAVEATS

该游戏维护一个记录你赌博式账户余额的得分数据库。其计分系统模拟了这款接龙的赌场版本：玩家需要付费游玩，放入基础堆的牌可赢取奖金。

# HISTORY

Canfield 接龙得名于 **Richard A. Canfield**，他是 19 世纪的一位美国赌场老板，曾在其赌场推广这种接龙玩法。BSD 游戏的实现最初由 Steve Levine 编写，Steve Feldman、Kirk McKusick、Mikey Olson 和 Eric Allman 也做出了贡献。

# SEE ALSO

[mille](/man/mille)(6)
