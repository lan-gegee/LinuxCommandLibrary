# TAGLINE

FIDO2/WebAuthn 安全密钥管理工具

# TLDR

**列出已连接的令牌**

```fido2-token -L```

**获取令牌信息**

```fido2-token -I [/dev/hidraw0]```

**设置 PIN**

```fido2-token -S [/dev/hidraw0]```

**更改 PIN**

```fido2-token -C [/dev/hidraw0]```

**重置令牌**

```fido2-token -R [/dev/hidraw0]```

**列出驻留凭据**

```fido2-token -L -r [/dev/hidraw0]```

# SYNOPSIS

**fido2-token** [_options_] [_device_]

# PARAMETERS

**-L**
> 列出已连接的令牌。

**-I** _device_
> 获取设备信息。

**-S** _device_
> 设置新 PIN。

**-C** _device_
> 更改现有 PIN。

**-R** _device_
> 重置设备（危险）。

**-r**
> 与 -L 一起使用时，列出驻留凭据。

**-b**
> 与 -L 一起使用时，列出生物识别模板。

**-c**
> Blob（largeBlob）操作。

**-d**
> 调试输出。

# DESCRIPTION

**fido2-token** 管理 FIDO2/WebAuthn 安全密钥。它可以列出、配置和重置 YubiKey、SoloKey 等 FIDO2 认证器硬件令牌。

该工具是 libfido2 的一部分，把通常要通过浏览器 WebAuthn API 才能使用的令牌管理功能带到了命令行上。

# DEVICE PATH

令牌以 HID 设备的形式出现：
- Linux: /dev/hidraw*
- macOS：ioreg 设备路径

# CAVEATS

需要适当的权限（Linux 上需配置 udev 规则）。重置会销毁设备上的所有凭据。PIN 操作失败次数过多可能导致令牌被锁死。并非所有令牌都支持所有功能。

# HISTORY

fido2-token 是 **libfido2** 的一部分，由 **Yubico** 开发，首次发布于 **2019 年**前后。它为 FIDO2 标准提供开源工具支撑，而 FIDO2 是接替 U2F 的强认证标准。

# INSTALL

```apt: sudo apt install fido2-tools```

```dnf: sudo dnf install fido2-tools```

```apk: sudo apk add fido2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ykman](/man/ykman)(1)
