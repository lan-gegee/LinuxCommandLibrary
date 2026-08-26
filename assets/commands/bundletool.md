# TAGLINE

操作 Android App Bundle 和 APK

# TLDR

**从 app bundle 构建 APK 集**

```bundletool build-apks --bundle=[app.aab] --output=[app.apks]```

**带签名构建 APK**

```bundletool build-apks --bundle=[app.aab] --output=[app.apks] --ks=[keystore.jks] --ks-key-alias=[alias]```

**将 APK 安装到已连接的设备**

```bundletool install-apks --apks=[app.apks]```

**为特定设备提取 APK**

```bundletool extract-apks --apks=[app.apks] --output-dir=[output] --device-spec=[device.json]```

**获取设备规格**

```bundletool get-device-spec --output=[device.json]```

**验证 app bundle**

```bundletool validate --bundle=[app.aab]```

**打印 bundle 信息**

```bundletool dump manifest --bundle=[app.aab]```

**构建包含所有配置的通用 APK**

```bundletool build-apks --mode=universal --bundle=[app.aab] --output=[app.apks]```

**仅为已连接的设备**构建 APK

```bundletool build-apks --connected-device --bundle=[app.aab] --output=[app.apks]```

**获取 APK 大小估算**

```bundletool get-size total --apks=[app.apks]```

# SYNOPSIS

**bundletool** _command_ [_options_]

# DESCRIPTION

**bundletool** 是用于操作 Android App Bundle 的命令行工具。它可以构建 app bundle、为各种设备配置生成 APK 集合，以及将 APK 安装到已连接的设备上。

Android Studio、Android Gradle 插件和 Google Play 都使用该工具来构建和处理 Android App Bundle。

# COMMANDS

**build-bundle**
> 从模块 zip 文件构建 Android App Bundle

**build-apks**
> 从 app bundle 生成 APK 集合

**extract-apks**
> 为特定设备配置提取 APK

**install-apks**
> 将 APK 安装到已连接的设备

**get-device-spec**
> 将设备规格写入 JSON 文件

**validate**
> 验证 app bundle 的有效性

**dump**
> 以人类可读的形式打印 bundle 信息

**get-size**
> 计算下载大小估算

**version**
> 输出 bundletool 版本

# PARAMETERS

**--bundle** _file_
> Android App Bundle（.aab）的路径

**--output** _file_
> 输出文件路径

**--apks** _file_
> APK 集合归档文件的路径

**--device-spec** _file_
> 设备规格 JSON 文件

**--ks** _file_
> 用于签名的 keystore 路径

**--ks-pass** _pass_
> Keystore 密码（pass:password 或 file:/path）

**--ks-key-alias** _alias_
> Keystore 中的密钥别名

**--key-pass** _pass_
> 密钥密码（pass:password 或 file:/path）

**--connected-device**
> 仅针对当前连接的 Android 设备的配置。

**--device-id** _serial_
> 按 ADB 序列号指定设备。

**--mode** _mode_
> APK 生成模式：_default_、_universal_、_system_、_persistent_、_instant_、_archive_。

**--local-testing**
> 添加用于本地功能模块（动态交付）测试的元数据。

**--overwrite**
> 覆盖已存在的输出文件。

**--aapt2** _path_
> 自定义 AAPT2 二进制文件的路径。

# CAVEATS

需要 Java 运行时环境。安装到设备需要 ADB 和已连接的 Android 设备。签名 APK 需要 keystore 凭据。app bundle 必须符合 Android App Bundle 规范。

# INSTALL

```brew: brew install bundletool```

```nix: nix profile install nixpkgs#bundletool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[adb](/man/adb)(1), [apksigner](/man/apksigner)(1), [zipalign](/man/zipalign)(1)
