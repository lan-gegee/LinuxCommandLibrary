# TAGLINE

Trezor 硬件钱包命令行界面

# TLDR

列出已连接的 Trezor 设备

```trezorctl list```

获取设备特性与信息

```trezorctl get-features```

获取特定路径下的比特币地址

```trezorctl btc get-address -n "m/84'/0'/0'/0/0"```

用比特币签名消息

```trezorctl btc sign-message -n "m/84'/0'/0'/0/0" "[message]"```

擦除设备（恢复出厂设置）

```trezorctl device wipe```

更新固件

```trezorctl firmware-update```

设置设备标签

```trezorctl device set-label "[My Trezor]"```

更改 PIN

```trezorctl device change-pin```

# SYNOPSIS

**trezorctl** [_options_] _command_ [_subcommand_] [_arguments_]

# PARAMETERS

**list**
> 列出所有已连接的 Trezor 设备。

**get-features**
> 获取设备信息，包括型号、固件版本和设置。

**btc get-address** **-n** _path_
> 获取指定 BIP32 派生路径下的比特币地址。

**btc sign-message** **-n** _path_ _message_
> 使用指定路径的密钥对消息签名。

**btc sign-tx**
> 以交互方式对比特币交易签名。

**device wipe**
> 擦除设备并恢复出厂设置。

**device setup**
> 通过生成助记词初始化新设备。

**device recover**
> 使用已有的助记词恢复设备。

**device change-pin**
> 更改或设置设备 PIN。

**device set-label** _label_
> 为设备设置自定义标签。

**device unlock-bootloader**
> 解锁引导加载程序以进行高级操作。

**firmware-update**
> 将设备固件更新到最新版本。

**set safety-checks** _strict_|_prompt_
> 设置安全检查级别。strict 强制执行完整校验；prompt 允许用户覆盖。

**crypto get-public-key** **-n** _path_
> 获取指定 BIP32 派生路径下的公钥。

**ethereum get-address** **-n** _path_
> 获取指定派生路径下的以太坊地址。

**-v**, **--verbose**
> 启用详细输出。

**--help**
> 显示某个命令的帮助。

# DESCRIPTION

**trezorctl** 是 Trezor 硬件钱包的命令行界面，可对设备配置、加密货币操作和安全设置进行高级控制。它属于 trezorlib Python 软件包，可与 Trezor One、Trezor Model T 和 Trezor Safe 设备通信。

借助该工具，无需使用图形化的 Trezor Suite 应用即可签署交易、派生地址、管理设备设置、更新固件以及执行恢复操作。它支持多种加密货币，包括比特币、以太坊和各种山寨币。

所有敏感操作都需要在设备上进行物理确认，因此即使使用命令行工具也能保持安全。该界面面向需要以脚本方式访问硬件钱包功能的高级用户。

# CAVEATS

需要 Python 3.8 或更高版本以及 libusb。在 Linux 上必须安装 udev 规则才能检测到设备（由 `trezor-common` 软件包提供）。某些操作（如擦除设备）不可逆；操作前请确保已备份助记词。大多数命令要求设备已连接并解锁。可通过 `pip install trezor` 安装。

# HISTORY

**trezorctl** 由 **SatoshiLabs** 开发，是 Trezor Python 工具的一部分；Trezor 是 **2014 年**发布的首款硬件加密货币钱包。命令行界面随设备固件一同演进，陆续增加了对新加密货币和安全特性的支持。该工具在官方 trezor-firmware 仓库中维护。

# INSTALL

```nix: nix profile install nixpkgs#trezorctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [openssl](/man/openssl)(1)
