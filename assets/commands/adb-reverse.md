# TAGLINE

设置从设备到主机的反向端口转发

# TLDR

将设备端口**反向转发**到本地端口

```adb reverse tcp:[8080] tcp:[8080]```

**列出**所有反向转发

```adb reverse --list```

**移除**特定的反向转发规则

```adb reverse --remove tcp:[8080]```

移除**所有**反向转发规则

```adb reverse --remove-all```

# SYNOPSIS

**adb reverse** [_--no-rebind_] _remote_ _local_

**adb reverse** --list | --remove _remote_ | --remove-all

# DESCRIPTION

**adb reverse** 建立从 Android 设备到电脑的反向端口转发。这让设备上的应用可以连接开发机上运行的服务，就像它们运行在设备本地一样。

常见用途包括：让 React Native 应用连接 Metro 打包器，或让设备上的应用访问本地开发服务器。

# PARAMETERS

**tcp:**_port_
> TCP 端口号

**localabstract:**_name_
> 抽象命名空间中的 Unix 域套接字

**--no-rebind**
> 若远程端口已被转发则失败

**--list**
> 列出所有活动的反向转发

**--remove** _remote_
> 移除指定的反向转发规则

**--remove-all**
> 移除所有反向转发规则

# CAVEATS

反向转发仅在 Android 5.0 及以上版本可用。该功能要求 adb 服务器维持连接。设备断开或 adb 服务器重启后，反向转发会丢失。

# HISTORY

**adb reverse** 在 Android 5.0 Lollipop（**2014** 年）中加入，用于支持设备应用需要连接开发机服务的开发工作流。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-forward](/man/adb-forward)(1), [adb-shell](/man/adb-shell)(1), [scrcpy](/man/scrcpy)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/packages/modules/adb/)```

```[Documentation](https://developer.android.com/tools/adb)```

<!-- verified: 2026-06-11 -->
