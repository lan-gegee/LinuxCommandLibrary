# TAGLINE

支持本地和虚拟文件系统的 GNOME 文件操作工具

# TLDR

用默认应用**打开**文件

```gio open [path/to/file]```

**列出**目录中的文件

```gio list [path/to/directory]```

显示文件的**信息**

```gio info [path/to/file]```

**复制**文件

```gio copy [path/to/source] [path/to/destination]```

将文件移入**回收站**（可恢复）

```gio trash [path/to/file]```

从 .desktop 文件**启动**应用程序

```gio launch [path/to/file].desktop```

# SYNOPSIS

**gio** _command_ [_arguments_]

# PARAMETERS

**open** _FILE_
> 用默认应用打开文件

**list** _DIR_
> 列出目录内容

**info** _FILE_
> 显示文件的相关信息

**copy** _SRC_ _DEST_
> 复制文件

**move** _SRC_ _DEST_
> 移动文件

**trash** _FILE_
> 将文件移入回收站

**remove** _FILE_
> 永久删除文件

**cat** _FILE_
> 显示文件内容

**launch** _DESKTOP_
> 从 .desktop 文件启动应用程序

**mime** _FILE_
> 获取或设置 MIME 类型的处理程序

**mount** _LOCATION_
> 挂载某个位置

# DESCRIPTION

**gio** 是 GNOME 系统中用于文件操作的 GIO 命令行工具。它为本地文件和虚拟文件系统（GVfs）提供统一接口，包括网络位置、回收站和可移动介质。

与标准 Unix 命令不同，**gio** 与 GNOME 的基础设施深度集成，会遵循桌面关于默认应用、回收站行为和虚拟文件系统挂载的设置。它可以访问 **smb://**、**sftp://**、**mtp://** 和 **trash://** 等位置。

# CAVEATS

需要正确安装 GLib 和 GVfs。某些虚拟文件系统操作要求 gvfsd 守护进程正在运行。对本地文件操作而言，性能可能比原生命令慢。

# HISTORY

gio 随 GLib 2.50（**2016 年**）推出，作为 GIO 操作的统一命令行接口，将各种 gvfs-* 工具整合为一个带子命令的单一工具。

# INSTALL

```apt: sudo apt install libglib2.0-bin```

```dnf: sudo dnf install glib```

```apk: sudo apk add glib```

```brew: brew install glib```

```nix: nix profile install nixpkgs#glib```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-open](/man/xdg-open)(1), [nautilus](/man/nautilus)(1)
