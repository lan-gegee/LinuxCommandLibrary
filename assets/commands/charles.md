# TAGLINE

HTTP 代理与网络流量监视器

# TLDR

**启动 Charles Proxy**

```charles```

**以无头模式启动**（无 GUI）

```charles -headless```

**使用自定义配置文件启动**

```charles -headless -config [config.xml]```

**启用限速后启动**

```charles -throttling```

# SYNOPSIS

**charles** [_options_]

# PARAMETERS

**-config** _file_
> 从指定文件加载配置。

**-headless**
> 无 GUI 运行。通过 http://control.charles/ 的 Web 界面进行控制。

**-throttling**
> 启动时开启带宽限速。

# PROXY CONFIGURATION

默认 HTTP 代理：**localhost:8888**

HTTPS 抓包步骤：
1. 在 Charles 设置中配置 SSL Proxying
2. 在设备上安装 Charles 根证书
3. 在系统/浏览器中信任该证书

iOS/Android：将 WiFi 代理配置指向 Charles 的 IP:8888

# DESCRIPTION

**Charles** 是一款跨平台的 HTTP 代理和监控工具，可让开发者查看本机与互联网之间的 HTTP/HTTPS 流量。它对调试 Web 应用、API 以及移动应用的网络通信尤为有用。

主要功能包括用于解密 HTTPS 流量的 SSL 代理、模拟慢速网络的带宽限速、请求/响应修改、拦截请求的断点以及自动化测试支持。

Charles 以按主机组织的树状视图展示流量，可详细检查头部、Cookie、请求/响应正文和计时信息。会话可以保存以便后续分析或分享。

# CONFIGURATION

**config.xml**
> Charles 配置文件，包含代理设置、SSL 证书和录制选项。通过 -config 标志加载。

# CAVEATS

Charles 是商业软件，试用期结束后需要许可证。HTTPS 抓包需要安装 Charles 的根证书，这存在安全影响。某些采用证书锁定（certificate pinning）的应用可能无法配合 Charles 的 SSL 代理工作。移动设备配置要求能够通过网络访问 Charles 主机。

# HISTORY

Charles Proxy 由 **Karl von Randow** 开发，首发于 **2002 年**。它最初面向 macOS，后来扩展到 Windows 和 Linux。随着移动开发的兴起——浏览器开发者工具已不足以调试原生应用——该工具被移动和 Web 开发者广泛用于调试网络流量。

# INSTALL

```nix: nix profile install nixpkgs#charles```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mitmproxy](/man/mitmproxy)(1), [burpsuite](/man/burpsuite)(1), [wireshark](/man/wireshark)(1)
