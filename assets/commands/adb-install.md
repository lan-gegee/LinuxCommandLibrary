# TAGLINE

Android 应用安装器

# TLDR

**安装** APK

```adb install [app.apk]```

**重新安装**现有应用并保留其数据

```adb install -r [app.apk]```

允许安装**测试 APK**

```adb install -t [app.apk]```

安装时允许**版本降级**

```adb install -d [app.apk]```

安装时**授予全部权限**

```adb install -g [app.apk]```

# SYNOPSIS

**adb install** [_-rtdgf_] [_options_] _file_

# DESCRIPTION

**adb install** 将 Android 应用软件包（APK）推送到已连接的设备并进行安装。APK 先被复制到设备的临时存储，由软件包管理器安装，然后临时文件会被删除。

该命令提供多种选项控制安装行为，包括替换现有应用、版本降级以及自动授予运行时权限。

# PARAMETERS

**-r**
> 重新安装已有应用并保留其数据

**-t**
> 允许安装测试 APK

**-d**
> 允许版本号降级

**-g**
> 授予清单中列出的所有运行时权限

**-f**
> 将软件包安装到内部系统存储

**-i** _installer_package_name_
> 指定安装来源软件包名称

**--user** _user_id_
> 为特定用户安装软件包（默认：所有用户）

**--install-location** _location_
> 设置安装位置：0（默认）、1（内部存储）、2（外部存储介质）

**--fastdeploy**
> 只更新已安装软件包中发生变化的部分

**--incremental**
> 在后台流式传输 APK；可在完全安装前启动（要求 APK Signature Scheme v4）。追加 **--wait** 可阻塞直至完成，或用 **--no-incremental** 禁用

# CAVEATS

如果 APK 的签名密钥与已安装的应用不同，安装会失败（需先卸载）。某些设备限制安装来自未知来源的应用。降级已安装的版本需要 **-d** 标志。要安装拆分为多个 APK 的应用，请改用 **adb install-multiple**。

# HISTORY

**adb install** 自 **2008** 年 Android SDK 首次发布起即可用。选项随时间不断扩展，以支持拆分 APK、即时应用和 Android App Bundle。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-uninstall](/man/adb-uninstall)(1), [adb-shell-pm](/man/adb-shell-pm)(1), [aapt](/man/aapt)(1), [apksigner](/man/apksigner)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/packages/modules/adb/)```

```[Documentation](https://developer.android.com/tools/adb)```

<!-- verified: 2026-06-11 -->
