# TAGLINE

显示 Raspberry Pi 开发板 GPIO 排针的 ASCII 示意图

# TLDR

显示 **GPIO 引脚分布**示意图

```pinout```

打开 **pinout.xyz** 网站

```pinout -x```

# SYNOPSIS

**pinout** [**-x**|**--xyz**] [**-r** _revision_] [**-c**|**--color**]

# PARAMETERS

**-x, --xyz**
> 在默认浏览器中打开 pinout.xyz 网站

**-r _revision_**
> 显示特定板卡修订版的引脚分布

**-c, --color**
> 强制彩色输出

**-m, --monochrome**
> 强制单色输出

# DESCRIPTION

**pinout** 显示 Raspberry Pi 开发板 GPIO 排针的 ASCII 示意图。它展示全部 40 个引脚的引脚编号、GPIO 编号和功能标签，帮助硬件项目确定接线。

该工具自动检测 Pi 型号并显示相应的引脚分布。它属于 gpiozero Python 软件包的命令行工具。

# CAVEATS

只能在 Raspberry Pi 硬件上工作。需要 gpiozero 软件包。在软件包更新之前可能无法识别很新的 Pi 型号。ASCII 输出最好在足够宽的终端中查看。

# HISTORY

**pinout** 属于 **gpiozero**，这是一个由 **Ben Nuttall** 和 Raspberry Pi Foundation 创建的 GPIO 编程 Python 库。它提供了友好的界面，无需外部文档即可理解 Pi 的 GPIO 布局。

# INSTALL

```apt: sudo apt install python3-gpiozero```

```dnf: sudo dnf install python3-gpiozero```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpio](/man/gpio)(1), [raspi-config](/man/raspi-config)(1), [raspi-gpio](/man/raspi-gpio)(1)
