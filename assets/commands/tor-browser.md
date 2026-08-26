# TAGLINE

注重隐私的匿名网页浏览器

# TLDR

**启动 Tor Browser**

```tor-browser```

**以指定的配置文件启动**

```tor-browser --profile [path/to/profile]```

**启动并打开 URL**

```tor-browser [url]```

**以离线模式启动**

```tor-browser --offline```

**以新实例启动**（与现有实例分离）

```tor-browser --new-instance```

**显示版本信息**

```tor-browser --version```

# SYNOPSIS

**tor-browser** [_options_] [_url_]

# PARAMETERS

**--profile** _path_
> 以指定的配置文件目录启动。

**--new-instance**
> 打开新的浏览器实例，而不是使用现有实例。

**--offline**
> 以离线模式启动。

**--private-window**
> 打开隐私浏览窗口。

**--safe-mode**
> 以禁用所有扩展的方式启动。

**--headless**
> 在无可见 UI 的情况下运行（用于自动化）。

**--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Tor Browser** 是一款基于 Mozilla Firefox、注重隐私的网页浏览器，它将所有流量经 Tor 匿名网络路由。它预置了多项隐私保护措施，包括 NoScript、仅 HTTPS 模式和反指纹追踪。

该浏览器通常在 Debian/Ubuntu 系统上通过 **torbrowser-launcher** 安装，或从官方 tarball 安装。通过启动器安装时，**torbrowser-launcher** 命令负责下载、验证、更新和启动浏览器。手动安装时，可在解压后的目录中使用 **./start-tor-browser.desktop** 启动浏览器。

Tor Browser 会在启动时自动连接 Tor 网络，通过多个中继加密流量，以匿名化用户的位置和浏览活动。它包含显示中继路径的链路视图（circuit display），并允许请求新的链路以使用不同的出口节点。

# CAVEATS

需要匿名的活动不要同时使用 Tor Browser 和其他浏览器，否则可能危害隐私。下载文件或启用插件可能暴露你的真实 IP 地址。由于流量要经过多个中继路由，其性能比普通浏览器慢。该浏览器的设计目标是匿名性，而不仅仅是隐私。

# HISTORY

**Tor Browser** 由 **The Tor Project** 于 **2008 年**首次发布，最初是 Firefox 与 Tor 的组合包。它由 Torbutton 等早期工具演变而来，成为官方推荐的 Tor 匿名上网方式。该项目仍在积极开发中，定期发布安全更新并跟进 Firefox ESR 版本。

# INSTALL

```nix: nix profile install nixpkgs#tor-browser```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tor](/man/tor)(1), [torbrowser-launcher](/man/torbrowser-launcher)(1), [torify](/man/torify)(1), [firefox](/man/firefox)(1)
