# TAGLINE

DVD 和蓝光盘刻录工具

# TLDR

**将 ISO 刻录到 DVD**

```growisofs -dvd-compat -Z /dev/dvd=[image.iso]```

**从目录创建 DVD**

```growisofs -Z /dev/dvd -R -J [directory]```

**追加到多区段 DVD**

```growisofs -M /dev/dvd -R -J [directory]```

**刻录并进行校验**

```growisofs -dvd-compat -Z /dev/dvd=[image.iso] && md5sum /dev/dvd```

# SYNOPSIS

**growisofs** [_options_] **-Z** _device_ [_mkisofs-options_] _path_

# PARAMETERS

**-Z** _DEVICE_
> 在设备上创建新区段。

**-M** _DEVICE_
> 追加到已有的多区段。

**-dvd-compat**
> 封盘以获得最大兼容性。

**-speed=** _N_
> 设置刻录速度。

**-dry-run**
> 模拟而不实际写入。

**-use-the-force-luke**
> 覆盖安全检查。

**--help**
> 显示帮助信息。

# DESCRIPTION

**growisofs** 用于刻录 DVD 和蓝光光盘。它将 mkisofs 前端与 dvd+rw-tools 后端结合在一起，实现无缝的光盘创建。

该工具负责区段管理、支持多区段 DVD，并兼容 DVD-R、DVD+R、DVD-RW 和蓝光介质。它是 Linux 上的标准 DVD 刻录工具。

# CAVEATS

需要 dvd+rw-tools。介质类型会影响可用选项。速度取决于驱动器和介质。

# HISTORY

growisofs 由 **Andy Polyakov** 开发，是用于 Linux 光盘刻录的 **dvd+rw-tools** 软件包的一部分。

# INSTALL

```apt: sudo apt install growisofs```

```dnf: sudo dnf install dvd+rw-tools```

```pacman: sudo pacman -S dvd+rw-tools```

```apk: sudo apk add dvd+rw-tools```

```zypper: sudo zypper install dvd+rw-tools```

```brew: brew install dvd+rw-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkisofs](/man/mkisofs)(1), [cdrecord](/man/cdrecord)(1)
