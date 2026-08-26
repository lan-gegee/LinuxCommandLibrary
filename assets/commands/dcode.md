# TAGLINE

递归检测并解码被编码的字符串

# TLDR

**递归检测并解码**字符串

```dcode "[NjM3YTQyNzQ1YTQ0NGUzMg==]"```

**用已知偏移解码凯撒密码**

```dcode -rot [11] "[spwwz hzcwo]"```

**尝试凯撒密码的全部 26 个偏移**

```dcode -rot all "[bpgkta xh qtiitg iwpc sr]"```

**反转**字符串

```dcode -rev "[hello world]"```

**不使用第三方服务解码**（跳过在线哈希查询）

```dcode -s "[string]"```

# SYNOPSIS

**dcode** [_options_] "_string_"

# PARAMETERS

**-rot** _offset_|**all**
> 用给定偏移解码凯撒密码，或尝试全部 26 个偏移。

**-rev**
> 反转给定的字符串。

**-s**
> 安全模式：不查询第三方 Web 服务做哈希查询。

# DESCRIPTION

**dcode** 是 **Decodify** 提供的命令。Decodify 是一个能检测字符串编码并将其递归解码的工具。如果解码结果本身仍是编码形式，Decodify 会继续解码，直到得到明文。

支持的编码和密码包括 Base64、十六进制、十进制、二进制、URL 编码、FromChar 以及凯撒密码。它还能识别 MD5、SHA1 和 SHA2 哈希，并通过在线哈希查询服务尝试解析。

该工具在 CTF 竞赛和安全分析中很受欢迎——在这些场景下分层编码或未知编码很常见，手动串联 base64、xxd 等工具又十分繁琐。

# CAVEATS

哈希"解码"依赖第三方在线查询服务；处理敏感数据时请使用 -s 保持离线。编码检测是启发式的，可能误判较短或有歧义的字符串。由 Python 编写，需从源码安装（先 git clone，再 make install）。

# HISTORY

Decodify 由安全研究员 Somdev Sangwan（s0md3v）创建，他还开发了 XSStrike 和 Photon 等知名工具。

# SEE ALSO

[base64](/man/base64)(1), [xxd](/man/xxd)(1), [uudecode](/man/uudecode)(1)

# RESOURCES

```[Source code](https://github.com/s0md3v/Decodify)```

<!-- verified: 2026-07-11 -->
