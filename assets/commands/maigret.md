# TAGLINE

跨社交网络和网站收集用户名相关信息的 OSINT 工具

# TLDR

**跨网站搜索用户名**

```maigret [username]```

**只在指定网站上搜索**

```maigret [username] --site [twitter] --site [github]```

**输出到文件**

```maigret [username] -o [report.txt]```

**生成 HTML 报告**

```maigret [username] --html```

# SYNOPSIS

**maigret** [_options_] _username_

# PARAMETERS

**-o** _file_
> 将结果输出到文件。

**--html**
> 生成 HTML 报告。

**--pdf**
> 生成 PDF 报告。

**--site** _name_
> 只检查指定的网站。

**--timeout** _seconds_
> 请求超时时间。

**--tor**
> 使用 Tor 网络。

**--proxy** _url_
> 使用 HTTP 代理。

**-a**, **--all-sites**
> 检查所有可用网站。

# DESCRIPTION

**maigret** 是一款 OSINT 工具，用于跨社交网络和网站收集与用户名相关的信息。它会搜索数百个平台来查找与某个用户名关联的账号，并生成详细的调查报告。

# CAVEATS

仅限用于获得授权的安全研究和 OSINT 调查。请尊重隐私和适用法律。

# INSTALL

```brew: brew install maigret```

```nix: nix profile install nixpkgs#maigret```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sherlock](/man/sherlock)(1)
