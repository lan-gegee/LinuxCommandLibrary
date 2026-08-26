# TAGLINE

Android 软件包管理器 shell 接口

# TLDR

**列出**所有已安装的软件包

```adb shell pm list packages```

只列出**系统**软件包

```adb shell pm list packages -s```

只列出**第三方**软件包

```adb shell pm list packages -3```

**卸载**软件包

```adb shell pm uninstall [com.example.app]```

**清除**应用数据和缓存

```adb shell pm clear [com.example.app]```

获取 APK 的**路径**

```adb shell pm path [com.example.app]```

# SYNOPSIS

**adb shell pm** _command_ [_options_]

# DESCRIPTION

**pm**（Package Manager，软件包管理器）是用于管理已安装应用的 Android shell 命令。它提供列出、安装、卸载以及查询设备上软件包信息的功能。

该工具比标准的 adb install/uninstall 命令更强大，提供了管理权限、禁用软件包和查询详细软件包信息的选项。

# PARAMETERS

**list packages** [_-f_] [_-d_] [_-e_] [_-s_] [_-3_] [_-i_] [_-u_] [_filter_]
> 列出软件包（-f：含 APK 路径，-d：已禁用，-e：已启用，-s：系统，-3：第三方，-i：含安装来源，-u：包含已卸载）

**path** _package_
> 打印 APK 的路径

**install** [_-r_] [_-t_] [_-d_] _path_
> 从设备路径安装软件包

**uninstall** [_-k_] _package_
> 移除软件包（-k：保留数据）

**clear** _package_
> 删除与软件包关联的所有数据

**enable** _package_
> 启用被禁用的软件包

**disable** _package_
> 禁用软件包

**grant** _package_ _permission_
> 向软件包授予权限

**revoke** _package_ _permission_
> 撤销软件包的权限

**dump** _package_
> 打印软件包信息

# CAVEATS

部分操作需要 system 或 root 权限。禁用系统软件包可能导致不稳定。软件包名区分大小写。卸载系统应用可能需要 root 权限。

# HISTORY

软件包管理器命令自 **2008** 年 Android 首次发布起就存在，为 PackageManager 系统服务提供命令行访问入口。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-shell](/man/adb-shell)(1), [adb-shell-pm-list-packages](/man/adb-shell-pm-list-packages)(1), [adb-install](/man/adb-install)(1), [adb-uninstall](/man/adb-uninstall)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/packages/modules/adb/)```

```[Documentation](https://developer.android.com/tools/adb)```

<!-- verified: 2026-06-11 -->
