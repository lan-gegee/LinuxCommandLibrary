# TAGLINE

管理 YubiKey FIDO2 凭据

# TLDR

**显示 FIDO 应用信息**

```ykman fido info```

**列出常驻凭据（passkey）**

```ykman fido credentials list```

**删除一个常驻凭据**

```ykman fido credentials delete [id]```

**设置或更改 FIDO PIN**

```ykman fido access change-pin```

**列出已注册的指纹**

```ykman fido fingerprints list```

**重置 FIDO 应用**

```ykman fido reset```

# SYNOPSIS

**ykman** **fido** _command_ [_options_]

# PARAMETERS

**info**
> 显示 FIDO2 应用信息。

**credentials list**
> 列出可发现（常驻）凭据。

**credentials delete** _id_
> 删除一个常驻凭据。

**access change-pin**
> 设置或更改 FIDO PIN。

**access verify-pin**
> 向 YubiKey 验证 FIDO PIN。

**fingerprints list**
> 按 ID 和标签列出已注册的指纹。

**fingerprints add** _name_
> 添加新指纹（需要 YubiKey Bio）。

**fingerprints delete** _id_
> 按 ID 删除指纹。

**fingerprints rename** _id_ _name_
> 设置指纹的标签。

**reset**
> 重置 FIDO 应用，移除所有凭据和 PIN。

# DESCRIPTION

**ykman fido** 管理 YubiKey 上的 FIDO2/WebAuthn 应用。它允许查看和管理 passkey（可发现/常驻凭据），配置 FIDO PIN，以及在 YubiKey Bio 系列设备上管理生物识别指纹。

# CAVEATS

重置会永久移除设备上的所有 FIDO 凭据、PIN 和指纹。指纹命令需要带指纹传感器的 YubiKey，并且必须先设置 FIDO PIN。

# INSTALL

```dnf: sudo dnf install yubikey-manager```

```pacman: sudo pacman -S yubikey-manager```

```apk: sudo apk add yubikey-manager```

```zypper: sudo zypper install yubikey-manager```

```brew: brew install ykman```

```nix: nix profile install nixpkgs#yubikey-manager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ykman](/man/ykman)(1), [ykman-oath](/man/ykman-oath)(1)
