# TAGLINE

管理 XDG 默认应用设置

# TLDR

**打印**默认 Web 浏览器

```xdg-settings get default-web-browser```

**将**默认 Web 浏览器设置为 Firefox

```xdg-settings set default-web-browser firefox.desktop```

**检查** Firefox 是否为默认浏览器

```xdg-settings check default-web-browser firefox.desktop```

**将**默认邮件处理器设置为 Evolution

```xdg-settings set default-url-scheme-handler mailto evolution.desktop```

**获取** mailto 协议的默认处理器

```xdg-settings get default-url-scheme-handler mailto```

# SYNOPSIS

**xdg-settings** {**get**|**check**|**set**} _property_ [_subproperty_] [_value_]

# PARAMETERS

**get _property_**
> 获取属性的当前值

**set _property_ _value_**
> 设置属性的值

**check _property_ _value_**
> 检查属性是否具有特定值

**default-web-browser**
> 默认 Web 浏览器属性

**default-url-scheme-handler _scheme_**
> URL 协议的默认处理器（mailto、ftp、https 等）

**--list**
> 列出 xdg-settings 支持的所有属性

# DESCRIPTION

**xdg-settings** 管理符合 XDG 规范的桌面环境的设置。它主要处理默认应用设置，如 Web 浏览器和 URL 协议处理器。

该工具提供了一种标准化的方式来配置这些设置，适用于不同的桌面环境（GNOME、KDE、XFCE 等）。

# CAVEATS

应用程序的值为不带路径的 .desktop 文件名。某些桌面环境可能有额外的配置工具。属于 xdg-utils 软件包的一部分。

# INSTALL

```dnf: sudo dnf install xdg-utils```

```pacman: sudo pacman -S xdg-utils```

```apk: sudo apk add xdg-utils```

```zypper: sudo zypper install xdg-utils```

```nix: nix profile install nixpkgs#xdg-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-mime](/man/xdg-mime)(1), [xdg-open](/man/xdg-open)(1)
