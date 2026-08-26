# TAGLINE

GNOME 光盘刻录应用程序

# TLDR

**启动 Brasero**

```brasero```

**打开音频项目**

```brasero --audio```

**打开数据项目**

```brasero --data```

**打开指定的项目文件**

```brasero --project [project.brasero]```

**复制光盘**

```brasero --copy [/dev/sr0]```

**打开擦除光盘对话框**

```brasero --blank```

**检查光盘完整性**

```brasero --check```

**刻录并删除项目**

```brasero --burn-and-remove-project [project.brasero]```

# SYNOPSIS

**brasero** [_options_]

# DESCRIPTION

**brasero** 是一款 GNOME 应用程序，用于刻录 CD/DVD 介质。它支持创建音频、视频和数据光盘，复制现有光盘，刻录 ISO 镜像，以及擦除可重写介质。

该应用具备即时刻录（on-the-fly）、多段刻录支持，以及借助 GStreamer 自动转换音乐播放列表的功能。它支持多种后端，包括 cdrtools、growisofs 和 libburn。

# PARAMETERS

**-p, --project** _file_
> 打开指定的项目。

**-a, --audio**
> 打开空白的音频项目。

**-d, --data**
> 打开空白的数据项目。

**-c, --copy** _path_
> 从指定设备复制光盘。

**-j, --cover** _path_
> 要使用的封面图片。

**-e, --empty**
> 强制显示项目选择页面。

**-b, --blank**
> 打开擦除光盘对话框。

**-k, --check**
> 打开检查光盘对话框。

**-n, --ncb**
> 打开包含 burn:/// URI 内容的数据项目。

**-r, --burn-and-remove-project** _file_
> 刻录项目并在完成后删除文件。

# CAVEATS

刻录音频 CD 需要使用 WAV 或 Ogg Vorbis 格式的音轨。使用较低的刻录速度可以降低刻录出错的风险。需要合适的光驱硬件以及受支持的后端工具。

# HISTORY

Brasero 作为 GNOME 桌面环境的一部分而开发，旨在提供一款简单易用的光盘刻录应用程序。它与 Nautilus 集成，支持拖放文件操作。

# INSTALL

```apt: sudo apt install brasero```

```dnf: sudo dnf install brasero```

```pacman: sudo pacman -S brasero```

```apk: sudo apk add brasero```

```zypper: sudo zypper install brasero```

```nix: nix profile install nixpkgs#brasero```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wodim](/man/wodim)(1), [growisofs](/man/growisofs)(1), [cdrecord](/man/cdrecord)(1)
