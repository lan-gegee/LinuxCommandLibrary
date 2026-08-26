# TAGLINE

PlatformIO 的统一软件包管理器

# TLDR

**安装库包**

```pio pkg install -l [library_name]```

**安装平台包**

```pio pkg install -p [espressif32]```

**安装工具包**

```pio pkg install -t [openocd]```

**列出已安装的软件包**

```pio pkg list```

**更新软件包**

```pio pkg update```

# SYNOPSIS

**pio pkg** _command_ [_options_]

# PARAMETERS

**install**
> 安装软件包。

**uninstall**
> 移除软件包。

**update**
> 更新软件包。

**list**
> 列出已安装的软件包。

**show**
> 显示软件包详情。

**-l**, **--library** _name_
> 库（library）软件包。

**-p**, **--platform** _name_
> 平台（platform）软件包。

**-t**, **--tool** _name_
> 工具（tool）软件包。

# DESCRIPTION

**pio pkg** 是 PlatformIO 的统一软件包管理器，通过单一界面管理库、平台和工具，取代旧版的 pio lib 和 pio platform 命令。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-lib](/man/pio-lib)(1), [pio-platform](/man/pio-platform)(1)
