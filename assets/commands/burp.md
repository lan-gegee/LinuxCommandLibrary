# TAGLINE

Web 应用安全测试平台

# TLDR

**启动 Burp Suite**

```burpsuite```

**使用指定内存分配启动**

```java -jar -Xmx4g [burpsuite_pro.jar]```

**启动并加载项目文件**

```burpsuite --project-file=[project.burp]```

**以无头模式启动**

```java -jar [burpsuite_pro.jar] --project-file=[project.burp] --unpause-spider-and-scanner```

# SYNOPSIS

**burpsuite** [_options_]

# PARAMETERS

**--project-file** _file_
> 加载已有的项目文件。

**--config-file** _file_
> 从文件加载配置。

**--user-config-file** _file_
> 从文件加载用户配置。

**--unpause-spider-and-scanner**
> 启动时不暂停 Spider 和 Scanner。

**--disable-extensions**
> 启动时不加载扩展。

**--collaborator-server**
> 仅作为 Collaborator 服务器运行。

**--collaborator-config** _file_
> Collaborator 服务器配置。

# PROXY CONFIGURATION

默认代理监听地址：**127.0.0.1:8080**

将浏览器配置为使用：
- HTTP/HTTPS Proxy: 127.0.0.1
- Port: 8080

从此处安装 Burp CA 证书：**http://burp/cert**

# DESCRIPTION

**Burp Suite** 是一个集成的 Web 应用安全测试平台。它充当拦截代理，让安全测试人员能够检查和修改浏览器与目标 Web 应用之间的流量。

核心功能包括：拦截 HTTP/S 流量的 **Proxy**、自动化漏洞检测的 **Scanner**（仅限 Pro）、执行模糊测试等定制化攻击的 **Intruder**、手动操作请求的 **Repeater**，以及分析会话令牌随机性的 **Sequencer**。

该工具支持通过 BApp Store 安装扩展以及自定义 Java/Python 开发。它可以保存完整的项目状态以便日后恢复，并能生成专业的漏洞报告。

# CAVEATS

Burp Suite Community Edition 缺少自动扫描功能。未经授权对系统使用 Burp 属于违法行为。HTTPS 拦截需要安装 Burp 的 CA 证书。大型项目的内存占用可能很高；请分配足够的堆空间。

# HISTORY

Burp Suite 由 **Dafydd Stuttard**（《The Web Application Hacker's Handbook》作者）创建，于 **2003 年**前后首次发布。最初是一组独立的工具，后演变为集成套件。PortSwigger Ltd 成立于 **2004 年**，专门开发和销售 Burp Suite。它已成为 Web 应用渗透测试的行业标准工具。

# INSTALL

```apt: sudo apt install burp```

```brew: brew install burp```

```nix: nix profile install nixpkgs#burp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mitmproxy](/man/mitmproxy)(1), [nikto](/man/nikto)(1), [sqlmap](/man/sqlmap)(1)
