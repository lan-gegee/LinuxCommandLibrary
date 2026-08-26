# TAGLINE

Google Chrome 稳定版浏览器

# TLDR

**打开一个 URL**

```google-chrome-stable [https://example.com]```

**以无痕模式打开**

```google-chrome-stable --incognito [https://example.com]```

**以无头模式打开**并打印为 PDF

```google-chrome-stable --headless --print-to-pdf=[output.pdf] [https://example.com]```

**启用远程调试**启动

```google-chrome-stable --remote-debugging-port=[9222]```

**禁用所有扩展**

```google-chrome-stable --disable-extensions```

**以信息亭模式打开**（全屏、无浏览器界面）

```google-chrome-stable --kiosk [https://example.com]```

**使用自定义的用户数据目录**

```google-chrome-stable --user-data-dir=[/path/to/profile]```

# SYNOPSIS

**google-chrome-stable** [_options_] [_URL_...]

# PARAMETERS

**--incognito**
> 以隐私浏览模式打开。

**--headless**
> 不显示可视界面运行（用于自动化和测试）。

**--print-to-pdf=**_file_
> 把页面打印为 PDF（配合 --headless 使用）。

**--remote-debugging-port=**_port_
> 在指定端口上启用远程调试。

**--disable-extensions**
> 禁用所有浏览器扩展。

**--no-sandbox**
> 禁用沙箱（用于测试环境）。

**--disable-gpu**
> 禁用 GPU 硬件加速。

**--user-data-dir=**_dir_
> 使用自定义的用户数据目录存放配置。

**--proxy-server=**_proxy_
> 让流量经由指定的代理服务器转发。

**--window-size=**_W,H_
> 设置初始窗口尺寸（例如 1024,768）。

**--app=**_URL_
> 以应用模式启动 URL（极简界面）。

**--kiosk**
> 以信息亭模式启动（全屏、受限界面）。

**--new-window**
> 在新窗口而非新标签页中打开 URL。

# DESCRIPTION

**google-chrome-stable** 是 Google Chrome 稳定版的命令行启动器。它与开源的 Chromium 浏览器共享大部分功能，但包含一些 Google 特有的特性，如自动更新、专有编解码器以及与 Google 服务的集成。

常用的命令行选项与 Chromium 一致，包括无头模式、远程调试、用户配置管理，以及各种面向开发和测试的开关。命令名因系统而异：可用的可能是 **google-chrome**、**google-chrome-stable**，或简称 **chrome**。

# INSTALL

```nix: nix profile install nixpkgs#google-chrome```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chromium](/man/chromium)(1), [firefox](/man/firefox)(1)
