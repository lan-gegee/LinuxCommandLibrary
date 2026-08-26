# TAGLINE

Web 服务器漏洞扫描器

# TLDR

**扫描 Web 服务器**

```nikto -h [http://example.com]```

**扫描指定端口**

```nikto -h [example.com] -p [8080]```

**以 SSL 方式扫描**

```nikto -h [https://example.com]```

**将结果输出到文件**

```nikto -h [example.com] -o [report.html] -Format htm```

**从文件读取多台主机进行扫描**

```nikto -h [hosts.txt]```

**使用指定的扫描类型**（例如 1=有趣的文件，2=错误配置，3=信息泄露）

```nikto -h [example.com] -Tuning [123]```

**通过 HTTP 代理扫描**

```nikto -h [example.com] -useproxy [http://proxy:8080]```

**更新插件和数据库**

```nikto -update```

# SYNOPSIS

**nikto** [_options_]

# PARAMETERS

**-h** _HOST_
> 目标主机、IP 地址或 URL。也可以是包含主机列表的文件。

**-p** _PORT_
> 目标端口。可以用逗号分隔的列表指定多个端口（如 80,443,8080）。

**-ssl**
> 强制在连接上使用 SSL 模式。

**-o** _FILE_
> 扫描报告的输出文件。

**-Format** _TYPE_
> 输出格式：htm、txt、csv、xml、json、nbe 或 sql。

**-Tuning** _TYPE_
> 扫描调优选项，用于控制测试类型。取值：0=文件上传，1=有趣的文件，2=错误配置，3=信息泄露，4=注入（XSS/脚本/HTML），5=远程文件获取（web 根目录内），6=拒绝服务，7=远程文件获取（整个服务器范围），8=命令执行，9=SQL 注入，a=绕过身份验证，b=软件识别，c=远程源包含，x=反向调优（排除指定类型）。

**-useproxy** _PROXY_
> 通过指定的 HTTP 代理建立连接。

**-id** _AUTH_
> 主机身份验证凭据，格式为 id:password 或 id:password:realm。

**-evasion** _TECHNIQUE_
> IDS 规避技术（1-8）。可组合使用多项。

**-timeout** _SECONDS_
> 请求超时时间（默认：10 秒）。

**-Plugins** _PLUGINS_
> 选择要运行的插件（默认：ALL）。可用 -list-plugins 查看可用插件。

**-list-plugins**
> 列出所有可用插件及其说明。

**-maxtime** _SECONDS_
> 每台主机的最长测试时间。

**-nointeractive**
> 禁用交互功能（适合脚本化运行）。

**-update**
> 从 cirt.net 更新扫描插件和数据库。

**-Version**
> 显示 nikto 版本、插件版本和数据库版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nikto** 是一款开源的 Web 服务器漏洞扫描器。它针对 Web 服务器执行全面测试，检查超过 6700 个潜在危险的文件/CGI、过时的服务器软件版本，以及 270 多种服务器的特定版本问题。

该工具会检查服务器配置问题，例如是否存在多个索引文件以及 HTTP 服务器选项等。它还会尝试识别已安装的 Web 服务器和软件。插件更新频繁，并且可以自动获取。

# CAVEATS

仅限授权测试——未经许可扫描服务器可能违法。Nikto 有意不追求隐蔽性；它会产生大量请求，都会被目标服务器记入日志。它是基于 Perl 的工具，依赖 LibWhisker 库。

# HISTORY

Nikto 由 **Chris Sullo** 和 **David Lodge** 创建，是一款面向安全测试的开源 Web 服务器扫描器。目前由 CIRT.net 项目维护。

# INSTALL

```pacman: sudo pacman -S nikto```

```brew: brew install nikto```

```nix: nix profile install nixpkgs#nikto```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [dirb](/man/dirb)(1), [gobuster](/man/gobuster)(1), [curl](/man/curl)(1)
