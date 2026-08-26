# TAGLINE

解码 EDID 显示器描述数据

# TLDR

**解码** DRM 下已连接显示器的 EDID

```edid-decode /sys/class/drm/card1-DP-1/edid```

**从 stdin 解码** EDID（例如来自 xrandr 属性输出）

```xrandr --props | edid-decode```

**检查** EDID 是否符合标准并报告问题

```edid-decode --check /sys/class/drm/card0-HDMI-A-1/edid```

**报告原生分辨率**，仅在末尾显示摘要

```edid-decode --native-resolution /sys/class/drm/card1-eDP-1/edid```

**输出 xorg ModeLine** 时序，供 xrandr --newmode 使用

```edid-decode --xmodeline /sys/class/drm/card1-DP-1/edid```

**将**原始二进制 EDID **转换为**十六进制转储文件

```edid-decode -o hex monitor.bin monitor.hex```

**在没有 EDID 的情况下显示**已知 CTA VIC 码的时序

```edid-decode --vic 16```

# SYNOPSIS

**edid-decode** [_options_] [_in_ [_out_]]

# DESCRIPTION

**edid-decode** 对显示器中的扩展显示识别数据（EDID）进行解码，并以人类可读的形式展示。它支持 EDID 1.3/1.4、DisplayID 1.3/2.1、HDMI 和 CTA-861 扩展块，以及相关的 VESA/CTA 标准。

如果省略 _in_ 或其为 **-**，则从标准输入读取 EDID。输入可以是原始二进制或 ASCII 文本；该工具会扫描十六进制转储，也能识别来自 **edid-decode** 自身、**xrandr** 属性输出以及 **Xorg** 日志文件的格式。在启用内核模式设置（KMS）的现代 Linux 系统上，已连接显示器的 EDID 位于 **/sys/class/drm/\*/edid**。

如果给定了 _out_，工具会按要求的格式写出 EDID 并跳过解码步骤。默认情况下，stdout 得到十六进制转储，文件路径得到原始二进制。时序行以简短形式显示（分辨率、刷新率、像素时钟），详细时序可选择显示完整的 porch/sync 细节。

# PARAMETERS

**-h**, **--help**
> 打印帮助消息。

**-o**, **--output-format** _fmt_
> 写入 _out_ 时使用格式 _fmt_：**hex**（stdout 的默认值）、**raw**（文件的默认值）、**carray** 或 **xml**。

**-c**, **--check**
> 根据已知标准校验 EDID；在末尾报告警告和失败项。

**-C**, **--check-inline**
> 与 **--check** 相同的检查，但在发现时即时报告。

**-n**, **--native-resolution**
> 在末尾报告原生分辨率（Block 0、CTA 和 DisplayID 块之间可能不同）。

**-p**, **--preferred-timings**
> 在末尾报告首选时序。

**--diagonal** _inches_
> 假定显示器对角线为 _inches_ 英寸，用于图像尺寸一致性检查（方形像素）。

**-P**, **--physical-address**
> 仅打印 HDMI CEC 源物理地址（缺失或无法解析时为 f.f.f.f）。配合 **cec-ctl** 使用很有用。

**-S**, **--short-timings**
> 以短格式显示所有视频时序。

**-L**, **--long-timings**
> 以长格式显示所有视频时序（porch/sync 细节）。

**-N**, **--ntsc**
> 对 6 Hz 的倍数优先采用 NTSC 风格的刷新率（如 29.97 Hz 而非 30）。

**-X**, **--xmodeline**
> 将长时序格式化为 **xorg.conf** 的 ModeLine 字符串，供 **xrandr --newmode** 使用。

**-F**, **--fbmode**
> 将长时序格式化为 **fb.modes** 视频模式。

**-V**, **--v4l2-timings**
> 将长时序格式化为 V4L2 **VIDIOC_S_DV_TIMINGS** 所需的形式。

**-s**, **--skip-hex-dump**
> 省略 EDID 开头的十六进制转储。

**-H**, **--only-hex-dump**
> 仅打印十六进制转储后退出。

**--skip-sha**
> 不在输出中打印 edid-decode 构建的 git SHA。

**--hide-serial-numbers**
> 将人类可读部分中的序列号替换为 "..."。

**--version**
> 显示构建 SHA 和最后一次提交日期。

**--vic** _n_, **--dmt** _id_, **--hdmi-vic** _n_, **--cvt** ..., **--gtf** ..., **--ovt** ...
> 时序计算器/查询表（其中大多数无需解码 EDID）。参数形式见完整 man page。

**--list-established-timings**, **--list-dmts**, **--list-vics**, **--list-hdmi-vics**, **--list-rids**
> 列出已知的时序表。

# CAVEATS

并非每个 EDID 字段都会被完整解码。标准校验是尽力而为的，可能与各标准机构的解释不完全一致。输出格式在不同版本之间不稳定。当内核模式设置可用时，应优先读取 **/sys/class/drm/\*/edid** 而非旧式 BIOS/VBE 方法。即使使用 **--hide-serial-numbers**，序列号在十六进制转储中仍然可见。

# HISTORY

**edid-decode** 最初由 **Adam Jackson** 编写，后来 Eric Anholt、Damien Lespiau、Hans Verkuil 等人也有贡献。维护工作和主仓库迁移到了 **git.linuxtv.org** 下的 LinuxTV 项目。

# INSTALL

```apt: sudo apt install edid-decode```

```dnf: sudo dnf install v4l-utils```

```pacman: sudo pacman -S v4l-utils```

```apk: sudo apk add v4l-utils```

```zypper: sudo zypper install edid-decode```

```nix: nix profile install nixpkgs#v4l-utils```

<!-- packages: 2026-08-12 -->

# SEE ALSO

[get-edid](/man/get-edid)(1), [xrandr](/man/xrandr)(1), [xorg](/man/Xorg)(1), [cec-ctl](/man/cec-ctl)(1)

# RESOURCES

```[Source code](https://git.linuxtv.org/edid-decode.git)```

<!-- verified: 2026-08-12 -->
