# TAGLINE

开源网页浏览器

# TLDR

**打开 Chromium 浏览器**

```chromium```

**在新窗口中打开 URL**

```chromium --new-window [https://example.com]```

**以无痕模式打开**

```chromium --incognito```

**以应用模式打开 URL（极简 UI）**

```chromium --app=[https://example.com]```

**使用特定的用户数据目录**

```chromium --user-data-dir=[path/to/directory]```

**使用特定的代理服务器**

```chromium --proxy-server=[host:port]```

**以无头模式运行**

```chromium --headless --dump-dom [https://example.com]```

**以信息亭模式打开（全屏）**

```chromium --kiosk [https://example.com]```

# SYNOPSIS

**chromium** [_options_] [_URL..._]

# DESCRIPTION

**Chromium** 是开源网页浏览器项目，是 Google Chrome 的基础。它提供快速、安全的浏览体验，支持现代 Web 标准。

该浏览器支持数百个命令行标志，可用于自定义、调试和自动化。大多数标志没有官方文档且属于实验性质；常用标志相对稳定。

在 Linux 上，配置数据默认存储于 **~/.config/chromium**，缓存位于 **~/.cache/chromium**。

# PARAMETERS

**--user-data-dir=**_DIR_
> 使用指定目录存放用户数据（配置文件）。运行多个实例时必需

**--incognito**
> 以无痕（隐私浏览）模式打开

**--new-window**
> 在新窗口中打开 URL

**--app=**_URL_
> 以应用模式运行 URL，浏览器 UI 极简

**--proxy-server=**_host:port_
> 指定 HTTP/SOCKS 代理服务器

**--headless**
> 无图形界面运行

**--disable-gpu**
> 禁用 GPU 硬件加速

**--no-first-run**
> 跳过首次运行的欢迎对话框

**--kiosk**
> 以全屏信息亭模式运行

**--remote-debugging-port=**_port_
> 在指定端口启用远程调试

# CONFIGURATION

**~/.config/chromium/**
> 用户配置目录，包含偏好设置、书签、扩展、cookie 和浏览历史。

**~/.config/chromium/Default/Preferences**
> 存储浏览器设置的 JSON 文件。可以直接编辑，但在浏览器运行时所做的更改可能被覆盖。

# CAVEATS

**--no-sandbox** 标志会禁用安全沙箱，仅在必要时使用（例如容器中）。大多数命令行标志属于实验性质，可能随版本变化。

在浏览器中访问 **about:version** 可查看当前生效的标志。

# HISTORY

**Chromium** 由 Google 于 **2008 年 9 月**首次发布，作为 Google Chrome 的开源基础。该项目使用 Blink 渲染引擎（2013 年从 WebKit 分支而来）和 V8 JavaScript 引擎。

# INSTALL

```apt: sudo apt install chromium```

```dnf: sudo dnf install chromium```

```pacman: sudo pacman -S chromium```

```apk: sudo apk add chromium```

```zypper: sudo zypper install chromium```

```nix: nix profile install nixpkgs#chromium```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[google-chrome](/man/google-chrome)(1), [firefox](/man/firefox)(1)

# RESOURCES

```[Source code](https://chromium.googlesource.com/chromium/src/)```

```[Homepage](https://www.chromium.org/Home/)```

<!-- verified: 2026-06-22 -->
