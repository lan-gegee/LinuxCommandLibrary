# TAGLINE

读取或写入 Raspberry Pi OTP 内存中的私钥

# TLDR

**读取 OTP 私钥**

```sudo rpi-otp-private-key```

从二进制文件**写入私钥**（不可逆！）

```sudo rpi-otp-private-key -w [keyfile.bin]```

**指定要读取或写入的 OTP 内存行**

```sudo rpi-otp-private-key -y [56]```

# SYNOPSIS

**rpi-otp-private-key** [**-w** _file_] [**-y** _row_] [**-c**]

# PARAMETERS

**-w** _file_
> 将 _file_ 的内容（必须为 32 字节 / 256 位）写入 OTP 内存。此操作是永久性的。

**-y** _row_
> 覆盖用于存储密钥的默认 OTP 行。

**-c**
> 检查 OTP 密钥是否已被编程写入，但不打印出来。

# DESCRIPTION

**rpi-otp-private-key** 读取或写入存储在 Raspberry Pi SoC 一次性可编程（OTP）内存中由客户控制的 256 位私钥。该密钥用于在 Raspberry Pi 安全启动链中对材料进行签名或解密（有时称为 "Customer OTP"）。

不带任何标志调用时，它会以 64 个字符的十六进制字符串打印当前已写入的密钥（若尚未写入则全为零）。使用 **-w** 时，它会将提供的 32 字节文件烧录进 OTP——这是**永久性且无法撤销的**，即使恢复出厂设置也无法改变。

# CAVEATS

OTP 编程是**不可逆的**：一旦烧录，这些位便无法清除。一次错误的写入可能让安全启动部署永久报废。打印出的私钥应视为敏感信息，绝不外传。必须以 root 身份运行，因为它要通过 VideoCore mailbox 接口（vcgencmd）访问 OTP。

# HISTORY

属于 Raspberry Pi OS 附带的 **rpi-eeprom** 软件包，提供管理 Raspberry Pi 4 及更新型号上 EEPROM 与 OTP 的工具。被随 Raspberry Pi 4 引导 ROM 更新推出的 Raspberry Pi 安全启动基础设施所使用。

# SEE ALSO

[rpi-eeprom-update](/man/rpi-eeprom-update)(1), [vcgencmd](/man/vcgencmd)(1)
