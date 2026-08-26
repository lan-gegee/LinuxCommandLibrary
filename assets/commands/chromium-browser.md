# TAGLINE

拥有丰富命令行控制选项的开源网页浏览器

# TLDR

**打开 URL**

```chromium-browser [https://example.com]```

**以无痕模式打开**

```chromium-browser --incognito```

**开启远程调试打开**

```chromium-browser --remote-debugging-port=[9222]```

**禁用 GPU 加速**

```chromium-browser --disable-gpu```

**以无头模式启动**

```chromium-browser --headless --screenshot [https://example.com]```

**使用特定的用户配置**

```chromium-browser --user-data-dir=[/path/to/profile]```

# SYNOPSIS

**chromium-browser** [_options_] [_URL_...]

# DESCRIPTION

**chromium-browser** 是开源网页浏览器项目，它是 Google Chrome、Microsoft Edge 以及许多其他浏览器的基础。它提供功能完整的浏览体验，支持现代 Web 标准、扩展和开发者工具。

该浏览器支持大量命令行开关，用于自定义、调试和自动化。无头模式可在没有图形显示的情况下实现服务器端渲染、自动化测试以及截图/PDF 生成。通过 DevTools 协议进行远程调试，允许外部工具检查和控制浏览器会话。

Chromium 可以配置为使用特定的用户配置、代理服务器和实验性特性。它常与 Puppeteer、Playwright 等工具一起用于 CI/CD 流水线、网页抓取和自动化测试环境。

# PARAMETERS

**--incognito**
> 以无痕模式启动

**--headless**
> 无 UI 运行

**--disable-gpu**
> 禁用 GPU 硬件加速

**--remote-debugging-port** _port_
> 启用远程调试

**--user-data-dir** _dir_
> 自定义配置目录

**--no-sandbox**
> 禁用沙箱（用于容器）

**--disable-extensions**
> 禁用扩展

**--start-maximized**
> 以最大化窗口启动

**--kiosk**
> 以信息亭模式启动

**--proxy-server** _server_
> 使用代理服务器

**--enable-features** _features_
> 启用实验性特性

**--disable-features** _features_
> 禁用特性

**--screenshot** _file_
> 截取屏幕截图（无头模式）

**--print-to-pdf** _file_
> 将页面打印为 PDF（无头模式）

# HEADLESS USAGE

```
chromium-browser --headless --print-to-pdf=page.pdf https://example.com
```

# CONFIGURATION

**~/.config/chromium/**
> 用户配置目录，包含偏好设置、书签、历史记录和扩展。

**~/.config/chromium/Default/Preferences**
> 存储每个配置浏览器设置的 JSON 文件。

# CAVEATS

命令行开关可能随版本变化而改变。可通过 about:version 查看当前生效的开关。实验性特性请使用 chrome://flags。

# INSTALL

```dnf: sudo dnf install chromium```

```pacman: sudo pacman -S chromium```

```apk: sudo apk add chromium```

```zypper: sudo zypper install chromium```

```nix: nix profile install nixpkgs#chromium```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[google-chrome](/man/google-chrome)(1), [firefox](/man/firefox)(1), [chromium](/man/chromium)(1)

# RESOURCES

```[Source code](https://chromium.googlesource.com/chromium/src/)```

```[Homepage](https://www.chromium.org/Home/)```

<!-- verified: 2026-06-22 -->
