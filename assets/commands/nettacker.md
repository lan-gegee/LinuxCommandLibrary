# TAGLINE

自动化渗透测试框架

# TLDR

**扫描目标漏洞**

```nettacker -i [target.com]```

**使用指定模块扫描**

```nettacker -i [target] -m [ssh_brute,ftp_brute]```

**从文件读取目标进行扫描**

```nettacker -l [targets.txt]```

**使用全部模块扫描**

```nettacker -i [target] -m all```

**扫描指定端口**

```nettacker -i [target] -p [22,80,443]```

**将结果保存到文件**

```nettacker -i [target] -o [report.html]```

**设置线程数和超时时间**

```nettacker -i [target] -t [10] --timeout [5]```

# SYNOPSIS

**nettacker** [_-i target_] [_-l file_] [_-m modules_] [_-p ports_] [_-o output_] [_options_]

# PARAMETERS

**-i** _TARGET_
> 目标（IP、主机名、CIDR）。

**-l** _FILE_
> 目标列表文件。

**-m** _MODULES_
> 要运行的模块（逗号分隔）。

**-p** _PORTS_
> 要扫描的端口。

**-o** _FILE_
> 输出文件。

**-t** _N_
> 线程数量。

**--timeout** _SEC_
> 超时时间（秒）。

**-u** _USER_
> 用于暴力破解的用户名。

**-U** _FILE_
> 用户名列表文件。

**-P** _FILE_
> 密码列表文件。

**--method** _METHOD_
> 扫描方法。

**--graph** _TYPE_
> 生成图表（d3_tree 等）。

**--api**
> 运行 API 服务器。

# DESCRIPTION

**nettacker** 是一个自动化渗透测试框架。它可以扫描漏洞、执行暴力破解攻击并识别配置错误。

各模块针对特定的漏洞或服务：SSH 暴力破解、FTP 匿名访问、Web 漏洞、子域名枚举等。

该框架支持在自动化工作流中进行网络扫描、服务识别和漏洞利用。结果会被收集并生成报告。

输出格式包括带图表的 HTML 报告、便于处理的 JSON 以及纯文本。D3 图形可视化可展示攻击路径和发现的问题。

API 服务器支持与其他工具和自动化框架集成。Web 界面则提供点击式扫描操作。

该工具专为授权的安全评估与渗透测试设计。

# CAVEATS

仅在获得适当授权的情况下使用。可能触发 IDS/IPS 告警。暴力破解可能导致账户锁定。某些模块具有侵入性。

# HISTORY

**OWASP Nettacker** 是作为 **OWASP**（开放 Web 应用安全项目）的一部分开发的开源渗透测试框架。它为安全专业人员提供自动化的安全扫描能力。

# SEE ALSO

[nmap](/man/nmap)(1), [metasploit](/man/metasploit)(1), [nikto](/man/nikto)(1), [sqlmap](/man/sqlmap)(1)
