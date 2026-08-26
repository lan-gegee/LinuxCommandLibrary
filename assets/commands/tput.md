# TAGLINE

查询和设置终端能力

# TLDR

**设置粗体文本**

```tput bold```

**设置前景色**（0-7：黑、红、绿、黄、蓝、洋红、青、白）

```tput setaf [2]```

**设置背景色**

```tput setab [4]```

将所有属性**重置**为默认值

```tput sgr0```

**清屏**

```tput clear```

以列数**获取终端宽度**

```tput cols```

以行数**获取终端高度**

```tput lines```

将光标**移动**到指定行列

```tput cup [5] [10]```

# SYNOPSIS

**tput** [**-T** _type_] _capname_ [_parameters_...]

# PARAMETERS

**-T** _type_
> 指定终端类型；默认取 $TERM 环境变量

**-S**
> 从 stdin 读取能力，允许执行多个操作

**-V**
> 打印 ncurses 版本并退出

# COMMON CAPABILITIES

**bold**
> 启用粗体模式

**dim**
> 启用半亮/暗淡模式

**smul** / **rmul**
> 开始/结束下划线模式

**rev**
> 启用反显模式

**blink**
> 启用闪烁文本

**smso** / **rmso**
> 开始/结束突出显示模式

**sgr0**
> 将所有属性重置为默认值

**setaf** _n_
> 设置前景色（0-7 或 0-255）

**setab** _n_
> 设置背景色

**clear**
> 清屏并将光标移回起始位置

**cup** _row_ _col_
> 将光标移动到指定位置

**cols**
> 输出列数

**lines**
> 输出行数

**sc** / **rc**
> 保存/恢复光标位置

**civis** / **cnorm**
> 隐藏/显示光标

# DESCRIPTION

**tput** 查询 terminfo 数据库以输出与终端相关的能力。它提供了一种可移植的方式来控制颜色、光标定位和文本属性等终端特性，而无需硬编码转义序列。

该命令使用 **$TERM** 环境变量确定终端类型，并查找相应的转义序列。这使脚本可以在不同终端模拟器之间移植。

颜色编号 0-7 代表基本颜色：黑（0）、红（1）、绿（2）、黄（3）、蓝（4）、洋红（5）、青（6）、白（7）。扩展颜色的终端支持 256 色（0-255）。

脚本中的常见用法是将多种能力组合起来：**$(tput bold)$(tput setaf 1)Error$(tput sgr0)** 会以红色粗体打印 "Error"，然后重置属性。

# CAVEATS

能力因终端类型而异；并非所有终端都支持全部特性。使用后务必用 **sgr0** 重置属性，以免影响后续输出。为获得正确行为，**-T** 选项应与实际终端匹配。

# HISTORY

**tput** 于 20 世纪 80 年代初随 **System V Unix** 推出，是 terminfo 系统（取代较旧的 termcap）的一部分。如今大多数 Linux 系统上的 tput 命令由 ncurses 实现提供。其设计目的是将特定于终端的转义码抽象到统一接口之后。

# INSTALL

```apt: sudo apt install ncurses-bin```

```dnf: sudo dnf install ncurses```

```pacman: sudo pacman -S ncurses```

```apk: sudo apk add ncurses```

```brew: brew install ncurses```

```nix: nix profile install nixpkgs#ncurses```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[infocmp](/man/infocmp)(1), [tic](/man/tic)(1), [clear](/man/clear)(1), [reset](/man/reset)(1)
