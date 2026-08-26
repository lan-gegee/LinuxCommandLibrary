# TAGLINE

清理磁盘空间并保护隐私

# TLDR

启动**图形界面**

```bleachbit --gui```

**粉碎**一个文件

```bleachbit -s path/to/file```

列出**清理器**

```bleachbit -l```

**预览**指定清理器的清理效果

```bleachbit -p [system.cache] [system.tmp]```

**执行**指定清理器的清理

```bleachbit -c [system.cache] [system.tmp]```

**清理所有**在 GUI 中配置的预设项

```bleachbit -c --preset```

**擦除分区上的空闲磁盘空间**

```bleachbit --wipe-free-space [path/to/mount_point]```

# SYNOPSIS

**bleachbit** [_OPTIONS_] [_cleaner.option_...]

# DESCRIPTION

**bleachbit** 通过清理缓存、cookie、临时文件、日志和其他垃圾文件来释放磁盘空间并保护隐私。它通过清理器系统支持数百种应用，可识别并移除各程序特有的不必要文件。

该工具还能安全粉碎单个文件以防止恢复。它同时提供图形界面和命令行模式，便于脚本化或定时清理。

# PARAMETERS

**--gui**
> 启动图形用户界面

**-s, --shred** _file_
> 安全删除文件

**-l, --list-cleaners**
> 列出可用的清理器选项

**-p, --preview**
> 预览将被删除的文件

**-c, --clean**
> 执行清理操作

**--preset**
> 使用图形界面中配置的清理器选项

**-o, --overwrite**
> 覆写文件内容以隐藏其痕迹

**--wipe-free-space** _path_
> 擦除给定路径所在分区的空闲磁盘空间

**--sysinfo**
> 显示系统信息

**--all-but-warning**
> 启用除带警告者之外的所有清理器

**--except** _cleaner.option_
> 将指定的清理器选项排除在操作之外

**--no-uac**
> 不提示 UAC 提权（仅限 Windows）

**--exit**
> 执行操作后退出

**--version**
> 显示版本信息

# CAVEATS

清理前先预览，以免删除重要数据。粉碎文件较慢但比普通删除更安全。某些清理器可能影响应用程序设置。

# HISTORY

**bleachbit** 由 **Andrew Ziem** 创建，于 **2008 年**首次发布。它是一款开源磁盘清理工具，常被拿来与 Windows 上的 CCleaner 比较。它使用 Python 编写，可在 Linux 和 Windows 上运行。

# INSTALL

```dnf: sudo dnf install bleachbit```

```pacman: sudo pacman -S bleachbit```

```zypper: sudo zypper install bleachbit```

```nix: nix profile install nixpkgs#bleachbit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rm](/man/rm)(1), [shred](/man/shred)(1)
