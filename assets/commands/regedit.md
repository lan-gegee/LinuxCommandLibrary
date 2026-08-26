# TAGLINE

通过 Wine 使用的 Windows 注册表编辑器

# TLDR

**打开图形化注册表编辑器**

```regedit```

**导入注册表文件**

```regedit [file.reg]```

**静默导入注册表文件**（无确认对话框）

```regedit /S [file.reg]```

**将注册表键导出**到文件

```regedit /E [output.reg] [HKEY_CURRENT_USER\Software\App]```

**删除注册表键**（Wine 特有）

```regedit /D [HKEY_CURRENT_USER\Software\App]```

# SYNOPSIS

**regedit** [_/S_] [_file.reg_]
**regedit** **/E** _file_ _key_
**regedit** **/D** _key_

# PARAMETERS

**/E** _FILE_ _KEY_
> 将指定的注册表键及其所有子键导出为 .reg 文件。

**/S**
> 静默模式；导入 .reg 文件时不显示确认对话框。

**/D** _KEY_
> 删除注册表键及其所有子键（Wine 扩展，Windows regedit 中没有）。

**/C** _FILE_
> 根据指定的 .reg 文件创建新注册表（替换整个注册表）。

**/V**
> 以高级模式打开。

# DESCRIPTION

**regedit** 是 Windows 注册表编辑器，在 Linux 上可通过 Wine 兼容层使用。它提供图形界面，用于浏览、搜索和修改分层的 Windows 注册表数据库，其中存储着在 Wine 下运行的 Windows 应用程序的配置设置。

该工具支持以标准 .reg 格式导入和导出注册表文件，从而实现批量配置更改和注册表片段的备份。**/S** 标志允许脚本化的静默导入，而 **/E** 可导出特定的注册表键及其子树。这些操作对于配置依赖注册表设置才能在 Wine 下正常工作的 Windows 应用程序至关重要。

在 Linux 上，regedit 管理的是存储在用户 Wine 前缀目录（通常为 **~/.wine**）中的 Wine 模拟注册表。注册表被拆分为多个文件：**system.reg**（HKEY_LOCAL_MACHINE）、**user.reg**（HKEY_CURRENT_USER）和 **userdef.reg**（HKEY_USERS\\.Default）。通过 regedit 所做的更改会影响 Windows 应用程序在 Wine 环境中的行为。

# CAVEATS

需要 Linux 上已安装 Wine。图形界面需要显示服务器（X11 或经 XWayland 的 Wayland）。用于删除键的 **/D** 标志是 Windows regedit 中不存在的 Wine 扩展。使用 **/C** 时务必极其谨慎，因为它会替换整个注册表。对于脚本化操作，Wine 特有的 **wine reg** 命令可能更合适。

# HISTORY

**regedit** 是微软的注册表编辑器，自 Windows 3.1 起随 Windows 提供。Wine 提供了一个兼容实现，操作 Wine 自己的注册表文件，使得在 Linux 和 macOS 上配置 Windows 应用程序成为可能。

# INSTALL

```dnf: sudo dnf install wine```

```pacman: sudo pacman -S wine```

```apk: sudo apk add wine```

```zypper: sudo zypper install wine```

```nix: nix profile install nixpkgs#wine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wine](/man/wine)(1), [winecfg](/man/winecfg)(1), [winetricks](/man/winetricks)(1)
