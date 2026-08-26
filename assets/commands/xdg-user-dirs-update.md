# TAGLINE

更新 XDG 用户目录配置

# TLDR

将 XDG 的 DESKTOP 目录**更改为**指定目录

```xdg-user-dirs-update --set DESKTOP "/[path/to/directory]"```

**将** DOWNLOAD 目录设置为自定义路径

```xdg-user-dirs-update --set DOWNLOAD "/[path/to/downloads]"```

**将**结果写入 dry-run 文件而不是 user-dirs.dirs

```xdg-user-dirs-update --dummy-output "[path/to/dry_run_file]" --set [xdg_user_directory] "/[path/to/directory]"```

**强制**完全重置用户目录配置

```xdg-user-dirs-update --force```

# SYNOPSIS

**xdg-user-dirs-update** [_OPTION..._] [_--set NAME PATH..._]

# PARAMETERS

**--set** _NAME_ _PATH_
> 设置指定的用户目录。NAME 必须是 DESKTOP、DOWNLOAD、TEMPLATES、PUBLICSHARE、DOCUMENTS、MUSIC、PICTURES 或 VIDEOS 之一。PATH 必须是绝对路径。

**--dummy-output** _PATH_
> 将配置写入 PATH 而不是默认配置文件。使用此选项时不会创建目录。

**--force**
> 强制完全重置现有配置。会重新创建目录而不是重置为 HOME，并且总是重新创建 locale 文件。

**--help**
> 打印帮助信息并退出。

# DESCRIPTION

**xdg-user-dirs-update** 更新用户的 user-dirs.dirs 文件的当前状态。如果之前不存在该文件，则基于系统默认值创建一个。XDG 用户目录是 Desktop、Documents、Downloads、Music、Pictures 和 Videos 等特殊文件夹。

配置存储在 **~/.config/user-dirs.dirs** 中，定义应用程序应在哪里查找用户内容目录。首次运行时还会创建 **user-dirs.locale** 文件，用于记录目录名称翻译所使用的区域设置。

此命令通常在用户会话开始时自动运行。指向不存在位置的目录会被重置为用户的主目录。

# CAVEATS

更改目录不会移动现有内容。应用程序可能需要重启才能识别更改。指定的路径必须是绝对路径。属于 xdg-user-dirs 软件包的一部分。

# INSTALL

```apt: sudo apt install xdg-user-dirs```

```dnf: sudo dnf install xdg-user-dirs```

```pacman: sudo pacman -S xdg-user-dirs```

```apk: sudo apk add xdg-user-dirs```

```zypper: sudo zypper install xdg-user-dirs```

```nix: nix profile install nixpkgs#xdg-user-dirs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-user-dir](/man/xdg-user-dir)(1), [xdg-open](/man/xdg-open)(1), [xdg-mime](/man/xdg-mime)(1), [xdg-settings](/man/xdg-settings)(1)
