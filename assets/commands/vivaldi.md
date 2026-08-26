# TAGLINE

可深度定制的基于 Chromium 的网页浏览器

# TLDR

**启动浏览器**

```vivaldi```

**打开 URL**

```vivaldi [https://example.com]```

**新窗口**

```vivaldi --new-window [url]```

**无痕模式**

```vivaldi --incognito```

**使用指定配置文件**

```vivaldi --profile-directory="[Profile 1]"```

# SYNOPSIS

**vivaldi** [_--new-window_] [_--incognito_] [_options_] [_url_]

# PARAMETERS

**--new-window**
> 打开一个新的浏览器窗口。

**--incognito**
> 以隐私浏览模式打开新窗口。

**--profile-directory** _DIR_
> 使用指定的配置文件目录。

**--app** _URL_
> 以应用模式启动 URL（极简界面，没有标签页和地址栏）。

**--no-sandbox**
> 禁用安全沙箱。

**--user-data-dir** _DIR_
> 使用自定义的用户数据目录。

**--help**
> 显示帮助。

# DESCRIPTION

**vivaldi** 是一款功能丰富、基于 Chromium 的网页浏览器，专为希望对浏览体验进行深度控制的高级用户设计。它通过 Chromium 引擎支持现代 Web 标准，并在此基础上叠加了高度可定制的用户界面。

浏览器包含先进的标签页管理功能，例如标签页堆叠、并排查看的标签页平铺，以及可放置在窗口任意一边的标签栏。内置的效率工具包括笔记面板、邮件客户端、日历、订阅阅读器和翻译服务，减少了对独立应用或扩展的需求。

界面的几乎每个方面都可以定制，从键盘快捷键、鼠标手势到工具栏布局和配色主题。浏览器还支持命令链、自定义搜索引擎，以及用于随手访问常用网站的网络面板侧边栏。

# CAVEATS

在开源的 Chromium 之上包含专有 UI 组件。支持大多数 Chromium 命令行开关。自定义开关可放入 `~/.config/vivaldi-stable.conf`。

# HISTORY

**Vivaldi** 由 Opera 联合创始人 **Jon von Tetzchner** 创建，面向希望深度定制的资深用户。

# INSTALL

```pacman: sudo pacman -S vivaldi```

```nix: nix profile install nixpkgs#vivaldi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vivaldi-stable](/man/vivaldi-stable)(1), [firefox](/man/firefox)(1), [chromium](/man/chromium)(1), [google-chrome](/man/google-chrome)(1)
