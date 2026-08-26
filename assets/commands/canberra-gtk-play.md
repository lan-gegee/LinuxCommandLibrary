# TAGLINE

播放桌面声音事件

# TLDR

**按标识符播放声音事件**

```canberra-gtk-play --id [desktop-login]```

**播放指定的音频文件**

```canberra-gtk-play --file [path/to/sound.ogg]```

**播放带描述的声音事件**

```canberra-gtk-play --id [bell] --description "[Alert sound]"```

**多次播放同一声音**

```canberra-gtk-play --file [path/to/sound.ogg] --loop [3]```

**对常用声音使用永久缓存**

```canberra-gtk-play --id [message] --cache-control permanent```

# SYNOPSIS

**canberra-gtk-play** [**-i** _id_] [**-f** _file_] [**-d** _description_] [**-l** _loops_] [**-c** _cache_] [_options..._]

# DESCRIPTION

**canberra-gtk-play** 播放符合 XDG 声音主题与命名规范的声音事件。它通过 **libcanberra** 与系统声音服务器（PulseAudio 或 PipeWire）交互，为桌面事件播放情境化音效。

该工具可按标识符（如 "window-close"、"dialog-information"、"bell"）播放预定义的事件声音，也可以播放具体的音频文件。它会把元数据传递给声音服务器，以实现感知上下文的音量控制和路由。

# PARAMETERS

**-i, --id=**_identifier_
> 播放具有指定 XDG 标识符的声音事件

**-f, --file=**_file_
> 播放指定的音频文件

**-d, --description=**_description_
> 为声音事件提供描述

**-l, --loop=**_times_
> 播放次数（默认：1）

**-c, --cache-control=**_mode_
> 缓存模式："permanent" 用于常用声音，"volatile" 用于临时缓存

**--media-role=**_role_
> 设置媒体角色：event、feedback、notification、alarm

**--display=**_display_
> 指定要使用的 X display

# CAVEATS

需要正在运行且支持 libcanberra 的声音服务器（PulseAudio 或 PipeWire）。声音主题事件标识符取决于已安装的声音主题，不同系统之间可能不同。

# HISTORY

包含 canberra-gtk-play 的 **libcanberra** 项目于 **2007-2008 年前后**启动，旨在 Linux 桌面上实现 FreeDesktop.org 的声音主题规范。它为在不同声音服务器之间播放事件声音提供了抽象接口。

# INSTALL

```apt: sudo apt install gnome-session-canberra```

```dnf: sudo dnf install libcanberra-gtk3```

```apk: sudo apk add libcanberra-gtk3```

```zypper: sudo zypper install canberra-gtk-play```

```nix: nix profile install nixpkgs#libcanberra-gtk3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aplay](/man/aplay)(1)
