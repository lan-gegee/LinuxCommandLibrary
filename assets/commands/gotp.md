# TAGLINE

命令行 TOTP/MFA 身份验证器

# TLDR

**显示**当前 TOTP 验证码

```gotp show [account-name]```

**添加**新的 TOTP 账户

```gotp add [name] [secret-key]```

**生成**用于设置的二维码

```gotp qr [account-name]```

**列出**所有账户

```gotp list```

# SYNOPSIS

**gotp** [_options_] _command_

# PARAMETERS

**show** _NAME_
> 显示账户当前的 TOTP 验证码

**add** _NAME_ _SECRET_
> 添加新的 TOTP 账户

**remove** _NAME_
> 删除账户

**list**
> 列出所有账户

**qr** _NAME_
> 为账户生成二维码

**export**
> 导出账户（加密）

**import** _FILE_
> 从文件导入账户

**-c, --config** _FILE_
> 配置文件路径

**--clip**
> 将验证码复制到剪贴板

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**gotp** 是一个命令行 TOTP（基于时间的一次性密码）身份验证器。它为账户存储并生成 2FA/MFA 验证码，无需手机或浏览器扩展。

该工具会对存储的密钥进行加密，并能生成二维码以便在手机应用中快速设置。

# SECURITY

密钥使用主密码进行静态加密。支持剪贴板集成以安全复制验证码。完成设置后无需访问网络。

# CAVEATS

系统时钟必须准确才能生成有效验证码。密钥的安全性取决于加密密码的强度。建议保留备份码用于账户恢复。

# HISTORY

**gotp** 是为偏好基于终端的 2FA 管理、或需要在无头（headless）服务器上使用 MFA 的用户而创建的。

# INSTALL

```aur: yay -S gotp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[oathtool](/man/oathtool)(1), [pass](/man/pass)(1), [op](/man/op)(1)
