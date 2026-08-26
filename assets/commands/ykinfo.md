# TAGLINE

显示 YubiKey 设备信息

# TLDR

**显示所有 YubiKey 信息**

```ykinfo -a```

**以十进制显示序列号**

```ykinfo -s```

**以十六进制显示序列号**

```ykinfo -H```

**显示固件版本**

```ykinfo -v```

**检查槽位 1 是否已编程**

```ykinfo -1```

**显示能力（供脚本使用的静默模式）**

```ykinfo -c -q```

# SYNOPSIS

**ykinfo** [_options_]

# PARAMETERS

**-a**
> 显示所有可用信息。

**-s**
> 十进制序列号。

**-m**
> modhex 序列号。

**-H**
> 十六进制序列号。

**-v**
> 固件版本。

**-t**
> 触碰等级。

**-p**
> 编程序列。

**-1**
> 检查槽位 1 是否已编程。

**-2**
> 检查槽位 2 是否已编程。

**-c**
> 能力信息。

**-q**
> 静默模式；输出值时不带标签。

# DESCRIPTION

**ykinfo** 查询已连接的 YubiKey 设备并显示其标识信息。它可以报告硬件令牌的序列号、固件版本和支持的能力。

**-a** 标志一次性显示所有可用信息。单独的标志如 **-s**（序列号）、**-v**（版本）和 **-c**（能力）则显示特定的细节。静默模式（**-q**）输出的值不带标签，便于在脚本中使用。

当连接了多个 YubiKey 时，该工具可以按序列号选择特定设备。它属于 **yubikey-personalization** 软件包，可用于诊断、盘点以及围绕 YubiKey 管理编写脚本。

# CAVEATS

需要通过 USB 连接 YubiKey。属于 **yubikey-personalization** 软件包。yubikey-personalization 项目已进入维护模式；对于较新的 YubiKey，推荐使用 **ykman**。

# HISTORY

**ykinfo** 是 **yubikey-personalization** 的一部分，用于提供已连接 YubiKey 设备的信息。

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

[ykman](/man/ykman)(1), [ykpersonalize](/man/ykpersonalize)(1), [gpg](/man/gpg)(1)
