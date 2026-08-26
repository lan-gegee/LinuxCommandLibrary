# TAGLINE

保存和恢复 ALSA 声卡设置。

# TLDR

**保存**当前声卡设置

```sudo alsactl store```

**恢复**已保存的设置

```sudo alsactl restore```

保存**特定声卡**的设置

```sudo alsactl store [0]```

将声卡**初始化**为默认状态

```sudo alsactl init```

使用**指定的状态文件**恢复

```sudo alsactl -f [/path/to/asound.state] restore```

**监视**驱动程序事件

```sudo alsactl monitor```

带**调试输出**地恢复

```sudo alsactl -d restore```

# SYNOPSIS

**alsactl** [_options_] _command_ [_card_]

# DESCRIPTION

**alsactl** 是一个 ALSA 声卡控制工具，用于管理声卡的配置状态。它可以保存和恢复混音器设置、音量级别及其他音频参数。

该工具通常在系统启动和关机时自动调用，以便在重启后保留音频设置。

# PARAMETERS

**store** [_card_]
> 将当前状态保存到文件

**restore** [_card_]
> 从文件恢复状态

**init** [_card_]
> 将声卡初始化为默认状态

**nrestore** [_card_]
> 恢复状态，但在缺少状态文件时不报错

**monitor**
> 监视驱动程序事件

**-f** _file_
> 状态文件（默认：/var/lib/alsa/asound.state）

**-d**
> 调试模式

**-F**
> 强制恢复，尽可能多地恢复控件

**-g**, **--ignore**
> 忽略缺失的声卡（不输出错误信息或返回错误码）

**-P**, **--pedantic**
> 不恢复不匹配的控件元素

**-I**, **--no-init-fallback**
> 恢复失败时不初始化声卡

**-r**, **--runstate** _file_
> 将恢复/初始化状态保存到文件以供错误报告

# CONFIGURATION

**/var/lib/alsa/asound.state**
> 默认的状态文件，混音器设置和音量级别从中保存和恢复。在某些发行版上也可能位于 /etc/asound.state。

# CAVEATS

系统级操作需要 root 权限。状态文件是针对特定声卡的；将声卡移动到不同插槽可能会导致问题。某些驱动程序更新可能会使已保存的状态失效。

# HISTORY

**alsactl** 是 ALSA（Advanced Linux Sound Architecture）项目的一部分，自 **2000** 年代初 ALSA 取代 OSS（Open Sound System）成为 Linux 标准音频框架以来就一直存在。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[alsamixer](/man/alsamixer)(1), [amixer](/man/amixer)(1), [aplay](/man/aplay)(1)
