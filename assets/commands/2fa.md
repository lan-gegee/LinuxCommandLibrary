# TAGLINE

命令行双因素认证验证码生成器

# TLDR

为账户**添加新的 TOTP 密钥**

```2fa -add [account_name]```

为指定账户**生成 TOTP 验证码**

```2fa [account_name]```

**列出所有已配置的账户**

```2fa -list```

添加基于计数器的（HOTP）账户

```2fa -add -hotp [account_name]```

添加生成 8 位验证码的账户

```2fa -add -8 [account_name]```

**为所有 TOTP 账户生成验证码**

```2fa```

# SYNOPSIS

**2fa** [**-add** [**-7**|**-8**] [**-hotp**] _name_]

**2fa** [**-list**]

**2fa** [**-clip**] _name_

# PARAMETERS

**-add**
> 以给定名称添加新账户。会提示输入 base32 编码的 TOTP/HOTP 密钥。

**-list**
> 列出所有已配置的账户名。

**-7**
> 添加密钥时，生成 7 位验证码而非默认的 6 位。

**-8**
> 添加密钥时，生成 8 位验证码而非默认的 6 位。

**-hotp**
> 添加密钥时，将其视为基于计数器的 HOTP 密钥，而非基于时间的 TOTP 密钥。

**-clip**
> 将生成的验证码复制到系统剪贴板，而不是打印出来。

# DESCRIPTION

**2fa** 是一个命令行双因素认证工具，可生成与 Google Authenticator 等服务兼容的一次性密码。它同时支持基于时间的（TOTP）和基于计数器的（HOTP）密钥，默认生成 6 位验证码（使用 **-7**/**-8** 可生成 7 或 8 位）。TOTP 验证码每 30 秒刷新一次。

该工具读取 base32 格式的密钥（与网站上设置双因素认证时显示的格式相同）。不带参数运行时，它会显示所有已配置 TOTP 账户的验证码。指定账户名则只获取该账户的验证码。

密钥默认存储在 **~/.2fa** 中。该文件包含敏感的认证信息，应设置合适的权限加以保护。

# CAVEATS

密钥以未加密形式存储在纯文本文件中。请确保存储文件的权限正确（**chmod 600**）。TOTP 验证码要正常工作，系统时钟必须准确；时间漂移会导致认证失败。

# HISTORY

**2fa** 命令由 Russ Cox 开发，作为开源 Go 工具发布。它以极简的 Unix 哲学方式实现 TOTP 生成，专为偏好命令行工具而非手机验证器应用的用户设计。

# INSTALL

```aur: yay -S 2fa```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[oathtool](/man/oathtool)(1), [pass-otp](/man/pass-otp)(1), [gpg](/man/gpg)(1)

# RESOURCES

```[Source code](https://github.com/rsc/2fa)```

<!-- verified: 2026-06-10 -->
