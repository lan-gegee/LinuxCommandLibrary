# TAGLINE

用于渗透测试的浏览器漏洞利用框架

# TLDR

以默认配置**启动 BeEF 服务器**

```beef-xss```

使用自定义配置文件**启动**

```beef-xss -c [/path/to/config.yaml]```

以详细输出**启动**

```beef-xss -v```

**重置 BeEF 数据库并全新启动**

```beef-xss -x```

# SYNOPSIS

**beef-xss** [_options_]

# DESCRIPTION

**beef-xss**（Browser Exploitation Framework）是一款专注于 Web 浏览器漏洞的渗透测试工具。它通过 XSS 或其他注入向量钩住（hook）Web 浏览器，将其作为发动客户端攻击的滩头阵地。

该框架提供一个基于 Web 的控制面板，用于管理被钩住的浏览器、执行 JavaScript 模块以及评估客户端安全状况。它从浏览器内部而非网络边界来考察可利用性。

# PARAMETERS

**-c, --config** _file_
> 使用自定义配置文件

**-x, --resetdb**
> 重置 BeEF 数据库

**-v, --verbose**
> 启用详细输出

**-h, --help**
> 显示帮助消息

# COMPONENTS

**钩子（hook.js）**
> 用于钩住浏览器的 JavaScript 文件；可通过 XSS 或社会工程学注入

**Web 界面**
> 位于 http://127.0.0.1:3000/ui/panel 的控制面板

**RESTful API**
> 对 BeEF 功能的编程式访问接口

**命令模块**
> 浏览器漏洞利用模块（键盘记录、网络钓鱼、网络发现）

# CONFIGURATION

**/etc/beef-xss/config.yaml**
> Kali Linux 安装中的主配置文件。控制网络设置、凭据和已启用的扩展。

**/usr/share/beef-xss/config.yaml**
> 软件包安装中主配置文件的备用位置。

# CAVEATS

使用前必须修改默认凭据。需要 Ruby 及各种依赖。仅可在获得授权的渗透测试项目中使用。必须通过 XSS 或其他方式将 hook.js 注入目标浏览器。网络接口和端口可在 config.yaml 中配置。

# HISTORY

BeEF 由 **Wade Alcorn** 和 BeEF 开发团队创建。自 **2006** 年以来它一直是一个活跃的开源项目，已成为评估基于浏览器攻击向量的 Web 应用渗透测试标准工具。

# INSTALL

```aur: yay -S beef-xss```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[metasploit](/man/metasploit)(1), [burpsuite](/man/burpsuite)(1), [nikto](/man/nikto)(1)
