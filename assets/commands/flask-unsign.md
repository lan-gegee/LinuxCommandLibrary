# TAGLINE

Flask 会话 cookie 的操作与破解

# TLDR

**解码 Flask 会话 cookie**

```flask-unsign --decode --cookie "[cookie_value]"```

**暴力破解密钥**

```flask-unsign --unsign --cookie "[cookie]" --wordlist [wordlist.txt]```

**用已知密钥签名 cookie**

```flask-unsign --sign --cookie "{'user':'admin'}" --secret "[key]"```

直接从 URL **获取并解码** cookie

```flask-unsign --decode --server https://[example.com]/```

**不验证签名**直接显示 cookie

```flask-unsign --decode --cookie "[cookie]" --no-verify```

# SYNOPSIS

**flask-unsign** [_options_]

# PARAMETERS

**--decode**
> 解码会话 cookie 并打印其内容。

**--unsign**
> 从已签名的会话 cookie 中暴力破解密钥。

**--sign**
> 用已知的密钥为 cookie 值签名。

**--cookie** _value_
> 要操作的会话 cookie 值。

**--server** _url_
> 自动从给定 URL 获取会话 cookie。

**--secret**, **-S** _key_
> 用于签名或校验 cookie 的密钥。

**--wordlist** _file_
> 用于暴力破解密钥的字典文件。

**--threads** _num_
> 暴力破解期间使用的线程数。

**--no-verify**
> 解码时跳过签名验证。

**--salt** _salt_
> 自定义盐值字符串（默认：`cookie-session`）。

**--legacy**
> 使用较旧的 itsdangerous 签名算法，以兼容旧版 Flask 应用。

**--no-literal-eval**
> 禁用对字典条目的 Python 字面量求值。

# DESCRIPTION

**Flask-unsign** 是一款用于分析和操作 Flask 会话 cookie 的安全测试工具。Flask 将会话数据存储在经过加密签名的 cookie 中，此工具可以解码其内容、通过暴力破解尝试恢复密钥，以及构造自定义的签名 cookie。

该工具主要用于 Web 应用安全评估中测试 Flask 应用是否存在弱密钥问题。如果密钥被恢复，攻击者可以伪造任意会话数据，从而可能导致权限提升或身份验证绕过漏洞。

Flask-unsign 支持多线程暴力破解、自定义字典以及编码和解码两种操作。即使签名验证失败它也能处理会话，便于检查被篡改或已过期的 cookie。

# INSTALL

```nix: nix profile install nixpkgs#flask-unsign```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flask](/man/flask)(1), [hashcat](/man/hashcat)(1), [john](/man/john)(1)
