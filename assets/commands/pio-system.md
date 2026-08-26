# TAGLINE

管理 PlatformIO 系统信息与维护

# TLDR

**显示系统信息**

```pio system info```

**清理未使用的数据**

```pio system prune```

**以试运行方式清理**

```pio system prune --dry-run```

# SYNOPSIS

**pio system** _command_ [_options_]

# PARAMETERS

**info**
> 显示系统信息。

**prune**
> 移除未使用的数据。

**--dry-run**
> 显示将被移除的内容。

**--force**
> 跳过确认提示。

# DESCRIPTION

**pio system** 提供系统信息查看和维护命令，可显示 PlatformIO 安装详情并清理未使用的软件包和缓存数据。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-settings](/man/pio-settings)(1), [pio-upgrade](/man/pio-upgrade)(1)
