# TAGLINE

列出并过滤已安装的 Android 软件包

# TLDR

**列出**所有已安装的软件包

```adb shell pm list packages```

以 **APK 路径**列出

```adb shell pm list packages -f```

只列出**系统**软件包

```adb shell pm list packages -s```

只列出**第三方**软件包

```adb shell pm list packages -3```

列出**已禁用**的软件包

```adb shell pm list packages -d```

列出带**版本号**的软件包

```adb shell pm list packages --show-versioncode```

按名称**过滤**软件包

```adb shell pm list packages [google]```

# SYNOPSIS

**adb shell pm list packages** [_-f_] [_-d_] [_-e_] [_-s_] [_-3_] [_-i_] [_-U_] [_-u_] [_--show-versioncode_] [_--apex-only_] [_--user user_id_] [_filter_]

# DESCRIPTION

**pm list packages** 显示 Android 设备上已安装的应用。输出可以按软件包类型（系统、第三方、已启用、已禁用）过滤，还可选择包含 APK 文件路径。

filter 参数对软件包名做子串匹配，适合查找特定厂商或包含特定组件的软件包。

# PARAMETERS

**-f**
> 显示关联的 APK 文件路径。

**-a**
> 显示所有已知软件包（不含 APEX）。

**-d**
> 只显示已禁用的软件包。

**-e**
> 只显示已启用的软件包。

**-s**
> 只显示系统软件包。

**-3**
> 只显示第三方软件包。

**-i**
> 显示每个软件包的安装来源。

**-U**
> 显示软件包的 UID。

**-u**
> 包含已卸载的软件包。

**--show-versioncode**
> 显示每个软件包的版本号。

**--apex-only**
> 只显示 APEX 软件包。

**--uid** _UID_
> 过滤为只显示具有给定 UID 的软件包。

**--user** _user_id_
> 列出特定用户的软件包。

# CAVEATS

输出格式在 Android 版本之间可能略有差异。系统软件包既包括真正的系统应用，也包括安装在系统分区中的应用。某些软件包可能被隐藏，不会出现在标准列表中。`--show-versioncode` 和 `--apex-only` 等标志需要较新的 Android 版本。

# HISTORY

软件包列表功能自 **2008** 年 Android 1.0 起即可用，后续版本陆续加入过滤选项，以应对日益增多的已安装应用。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb-shell-pm](/man/adb-shell-pm)(1), [adb](/man/adb)(1)
