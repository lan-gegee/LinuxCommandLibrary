# TAGLINE

查找 XDG 用户目录路径

# TLDR

显示**主目录**（无参数时的默认行为）

```xdg-user-dir```

显示**下载**目录路径

```xdg-user-dir DOWNLOAD```

显示**文档**目录路径

```xdg-user-dir DOCUMENTS```

显示**桌面**目录路径

```xdg-user-dir DESKTOP```

# SYNOPSIS

**xdg-user-dir** [_DIRECTORY_]

# PARAMETERS

**DESKTOP**
> 桌面目录

**DOWNLOAD**
> 下载目录

**DOCUMENTS**
> 文档目录

**MUSIC**
> 音乐目录

**PICTURES**
> 图片目录

**VIDEOS**
> 视频目录

**TEMPLATES**
> 模板目录

**PUBLICSHARE**
> 公共共享目录

**--help**
> 显示帮助并退出

**--version**
> 显示版本信息并退出

# DESCRIPTION

**xdg-user-dir** 在 user-dirs.dirs 配置文件定义的内容中查找某个 XDG 用户目录的当前路径。这些是存放文档、音乐、下载等常见内容类型的标准目录。

路径配置在 **~/.config/user-dirs.dirs** 中，可按用户自定义。**XDG_CONFIG_HOME** 环境变量决定配置文件的位置。

# CAVEATS

如果请求的目录未配置或给出了未知的目录名，则返回主目录。目录路径在文件系统上可能不存在。

# INSTALL

```apt: sudo apt install xdg-user-dirs```

```dnf: sudo dnf install xdg-user-dirs```

```pacman: sudo pacman -S xdg-user-dirs```

```apk: sudo apk add xdg-user-dirs```

```zypper: sudo zypper install xdg-user-dirs```

```nix: nix profile install nixpkgs#xdg-user-dirs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-user-dirs-update](/man/xdg-user-dirs-update)(1), [xdg-open](/man/xdg-open)(1), [xdg-mime](/man/xdg-mime)(1)
