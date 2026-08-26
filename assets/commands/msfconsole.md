# TAGLINE

Metasploit Framework 控制台

# TLDR

**启动 Metasploit 控制台**

```msfconsole```

**执行 resource 脚本**

```msfconsole -r [script.rc]```

**执行单条命令**

```msfconsole -x "[use exploit/multi/handler; run]"```

**安静模式**

```msfconsole -q```

**连接数据库**

```msfconsole -d```

**显示版本**

```msfconsole -v```

# SYNOPSIS

**msfconsole** [_options_]

# PARAMETERS

**-r** _FILE_
> 执行 resource 脚本。

**-x** _CMD_
> 执行命令字符串。

**-q**
> 安静模式，不显示横幅。

**-d**
> 连接数据库。

**-v**
> 显示版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**msfconsole** 是 Metasploit Framework 的控制台。它提供对漏洞利用模块和安全工具的访问。

该工具是 Metasploit 的主要界面，用于渗透测试和安全研究。

# CAVEATS

仅限授权测试。需要正确的环境配置。资源消耗较大。

# HISTORY

msfconsole 是 **Metasploit Framework** 的一部分，后者由 H.D. Moore 于 2003 年创建，用于渗透测试。

# SEE ALSO

[msfvenom](/man/msfvenom)(1), [nmap](/man/nmap)(1), [msfpc](/man/msfpc)(1)
