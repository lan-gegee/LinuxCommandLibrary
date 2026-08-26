# TAGLINE

Mozilla 出品的开源网页浏览器

# TLDR

**打开 Firefox**

```firefox```

**打开指定 URL**

```firefox [https://example.com]```

**新建窗口**

```firefox --new-window [url]```

**隐私浏览**

```firefox --private-window```

**使用指定配置档**

```firefox -P [profilename]```

# SYNOPSIS

**firefox** [_options_] [_urls_...]

# PARAMETERS

_URLS_
> 要打开的 URL。

**--new-window** _URL_
> 在新窗口中打开 URL。

**--new-tab** _URL_
> 在新标签页中打开 URL。

**--private-window**
> 进入隐私浏览模式。

**-P** _PROFILE_
> 使用指定名称的配置档。

**--ProfileManager**
> 打开配置档管理器。

**--safe-mode**
> 在禁用扩展的状态下启动。

**--headless**
> 无界面运行。

**--screenshot** _FILE_
> 把页面截图保存到文件。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.mozilla/firefox/profiles.ini**
> 配置档设置及其位置映射。

**~/.mozilla/firefox/[profile]/prefs.js**
> 某个配置档的用户偏好设置。

**~/.mozilla/firefox/[profile]/user.js**
> 用户对偏好项的自定义覆盖。

# DESCRIPTION

**firefox** 是 Mozilla 的开源网页浏览器。其命令行接口支持以多种选项启动浏览器，可用于窗口管理、配置档切换和自动化任务。

浏览器支持多配置档，便于把工作浏览和个人浏览分隔开。无头模式能够在没有可见窗口的情况下执行自动截图和测试。

Firefox 提供丰富的隐私特性，并借助扩展生态提供强大的插件支持。

# CAVEATS

使用配置档相关选项时不能有正在运行的实例。无头模式的功能有限。某些选项的行为随平台而异。

# HISTORY

Firefox 由 **Mozilla** 项目孕育，2002 年以 Phoenix 之名诞生，2004 年更名为 Firefox。它是撼动 Internet Explorer 统治地位的主要浏览器之一，率先普及了标签页浏览和扩展机制。

# INSTALL

```apt: sudo apt install firefox-esr```

```dnf: sudo dnf install firefox```

```pacman: sudo pacman -S firefox```

```apk: sudo apk add firefox```

```zypper: sudo zypper install firefox-esr```

```nix: nix profile install nixpkgs#firefox-esr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chromium](/man/chromium)(1), [google-chrome](/man/google-chrome)(1)

# RESOURCES

```[Homepage](https://www.mozilla.org/firefox/)```

<!-- verified: 2026-07-15 -->
