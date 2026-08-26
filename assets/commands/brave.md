# TAGLINE

注重隐私的网络浏览器

# TLDR

**打开** Brave 浏览器

```brave```

**打开**某个 URL

```brave [https://example.com]```

以无痕模式**打开**

```brave --incognito [https://example.com]```

在新窗口中**打开**

```brave --new-window [https://example.com]```

以独立应用方式**打开** URL

```brave --app=[https://example.com]```

**使用**指定的配置目录

```brave --user-data-dir=[~/.config/brave-profile2]```

# SYNOPSIS

**brave** [_options_] [_url_]

# DESCRIPTION

**brave** 是一款基于 Chromium 构建的关注隐私的网页浏览器。它默认拦截广告和跟踪器，内置加密货币钱包，并通过向用户发放 BAT 代币来奖励其观看尊重隐私的广告。

该浏览器强调速度、隐私与安全，同时保持与 Chrome 扩展的兼容性。

# PARAMETERS

**--incognito**
> 以无痕（隐私）模式打开。

**--new-window**
> 在新窗口中打开 URL。

**--new-tab** _url_
> 在新标签页中打开 URL。

**--app=**_url_
> 以应用模式打开 URL，不带浏览器界面。

**--user-data-dir=**_dir_
> 使用指定的配置目录（默认：~/.config/brave-browser）。

**--proxy-server=**_server_
> 为请求使用指定的 HTTP/SOCKS4/SOCKS5 代理服务器。

**--disable-extensions**
> 禁用所有浏览器扩展。

**--no-proxy-server**
> 不使用代理服务器，始终直连。

**--headless**
> 以无头模式运行，不显示窗口。

# FEATURES

- 内置广告/跟踪器拦截（Brave Shields）
- 自动升级到 HTTPS
- 脚本拦截
- 指纹防护
- BAT 加密货币集成
- Brave Rewards
- 通过 Tor 进行私密浏览
- IPFS 支持
- Chrome 扩展兼容性

# PRIVACY FEATURES

- **Shields**——拦截广告、跟踪器和脚本
- **Tor 私密标签页**——匿名浏览
- **无遥测数据**——默认保护隐私
- **指纹随机化**

# BRAVE REWARDS

一种可选参与的机制，用户观看尊重隐私的广告可获得 BAT（Basic Attention Token）奖励。用户还可以给内容创作者打赏。

# CAVEATS

部分网站在激进拦截下可能无法正常工作。BAT 奖励的可用性因地区而异。同步功能需要 Brave 账户。有人认为内置的加密货币功能没有必要。基于 Chromium（Google 项目）构建。

# HISTORY

**Brave** 由 Brendan Eich（JavaScript 之父、Mozilla 联合创始人）创建，于 **2016** 年发布，旨在通过替代性的广告模式提供注重隐私的浏览体验。

# INSTALL

```nix: nix profile install nixpkgs#brave```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[firefox](/man/firefox)(1), [chromium](/man/chromium)(1), [google-chrome](/man/google-chrome)(1), [tor-browser](/man/tor-browser)(1)
