# TAGLINE

GNOME 桌面环境的默认文件管理器

# TLDR

**启动** Nautilus 文件管理器

```nautilus```

打开**指定目录**

```nautilus [path/to/directory]```

以 **root 用户**打开

```nautilus admin:/```

打开时**选中某个文件或目录**

```nautilus --select [path/to/file_or_directory]```

在**新窗口**中打开

```nautilus --new-window```

**关闭所有** Nautilus 实例

```nautilus --quit```

# SYNOPSIS

**nautilus** [**--new-window**] [**--select**] [**--quit**] [_URI_...]

# PARAMETERS

**--new-window**
> 打开新窗口，而不是复用现有实例

**--select**
> 在父文件夹中选中所指定的文件或目录

**--quit, -q**
> 关闭所有 Nautilus 实例

**--version**
> 显示版本信息

**--help, -h**
> 显示帮助信息

# URI SCHEMES

**file://**
> 本地文件系统路径

**admin://**
> 以 root 身份浏览文件系统（需要 polkit 认证）

**trash://**
> 查看回收站内容

**recent://**
> 查看最近访问的文件

**sftp://**
> 浏览远程 SSH/SFTP 服务器

**smb://**
> 浏览 Windows/Samba 共享

**ftp://**
> 浏览 FTP 服务器

# DESCRIPTION

**Nautilus**（GNOME Files）是 GNOME 桌面环境的默认文件管理器。它提供图形化的文件浏览、管理和导航，支持本地和远程文件系统。

功能包括标签页浏览、书签、文件预览、搜索以及与 GNOME 服务的集成。admin:// URI 方案允许在通过 polkit 认证后执行特权文件操作。

# CAVEATS

以 admin:// 运行 root 权限操作需要进行 polkit 认证。远程文件系统支持依赖于已安装的 GVFS 后端。某些功能需要 GNOME 桌面集成。

# HISTORY

**Nautilus** 最初由 **Eazel** 于 1999-2001 年开发，名字取自儒勒·凡尔纳《海底两万里》中的潜艇。Eazel 倒闭后，它成为 GNOME 的标准文件管理器，现在官方名称为 GNOME Files。

# INSTALL

```apt: sudo apt install nautilus```

```dnf: sudo dnf install nautilus```

```pacman: sudo pacman -S nautilus```

```apk: sudo apk add nautilus```

```zypper: sudo zypper install nautilus```

```nix: nix profile install nixpkgs#nautilus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolphin](/man/dolphin)(1), [thunar](/man/thunar)(1), [caja](/man/caja)(1), [nemo](/man/nemo)(1)
