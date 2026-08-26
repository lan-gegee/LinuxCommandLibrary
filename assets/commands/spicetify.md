# TAGLINE

自定义 Spotify 桌面客户端

# TLDR

**应用自定义设置**

```spicetify apply```

**备份 Spotify**

```spicetify backup```

**恢复 Spotify**

```spicetify restore```

**安装扩展**

```spicetify config extensions [extension.js]```

**更换主题**

```spicetify config current_theme [theme_name]```

**列出配置**

```spicetify config```

**更新 spicetify**

```spicetify upgrade```

**监视变更**

```spicetify watch```

# SYNOPSIS

**spicetify** _command_ [_options_]

# PARAMETERS

**apply**
> 应用自定义设置。

**backup**
> 备份 Spotify。

**restore**
> 恢复原始状态。

**config** _KEY_ _VALUE_
> 设置配置项。

**upgrade**
> 更新 spicetify。

**watch**
> 实时重载。

**update**
> 更新 Spotify 备份。

# CONFIG OPTIONS

**current_theme** - 当前主题
**color_scheme** - 配色方案
**extensions** - 已启用的扩展
**custom_apps** - 自定义应用
**inject_css** - 启用 CSS 注入

# DESCRIPTION

**spicetify** 是一款用于自定义 Spotify 桌面客户端的命令行工具，可以注入自定义 CSS 主题、JavaScript 扩展和自定义应用。它修改 Spotify 客户端文件以实现视觉和功能上的更改。

首次使用前，必须先用 **spicetify backup** 创建原始 Spotify 安装的备份。主题控制视觉外观和配色方案，扩展则添加歌词显示、快捷键、播放列表管理等功能。社区市场提供经过精选的主题和扩展合集。

**watch** 命令可开启开发模式，在主题或扩展文件被修改时实时应用更改。配置存储在 TOML 文件中，并通过 **spicetify config** 命令管理。

# CONFIGURATION

**~/.config/spicetify/config-xpui.ini**
> 主配置文件，存储当前主题、配色方案、已启用的扩展、自定义应用以及 Spotify 安装路径。

**~/.config/spicetify/Themes/**
> 存放各主题文件夹的目录，每个文件夹包含 color.ini 和 user.css 文件，定义视觉自定义内容。

**~/.config/spicetify/Extensions/**
> JavaScript 扩展文件所在目录，这些扩展为 Spotify 客户端添加新功能。

# CAVEATS

Spotify 更新后可能失效。需要桌面版 Spotify。更新前先备份。

# HISTORY

**spicetify** 为 Spotify 自定义而生。它提供了一个为桌面客户端更换主题和添加扩展的框架。

# SEE ALSO
