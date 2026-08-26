# TAGLINE

管理 PulseAudio 的 X11 设置

# TLDR

**将 PulseAudio 发布到 X11**

```pax11publish -e```

**移除 X11 属性**

```pax11publish -r```

**显示当前设置**

```pax11publish -d```

**设置显示器**

```pax11publish -e -d [display]```

# SYNOPSIS

**pax11publish** [_options_]

# PARAMETERS

**-e**
> 导出/发布设置。

**-r**
> 移除设置。

**-d**
> 显示设置。

**-S** _SERVER_
> 服务器字符串。

# DESCRIPTION

**pax11publish** 管理 PulseAudio 的 X11 设置。它将服务器信息发布到 X 属性中。

该工具启用 X11 会话音频。是 PulseAudio 的组成部分。

# CAVEATS

PulseAudio 的组成部分。仅适用于 X11。会话启动工具。

# HISTORY

pax11publish 用于实现 **PulseAudio 与 X11 会话**的集成。

# INSTALL

```apt: sudo apt install pulseaudio-utils```

```dnf: sudo dnf install pulseaudio-utils```

```apk: sudo apk add pulseaudio-utils```

```zypper: sudo zypper install pulseaudio-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulseaudio](/man/pulseaudio)(1), [pactl](/man/pactl)(1)
