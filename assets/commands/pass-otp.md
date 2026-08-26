# TAGLINE

为 pass 扩展 TOTP/HOTP 支持

# TLDR

**生成 OTP 验证码**

```pass otp [path/to/entry]```

**插入 OTP 密钥**

```pass otp insert [path/to/entry]```

**从 URI 插入**

```pass otp insert -u [path/to/entry]```

**向已有条目追加 OTP**

```pass otp append [path/to/entry]```

**显示 OTP URI**

```pass otp uri [path/to/entry]```

**复制 OTP 到剪贴板**

```pass otp -c [path/to/entry]```

**校验 OTP 配置**

```pass otp validate [path/to/entry]```

# SYNOPSIS

**pass otp** [_options_] _command_ [_entry_]

# PARAMETERS

**insert**
> 添加新的 OTP 条目。

**append**
> 向已有条目添加 OTP。

**uri**
> 显示 OTP URI。

**validate**
> 校验配置。

**-c**, **--clip**
> 复制到剪贴板。

**-q**, **--qrcode**
> 显示二维码。

**-u**, **--uri**
> 从 otpauth URI 读取。

**-s**, **--secret**
> 仅提示输入密钥。

# DESCRIPTION

**pass-otp** 为 pass（password-store）扩展了 TOTP/HOTP 支持。它可以生成基于时间的一次性密码。

OTP 密钥与密码一同加密存储。支持标准的 otpauth:// URI 格式。

TOTP 的令牌生成基于当前时间。验证码默认每 30 秒刷新一次。

二维码显示便于备份到认证器应用。URI 可以从其他认证器导入。

剪贴板集成会复制验证码以便粘贴。超时后验证码自动清除。

# CAVEATS

需要安装 pass（password-store）。OTP 密钥应另行备份。时间同步会影响 TOTP 的准确性。

# HISTORY

**pass-otp** 是作为 **zx2c4** 所写 **pass**（password-store）的扩展而创建的。它为这个 Unix 密码管理器带来了双因素认证能力。

# INSTALL

```dnf: sudo dnf install pass-otp```

```pacman: sudo pacman -S pass-otp```

```zypper: sudo zypper install pass-otp```

```brew: brew install pass-otp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [oathtool](/man/oathtool)(1), [gpg](/man/gpg)(1)
