# TAGLINE

在本地搜索 Exploit Database 归档

# TLDR

**按关键词搜索漏洞利用程序**

```searchsploit [apache] [struts]```

仅在标题中**搜索**

```searchsploit -t [oracle] [windows]```

执行**精确匹配搜索**

```searchsploit -e "[Microsoft IIS 6.0]"```

按 CVE ID **搜索**

```searchsploit --cve [2021-44228]```

将漏洞利用程序**复制**到当前目录

```searchsploit -m [39446]```

**查看/显示**漏洞利用程序内容

```searchsploit -x [39446]```

**显示漏洞利用程序的完整路径并复制到剪贴板**

```searchsploit -p [39446]```

以 JSON 格式**输出结果**

```searchsploit -j [linux kernel] [3.2]```

显示 **Exploit-DB.com URL** 而非本地路径

```searchsploit -w [apache] [remote]```

从结果中**排除**指定词项

```searchsploit [linux kernel] --exclude="(PoC)|/dos/"```

使用 Nmap XML 输出进行**搜索**

```searchsploit --nmap [scan_results.xml]```

**更新数据库**

```searchsploit -u```

# SYNOPSIS

**searchsploit** [_options_] _term1_ [_term2_...] [_termN_]

**searchsploit** --cve _CVE-ID_

**searchsploit** -m _EDB-ID_

# PARAMETERS

**-c**, **--case**
> 区分大小写搜索

**-e**, **--exact**
> 精确匹配搜索

**-s**, **--strict**
> 严格搜索；禁用模糊版本匹配

**-t**, **--title**
> 仅搜索漏洞利用标题（默认：标题和路径）

**--exclude** _TERM_
> 排除包含该词项的结果

**-p**, **--path**
> 显示漏洞利用文件的完整路径

**-m**, **--mirror** _ID_
> 将漏洞利用程序复制到当前目录

**-x**, **--examine** _ID_
> 显示漏洞利用程序内容

**-j**, **--json**
> 以 JSON 格式输出

**-w**, **--www**
> 显示 Exploit-DB.com URL 而非本地路径

**--cve** _ID_
> 按 CVE 标识符搜索

**--id**
> 显示 EDB-ID 而非本地路径

**--nmap** _FILE_
> 使用 Nmap XML 服务版本输出进行搜索

**-o**, **--overflow**
> 允许标题在列中溢出显示

**-v**, **--verbose**
> 显示扩展信息

**--colour**
> 在搜索结果中禁用颜色高亮

**-u**, **--update**
> 更新本地数据库

**-h**, **--help**
> 显示帮助

# DESCRIPTION

**searchsploit** 是一款在本地搜索 Exploit Database（exploit-db.com）归档的命令行工具。它提供对 Offensive Security 维护的数千个公开漏洞利用程序、shellcode、论文和漏洞信息的离线访问。

默认同时搜索漏洞利用标题和文件路径。多个搜索词以 AND 逻辑组合——所有词都必须匹配。使用引号表示精确短语，并用 **--exclude** 排除模式。结果显示漏洞利用标题和本地路径。

找到漏洞利用程序后，使用 **-m** 将其复制到当前目录，或用 **-x** 查看其内容。**--cve** 选项可按 CVE 标识符搜索已知漏洞。数据库需要定期用 **-u** 更新。

# CAVEATS

漏洞利用程序仅用于授权的安全测试。许多漏洞利用程序需要针对特定目标进行修改。使用前应审查并理解代码。部分漏洞利用程序可能已过时或失效。本地数据库必须定期更新才能包含最新的漏洞利用程序。

# HISTORY

SearchSploit 是由 Kali Linux 的缔造者 **Offensive Security** 维护的 **Exploit Database** 项目的一部分。Exploit Database 于 **2004 年**上线，是面向渗透测试人员和安全研究员的公开漏洞利用归档。SearchSploit 提供对该数据库的离线访问，这在隔离网络环境中测试时至关重要。数据库汇集了来自各种来源的漏洞利用程序，并随着社区贡献持续增长。

# SEE ALSO

[msfconsole](/man/msfconsole)(1), [nmap](/man/nmap)(1), [nikto](/man/nikto)(1)
