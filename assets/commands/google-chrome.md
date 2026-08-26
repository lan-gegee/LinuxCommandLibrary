# TAGLINE

Google Chrome 网页浏览器

# TLDR

**启动** Chrome

```google-chrome```

**打开一个或多个 URL**

```google-chrome [https://example.com] [https://wikipedia.org]```

以**无痕模式打开**

```google-chrome --incognito [url]```

对页面**进行无头截图**

```google-chrome --headless --disable-gpu --screenshot=[out.png] --window-size=[1280,800] [url]```

**将页面保存为 PDF**

```google-chrome --headless --disable-gpu --print-to-pdf=[out.pdf] [url]```

把渲染后的 **DOM 转储**到标准输出

```google-chrome --headless --disable-gpu --dump-dom [url]```

**以远程调试方式启动**（DevTools 协议）

```google-chrome --headless --disable-gpu --remote-debugging-port=[9222]```

**使用隔离的配置**目录

```google-chrome --user-data-dir=[/tmp/chrome-profile]```

# SYNOPSIS

**google-chrome** [_options_] [_urls_...]

# PARAMETERS

_urls_
> 要打开的一个或多个 URL 或本地文件路径。

**--incognito**
> 新建一个无痕（隐私）窗口。

**--new-window**
> 在新窗口而非新标签页中打开 URL。

**--headless**
> 不显示可视界面运行。新版本默认采用"新版"无头模式；如需旧版实现，请传入 `--headless=old`。

**--disable-gpu**
> 禁用 GPU 硬件加速。在 Linux/Windows 上传统上需与 `--headless` 搭配使用。

**--screenshot**[=_file_]
> 在无头模式下保存 PNG 截图（默认 `screenshot.png`）。

**--print-to-pdf**[=_file_]
> 在无头模式下将渲染好的页面保存为 PDF（默认 `output.pdf`）。

**--dump-dom**
> 将目标页面序列化后的 DOM 打印到标准输出。

**--window-size** _W,H_
> 设置初始窗口大小（有助于获得一致的截图效果）。

**--remote-debugging-port** _port_
> 在给定的 TCP 端口上启用 DevTools 协议，供 Puppeteer 或 ChromeDriver 等自动化工具使用。

**--no-sandbox**
> 禁用沙箱。有时在 Docker 容器内必须使用；切勿用于不受信任的内容。

**--disable-dev-shm-usage**
> 避免使用 `/dev/shm`，该目录在容器和 CI 环境中往往过小。

**--disable-extensions**
> 启动时禁用所有扩展。

**--no-first-run**
> 跳过首次运行引导和欢迎提示（在 CI 中很有用）。

**--proxy-server** _url_
> 让流量经由指定的 HTTP/SOCKS 代理转发。

**--user-data-dir** _dir_
> 使用自定义的配置目录（可实现完全隔离的会话）。

**--app** _url_
> 以无浏览器边框的独立应用窗口打开 URL。

# DESCRIPTION

**google-chrome** 是 Google 基于开源 Chromium 浏览器打造的专有版本。它内置 Blink 渲染引擎和 V8 JavaScript 引擎，采用多进程、沙箱化架构，支持与 Google 账户同步，并可接入 Chrome 网上应用店的扩展生态。

其命令行接口接受数百个开关，被广泛用于自动化、测试和数据抓取。无头模式配合 `--screenshot`、`--print-to-pdf`、`--dump-dom` 或 `--remote-debugging-port`，使 Chrome 成为 Puppeteer、Playwright、ChromeDriver 等工具常用的后端。

# CONFIGURATION

**~/.config/google-chrome/**
> 默认用户配置目录，包含书签、历史记录、扩展、偏好设置和缓存数据。

**chrome://flags**
> 浏览器内的实验功能列表页面，这些功能可以独立于命令行开关进行切换。

# CAVEATS

Chrome 较为消耗资源；一个典型会话会占用多个进程和相当多的内存。许多命令行开关没有正式文档、依赖具体版本，并且可能随时被移除而不会另行通知；权威参考是 [peter.sh/experiments/chromium-command-line-switches](https://peter.sh/experiments/chromium-command-line-switches/)。**--no-sandbox** 会削弱 Chrome 的安全模型，只应配合受信任的内容使用。在容器/CI 环境中，为了稳定运行，建议将 `--headless` 与 `--disable-gpu`、`--disable-dev-shm-usage`、`--no-first-run` 搭配使用。

# HISTORY

**Google Chrome** 于 **2008 年 9 月**首次登陆 Windows，并于 2010 年扩展到 Linux 和 macOS。它基于开源的 Chromium 项目构建，引入了沙箱化的每标签页进程模型和 V8 JavaScript 引擎，如今已成为全球使用最广泛的网页浏览器。

# INSTALL

```nix: nix profile install nixpkgs#google-chrome```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chromium](/man/chromium)(1), [firefox](/man/firefox)(1)
