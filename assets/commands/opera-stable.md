# TAGLINE

启动 Opera 网页浏览器，一款基于 Chromium 的浏览器

# TLDR

打开 **Opera 浏览器**

```opera-stable```

打开**特定 URL**

```opera-stable [https://example.com]```

以**无痕模式**打开

```opera-stable --private```

使用**特定配置文件**打开

```opera-stable --profile-directory="[Profile Name]"```

# SYNOPSIS

**opera-stable** [_options_] [_URL_...]

# PARAMETERS

**--private**
> 以隐私浏览模式打开

**--new-window**
> 在新窗口中打开 URL

**--incognito**
> 隐私模式的别名

**--profile-directory=**_name_
> 使用指定的配置目录

**--disable-extensions**
> 启动时禁用扩展

**--disable-gpu**
> 禁用 GPU 硬件加速

**--no-sandbox**
> 禁用沙箱模式（不推荐）

**--user-data-dir=**_path_
> 设置自定义用户数据目录

**--proxy-server=**_proxy_
> 使用指定的代理服务器

**--version**
> 显示版本信息

# DESCRIPTION

**opera-stable** 用于启动 Opera 网页浏览器——一款基于 Chromium 的浏览器，内置广告拦截、免费 VPN 和可自定义侧边栏等功能。作为 Chromium 衍生版，它支持大多数 Chrome 命令行标志以及 Chrome 应用商店的扩展。

Opera 还包含一些独特功能，例如 Flow（设备间同步）、Workspaces（标签页组织）以及面向社交平台的集成消息侧边栏。稳定版（stable）是可供生产使用的版本，与测试版或开发者版相对。

# CAVEATS

命令行选项遵循 Chromium 惯例。部分 Chrome 标志的行为可能不完全一致。内置 VPN 实为代理服务，并非完整的 VPN。使用 **--no-sandbox** 运行会显著降低安全性。

# HISTORY

Opera 最初由挪威 Telenor 公司于 **1995 年**开发，是仍在积极开发中最古老的网页浏览器之一。**2013 年**，Opera 从其专有的 Presto 引擎转向 Chromium/Blink。该浏览器于 **2016 年**被一个中国财团收购，并继续以 Opera Software 的名义开发。

# INSTALL

```aur: yay -S opera```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chromium](/man/chromium)(1), [google-chrome](/man/google-chrome)(1), [firefox](/man/firefox)(1), [vivaldi-stable](/man/vivaldi-stable)(1)
