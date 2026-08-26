# TAGLINE

用于渗透测试的浏览器漏洞利用框架

# TLDR

以默认配置**启动 BeEF** 服务器

```beef-xss```

使用自定义配置文件**启动 BeEF**

```beef-xss -c [path/to/config.yaml]```

在指定接口和端口**启动 BeEF**

```beef-xss -x [interface] -p [port]```

**显示帮助**信息

```beef-xss -h```

**停止 BeEF** 服务

```beef-xss-stop```

# SYNOPSIS

**beef-xss** [**-c** _config_] [**-x** _interface_] [**-p** _port_] [**-v**]

# PARAMETERS

**-c _config_**
> 自定义 YAML 配置文件的路径

**-x _interface_**
> 服务器绑定的网络接口

**-p _port_**
> 监听的端口号（默认：3000）

**-v**
> 启用详细输出

**-h**, **--help**
> 显示帮助和可用选项。首次运行时，若检测到默认凭据，BeEF 会提示设置密码。

# DESCRIPTION

**BeEF**（Browser Exploitation Framework）是一款专注于利用 Web 浏览器漏洞的渗透测试工具。与传统基于网络的工具不同，BeEF 通过向网页注入 JavaScript 钩子来攻击客户端攻击面。

当目标浏览器加载包含 BeEF 钩子脚本的页面时，它会与 BeEF 控制面板建立持久连接。安全专业人员随后可以对被钩住的浏览器执行各种命令模块，测试 XSS、会话劫持和社会工程学攻击等漏洞。

该工具提供一个基于 Web 的 UI，默认位于 **http://127.0.0.1:3000/ui/panel**。钩子脚本由 **http://\<IP\>:3000/hook.js** 提供，必须通过 script 标签嵌入目标页面。

# CONFIGURATION

**/etc/beef-xss/config.yaml**
> Kali Linux 安装中的主配置文件。控制网络设置、凭据和已启用的扩展。

**/usr/share/beef-xss/config.yaml**
> 软件包安装中主配置文件的备用位置。

# CAVEATS

BeEF 仅限**获得授权的渗透测试**使用。未经目标系统所有者明确书面许可而使用它属于违法行为，可能带来严重的法律后果。进行任何浏览器漏洞利用测试之前，请务必确保已获正当授权。

# HISTORY

BeEF 由 **Wade Alcorn** 于 **2006** 年创建，最初是一个演示浏览器安全弱点的研究项目。它后来成为开源项目并在安全社区流行开来。如今该工具由社区贡献者维护，并收录于 **Kali Linux** 等注重安全的 Linux 发行版中。

# INSTALL

```apt: sudo apt install beef```

```aur: yay -S beef```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[bettercap](/man/bettercap)(1), [mitmproxy](/man/mitmproxy)(1), [nikto](/man/nikto)(1), [burpsuite](/man/burpsuite)(1)
