# TAGLINE

安装桌面菜单项

# TLDR

将应用**安装**到菜单

```xdg-desktop-menu install [path/to/file.desktop]```

**不做厂商**检查直接安装

```xdg-desktop-menu install --novendor [path/to/file.desktop]```

从菜单**卸载**

```xdg-desktop-menu uninstall [path/to/file.desktop]```

**强制更新**菜单

```xdg-desktop-menu forceupdate --mode [user|system]```

# SYNOPSIS

**xdg-desktop-menu** _COMMAND_ [_OPTIONS_] [_FILE_]

# PARAMETERS

**install** _FILE_
> 将 desktop 文件安装到菜单系统

**uninstall** _FILE_
> 从菜单系统中移除 desktop 文件

**forceupdate**
> 强制菜单系统更新

**--novendor**
> 禁用厂商前缀检查

**--mode** _MODE_
> 指定 user 或 system 模式

# DESCRIPTION

**xdg-desktop-menu** 安装和卸载符合 FreeDesktop.org Desktop Entry 规范的桌面菜单项。它负责向桌面菜单系统注册应用程序。

该工具是 xdg-utils 软件包的一部分，后者提供标准化的桌面集成实用程序。

# CAVEATS

需要有效的 .desktop 文件。菜单系统必须符合 XDG 规范。更改可能需要注销或刷新菜单后才能显示。

# INSTALL

```dnf: sudo dnf install xdg-utils```

```pacman: sudo pacman -S xdg-utils```

```apk: sudo apk add xdg-utils```

```zypper: sudo zypper install xdg-utils```

```nix: nix profile install nixpkgs#xdg-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-open](/man/xdg-open)(1), [xdg-mime](/man/xdg-mime)(1), [desktop-file-validate](/man/desktop-file-validate)(1)
