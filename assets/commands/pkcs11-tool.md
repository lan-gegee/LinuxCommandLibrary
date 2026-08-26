# TAGLINE

管理 PKCS#11 加密令牌和智能卡

# TLDR

**列出可用的令牌槽位**

```pkcs11-tool --list-token-slots```

**列出令牌上的对象**

```pkcs11-tool --list-objects```

**列出支持的机制**

```pkcs11-tool --list-mechanisms```

**生成 RSA 密钥对**

```pkcs11-tool --login --keypairgen --key-type rsa:2048 --label [keyname]```

**使用密钥签名数据**

```pkcs11-tool --login --sign -m RSA-PKCS --id [key_id] --input [data] --output [signature]```

**初始化令牌**

```pkcs11-tool --init-token --label [label] --so-pin [so_pin]```

**使用指定的 PKCS#11 库模块**

```pkcs11-tool --module [/usr/lib/libpkcs11.so] --list-objects```

# SYNOPSIS

**pkcs11-tool** [_options_]

# PARAMETERS

**--list-token-slots**
> 列出可用槽位。

**--list-objects**
> 列出令牌上的对象。可用 --label、--id 或 --type 过滤。

**--list-mechanisms**
> 列出令牌支持的机制。

**--keypairgen**
> 在令牌上生成密钥对。

**--sign**
> 签名数据。

**--verify**
> 验证已签名的数据。

**--init-token**
> 初始化令牌。

**--init-pin**
> 初始化用户 PIN（首次设置）。

**--change-pin**
> 更改用户 PIN。

**--login**, **-l**
> 执行操作前先向令牌进行身份验证。

**--pin** _PIN_
> 在命令行上提供 PIN。

**--so-pin** _PIN_
> 提供 Security Officer PIN（用于令牌初始化）。

**--key-type** _spec_
> 密钥类型和长度（例如 rsa:2048、EC:prime256v1）。

**--id** _ID_
> 对象 ID（十六进制）。

**--label** _LABEL_
> 对象标签。

**--slot** _ID_
> 指定要使用的槽位。

**--module** _LIB_
> 要加载的 PKCS#11 库。

**--help**
> 显示帮助。

# DESCRIPTION

**pkcs11-tool** 与 PKCS#11 加密令牌交互，例如智能卡、USB 安全密钥和硬件安全模块（HSM）。它可以列出可用的槽位和对象、生成密钥对、签名和验证数据，以及初始化令牌。

它是 OpenSC 项目的一部分，通过 PKCS#11 库模块与令牌通信。不同的令牌类型需要各自的 PKCS#11 库，用 **--module** 选项指定。对私有对象的操作通常需要 PIN 身份验证。

# CAVEATS

属于 OpenSC 的组成部分。取决于具体的令牌/读卡器。操作需要 PIN。

# HISTORY

pkcs11-tool 是 **OpenSC** 中负责 PKCS#11 令牌管理的部分。

# INSTALL

```apt: sudo apt install opensc```

```dnf: sudo dnf install opensc```

```pacman: sudo pacman -S opensc```

```apk: sudo apk add opensc```

```zypper: sudo zypper install opensc```

```brew: brew install opensc```

```nix: nix profile install nixpkgs#opensc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[p11-kit](/man/p11-kit)(1), [opensc-tool](/man/opensc-tool)(1), [openssl](/man/openssl)(1), [ssh-keygen](/man/ssh-keygen)(1)
