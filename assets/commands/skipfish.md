# TAGLINE

Web 应用安全扫描器

# TLDR

**以默认设置扫描网站**

```skipfish -o [output_dir] [https://example.com]```

**带身份验证扫描**

```skipfish -o [output_dir] -A [user]:[password] [https://example.com]```

**使用自定义字典扫描**

```skipfish -o [output_dir] -W [wordlist.txt] [https://example.com]```

**限制扫描深度**

```skipfish -o [output_dir] -d [5] [https://example.com]```

**排除匹配模式的 URL**

```skipfish -o [output_dir] -X [/logout] [https://example.com]```

**限制每秒请求数**

```skipfish -o [output_dir] -l [10] [https://example.com]```

**携带 cookie 扫描**

```skipfish -o [output_dir] -C "[session=abc123]" [https://example.com]```

# SYNOPSIS

**skipfish** [_options_] -W _wordlist_ -o _output_dir_ _url_ [_url_...]

# PARAMETERS

**-o** _DIR_
> 报告的输出目录（必需，且必须不存在）

**-W** _FILE_
> 用于基于字典探测的词表文件

**-S** _FILE_
> 加载额外的范围规则

**-A** _USER:PASS_
> HTTP 身份验证凭据

**-C** _NAME=VAL_
> 为所有请求添加自定义 cookie

**-H** _NAME=VAL_
> 添加自定义 HTTP 头

**-b** _i|f|p_
> 浏览器请求头（MSIE、Firefox、iPhone）

**-d** _DEPTH_
> 最大爬取深度（默认：16）

**-c** _NUM_
> 每个节点的最大子节点数（默认：512）

**-r** _NUM_
> 最大总请求数

**-l** _NUM_
> 每秒最大请求数

**-I** _STRING_
> 仅爬取包含指定字符串的 URL

**-X** _STRING_
> 排除包含指定字符串的 URL

**-D** _DOMAIN_
> 将域名加入扫描范围

**-K** _PARAM_
> 跳过对指定参数的模糊测试

**-N**
> 不接受新 cookie

**-M**
> 记录混合内容（HTTPS 中的 HTTP）

**-E**
> 记录缓存不一致

**-U**
> 记录发现的外部 URL

**-Q**
> 在报告中隐藏重复节点

**-u**
> 安静模式；抑制控制台输出

**-v**
> 详细模式

# DESCRIPTION

**skipfish** 是一个高性能的 Web 应用安全扫描器，它通过递归爬取和基于字典的探测构建交互式站点地图。它会执行主动安全检查，并生成突出显示潜在漏洞的 HTML 报告。

该扫描器可检测 XSS、SQL 注入、shell 注入、目录遍历以及各类服务器配置错误等问题。它采用自适应技术尽量减少误报，并能处理带 AJAX 和复杂状态管理的现代 Web 应用。

输出是一份交互式 HTML 报告，其中站点地图展示发现的路径、参数以及识别出的安全问题。每项发现都包含严重程度评级、描述和证据。这份报告可作为人工安全评估的基础。

# CAVEATS

Skipfish 对扫描器和目标服务器都是资源密集型的。扫描前务必获得明确授权。激进的爬取可能触发 DoS 防护或产生大量日志数据。部分动态应用可能无法被完整覆盖。排除模式（**-X**）应包含登出 URL，以免会话被终止。

# HISTORY

Skipfish 由 **Google** 的 **Michal Zalewski**（lcamtuf）开发，于 **2010 年**发布。Zalewski 以 AFL fuzzer 等安全研究而闻名。Skipfish 的设计目标是速度和准确性，采用了优化的 HTTP 处理和智能爬取算法。虽然开发已经放缓，但它仍是 Web 应用侦察和自动化安全测试中的实用工具。

# INSTALL

```aur: yay -S skipfish```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nikto](/man/nikto)(1), [wpscan](/man/wpscan)(1), [sqlmap](/man/sqlmap)(1), [burpsuite](/man/burpsuite)(1)
