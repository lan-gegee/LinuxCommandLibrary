# TAGLINE

从网站内容生成自定义字典的工具

# TLDR

从 URL 创建**字典**，链接深度为 2

```cewl -d 2 -w [path/to/wordlist.txt] [url]```

输出包含**字母和数字**、最少 5 个字符的字典

```cewl --with-numbers -m 5 [url]```

以**详细**模式输出字典并列出**邮箱**地址

```cewl -v -e [url]```

使用 HTTP **认证**

```cewl --auth_type [basic|digest] --auth_user [username] --auth_pass [password] [url]```

输出带**词频统计**的字典

```cewl -c [url]```

使用**代理**

```cewl --proxy_host [host] --proxy_port [port] [url]```

# SYNOPSIS

**cewl** [_options_] _url_

# DESCRIPTION

**cewl**（Custom Word List generator）会爬取网站并根据找到的内容生成字典。该字典可用于密码破解，尤其适合目标组织的密码可能基于公司专有词汇的场景。

该工具按可配置的深度跟踪链接，并提取满足长度要求的去重单词。

# PARAMETERS

**-d**, **--depth** _n_
> 爬取链接至深度 n（默认：2）

**-w**, **--write** _file_
> 将字典写入文件

**-m**, **--min_word_length** _n_
> 最小单词长度（默认：3）

**--with-numbers**
> 包含带数字的单词

**-c**, **--count**
> 显示每个单词出现的次数

**-e**, **--email**
> 包含页面中发现的邮箱地址

**-a**, **--meta**
> 包含页面的元数据

**-u**, **--ua** _AGENT_
> 设置 user agent 字符串

**-v**, **--verbose**
> 启用详细输出

**--auth_type** _type_
> 认证类型：basic 或 digest

**--auth_user** _user_
> 认证用户名

**--auth_pass** _pass_
> 认证密码

**--proxy_host** _host_
> 代理主机

**--proxy_port** _port_
> 代理端口

# CAVEATS

仅可用于你已获得爬取授权的网站。激进的爬取可能触发限流或封禁。大型网站可能生成非常庞大的字典。

# INSTALL

```nix: nix profile install nixpkgs#cewl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[john](/man/john)(1), [hashcat](/man/hashcat)(1), [crunch](/man/crunch)(1)
