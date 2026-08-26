# TAGLINE

打开用户偏好的网页浏览器

# TLDR

打开默认浏览器的**新窗口**

```sensible-browser```

在默认浏览器中打开 **URL**

```sensible-browser https://example.com```

# SYNOPSIS

**sensible-browser** [_URL_]

# DESCRIPTION

**sensible-browser** 会打开用户偏好的网页浏览器。它通过检查环境变量和系统默认设置来确定要启动的浏览器。

浏览器选择顺序为：先检查 BROWSER 环境变量，再检查系统 alternatives。

# CAVEATS

行为取决于环境配置。未经适当设置时，在非图形环境中可能无法工作。

# HISTORY

属于 **sensible-utils** 软件包的一部分，提供符合 Debian 政策的默认应用启动器。

# SEE ALSO

[xdg-open](/man/xdg-open)(1), [update-alternatives](/man/update-alternatives)(8)
