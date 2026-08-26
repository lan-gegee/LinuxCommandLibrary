# TAGLINE

为 Wine 安装 Windows 运行库

# TLDR

在默认 Wine 位置启动**图形化安装**

```winetricks```

指定**自定义 Wine 目录**

```WINEPREFIX=[path/to/wine_directory] winetricks```

安装 Windows **DLL 或组件**

```winetricks [package]```

# SYNOPSIS

**winetricks** [_options_] [_verb_...]

# PARAMETERS

_verb_
> 要安装/配置的软件包、字体或设置

**--gui**
> 启动图形界面

**--force**
> 即使已安装也强制安装

**--unattended**
> 安装过程中不显示提示

**--no-isolate**
> 不在隔离环境中安装

**--verify**
> 完成后验证安装

**list**
> 列出可用的 verb

**list-download**
> 列出可下载的软件包

**apps** / **benchmarks** / **dlls** / **fonts** / **games** / **settings**
> 列出特定类别中的 verb

**WINEPREFIX=**_path_
> 指定 Wine 前缀的环境变量

# DESCRIPTION

**winetricks** 是一个辅助脚本，用于下载和安装在 Wine 下运行 Windows 程序所需的各种可再发行运行库和设置。它可以自动安装 DirectX、Visual C++ 运行库、字体和 .NET Framework 等组件。

该工具既提供图形界面，也支持命令行操作。它可以一次安装多个组件并自动处理依赖关系。每次安装都可以在指定的 Wine 前缀中进行。

# CAVEATS

某些组件即使在无人值守模式下也需要接受许可协议。下载的文件缓存在 ~/.cache/winetricks 中。某些 verb 需要联网才能从 Microsoft 或其他来源下载组件。

# HISTORY

由 **Dan Kegel** 创建，于 **2007 年**作为一个 shell 脚本发布，用于自动化常见的 Wine 配置任务。它已成为 Wine 用户必不可少的配套工具，降低了配置 Windows 应用程序的复杂度。现由 Wine 社区维护。

# INSTALL

```dnf: sudo dnf install winetricks```

```pacman: sudo pacman -S winetricks```

```zypper: sudo zypper install winetricks```

```brew: brew install winetricks```

```nix: nix profile install nixpkgs#winetricks```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wine](/man/wine)(1), [winecfg](/man/winecfg)(1)
