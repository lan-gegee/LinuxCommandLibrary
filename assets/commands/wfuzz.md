# TAGLINE

Web 应用模糊测试工具

# TLDR

**模糊测试 URL 参数**

```wfuzz -c -z file,[wordlist.txt] "[http://target/?param=FUZZ]"```

**模糊测试目录**

```wfuzz -c -z file,[dirs.txt] "[http://target/FUZZ]"```

**POST 数据模糊测试**

```wfuzz -c -z file,[wordlist.txt] -d "user=admin&pass=FUZZ" "[http://target/login]"```

**按响应码过滤**

```wfuzz -c --hc 404 -z file,[wordlist.txt] "[http://target/FUZZ]"```

**按响应大小过滤**

```wfuzz -c --hl 0 -z file,[wordlist.txt] "[http://target/FUZZ]"```

**多个模糊测试点**

```wfuzz -c -z file,[users.txt] -z file,[passwords.txt] "[http://target/?u=FUZ2Z&p=FUZZ]"```

# SYNOPSIS

**wfuzz** [_-c_] [_-z type,data_] [_--hc codes_] [_options_] _url_

# PARAMETERS

**-z** _TYPE,DATA_
> Payload 规范。

**-c**
> 彩色输出。

**--hc** _CODES_
> 隐藏指定响应码。

**--hl** _LINES_
> 按行数隐藏。

**--hw** _WORDS_
> 按单词数隐藏。

**--hh** _CHARS_
> 按字符数隐藏。

**-d** _DATA_
> POST 数据。

**-H** _HEADER_
> HTTP 请求头。

**-t** _N_
> 线程数。

# DESCRIPTION

**wfuzz** 是一款 Web 应用安全测试工具，用于对目录、参数、表单和其他注入点进行暴力发现。它将 URL、请求头或 POST 数据中的 FUZZ 关键字替换为字典或其他 payload 来源中的条目。

可以配合 FUZ2Z、FUZ3Z 标记同时使用多个注入点，实现用户名和密码的组合攻击或多参数模糊测试。通过状态码、行数、单词数或字符数过滤响应，可以隐藏无用的结果，并突出可能指示漏洞的异常。

Payload 来源包括字典文件、数字范围和编码变体。多线程加速测试，彩色输出让结果更易于浏览。该工具常用于经授权的安全评估中的目录枚举、参数发现和身份验证测试。

# CAVEATS

仅用于经授权的测试。可能需要控制请求速率。大型字典运行较慢。

# HISTORY

**wfuzz** 由 **Christian Martorella**（Edge-Security）创建，用于 Web 应用测试。它是渗透测试的标准工具之一。

# INSTALL

```nix: nix profile install nixpkgs#wfuzz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffuf](/man/ffuf)(1), [gobuster](/man/gobuster)(1), [dirb](/man/dirb)(1)
