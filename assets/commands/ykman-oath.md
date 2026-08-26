# TAGLINE

管理 YubiKey OATH 账户

# TLDR

**列出 OATH 账户**

```ykman oath accounts list```

**添加 TOTP 账户**

```ykman oath accounts add [name] [secret]```

**生成验证码**

```ykman oath accounts code [name]```

**删除账户**

```ykman oath accounts delete [name]```

# SYNOPSIS

**ykman** **oath** _command_ [_options_]

# PARAMETERS

**accounts** _cmd_
> 管理 OATH 账户。

**info**
> 显示 OATH 信息。

**access** _cmd_
> 管理密码保护。

**reset**
> 重置 OATH 应用。

# DESCRIPTION

**ykman oath** 管理 YubiKey 上的 TOTP/HOTP 账户。将双因素认证机密安全地存储在硬件中，并可生成用于身份验证的一次性密码。

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
