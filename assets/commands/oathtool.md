# TAGLINE

生成和验证用于双因素认证的一次性密码

# TLDR

**从密钥生成 TOTP 验证码**

```oathtool --totp --base32 [SECRET_KEY]```

**生成 HOTP 验证码**（基于计数器）

```oathtool --hotp --counter [1] --base32 [SECRET_KEY]```

**生成 8 位验证码**

```oathtool --totp --base32 --digits [8] [SECRET_KEY]```

**验证一个 TOTP 验证码**

```oathtool --totp --base32 [SECRET_KEY] [123456]```

**按指定时间点生成验证码**

```oathtool --totp --base32 --now "[2024-01-15 12:00:00 UTC]" [SECRET_KEY]```

**使用 SHA256 算法**

```oathtool --totp=sha256 --base32 [SECRET_KEY]```

**显示详细输出**

```oathtool --totp --base32 -v [SECRET_KEY]```

# SYNOPSIS

**oathtool** [_--totp_[=_alg_]|_--hotp_] [_--base32_] [_--digits num_] [_--counter num_] [_options_] _secret_ [_otp_]

# PARAMETERS

**--totp**[=_ALG_]
> 生成基于时间的 OTP（sha1、sha256、sha512）。

**--hotp**
> 生成基于计数器的 OTP。

**-b**, **--base32**
> 密钥为 base32 编码。

**-d** _NUM_, **--digits** _NUM_
> 验证码位数（默认：6）。

**-c** _NUM_, **--counter** _NUM_
> HOTP 的计数值。

**-s** _SEC_, **--time-step-size** _SEC_
> 时间步长（秒）（默认：30）。

**-S** _TIME_, **--start-time** _TIME_
> TOTP 的起始时间（Unix 时间戳或 ISO 格式）。

**-N** _TIME_, **--now** _TIME_
> 使用指定时间代替当前时间。

**-w** _NUM_, **--window** _NUM_
> 验证窗口。

**-v**, **--verbose**
> 显示详细输出。

# DESCRIPTION

**oathtool** 用于生成和验证双因素认证所需的一次性密码。它同时支持 HOTP（RFC 4226，基于计数器）和 TOTP（RFC 6238，基于时间）算法。

TOTP 是身份验证器应用（Google Authenticator、Authy 等）使用的标准。密钥通常在设置双因素认证时以 base32 字符串形式提供。用该密钥运行 oathtool 会生成与身份验证器应用相同的验证码。

进行验证时，需要同时提供密钥和待校验的验证码。window 选项通过接受相邻时间段的验证码来容忍时钟偏差。

HOTP 使用递增计数器而非时间。每次生成验证码都应递增计数器。这种模式较少见，但对硬件令牌很有用。

不同服务使用不同的参数——有些要求 8 位验证码或 SHA256。verbose 标志可显示计算细节，便于排查配置问题。

# CAVEATS

密钥必须妥善保管——任何拿到密钥的人都能生成验证码。TOTP 要求系统时间准确。没有内建的密钥存储功能——可与密码管理器集成使用。命令历史可能泄露密钥——编写脚本时请使用环境变量或文件。

# HISTORY

**oathtool** 是 **OATH Toolkit** 项目的一部分，实现了开放认证倡议（OATH）标准。它的开发目的是提供开源的 HOTP 和 TOTP 实现。该工具集还包含用于系统认证的 PAM 模块和面向开发者的库。

# INSTALL

```apt: sudo apt install oathtool```

```dnf: sudo dnf install oathtool```

```apk: sudo apk add oath-toolkit-oathtool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass-otp](/man/pass-otp)(1), [2fa](/man/2fa)(1), [gpg](/man/gpg)(1), [openssl](/man/openssl)(1)
