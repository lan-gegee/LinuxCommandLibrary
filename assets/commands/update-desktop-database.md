# TAGLINE

为桌面应用构建 MIME 类型缓存

# TLDR

为默认目录**更新 MIME 类型缓存**

```sudo update-desktop-database```

**为特定目录更新缓存**

```update-desktop-database [path/to/applications]```

**以安静模式更新**（抑制输出）

```update-desktop-database -q```

**以详细输出更新**

```update-desktop-database -v```

**安装新的 .desktop 文件后更新**

```sudo update-desktop-database /usr/share/applications```

# SYNOPSIS

**update-desktop-database** [**-q**|**--quiet**] [**-v**|**--verbose**] [_DIRECTORY_...]

# PARAMETERS

**-q**, **--quiet**
> 不显示任何处理与更新进度信息。

**-v**, **--verbose**
> 显示处理与更新进度的详细信息。

**-h**, **--help**
> 显示帮助信息并退出。

# DESCRIPTION

**update-desktop-database** 为 desktop 文件所处理的 MIME 类型构建缓存数据库。该缓存保存 MIME 类型与能够处理它们的 desktop 文件（应用程序）之间的映射关系。

借助这个缓存，应用程序可以快速找出有哪些程序能够打开特定 MIME 类型的文件，而无需逐一解析系统上的每个 .desktop 文件。缓存存储在每个 applications 目录下的 mimeinfo.cache 文件中。

如果未指定目录，该命令会处理标准 XDG 数据目录（$XDG_DATA_DIRS/applications）中的 desktop 文件，通常是 /usr/share/applications 和 /usr/local/share/applications。

安装、删除或修改 .desktop 文件之后都应运行此命令，以保证 MIME 类型关联处于最新状态。软件包管理器通常会在安装软件的过程中自动执行它。

# CAVEATS

desktop 文件中无效的 MIME 类型会被静默忽略。该缓存只决定哪些应用程序可以处理某种 MIME 类型；首选应用程序的顺序由 xdg-mime 或桌面环境设置等外部机制控制。在没有系统目录所需权限的情况下运行会失败。

# HISTORY

**update-desktop-database** 属于 **freedesktop.org** 项目的 **desktop-file-utils** 软件包。它的开发是为了支持 Desktop Entry 规范——该规范对 Linux 桌面环境中应用程序的描述与启动方式进行了标准化。自 **2000 年代初**起，该工具就一直是 Linux 桌面系统的标准组件。

# INSTALL

```apt: sudo apt install desktop-file-utils```

```dnf: sudo dnf install desktop-file-utils```

```pacman: sudo pacman -S desktop-file-utils```

```apk: sudo apk add desktop-file-utils```

```zypper: sudo zypper install desktop-file-utils```

```brew: brew install desktop-file-utils```

```nix: nix profile install nixpkgs#desktop-file-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[update-mime-database](/man/update-mime-database)(1), [desktop-file-validate](/man/desktop-file-validate)(1), [xdg-mime](/man/xdg-mime)(1), [xdg-open](/man/xdg-open)(1)
