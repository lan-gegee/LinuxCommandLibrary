# TAGLINE

Wine 图形化配置工具

# TLDR

**打开 Wine 配置**

```winecfg```

**配置特定的 Wine 前缀**

```WINEPREFIX=[~/.wine32] winecfg```

**创建并配置新的 32 位 Wine 前缀**

```WINEPREFIX=[~/.wine32] WINEARCH=win32 winecfg```

通过命令行将 **Windows 版本设置为 Windows 10**

```WINEPREFIX=[~/.wine] wine reg add "HKCU\\Software\\Wine" /v Version /d win10```

# SYNOPSIS

**winecfg** [_options_]

# DESCRIPTION

**winecfg** 是 Wine 的图形化配置工具。它无需手动编辑注册表即可调整 Wine 设置，包括 Windows 版本模拟、DLL 覆盖、显示选项和音频配置。

"应用程序"选项卡可为每个应用程序配置不同的 Windows 版本以保证兼容性。"库"选项卡对需要特定 DLL 版本或覆盖的应用程序至关重要。

每个 Wine 前缀都可以有独立的设置。使用 WINEPREFIX 可以为不同应用管理多个相互隔离的 Wine 环境。

# ENVIRONMENT

**WINEPREFIX**
> 包含 Wine 配置的目录。默认为 ~/.wine。

**WINEARCH**
> 新前缀的架构：win32 或 win64。仅在创建新前缀时生效。

**WINEDEBUG**
> 用于排错的调试通道（如 +all、-all、+relay）。

# TABS

**Applications**：按应用程序的设置和 Windows 版本。

**Libraries**：DLL 覆盖设置（原生与内建之间选择）。

**Graphics**：显示设置、虚拟桌面、屏幕分辨率。

**Desktop Integration**：主题和文件夹集成。

**Drives**: 配置虚拟驱动器映射。

**Audio**：声音驱动选择和配置。

**Staging**：Wine Staging 实验性功能（如果可用）。

# CAVEATS

除非设置了针对应用程序的规则，否则更改会影响整个 Wine 前缀。DLL 覆盖若配置不当可能导致应用程序无法运行。某些设置需要重启 Wine 才能生效。WINEARCH 只在首次创建新前缀时有效；它无法更改现有前缀的架构。

# HISTORY

**winecfg** 作为 Wine 的一部分而创建，旨在提供用户友好的配置界面。Wine（Wine Is Not an Emulator）自 1993 年起持续开发，为在类 Unix 系统上运行 Windows 应用程序提供兼容层。

# INSTALL

```dnf: sudo dnf install wine```

```pacman: sudo pacman -S wine```

```apk: sudo apk add wine```

```zypper: sudo zypper install wine```

```nix: nix profile install nixpkgs#wine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wine](/man/wine)(1), [regedit](/man/regedit)(1), [winetricks](/man/winetricks)(1)
