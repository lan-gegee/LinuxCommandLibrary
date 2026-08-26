# TAGLINE

在 Unix 系统上运行 Windows 应用程序

# TLDR

在 **wine 环境**中运行特定程序

```wine [command]```

在**后台**运行程序

```wine start [command]```

**安装** MSI 软件包

```wine msiexec /i [path/to/package.msi]```

**卸载** MSI 软件包

```wine msiexec /x [path/to/package.msi]```

运行**文件资源管理器**、**记事本**或**写字板**

```wine [explorer|notepad|write]```

运行**注册表编辑器**、**控制面板**或**任务管理器**

```wine [regedit|control|taskmgr]```

运行**配置**工具

```wine winecfg```

# SYNOPSIS

**wine** [_options_] _program_ [_arguments_]

# PARAMETERS

**winecfg**
> 打开 Wine 配置对话框

**regedit**
> 打开 Wine 注册表编辑器

**control**
> 打开 Wine 控制面板

**explorer**
> 打开 Wine 文件资源管理器

**taskmgr**
> 打开 Wine 任务管理器

**msiexec** **/i** _package.msi_
> 安装 MSI 软件包

**msiexec** **/x** _package.msi_
> 卸载 MSI 软件包

**start** _program_
> 在后台（分离）运行程序

**--version**
> 显示 Wine 版本

**WINEPREFIX=**_path_
> 指定 Wine 前缀目录的环境变量

**WINEDEBUG=**_channels_
> 用于调试输出的环境变量

# DESCRIPTION

**wine**（Wine Is Not an Emulator）通过实时将 Windows API 调用转换为 POSIX 调用，在类 Unix 操作系统上运行 Windows 应用程序。它实现了 Windows 运行时环境，不需要 Windows 许可证，也不需要虚拟机。

Wine 会创建隔离的"前缀"（虚拟 C: 盘），其中包含 Windows 目录结构、注册表和已安装的程序。每个前缀都可以通过 winecfg 独立配置不同的 Windows 版本和设置。

# CAVEATS

并非所有 Windows 软件都能运行；请查看 Wine 应用数据库（AppDB）了解兼容性。某些应用程序需要通过 **winetricks** 安装额外的运行库。在 64 位系统上可能需要单独启用 32 位支持。

# HISTORY

开发始于 **1993 年**，由 Bob Amstadt 和 Eric Youngdale 发起，使 Wine 成为持续开发历史最悠久的自由软件项目之一。递归式缩写"Wine Is Not an Emulator"强调 Wine 是重新实现 Windows API，而不是模拟硬件。重要里程碑包括 **2008 年**的 Wine 1.0 和 **2024 年**的 9.0 版本。

# INSTALL

```dnf: sudo dnf install wine```

```pacman: sudo pacman -S wine```

```apk: sudo apk add wine```

```zypper: sudo zypper install wine```

```nix: nix profile install nixpkgs#wine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[winetricks](/man/winetricks)(1), [winecfg](/man/winecfg)(1)
