# TAGLINE

跨社交网络查找用户名

# TLDR

搜索用户名并将结果**保存到文件**

```sherlock [username] --output [path/to/file]```

搜索**多个用户名**并保存到目录

```sherlock [username1] [username2] --folderoutput [path/to/directory]```

使用 **Tor 网络**搜索

```sherlock --tor [username]```

每个请求使用**独立的 Tor 链路**

```sherlock --unique-tor [username]```

使用**代理**搜索

```sherlock [username] --proxy [proxy_url]```

搜索并在浏览器中**打开结果**

```sherlock [username] --browse```

只搜索**特定网站**

```sherlock [username] --site github --site twitter```

# SYNOPSIS

**sherlock** [_OPTIONS_] _username_ [_username_...]

# PARAMETERS

**--output, -o** _file_
> 将结果保存到指定文件

**--folderoutput, -fo** _directory_
> 将多个用户的搜索结果保存到目录

**--csv**
> 以 CSV 格式输出结果

**--xlsx**
> 以 Excel 格式输出结果

**--site** _site_name_
> 将搜索限制在特定站点（可重复使用）

**--tor, -t**
> 通过 Tor 网络路由请求

**--unique-tor, -u**
> 每个请求使用新的 Tor 链路

**--proxy, -p** _url_
> 通过指定代理路由（例如 socks5://127.0.0.1:1080）

**--timeout** _seconds_
> 请求超时时间，单位秒（默认：60）

**--print-all**
> 显示所有结果，包括未找到该用户名的站点

**--print-found**
> 只显示找到该用户名的站点

**--browse, -b**
> 在默认浏览器中打开找到的 URL

**--nsfw**
> 在搜索中包含 NSFW 站点

**--json, -j** _file_
> 从 JSON 文件加载自定义站点数据

**--verbose, -v, -d, --debug**
> 显示额外的调试输出

**--version**
> 显示版本信息

# DESCRIPTION

**Sherlock** 是一款 OSINT（开源情报）工具，可同时在 400 多个社交网络和网站上搜索用户名。它通过查询各平台的用户查找功能，帮助定位网络踪迹和关联账号。

结果会以每个被搜索的用户名命名的文本文件保存。该工具支持多种输出格式，包括用于进一步分析的 CSV 和 Excel。通过 Tor 或代理的网络路由可在搜索过程中提供匿名性。

# CAVEATS

目标站点的速率限制可能导致漏报。某些站点需要身份验证或有地区限制。由于用户名可用并不代表确认身份，结果需要人工核实。过度使用可能触发目标平台的 IP 封禁。Tor 路由会显著增加搜索时间。

# HISTORY

**Sherlock** 由 **Siddharth Dushantha** 创建，最初发布于 **2019 年**。该项目凭借易用性和广泛的站点覆盖，很快在安全与 OSINT 社区流行起来。它以那位著名侦探命名，目前作为 GitHub 上的开源项目维护，社区积极贡献新站点的支持。

# INSTALL

```brew: brew install sherlock```

```nix: nix profile install nixpkgs#sherlock```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tor](/man/tor)(1), [curl](/man/curl)(1), [wget](/man/wget)(1)
