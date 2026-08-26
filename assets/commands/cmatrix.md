# TAGLINE

基于终端的《黑客帝国》数字雨特效

# TLDR

**以默认设置显示 Matrix 效果**

```cmatrix```

**使用粗体字符**获得更亮的显示效果

```cmatrix -b```

**使用特定颜色**（green、red、blue、yellow、white、magenta、cyan）

```cmatrix -C [green]```

**启用异步滚动**以获得更逼真的效果

```cmatrix -a```

**调整滚动速度**（0-9，数字越大越快）

```cmatrix -s -u [2]```

**以彩虹色显示**

```cmatrix -r```

# SYNOPSIS

**cmatrix** [_-abBflohnsmVx_] [_-u update_] [_-C color_]

# PARAMETERS

**-a**
> 启用异步滚动模式

**-b**
> 开启粗体字符

**-B**
> 全部使用粗体字符（覆盖 -b）

**-f**
> 强制使用 Linux $TERM 类型

**-l**
> Linux 模式（使用 matrix 控制台字体）

**-o**
> 使用旧式滚动

**-h**
> 打印用法并退出

**-n**
> 不使用粗体字符（覆盖 -b 和 -B）

**-s**
> 屏幕保护模式，首次按键即退出

**-x**
> X 窗口模式，在 X 终端中运行时每次按键即退出

**-V**
> 打印版本信息并退出

**-u** _delay_
> 屏幕刷新延迟（0-9，默认 4）

**-C** _color_
> 使用指定颜色（green、red、blue、white、yellow、cyan、magenta、black）

**-r**
> 彩虹模式

**-m**
> Lambda 模式（显示 lambda 符号而非字符）

# DESCRIPTION

**cmatrix** 是一款基于终端的程序，用于模拟《黑客帝国》电影系列中标志性的数字雨特效。它在屏幕上显示不断下落的绿色滚动字符，营造出类似影片中 Matrix 代码的视觉效果。

该程序主要用于美观目的，可用作屏幕保护，或纯粹为了娱乐。它可以自定义各种颜色、速度和显示模式，以满足用户偏好。

# CAVEATS

需要支持 ANSI 转义码和 curses 库的终端。较慢的系统在高速度下可能占用大量 CPU。Linux 控制台字体模式（**-l**）只能在真实的 Linux 控制台上工作，不适用于终端模拟器。

# HISTORY

CMatrix 由 **Chris Allegretta** 于 **1999 年**编写，灵感来自 1999 年电影《黑客帝国》中的视觉特效。它最初是作为类 Unix 系统上一个有趣的终端应用而诞生的，如今已成为为终端会话增添视觉趣味的热门方式。该项目开源，并持续接受社区的更新。

# INSTALL

```apt: sudo apt install cmatrix```

```dnf: sudo dnf install cmatrix```

```pacman: sudo pacman -S cmatrix```

```apk: sudo apk add cmatrix```

```zypper: sudo zypper install cmatrix```

```brew: brew install cmatrix```

```nix: nix profile install nixpkgs#cmatrix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sl](/man/sl)(1), [cowsay](/man/cowsay)(1), [figlet](/man/figlet)(1), [lolcat](/man/lolcat)(1)
