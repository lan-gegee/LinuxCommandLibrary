# TAGLINE

用于生成一次性密码的 TUI

# TLDR

**启动 OTP 生成器**

```otti```

# SYNOPSIS

**otti** [_options_]

# DESCRIPTION

**otti** 是一个生成一次性密码（OTP）的终端用户界面。它可以直接从终端快速、可靠地生成用于双因素认证的 TOTP 验证码，适合需要在多个平台频繁进行认证的用户。

# CAVEATS

OTP 密钥必须手动配置。准确的 TOTP 生成要求时间同步。

# HISTORY

**otti** 由 **dnaka91** 创建，使用 **Rust** 编写。支持 macOS、Linux、BSD 和 Windows。

# INSTALL

```aur: yay -S otti```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass-otp](/man/pass-otp)(1), [oathtool](/man/oathtool)(1)
