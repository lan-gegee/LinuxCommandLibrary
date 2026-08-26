# TAGLINE

列出 Android 设备上已安装的软件包

# TLDR

**列出**所有软件包

```adb shell pm list packages```

显示软件包的 **APK 路径**

```adb shell pm list packages -f```

只列出**系统应用**

```adb shell pm list packages -s```

只列出**用户安装的应用**

```adb shell pm list packages -3```

**搜索**软件包

```adb shell pm list packages | grep [keyword]```

# SYNOPSIS

**adb shell pm list packages** [_options_] [_filter_]

# DESCRIPTION

**pm list packages** 枚举 Android 设备上已安装的应用。它是软件包管理器 **pm list** 命令组的子命令，专门用于列示应用软件包。

输出格式为 **package:com.example.app**，每行一个软件包。可选的 _filter_ 参数将结果限制为名称包含指定文本的软件包。更复杂的过滤可配合 grep 等工具使用。

# PARAMETERS

**-f**
> 包含 APK 文件路径

**-d**
> 只显示已禁用的软件包

**-e**
> 只显示已启用的软件包

**-s**
> 只显示系统软件包

**-3**
> 只显示第三方（用户安装的）软件包

**-i**
> 显示软件包的安装来源

**-u**
> 包含已卸载但仍有数据的软件包

# CAVEATS

输出格式一致但较为冗长。通过管道传给 **cut -d: -f2** 可以只提取软件包名。在多用户设备上，不同设备用户的结果可能不同。

# HISTORY

自 **2008** 年平台首次发布起就是 Android 软件包管理器的一部分。该命令至今仍是设备管理和调试中最常用的 adb shell 操作之一。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb-shell-pm](/man/adb-shell-pm)(1), [adb-shell-pm-list](/man/adb-shell-pm-list)(1), [adb-shell](/man/adb-shell)(1), [adb](/man/adb)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/packages/modules/adb/)```

```[Documentation](https://developer.android.com/tools/adb)```

<!-- verified: 2026-06-11 -->
