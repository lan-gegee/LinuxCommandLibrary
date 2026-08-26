# TAGLINE

智能卡诊断工具

# TLDR

**列出读卡器**

```opensc-tool --list-readers```

**显示卡片信息**

```opensc-tool --info```

**显示 ATR（Answer To Reset）**

```opensc-tool --atr```

**列出卡片上的文件**

```opensc-tool --list-files```

**发送 APDU 命令**

```opensc-tool --send-apdu [00:A4:04:00:00]```

**详细输出**

```opensc-tool -v --info```

# SYNOPSIS

**opensc-tool** [_options_]

# PARAMETERS

**-l**, **--list-readers**
> 列出所有已配置的读卡器。

**-i**, **--info**
> 打印 OpenSC 信息（版本及已启用的组件）。

**-a**, **--atr**
> 以十六进制打印卡片的 Answer To Reset（ATR）。

**-s** _apdu_, **--send-apdu** _apdu_
> 向卡片发送任意 APDU 命令。

**-f**, **--list-files**
> 递归列出卡片上存储的所有文件。

**--list-algorithms**
> 列出卡片支持的算法。

**-r** _reader_, **--reader** _reader_
> 使用特定读卡器（按编号或 ATR）。

**-n**, **--name**
> 打印已插入卡片所用驱动程序的名称。

**--serial**
> 以十六进制打印卡片序列号。

**-D**, **--list-drivers**
> 列出所有已安装的卡片驱动程序。

**-c** _driver_, **--card-driver** _driver_
> 使用指定的卡片驱动程序（输入 '?' 可列出全部）。

**--reset**
> 复位卡片（冷复位或热复位）。

**-G** _section:name:key_, **--get-conf-entry**
> 获取 opensc.conf 配置值。

**-S** _section:name:key:value_, **--set-conf-entry**
> 设置 opensc.conf 配置值。

**-w**, **--wait**
> 等待插入卡片。

**-v**, **--verbose**
> 详细输出（可多次指定以进行调试）。

**--version**
> 显示 OpenSC 软件包版本。

# DESCRIPTION

**opensc-tool** 是一款智能卡诊断工具。它可以查询读卡器、获取卡片信息，并发送原始 APDU 命令用于测试和调试。

属于 OpenSC 项目的一部分，用于在 Unix 系统上提供智能卡支持。

# EXAMPLE

```bash
# Check for card
opensc-tool --list-readers
# Reader 0: Alcor Micro AU9540

# Get card info
opensc-tool --info
# Card type: PIV-II
```

# CAVEATS

需要 PC/SC 守护进程（pcscd）。必须插入卡片。某些命令需要 PIN。

# HISTORY

OpenSC 的创建是为了在 Unix 系统上提供开源的智能卡支持，包括 PKCS#11 和密码学操作。

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

[pkcs11-tool](/man/pkcs11-tool)(1)
