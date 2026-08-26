# TAGLINE

3D 落块拼图游戏

# TLDR

**启动 BlockOut II**

```blockout2```

# SYNOPSIS

**blockout2**

# DESCRIPTION

**BlockOut II** 是一款免费开源的 3D 俄罗斯方块游戏，改编自 California Dreams 于 1989 年发行的原始 BlockOut DOS 游戏。它使用 OpenGL 渲染，并提供带回放功能的在线分数数据库。

游戏中需要操纵在坑道中下落的 3D 方块，通过旋转和摆放来填满水平层。填满的层会被消除，目标是在坑被填满之前尽可能多地消除层数。

**游戏内控制：**
- **Q, W, E, A, S, D** - 旋转方块（小键盘也可）
- **方向键** - 水平移动方块
- **空格** - 投放方块
- **P** - 暂停游戏
- **Esc** - 返回菜单

回放文件存储在 Linux 系统的 **~/.bl2/replay/** 目录中。

# CONFIGURATION

**~/.bl2/blockout.cfg**
> 游戏设置，包括坑道尺寸、方块集合和显示选项。

# CAVEATS

需要 OpenGL 支持。如果从自定义位置运行，可能需要将 **BL2_HOME** 环境变量设置为安装目录。

# HISTORY

最初的 BlockOut 由 California Dreams 于 **1989 年**发布（DOS 平台）。BlockOut II 是其开源重制版，于 21 世纪初开始开发，2.5 版增加了 64 位支持并统一了各平台的 OpenGL 渲染器。

# INSTALL

```aur: yay -S blockout2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tetris-bsd](/man/tetris-bsd)(6)
