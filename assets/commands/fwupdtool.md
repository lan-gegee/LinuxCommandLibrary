# TAGLINE

底层固件操作工具

# TLDR

显示 fwupd 检测到的所有**设备**

```fwupdtool get-devices```

**从文件安装**固件

```fwupdtool install [path/to/firmware]```

显示**帮助**

```fwupdtool -h```

# SYNOPSIS

**fwupdtool** [_command_] [_options_]

# PARAMETERS

**get-devices**
> 列出 fwupd 检测到的所有设备

**install** _FILE_
> 从本地 cabinet（.cab）文件安装固件

**get-details** _FILE_
> 显示固件文件的详细信息

**verify** _DEVICE_
> 校验设备上的固件

**firmware-parse** _FILE_
> 解析并显示固件文件结构

**firmware-convert** _FILE_
> 将固件转换为其他格式

**-h**, **--help**
> 显示帮助信息

**-v**, **--verbose**
> 启用详细输出

# DESCRIPTION

**fwupdtool** 是与 fwupd 配套的底层固件操作工具。与处理 LVFS 自动更新的 **fwupdmgr** 不同，fwupdtool 支持手动固件操作，包括安装本地固件文件、解析固件归档和设备校验。

该工具主要用于调试、开发，以及必须从厂商提供的文件手动安装固件而非通过 LVFS 软件仓库的场景。

# CAVEATS

手动安装固件会绕过 LVFS 签名校验。只应安装来自可信来源的固件。错误的固件可能使设备变砖。日常更新大多数用户应优先使用 **fwupdmgr**。

# HISTORY

fwupdtool 属于 fwupd 项目，由 Richard Hughes 于 **2015 年**创建。它是主工具 fwupdmgr 的开发与调试配套工具。

# INSTALL

```apt: sudo apt install fwupd```

```dnf: sudo dnf install fwupd```

```pacman: sudo pacman -S fwupd```

```apk: sudo apk add fwupd```

```zypper: sudo zypper install fwupd```

```brew: brew install fwupd```

```nix: nix profile install nixpkgs#fwupd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fwupdmgr](/man/fwupdmgr)(1), [efibootmgr](/man/efibootmgr)(8)

# RESOURCES

```[Source code](https://github.com/fwupd/fwupd)```

```[Homepage](https://fwupd.org/)```

<!-- verified: 2026-07-15 -->
