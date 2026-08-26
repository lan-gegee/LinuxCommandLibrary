# TAGLINE

从 Android 设备移除应用

# TLDR

**卸载**应用

```adb uninstall [com.example.app]```

卸载但**保留数据**和缓存

```adb uninstall -k [com.example.app]```

为**特定用户**卸载

```adb uninstall --user [user_id] [com.example.app]```

仅在**版本号匹配时**卸载

```adb uninstall --versionCode [version_code] [com.example.app]```

# SYNOPSIS

**adb uninstall** [_options_] _package_

# DESCRIPTION

**adb uninstall** 从设备中移除已安装的 Android 应用。软件包以其完整的包名（如 com.example.app）指定，而不是 APK 文件名。

默认情况下，卸载会移除应用及其所有数据、缓存和相关文件，并作用于设备上的所有用户。使用 **-k** 标志可保留应用数据。

# PARAMETERS

**-k**
> 移除软件包后保留数据目录和缓存目录。

**--user** _user_id_
> 仅为指定用户移除软件包。默认为所有用户移除。

**--versionCode** _code_
> 仅当已安装应用的版本号与给定的相同时才卸载。

**package**
> 要移除的应用的完整包名。

# CAVEATS

没有 root 权限无法卸载系统应用，除非使用 **adb shell pm uninstall -k --user 0**。包名区分大小写。预装应用可能只能被禁用，而无法彻底移除。

# HISTORY

**adb uninstall** 自 **2008** 年 Android SDK 首次发布起即可用，为开发和测试期间移除应用提供了简单方式。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-install](/man/adb-install)(1), [adb-shell-pm](/man/adb-shell-pm)(1)
