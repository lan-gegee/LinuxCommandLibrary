# TAGLINE

配置 YubiKey 认证插槽

# TLDR

**显示 YubiKey 状态**

```ykpersonalize -v```

**以 Yubico OTP 编程插槽 1**

```ykpersonalize -1```

**以挑战-应答模式编程插槽 2**

```ykpersonalize -2 -ochal-resp -ochal-hmac```

**在插槽 2 中设置静态密码**

```ykpersonalize -2 -ostatic-ticket```

**设置 CCID 模式**

```sudo ykpersonalize -m 86```

**以指定的 AES 密钥编程**

```ykpersonalize -1 -a[hex_key]```

**设置访问码保护配置**

```ykpersonalize -oaccess=[hex_code]```

# SYNOPSIS

**ykpersonalize** [_options_]

# PARAMETERS

**-1** / **-2**
> 编程插槽 1 或插槽 2。

**-a** _key_
> 设置 AES 密钥（十六进制编码）。

**-c** _code_
> 用于解锁的当前访问码。

**-oaccess=** _code_
> 设置新的访问码。

**-ochal-resp**
> 启用挑战-应答模式。

**-ochal-hmac**
> 挑战-应答使用 HMAC-SHA1。

**-ostatic-ticket**
> 启用静态密码模式。

**-m** _mode_
> 设置 USB 模式（OTP、CCID 等）。

**-v**
> 详细输出。

**-y**
> 自动确认操作。

# DESCRIPTION

**ykpersonalize** 用于配置 Yubico 的 YubiKey 硬件密钥。它可以为两个配置槽位编程多种认证模式，包括 Yubico OTP、HMAC-SHA1 挑战-应答以及静态密码。

每个 YubiKey 有两个插槽：插槽 1 在短触时激活，插槽 2 在长触时激活。两个插槽可以独立配置，用于 OTP 认证和磁盘加密等不同用途。

访问码可以防止配置被未经授权地修改。该工具需要直接通过 USB 访问 YubiKey。

# CAVEATS

编程会覆盖插槽的现有配置。设置访问码后，没有访问码将无法重新配置。某些操作需要 root 权限。较新的功能已由 ykman 取代。

# HISTORY

**ykpersonalize** 由 Yubico 开发，是 yubikey-personalization 软件包的一部分，用于配置 YubiKey 密钥。虽然它仍然可用，但 Yubico 现在对较新的 YubiKey 型号和功能推荐使用 ykman（YubiKey Manager）。

# INSTALL

```apt: sudo apt install yubikey-personalization```

```dnf: sudo dnf install ykpers```

```pacman: sudo pacman -S yubikey-personalization```

```apk: sudo apk add ykpers```

```zypper: sudo zypper install ykpers```

```brew: brew install yubikey-personalization```

```nix: nix profile install nixpkgs#yubikey-personalization```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ykman](/man/ykman)(1), [ykinfo](/man/ykinfo)(1)
