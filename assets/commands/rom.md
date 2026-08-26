# TAGLINE

通过 libretro 在终端中游玩游戏 ROM

# TLDR

**运行**一个 ROM（首次启动时可能会提示获取核心）

```rom [path/to/game.sfc]```

从最新的存档状态**继续**最近玩过的游戏

```rom --resume```

**使用**指定的 libretro 核心

```rom --core [path/to/core.so] [path/to/game.gb]```

在终端窗口中**全屏**显示

```rom --fullscreen [path/to/game.gba]```

**整数倍缩放**（inline 模式）并按终端主题**重新着色**

```rom --scale [3] --recolor [hue] [path/to/game.nes]```

**打印**某个 ROM 的按键绑定

```rom --keys [path/to/game.sfc]```

**禁用**音频

```rom --no-audio [path/to/game.md]```

# SYNOPSIS

**rom** [_options_] _rom-file_

**rom** **--resume**

# PARAMETERS

**--resume**
> 从最近玩过的游戏中选择，并加载最新的存档状态。

**--core** _path_
> 使用指定的 libretro 核心（Linux 上为 .so，macOS 上为 .dylib）。

**--fullscreen**
> 填满终端窗口。

**--scale** _n_
> inline 模式下的整数倍缩放，1–8（默认 2）；可用 **[** / **]** 实时调整。

**--slot** _n_
> 初始存档槽位，0–9。

**--no-audio**
> 禁用音频。

**--recolor** _mode_
> 终端主题重新着色模式：**off**、**hue**、**nearest**、**duotone**、**tint** 或 **dither**。

**--recolor-strength** _0..1_
> 将重新着色与原始调色板混合。

**--keys**
> 打印当前按键绑定（可选附带 ROM 路径以显示实际生效的设置）。

**--selftest** _n_
> 在无终端的情况下运行 _n_ 帧（用于测试）。

**--shot** _file_
> 将最终的自测帧保存为 BMP。

**--force**
> 跳过终端图形能力检测。

# DESCRIPTION

**rom** 是一款面向 **macOS** 和 **Linux** 的小型 **libretro** 前端，可在终端内直接游玩主机和经典 PC 游戏 ROM。它通过 **kitty graphics protocol** 渲染原生像素（在 **Ghostty** 或 **kitty** 中可用，包括在启用了 passthrough 的 **tmux** 下），支持真实的按键释放事件、存档状态、音频、快进以及实时的终端主题重新着色。

该工具**不**附带游戏、BIOS 文件或模拟器核心。打开某个平台没有对应核心的 ROM 时，会提示浅克隆并将匹配的 libretro 核心构建到 **~/.config/rom/cores/** 中（需要 git、make 和 C/C++ 工具链）。此外还会在 **./cores/** 目录和可执行文件旁边搜索核心。

支持的扩展名映射到常见核心，包括 SNES（**.sfc**/**.smc**）、NES（**.nes**）、Game Boy/Color（**.gb**/**.gbc**）、GBA（**.gba**）、Genesis（**.md**/**.gen**）、PC Engine（**.pce**）、N64（**.n64**/**.z64**）、Doom 系 WAD（**.wad**）和 Wolfenstein 数据（**.wl6** 等）。请只运行你有合法权利使用的软件。

# CONFIGURATION

**~/.config/rom/config**
> 主设置文件：缩放、终端缩放方式、重新着色模式、音频/焦点行为、按键绑定，以及可选的按系统（**snes**、**nes**、**gb**、**gba**、**genesis**、**pce**、**n64**、**doom**、**wolf3d**）划分的配置段和 **[core.**_system_**]** libretro 选项段。

**~/.config/rom/cores/**
> 已安装的 libretro 核心库。

**~/.config/rom/saves/** / **~/.config/rom/states/**
> 电池存档与即时存档。

**~/.config/rom/games/** / **~/.config/rom/recent**
> 每个 ROM 的音量/缩放记忆以及续玩列表。

**tmux**：用 **tmux set -g allow-passthrough all** 启用一次图形 passthrough（或写入 **~/.tmux.conf**）。

# CAVEATS

需要支持 **kitty graphics protocol** 的终端（Ghostty 或 kitty）。音频在 macOS 上使用 CoreAudio，在 Linux 上使用 ALSA。macOS 上通过离屏 CGL 支持 OpenGL 核心；在 EGL 后端落地之前，Linux 使用软件渲染。不支持 Vulkan 核心。仅支持玩家 1 键盘。ROM、BIOS 和核心不随软件分发——请自行合法获取。

# HISTORY

**rom** 是 **jhickner** 开发的开源 libretro 前端，专注于终端原生游戏体验：kitty 协议帧输出、即时存档，以及可选的调色板重新着色以匹配宿主终端主题。

# SEE ALSO

[retroarch](/man/retroarch)(1), [emulationstation](/man/emulationstation)(1), [kitty](/man/kitty)(1)

# RESOURCES

```[Source code](https://github.com/jhickner/rom)```

<!-- verified: 2026-07-31 -->
