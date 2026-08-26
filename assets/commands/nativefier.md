# TAGLINE

用 Electron 将网站封装为桌面应用

# TLDR

**从网站创建应用**

```nativefier "[https://example.com]"```

**以自定义名称创建**

```nativefier --name "[App Name]" "[https://example.com]"```

**以自定义图标创建**

```nativefier --icon [icon.png] "[https://example.com]"```

**在指定目录创建**

```nativefier "[https://example.com]" [/output/dir]```

**创建带托盘图标的应用**

```nativefier --tray "[https://example.com]"```

**创建最大化窗口**

```nativefier --maximize "[https://example.com]"```

**创建单实例应用**

```nativefier --single-instance "[https://example.com]"```

**注入 CSS 创建**

```nativefier --inject [style.css] "[https://example.com]"```

# SYNOPSIS

**nativefier** [_--name name_] [_--icon path_] [_--tray_] [_options_] _url_ [_output_dir_]

# PARAMETERS

**--name** _NAME_
> 应用程序名称。

**--icon** _PATH_
> 自定义图标文件。

**-p**, **--platform** _OS_
> 目标平台（mac、windows、linux）。

**-a**, **--arch** _ARCH_
> 目标架构。

**--tray**
> 添加系统托盘图标。

**--maximize**
> 以最大化方式启动。

**--single-instance**
> 只允许一个实例。

**--inject** _FILE_
> 注入 CSS 或 JavaScript。

**--user-agent** _STRING_
> 自定义用户代理。

**--internal-urls** _REGEX_
> 在应用内部打开的 URL。

**--file-download-options** _JSON_
> 下载行为设置。

**--disable-context-menu**
> 禁用右键菜单。

**--flash**
> 启用 Flash 插件。

**--widevine**
> 启用 Widevine DRM。

# DESCRIPTION

**nativefier** 使用 Electron 将网站封装为桌面应用。其结果是一个行为类似原生应用程序的独立应用。

应用程序拥有自己的窗口和 dock/任务栏图标，可以独立于浏览器运行。这对那些受益于专用窗口管理的 Web 应用很有用。

自定义图标、名称和窗口行为让应用更有原生感。托盘模式可最小化到系统托盘。单实例模式防止运行多个副本。

CSS 和 JavaScript 注入可以修改被封装的站点。这样可以定制外观、添加功能或移除不需要的元素。

内部 URL 模式控制哪些链接在应用内打开、哪些交给默认浏览器。这能让应用专注于其核心功能。

平台定向功能可以在任何开发机器上创建面向 Windows、macOS 或 Linux 的应用。

# CAVEATS

Electron 应用体积较大（100MB 以上）。安全性取决于被封装的网站。Flash 支持已弃用。某些网站会检测并阻止嵌入。项目已进入维护模式。

# HISTORY

**nativefier** 由 **Jia Hao Gao** 于 **2015 年**前后创建，用于轻松地将网页变成桌面应用。它因封装 Slack、WhatsApp Web 和内部工具等服务而流行。该项目现已进入维护模式，更新有限。

# SEE ALSO

[electron](/man/electron)(1), [pwa](/man/pwa)(1)
