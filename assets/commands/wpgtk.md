# TAGLINE

基于壁纸的配色方案管理器

# TLDR

**将壁纸加入收藏**

```wpg -a [/path/to/image.jpg]```

**设置壁纸并应用配色方案**

```wpg -s [wallpaper.jpg]```

**列出已添加的壁纸**

```wpg -l```

**显示当前壁纸**

```wpg -c```

**重新生成壁纸的配色方案**

```wpg -z [wallpaper.jpg]```

**导入 JSON 配色方案**

```wpg -i [wallpaper.jpg] [colorscheme.json]```

**将配色方案应用到终端**

```wpg -t```

**只设置壁纸而不更改配色方案**

```wpg -ns [wallpaper.jpg]```

**调整配色方案的饱和度**

```wpg --sat [wallpaper.jpg] [0.1]```

**启动图形界面**

```wpgtk```

# SYNOPSIS

**wpg** [_options_] [_wallpaper_]

**wpgtk**

# PARAMETERS

**-a** _image_
> 将壁纸加入收藏。

**-s** _wallpaper_ [_fallback_]
> 设置壁纸和配色方案。

**-l**
> 列出已添加的壁纸。

**-c**
> 打印当前壁纸名称。

**-d** _wallpaper_
> 从收藏中删除壁纸。

**-t**
> 将配色方案应用到终端。

**-z** _wallpaper_
> 重新生成配色方案。

**-n**
> 应用配色方案时不设置壁纸（与 -s 配合使用）。

**-i** _wallpaper_ _json_
> 从 JSON 文件导入配色方案。

**-A** _wallpaper_
> 自动调整配色方案以区分前景色和背景色。

**--auto** _wallpaper_
> 自动生成前 8 种颜色的前景版本。

**--sat** _wallpaper_ _value_
> 调整所有颜色的饱和度（负值为减）。

**--brt** _wallpaper_ _value_
> 调整所有颜色的亮度（负值为减）。

**--theme** [_theme_]
> 设置预设主题。不带参数时列出可用主题。

**--pywal** _theme_
> 选择并应用 pywal 主题。

**-h**
> 显示帮助。

# DESCRIPTION

**wpgtk** 是面向类 Unix 系统的配色方案、壁纸和模板管理器。它使用 pywal 作为后端从壁纸中提取颜色，并通过可配置的模板将其应用到整个系统。

该工具根据壁纸图像生成协调一致的配色方案，应用到终端、GTK 主题、窗口管理器及其他应用程序。模板定义了颜色如何应用到每个应用程序的配置文件中。它同时提供 CLI（wpg）和 GUI（wpgtk）两种界面。

配色方案与其壁纸一同保存，可实现即时主题切换。颜色可以手动编辑、从 JSON 导入（兼容 terminal.sexy），或自动调整以获得更好的对比度。

# CAVEATS

需要 pywal 作为后端。每个应用程序的模板文件需要手动设置。某些应用程序需要重启才能应用新颜色。GTK 主题更改可能需要重启会话。

# HISTORY

**wpgtk** 由 deviantfero 创建，旨在 pywal 之上提供友好的用户界面。pywal 负责颜色提取和基本应用，而 wpgtk 增加了壁纸管理、颜色编辑、模板管理和图形界面，适合偏好可视化配置的用户。

# INSTALL

```nix: nix profile install nixpkgs#wpgtk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wal](/man/wal)(1), [feh](/man/feh)(1), [nitrogen](/man/nitrogen)(1)
