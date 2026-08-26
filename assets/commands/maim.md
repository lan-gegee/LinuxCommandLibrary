# TAGLINE

X11 下的轻量级截图工具

# TLDR

**Capture** 整个屏幕截图

```maim [path/to/screenshot.png]```

Capture **选定的区域**

```maim --select [path/to/screenshot.png]```

Capture 到**剪贴板**

```maim --select | xclip -selection clipboard -target image/png```

Capture **活动窗口**

```maim --window $(xdotool getactivewindow) [path/to/screenshot.png]```

带 5 秒**延迟** Capture

```maim --delay 5 [path/to/screenshot.png]```

以指定质量 Capture 为 **JPEG**

```maim --format jpg --quality 7 [path/to/screenshot.jpg]```

# SYNOPSIS

**maim** [_options_] [_file_]

# DESCRIPTION

**maim**（make image）是一个 X11 下的轻量级截图工具。它可以捕获整个屏幕、选定区域或特定窗口，并以多种格式保存。

# PARAMETERS

**-s, --select**
> 交互式选择要捕获的区域

**-i, --window ID**
> 按 ID 捕获特定窗口

**-d, --delay SECONDS**
> 捕获前的延迟时间

**-u, --hidecursor**
> 在截图中隐藏光标

**-g, --geometry WxH+X+Y**
> 设置捕获区域几何尺寸

**-f, --format FORMAT**
> 输出格式（png、jpg、bmp、webp）。从文件名自动检测，默认为 png。

**-m, --quality QUALITY**
> 压缩质量（1-10）。对于有损格式，值越低文件越小、质量越低。

**-B, --capturebackground**
> 同时捕获指定窗口下方的内容。

**-q, --quiet**
> 禁用所有不必要的 stderr 输出。

**-k, --nokeyboard**
> 禁用通过键盘取消选择的功能。

**-l, --highlight**
> 高亮显示选定区域而不是描边。

# CAVEATS

仅支持 X11，不适用于 Wayland。区域选择需要 slop。窗口捕获通常配合 xdotool 使用。

# INSTALL

```apt: sudo apt install maim```

```dnf: sudo dnf install maim```

```pacman: sudo pacman -S maim```

```apk: sudo apk add maim```

```zypper: sudo zypper install maim```

```nix: nix profile install nixpkgs#maim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scrot](/man/scrot)(1), [import](/man/import)(1), [grim](/man/grim)(1), [flameshot](/man/flameshot)(1), [slop](/man/slop)(1), [xdotool](/man/xdotool)(1), [xclip](/man/xclip)(1)
