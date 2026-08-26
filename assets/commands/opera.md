# TAGLINE

网页浏览器

# TLDR

**启动 Opera 浏览器**

```opera```

**打开 URL**

```opera [https://example.com]```

**在新窗口中打开**

```opera --new-window [url]```

**隐私浏览**

```opera --private```

**以指定配置文件启动**

```opera --user-data-dir=[/path/to/profile]```

# SYNOPSIS

**opera** [_options_] [_url_]

# PARAMETERS

_URL_
> 要打开的 URL。

**--new-window**
> 在新窗口中打开。

**--private**
> 隐私浏览模式。

**--user-data-dir** _DIR_
> 配置目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**opera** 是 Opera 网页浏览器。一款基于 Chromium 并带有内置功能的浏览器。

该浏览器包含 VPN、广告拦截器和工作区。跨平台。

# CAVEATS

专有软件。基于 Chromium。内置 VPN 功能有限。

# HISTORY

Opera 创建于 **1995 年**，是最早的替代性网页浏览器之一。

# INSTALL

```aur: yay -S opera```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[firefox](/man/firefox)(1), [chromium](/man/chromium)(1), [vivaldi](/man/vivaldi)(1)
