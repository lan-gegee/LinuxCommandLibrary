# TAGLINE

支持动画的 ASCII/ANSI 字符画编辑器

# TLDR

**启动** ASCII/ANSI 字符画编辑器

```durdraw```

**打开文件**（.dur 或 ASCII/ANSI）进行编辑

```durdraw [filename.dur]```

**以指定尺寸创建新画布**

```durdraw -W [80] -H [25]```

**使用能容纳于终端的最大画布尺寸**

```durdraw -m```

**播放 .dur 动画**后退出

```durdraw -p [animation.dur]```

**循环播放动画**固定次数

```durdraw -p -x [3] [animation.dur]```

**强制 16 色或 256 色模式**

```durdraw --256color```

**将已加载的作品导出为 .ansi** 后退出

```durdraw --export-ansi [input.dur]```

# SYNOPSIS

**durdraw** [_options_] [_filename_]

# PARAMETERS

_FILENAME_
> 要加载的 .dur、ASCII 或 ANSI 文件。

**-p**, **--play**
> 播放 .dur 文件后退出。

**-x**, **--times** _N_
> 播放 _N_ 次（需要 **-p**）。

**--startup**
> 显示启动画面。

**-w**, **--wait**
> 在启动画面暂停。

**--256color**
> 强制 256 色模式。

**--16color**
> 强制 16 色模式。

**-b**, **--blackbg**
> 使用黑色背景代替终端默认背景。

**-W**, **--width** _N_
> 设置画布宽度。

**-H**, **--height** _N_
> 设置画布高度。

**-m**, **--max**
> 使用能容纳于终端的最大画布。

**--nomouse**
> 禁用鼠标支持。

**--cursor** _STYLE_
> 光标样式：block、underscore 或 pipe。

**--notheme**
> 禁用主题支持。

**--theme** _FILE_
> 加载自定义主题文件。

**--cp437**
> 使用 Code Page 437 编码（测试版）。

**--export-ansi**
> 将已加载的作品导出为 .ansi 文件并退出。

**-u**, **--undosize** _N_
> 撤销历史的状态数（默认：100）。

**-V**, **--version**
> 显示版本并退出。

**-h**, **--help**
> 显示帮助并退出。

# DESCRIPTION

**durdraw** 是一个功能多样的基于 curses 的 ASCII、ANSI 和 Unicode 字符画编辑器，可在 Linux、Unix 和 macOS 终端中作画。它支持 16 色和 256 色调色板、CP437 与 Unicode、自定义主题、鼠标输入，以及可调节延迟的逐帧动画。

文件以 durdraw 原生的基于 JSON 的 `.dur` 格式保存，完整保留动画帧和元数据。静态作品可以导出为 `.ansi`，以便在传统 ANSI 画板上分享。动画可通过 **durdraw -p** 或配套工具 **durview** 在终端中回放。

# KEYBINDINGS

**方向键**
> 移动光标

**Space**
> 用选定的画笔绘制

**Tab**
> 在前景色/背景色之间切换

**c**
> 取色模式

**b**
> 选择画笔

**f**
> 泛洪填充

**Ctrl+S**
> 保存文件

**Ctrl+Q**
> 退出

**PgUp/PgDn**
> 在动画帧之间导航

**F5**
> 播放/预览动画

# CAVEATS

需要具备完善 ANSI 支持的终端。动画播放效果取决于终端能力。大型动画可能消耗大量内存。部分导出格式需要额外的依赖。

# HISTORY

**durdraw** 由 Sam "cmang" Foster 创建，是 TheDraw 和 ACiDDraw 等 DOS 时代 ANSI 编辑器的现代后继者，凭借 256 色支持、Unicode 和帧动画等特性，把终端艺术创作带到了 Linux、Unix 和 macOS 上。

# INSTALL

```brew: brew install durdraw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gimp](/man/gimp)(1), [imagemagick](/man/imagemagick)(1)
