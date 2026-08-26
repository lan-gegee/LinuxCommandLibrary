# TAGLINE

管理 PlatformIO 开发平台

# TLDR

**列出已安装的平台**

```pio platform list```

**搜索平台**

```pio platform search [espressif]```

**安装平台**

```pio platform install [espressif32]```

**更新平台**

```pio platform update```

**卸载平台**

```pio platform uninstall [espressif32]```

# SYNOPSIS

**pio platform** _command_ [_options_]

# PARAMETERS

**list**
> 列出已安装的平台。

**search** _query_
> 搜索可用平台。

**install** _platform_
> 安装平台。

**uninstall** _platform_
> 移除平台。

**update**
> 更新已安装的平台。

**show** _platform_
> 显示平台详情。

# DESCRIPTION

**pio platform** 用于管理 PlatformIO 开发平台。平台为特定微控制器系列（如 ESP32、STM32 或 AVR）提供工具链、框架和开发板定义。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-boards](/man/pio-boards)(1), [pio-init](/man/pio-init)(1)
