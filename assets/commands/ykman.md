# TAGLINE

YubiKey 设备管理 CLI

# TLDR

**列出 YubiKey 设备**

```ykman list```

**显示设备信息**

```ykman info```

**列出 OATH 账户**

```ykman oath accounts list```

**生成 TOTP 验证码**

```ykman oath accounts code [account_name]```

**添加 OATH 账户**

```ykman oath accounts add -t [name] [secret]```

**重置 FIDO2**

```ykman fido reset```

**设置 FIDO2 PIN**

```ykman fido access change-pin```

**列出 PIV 证书**

```ykman piv certificates list```

# SYNOPSIS

**ykman** [_options_] _command_ [_subcommand_] [_args_]

# PARAMETERS

**list**
> 列出设备。

**info**
> 设备信息。

**oath**
> OATH 命令。

**fido**
> FIDO 命令。

**piv**
> PIV 命令。

**openpgp**
> OpenPGP 命令。

**config**
> 配置。

**-d** _SERIAL_
> 设备序列号。

# DESCRIPTION

**ykman**（YubiKey Manager）是 Yubico 官方的命令行工具，用于管理 YubiKey 硬件安全密钥的各个方面。它提供统一的接口来配置设备上的各种应用并与之交互。

**oath** 子命令管理 TOTP 和 HOTP 账户，将双因素认证密钥保存在硬件中并生成一次性验证码。**fido** 子命令处理用于无密码认证的 FIDO2/WebAuthn 凭据，包括 PIN 管理和驻留密钥存储。**piv** 子命令管理用于智能卡操作的 X.509 证书，**openpgp** 则配置用于签名、加密和 SSH 认证的 PGP 密钥。

**config** 子命令控制设备级设置，例如为特定应用启用或禁用 USB 和 NFC 接口。**info** 和 **list** 命令显示设备详情，包括序列号、固件版本和可用应用。当连接多个 YubiKey 时，可用 **-d** 选项选择特定设备。

# CAVEATS

需要 YubiKey 设备。部分操作具有破坏性，重置前请先备份。

# HISTORY

**ykman**（YubiKey Manager）是 **Yubico** 的官方命令行工具，以统一的管理方式取代了旧版工具。

# INSTALL

```dnf: sudo dnf install yubikey-manager```

```pacman: sudo pacman -S yubikey-manager```

```apk: sudo apk add yubikey-manager```

```zypper: sudo zypper install yubikey-manager```

```brew: brew install ykman```

```nix: nix profile install nixpkgs#yubikey-manager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [ssh-keygen](/man/ssh-keygen)(1)
