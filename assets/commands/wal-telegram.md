# TAGLINE

根据 pywal 生成 Telegram 主题

# TLDR

使用 **wal** 调色板生成

```wal-telegram```

使用**背景**图片

```wal-telegram --background=[path/to/image]```

使用**平铺**的纯色背景

```wal-telegram --tiled```

对背景应用**模糊**

```wal-telegram -g```

设置**输出位置**

```wal-telegram --destination=[path/to/destination]```

生成后**重启** Telegram

```wal-telegram --restart```

# SYNOPSIS

**wal-telegram** [_OPTIONS_]

# PARAMETERS

**--background** _PATH_
> 使用指定的背景图片

**--tiled**
> 使用调色板中的颜色作为背景

**-g**
> 对背景应用高斯模糊

**--destination** _PATH_
> 所生成主题的输出位置

**--restart**
> 生成主题后重启 Telegram

# DESCRIPTION

**wal-telegram** 生成配色与 pywal 调色板一致的 Telegram 桌面主题（`.tdesktop-theme`）。它从 `~/.cache/wal/colors.json` 读取缓存的颜色，并写出一个主题文件，Telegram 桌面客户端可通过 *Settings → Chat Settings → Theme → Apply theme from file* 加载。

默认情况下，聊天背景使用的壁纸是当前由 **feh** 设置的图片（读取自 `~/.fehbg`）；传入 `--background` 可覆盖它，或传入 `--tiled` 改用平铺的调色板颜色。

# CAVEATS

需要至少运行过一次 **pywal**，以确保 `colors.json` 存在。壁纸自动检测仅支持 **feh**；其他壁纸设置工具需要显式指定 `--background` 参数。除非使用 `--restart`，否则每次重新生成主题后都需要在 Telegram 设置中重新应用。

# INSTALL

```apk: sudo apk add py3-pywal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wal](/man/wal)(1)
