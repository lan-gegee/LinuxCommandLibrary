# TAGLINE

注册 LUKS2 磁盘解锁方式

# TLDR

注册新**密码**

```systemd-cryptenroll --password [/dev/luks_device]```

注册**恢复密钥**

```systemd-cryptenroll --recovery-key [/dev/luks_device]```

列出或注册 **PKCS#11** 令牌

```systemd-cryptenroll --pkcs11-token-uri [list|auto|uri] [/dev/luks_device]```

列出或注册 **FIDO2** 设备

```systemd-cryptenroll --fido2-device [list|auto|/path/to/hidraw] [/dev/luks_device]```

注册支持**生物识别**的 FIDO2

```systemd-cryptenroll --fido2-device auto --fido2-with-user-verification yes [/dev/luks_device]```

注册带 PIN 的 **TPM2**

```systemd-cryptenroll --tpm2-device auto --tpm2-with-pin yes [/dev/luks_device]```

注册绑定特定 PCR 寄存器的 **TPM2**

```systemd-cryptenroll --tpm2-device auto --tpm2-pcrs [7+11] [/dev/luks_device]```

**列出**候选的 LUKS2 块设备

```systemd-cryptenroll --list-devices```

**擦除**已注册的槽位

```systemd-cryptenroll --wipe-slot [empty|password|fido2|pkcs11|tpm2|recovery|all] [/dev/luks_device]```

# SYNOPSIS

**systemd-cryptenroll** [_OPTIONS_] [_DEVICE_]

# PARAMETERS

**--password**
> 注册用于解锁卷的常规口令。

**--recovery-key**
> 注册由计算机生成的高熵恢复密钥。

**--unlock-key-file=** _PATH_
> 使用包含解锁密钥的文件，而不是从 stdin 读取。

**--unlock-fido2-device=** _PATH_
> 使用 FIDO2 设备解锁以注册其他方式。支持 "auto" 自动检测。

**--unlock-tpm2-device=** _PATH_
> 使用 TPM2 设备解锁以注册其他方式。支持 "auto" 自动检测。

**--pkcs11-token-uri=** _list|auto|URI_
> 列出或注册 PKCS#11 安全令牌或智能卡。

**--fido2-device=** _list|auto|PATH_
> 列出或注册支持 hmac-secret 扩展的 FIDO2 安全令牌。

**--fido2-credential-algorithm=** _STRING_
> 凭证生成使用的 COSE 算法。支持："es256"（默认）、"rs256"、"eddsa"。

**--fido2-with-client-pin=** _BOOL_
> 使用 FIDO2 解锁时要求输入 PIN。默认为 "yes"。

**--fido2-with-user-presence=** _BOOL_
> 解锁时要求用户在场（触碰令牌）。默认为 "yes"。

**--fido2-with-user-verification=** _BOOL_
> FIDO2 要求进行生物识别用户验证。默认为 "no"。

**--tpm2-device=** _list|auto|PATH_
> 列出或注册 TPM2 安全芯片。

**--tpm2-pcrs=** _PCR[+PCR...]_
> 将注册绑定到特定的 PCR 寄存器（范围 0-23）。默认为 PCR 7。

**--tpm2-with-pin=** _BOOL_
> TPM2 解锁时要求额外输入 PIN。

**--tpm2-public-key=** _PATH_
> 用于签名 PCR 策略的 PEM 编码 RSA 公钥。

**--tpm2-public-key-pcrs=** _PCR[+PCR...]_
> 签名策略要绑定到的 PCR 寄存器。

**--tpm2-signature=** _PATH_
> 用于验证的 TPM2 PCR 签名文件。

**--wipe-slot=** _SLOT[,SLOT...]_
> 擦除指定的 LUKS2 密钥槽位。接受数字索引或："all"、"empty"、"password"、"recovery"、"pkcs11"、"fido2"、"tpm2"。

**--list-devices**
> 显示包含 LUKS 超级块的候选块设备。

**-h**, **--help**
> 显示帮助文本并退出。

**--version**
> 打印版本信息并退出。

**--no-pager**
> 不将输出送入分页器。

# DESCRIPTION

**systemd-cryptenroll** 管理 LUKS2 加密卷解锁方式的注册。它支持五种类型：密码、恢复密钥、PKCS#11 令牌（YubiKey 等智能卡）、FIDO2 令牌（带 hmac-secret 扩展）以及 TPM2 安全芯片。

该工具将令牌元数据存储在 LUKS2 的 JSON 令牌区，配合 `/etc/crypttab` 或 initramfs 配置即可在启动时自动解锁。

# CAVEATS

仅适用于 LUKS2 卷，不适用于 LUKS1。注册新解锁方式时需要已有一种可用的解锁方式。绑定到特定 PCR 状态的 TPM2 注册可能在固件或引导软件更新后失效。FIDO2 注册需要支持 hmac-secret 扩展的令牌。

# HISTORY

**systemd-cryptenroll** 加入 **systemd** 是为了给现代基于硬件的磁盘加密解锁提供统一接口。它与 **cryptsetup** 互为补充，并集成到 systemd 的启动流程中，为加密根文件系统提供无缝支持。

# INSTALL

```apt: sudo apt install systemd-cryptsetup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cryptsetup](/man/cryptsetup)(8), [systemd-cryptsetup](/man/systemd-cryptsetup)(8)
