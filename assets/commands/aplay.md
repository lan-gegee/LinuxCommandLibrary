# TAGLINE

通过 ALSA 播放音频文件

# TLDR

**播放**指定文件

```aplay [path/to/file]```

以 2500 Hz 播放前 **10 秒**

```aplay -d 10 -r 2500 [path/to/file]```

以指定格式播放**原始文件**

```aplay -c 1 -t raw -r 22050 -f mu_law [path/to/file]```

列出可用的**音频设备**

```aplay -l```

# SYNOPSIS

**aplay** [_-d duration_] [_-r rate_] [_-c channels_] [_-t type_] [_-f format_] [_file_]

# DESCRIPTION

**aplay** 是面向 ALSA 声卡驱动的命令行声音播放器。它支持多种音频格式，并能根据文件格式自动确定采样率、位深等参数。

# PARAMETERS

**-d, --duration seconds**
> 在指定秒数后停止播放

**-r, --rate rate**
> 采样率（Hz）

**-c, --channels count**
> 声道数（1 为单声道，2 为立体声）

**-t, --file-type type**
> 文件类型（voc、wav、raw、au）

**-f, --format format**
> 采样格式（S16_LE、U8、mu_law 等）

**-l, --list-devices**
> 列出所有可用音频设备

**-L, --list-pcms**
> 列出所有 PCM 设备

**-D, --device name**
> 按名称选择 PCM 设备

**-q, --quiet**
> 安静模式；不显示消息

**-v, --verbose**
> 详细模式；显示 PCM 结构和设置

**-i, --interactive**
> 允许通过 stdin 进行交互式操作（按空格或回车键暂停/恢复）

# CONFIGURATION

**/etc/asound.conf**
> 系统级 ALSA 配置文件，用于设备默认值和插件定义。

**~/.asoundrc**
> 每用户 ALSA 配置，覆盖系统默认值。

# CAVEATS

需要安装并配置 ALSA 驱动。原始文件需要显式指定格式。

# HISTORY

**ALSA**（Advanced Linux Sound Architecture）实用工具包的一部分，ALSA 取代 OSS 成为标准的 Linux 声音系统。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[arecord](/man/arecord)(1), [alsamixer](/man/alsamixer)(1), [amixer](/man/amixer)(1)
