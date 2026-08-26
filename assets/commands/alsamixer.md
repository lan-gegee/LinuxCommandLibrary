# TAGLINE

交互式 ncurses 音频混音器

# TLDR

选择要使用的**声卡**

```alsamixer -c [soundcard_number]```

选择要控制的**混音器设备**

```alsamixer -D [device_name]```

以**播放**视图模式启动

```alsamixer -V playback```

以**黑色背景**启动

```alsamixer -B```

# SYNOPSIS

**alsamixer** [_-c card_] [_-D device_] [_-V mode_]

# DESCRIPTION

**alsamixer** 是一款配合 ALSA 声卡驱动使用的 ncurses 混音器程序。它支持多块声卡上的多个设备，并提供图形化界面来调节音频电平。

# PARAMETERS

**-c, --card number**
> 选择声卡（从 0 开始编号）

**-D, --device id**
> 选择要控制的混音器设备

**-V, --view mode**
> 设置起始视图（playback、capture 或 all）

**-B, --black-background**
> 使用黑色背景色

**-g, --no-color**
> 禁用彩色显示

# KEYBOARD SHORTCUTS

**导航：**
> 左/右方向键或 n/p：选择声道
> 上/下方向键或 +/-：调整音量

**音量控制：**
> PageUp/PageDown：增加/减少 5
> Home：设为 100%
> End：设为 0%
> 0-9：设为 0-90% 音量
> Q/W/E：升高左/双/右声道
> Z/X/C：降低左/双/右声道

**静音与采集：**
> M：切换静音（双声道）
> , 或 <：仅静音左声道
> . 或 >：仅静音右声道
> Space：为当前声道启用录音

**视图模式：**
> F1 或 ?：帮助界面
> F2 或 /：系统信息
> F3/F4/F5：播放/采集/全部模式
> Tab：循环切换视图
> F6 或 S：选择声卡

**其他：**
> H：显示快捷键提醒
> B 或 =：平衡左右声道
> L：重绘屏幕
> Esc 或 Alt+Q：退出

# CONFIGURATION

**/etc/asound.conf**
> 系统级 ALSA 配置文件。

**~/.asoundrc**
> 每用户 ALSA 配置文件，用于自定义设备定义和插件设置。

# CAVEATS

需要已安装并配置 ALSA 驱动。部分选项是否可用取决于声卡的能力。

# HISTORY

属于 **ALSA**（Advanced Linux Sound Architecture）工具集的一部分，该框架取代 OSS 成为 Linux 的标准声音系统。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[amixer](/man/amixer)(1), [aplay](/man/aplay)(1), [arecord](/man/arecord)(1)
