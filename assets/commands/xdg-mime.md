# TAGLINE

查询和管理 MIME 类型关联

# TLDR

**显示**文件的 MIME 类型

```xdg-mime query filetype [path/to/file]```

**显示**打开 PNG 的默认应用程序

```xdg-mime query default image/png```

**显示**文件对应 MIME 类型的默认应用程序

```xdg-mime query default $(xdg-mime query filetype [path/to/file])```

为特定 MIME 类型**设置**默认应用程序

```xdg-mime default [imv.desktop] image/png image/jpeg```

# SYNOPSIS

**xdg-mime** _command_ [_arguments_]

# PARAMETERS

**query filetype _file_**
> 显示文件的 MIME 类型

**query default _mimetype_**
> 显示 MIME 类型的默认应用程序

**default _application_ _mimetype_...**
> 为 MIME 类型设置默认应用程序

**install _mimetypes-file_**
> 安装一个 MIME 类型定义

**uninstall _mimetypes-file_**
> 卸载一个 MIME 类型定义

# DESCRIPTION

**xdg-mime** 依据 XDG（freedesktop.org）标准查询和管理 MIME 类型。它可以检测文件类型、查询默认应用程序以及设置应用关联。

该工具与桌面环境的 MIME 类型处理集成，将用户偏好存储在 **~/.config/mimeapps.list** 中。

# CAVEATS

应用程序关联使用 .desktop 文件名。更改可能需要重启应用程序才能生效。适用于符合 XDG 规范的桌面环境。

# INSTALL

```dnf: sudo dnf install xdg-utils```

```pacman: sudo pacman -S xdg-utils```

```apk: sudo apk add xdg-utils```

```zypper: sudo zypper install xdg-utils```

```nix: nix profile install nixpkgs#xdg-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-open](/man/xdg-open)(1), [xdg-settings](/man/xdg-settings)(1), [update-mime-database](/man/update-mime-database)(1)
