# TAGLINE

管理 Solo FIDO2 安全密钥

# TLDR

**连接到设备**

```solo ls```

**更新固件**

```solo update```

**创建 FIDO2 凭据**

```solo key make-credential```

**让设备闪烁提示（闪烁 LED）**

```solo key wink```

**重置设备**

```solo key reset```

**生成随机字节**

```solo key rng```

**显示版本**

```solo version```

# SYNOPSIS

**solo** _command_ [_options_]

# PARAMETERS

**ls**
> 列出设备。

**update**
> 更新固件。

**key**
> 密钥操作。

**version**
> 显示版本。

**wink**
> 闪烁 LED。

**reset**
> 重置设备。

**make-credential**
> 生成一个 FIDO2 凭据。

**rng**
> 输出设备 RNG 的随机字节。

**verify**
> 验证设备是否为正版 Solo 密钥。

# DESCRIPTION

**solo** 是 Solo FIDO2 安全密钥的命令行管理工具。Solo 是开源硬件认证器，用于无密码登录和双因素认证。该工具负责固件更新、凭据管理和设备诊断。

它可以列出已连接的 Solo 设备、更新固件、为特定域名生成 FIDO2 凭据以及测试设备功能。wink 命令会闪烁设备 LED，在连接多个密钥时帮助识别特定的那一把。

Solo 密钥是完全开源的（硬件和固件皆是），允许独立的安全审计。CLI 工具基于 Python，通过 USB HID 与密钥通信。

# CAVEATS

需要 Solo 密钥。需要 USB 连接。基于 Python。

# HISTORY

**solo** 是 **Solo** FIDO2 安全密钥的 CLI 工具，提供开源的硬件身份验证。

# INSTALL

```apk: sudo apk add py3-solo1```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fido2-token](/man/fido2-token)(1), [ykman](/man/ykman)(1), [gpg](/man/gpg)(1)
