# TAGLINE

管理 YubiKey OpenPGP 密钥

# TLDR

**显示 OpenPGP 信息**

```ykman openpgp info```

**设置 PIN**

```ykman openpgp access change-pin```

**设置管理 PIN**

```ykman openpgp access change-admin-pin```

**重置 OpenPGP**

```ykman openpgp reset```

# SYNOPSIS

**ykman** **openpgp** _command_ [_options_]

# PARAMETERS

**info**
> 显示 OpenPGP 信息。

**access** _cmd_
> 管理 PIN 与访问控制。

**certificates** _cmd_
> 管理证书。

**keys** _cmd_
> 管理密钥。

**reset**
> 重置 OpenPGP 应用。

# DESCRIPTION

**ykman openpgp** 用于管理 YubiKey 上的 OpenPGP。可配置 PGP 密钥用于加密、签名和身份验证，提供基于硬件的 GPG 密钥存储。

# CAVEATS

重置操作会永久删除设备上的所有 OpenPGP 密钥。

# INSTALL

```dnf: sudo dnf install yubikey-manager```

```pacman: sudo pacman -S yubikey-manager```

```apk: sudo apk add yubikey-manager```

```zypper: sudo zypper install yubikey-manager```

```brew: brew install ykman```

```nix: nix profile install nixpkgs#yubikey-manager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ykman](/man/ykman)(1), [gpg](/man/gpg)(1)
