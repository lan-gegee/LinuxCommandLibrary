# TAGLINE

配置 YubiKey 设备设置

# TLDR

**显示设备信息**

```ykman config info```

**设置锁码**

```ykman config set-lock-code```

**启用 USB 接口应用**

```ykman config usb --enable [OTP]```

**禁用 NFC 接口应用**

```ykman config nfc --disable [FIDO2]```

# SYNOPSIS

**ykman** **config** _command_ [_options_]

# PARAMETERS

**info**
> 显示配置。

**set-lock-code**
> 设置或更改锁码。

**usb** [_options_]
> 配置通过 USB 启用的应用（OTP、FIDO2、U2F、OATH、PIV、OPENPGP、HSMAUTH）。

**nfc** [_options_]
> 配置通过 NFC 启用的应用。

**--enable** _APP_
> 为所选传输方式启用指定应用。

**--disable** _APP_
> 为所选传输方式禁用指定应用。

**--enable-all**
> 为该传输方式启用所有支持的应用。

**--disable-all**
> 为该传输方式禁用所有应用。

**--lock-code** _HEX_
> 更改受保护设置时提供当前锁码。

**-f**, **--force**
> 不经确认直接应用更改。

# DESCRIPTION

**ykman config** 管理 YubiKey 设备配置。可以启用或禁用应用和接口，并设置锁码以保护配置。

# INSTALL

```dnf: sudo dnf install yubikey-manager```

```pacman: sudo pacman -S yubikey-manager```

```apk: sudo apk add yubikey-manager```

```zypper: sudo zypper install yubikey-manager```

```brew: brew install ykman```

```nix: nix profile install nixpkgs#yubikey-manager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ykman](/man/ykman)(1), [ykman-fido](/man/ykman-fido)(1)
