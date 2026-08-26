# TAGLINE

依据规范校验 desktop entry 文件

# TLDR

**校验一个 desktop entry 文件**

```desktop-file-validate [path/to/file.desktop]```

**校验多个文件**

```desktop-file-validate [file1.desktop] [file2.desktop]```

**校验时不发出弃用警告**

```desktop-file-validate --no-warn-deprecated [path/to/file.desktop]```

**校验并对 KDE 特有扩展提出警告**

```desktop-file-validate --warn-kde [path/to/file.desktop]```

**校验一个目录下的所有 desktop 文件**

```desktop-file-validate /usr/share/applications/*.desktop```

# SYNOPSIS

**desktop-file-validate** [**--no-warn-deprecated**] [**--warn-kde**] _FILE_...

# PARAMETERS

**--no-warn-deprecated**
> 不对使用旧版规范中已弃用条目的情况发出警告。

**--warn-kde**
> 对 KDE 特有扩展发出警告，包括 KDE Desktop Entry 组、ServiceTypes、DocPath、Keywords、InitialPreference 键，以及 Service/ServiceType/FSDevice 类型。

# DESCRIPTION

**desktop-file-validate** 依据 freedesktop.org 的 Desktop Entry Specification 校验 desktop entry 文件（.desktop 文件）。Desktop entry 文件为应用启动器和菜单提供应用名称、图标、描述和分类等信息。

校验内容包括必需键是否齐全、值的类型是否正确、转义是否恰当、分类是否有效，以及可能导致显示异常或行为不当的常见错误。该工具常用于打包流程和构建系统，确保 desktop entry 符合规范要求。

如果所有文件均有效且没有错误或严格警告，命令返回退出状态 0；非零退出状态（通常为 1）表示校验失败。

# CAVEATS

该工具依据 freedesktop.org 规范进行校验，可能与特定桌面环境的要求不同。某些桌面环境接受的非标准扩展会被此工具标记为警告。若目标是跨桌面兼容性，可使用 --warn-kde 选项识别 KDE 特有扩展。

# HISTORY

desktop-file-validate 是由 freedesktop.org 维护的 **desktop-file-utils** 软件包的一部分。Desktop Entry Specification 的制定目的是为各 Linux 桌面环境提供统一的应用元数据格式。该规范历经多个版本演进，desktop-file-validate 也随之更新，并对过时的键给出弃用警告。

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

[update-desktop-database](/man/update-desktop-database)(1), [xdg-desktop-menu](/man/xdg-desktop-menu)(1)
