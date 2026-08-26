# TAGLINE

创建和管理 Android 虚拟设备

# TLDR

**列出所有可用的 Android 虚拟设备目标**

```avdmanager list target```

**列出所有可用的设备定义**

```avdmanager list device```

**列出所有已创建的 AVD**

```avdmanager list avd```

**创建新的 AVD**

```avdmanager create avd -n [avd_name] -k "[system_image]" -d "[device_id]"```

**以指定配置创建 AVD**

```avdmanager create avd -n [avd_name] -k "system-images;android-[34];google_apis;x86_64" -d "pixel_6"```

**删除一个 AVD**

```avdmanager delete avd -n [avd_name]```

**移动/重命名一个 AVD**

```avdmanager move avd -n [old_name] -r [new_name]```

# SYNOPSIS

**avdmanager** _command_ [_options_]

# PARAMETERS

**list target**
> 列出可用于创建 AVD 的 Android 目标。

**list device**
> 列出可用的设备定义（手机、平板、电视）。

**list avd**
> 列出所有已创建的 Android 虚拟设备。

**create avd**
> 创建一个新的 Android 虚拟设备。

**delete avd**
> 删除一个已有的 AVD。

**move avd**
> 移动或重命名一个 AVD。

**-n**, **--name** _name_
> AVD 的名称。

**-k**, **--package** _path_
> 系统镜像软件包路径（如 "system-images;android-34;google_apis;x86_64"）。

**-d**, **--device** _id_
> 要使用的设备定义。

**-g**, **--tag** _tag_
> 要使用的系统镜像标签（如 google_apis、default、google_apis_playstore）。

**-b**, **--abi** _abi_
> AVD 要使用的 ABI（如 x86_64、arm64-v8a）。当软件包只有一个 ABI 时会自动选择。

**-c**, **--sdcard** _value_
> 共享 SD 卡镜像的路径，或新 SD 卡的大小（如 512M）。

**-p**, **--path** _directory_
> AVD 文件的自定义存放位置。

**-r**, **--rename** _name_
> 移动 AVD 时使用的新名称（与 **move avd** 配合使用）。

**-f**, **--force**
> 强制创建，覆盖已存在的 AVD。

# DESCRIPTION

**avdmanager** 是 Android SDK 中用于创建和管理 Android 虚拟设备（AVD）的命令行工具。AVD 是一种模拟器配置，为 Android 模拟器实例定义硬件配置文件和系统镜像。

每个 AVD 指定设备类型（手机、平板、电视、穿戴设备）、Android API 级别、系统镜像（含或不含 Google API/Play 商店），以及屏幕尺寸、内存和存储等硬件特性。Android 模拟器使用这些配置来模拟各种 Android 设备。

该工具与用于下载系统镜像的 **sdkmanager** 以及用于运行虚拟设备的 **emulator** 配合工作。AVD 默认存储在 **~/.android/avd/** 目录中。

# CAVEATS

创建 AVD 前需要先通过 sdkmanager 安装对应的系统镜像。强烈建议启用硬件加速（Linux 上是 KVM，macOS/Windows 上是 HAXM）以获得可接受的模拟器性能。不同架构（arm64、x86_64）的 AVD 不能互换使用。

# HISTORY

**avdmanager** 于 Android SDK Tools 25.3 版（2017 年）引入，用于取代 **android** 命令中的 AVD 管理功能。它是 Google 为 Android 开发提供专注、独立命令行工具的努力的一部分。该工具作为 Android SDK command-line tools 软件包的一部分分发。

# SEE ALSO

[sdkmanager](/man/sdkmanager)(1), [emulator](/man/emulator)(1), [adb](/man/adb)(1)

# RESOURCES

```[Documentation](https://developer.android.com/tools/avdmanager)```

<!-- verified: 2026-06-17 -->
