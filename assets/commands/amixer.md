# TAGLINE

从命令行控制 ALSA 声卡混音器

# TLDR

将**主音量**调高 10%

```amixer -D pulse sset Master 10%+```

将**主音量**调低 10%

```amixer -D pulse sset Master 10%-```

**静音**主声道

```amixer -D pulse sset Master mute```

**取消静音**主声道

```amixer -D pulse sset Master unmute```

列出所有**简单混音器控件**

```amixer scontrols```

# SYNOPSIS

**amixer** [_-option_] [_cmd_]

# DESCRIPTION

**amixer** 是 ALSA 声卡驱动的命令行混音器控制工具。它可以调节音量、切换静音状态，以及查询任何可用声卡的混音器控件设置。不带参数运行时会显示默认声卡的当前混音器设置。

该工具提供简单和完整两种混音器接口。简单接口（以 **s** 为前缀的命令）使用人类可读的控件名称，如 "Master" 或 "PCM"；完整接口则操作数字形式的控件标识符。音量可以用绝对值、百分比或分贝表示。

# PARAMETERS

**-c card**
> 选择卡编号（如 0、1、2）

**-D device**
> 选择设备名称（默认：'default'）

**-s, --stdin**
> 从标准输入顺序读取并执行命令

**-q**
> 安静模式；抑制输出

**-R**
> 使用原始值计算百分比（默认）

**-M**
> 使用映射音量计算百分比

# COMMANDS

**scontrols**
> 列出所有简单混音器控件

**scontents**
> 列出简单混音器控件及其内容

**set/sset NAME PARAMETER**
> 配置混音器控件内容（支持百分比、dB 值、mute/unmute/toggle）

**get/sget NAME**
> 显示简单混音器控件内容

**controls**
> 列出所有声卡控件

**contents**
> 列出声卡控件及其内容

**info**
> 显示混音器设备信息

# CAVEATS

混音器控件名称因声卡而异。请使用 **scontrols** 列出你的声卡上可用的控件。

# HISTORY

属于 **ALSA**（Advanced Linux Sound Architecture）工具集。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[alsamixer](/man/alsamixer)(1), [aplay](/man/aplay)(1), [arecord](/man/arecord)(1)
