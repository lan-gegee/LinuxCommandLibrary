# TAGLINE

Web 目录暴力破解扫描器

# TLDR

**使用默认词典扫描 Web 服务器**

```dirb [https://example.org]```

**使用自定义词典扫描**

```dirb [https://example.org] [path/to/wordlist.txt]```

**非递归扫描**

```dirb [https://example.org] -r```

**带认证扫描**

```dirb [https://example.org] -u [admin:password]```

**指定文件扩展名扫描**

```dirb [https://example.org] -X [.php,.html,.txt]```

**将结果保存到文件**

```dirb [https://example.org] -o [results.txt]```

# SYNOPSIS

**dirb** _url_ [_wordlist_file_] [_options_]

# DESCRIPTION

**dirb** 是一个 Web 内容扫描器，它通过对 Web 服务器发起基于词典的攻击并分析响应，来发现存在以及隐藏的 Web 对象。

它常用于渗透测试中查找未被链接的内容、备份文件、配置文件和管理界面。DIRB 自带多个内置词典，位于 `/usr/share/dirb/wordlists/`。

# PARAMETERS

**-a** _agent_
> 自定义 User-Agent 字符串。

**-b**
> 不压缩或合并给定 URL 中的 /../ 或 /./ 序列。

**-c** _cookie_
> 为 HTTP 请求设置 cookie。

**-E** _certfile_
> 使用指定的客户端证书文件。

**-f**
> 微调 NOT_FOUND（404）检测。

**-H** _header_
> 向 HTTP 请求添加自定义头部。

**-i**
> 使用不区分大小写的搜索。

**-l**
> 找到时打印 "Location" 头部。

**-N** _code_
> 忽略具有此 HTTP 状态码的响应。

**-o** _file_
> 将输出保存到磁盘。

**-p** _proxy_[_:port_]
> 使用此代理（默认端口：1080）。

**-P** _user:pass_
> 代理认证。

**-r**
> 不递归搜索。

**-R**
> 交互式递归（询问要扫描哪些目录）。

**-S**
> 静默模式（不显示已测试的词）。

**-t**
> 不强制在 URL 末尾加 '/'。

**-u** _user:pass_
> HTTP 认证的用户名和密码。

**-v**
> 同时显示不存在的页面。

**-w**
> 遇到 WARNING 消息时不停止。

**-x** _extfile_
> 用此文件中的扩展名扩展搜索。

**-X** _extensions_
> 用这些扩展名扩展搜索（例如 ".php,.html"）。

**-z** _ms_
> 在请求之间添加毫秒级延迟。

# CAVEATS

仅可用于获得授权的目标。未经授权的扫描可能违法。使用 `-z` 进行限速，以避免被检测或造成拒绝服务。默认词典可能无法覆盖所有情况；自定义词典能改善结果。

# HISTORY

**dirb** 由 The Dark Raver 编写，一直是 Kali Linux 安全发行版的组成部分。它是最早的一批 Web 内容暴力破解工具之一，早于 gobuster 和 feroxbuster 等现代替代品。

# INSTALL

```apt: sudo apt install dirb```

```nix: nix profile install nixpkgs#dirb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gobuster](/man/gobuster)(1), [nikto](/man/nikto)(1), [dirbuster](/man/dirbuster)(1), [nmap](/man/nmap)(1), [curl](/man/curl)(1)
