# TAGLINE

启动 Android Debug Bridge 后台服务器

# TLDR

**启动** adb 服务器

```adb start-server```

以**指定端口**启动服务器

```ANDROID_ADB_SERVER_PORT=[5038] adb start-server```

# SYNOPSIS

**adb start-server**

# DESCRIPTION

**adb start-server** 在 adb 服务器尚未运行时显式启动它。服务器是一个后台进程，负责管理 adb 客户端与已连接 Android 设备之间的通信。

通常，运行任何 adb 命令都会自动启动服务器。当你想在连接设备前确保服务器已在运行，或在脚本中希望显式控制服务器启动时机时，这个命令很有用。

# CAVEATS

服务器通常在端口 5037 上启动。给定端口上同一时间只能运行一个 adb 服务器。如果另一个实例正在运行，此命令不会产生任何效果。若端口被其他进程占用，服务器可能无法启动。

# HISTORY

adb 服务器架构自 **2008** 年 Android SDK 首次发布起就是其组成部分。客户端-服务器模型使多个 adb 客户端能够高效共享设备连接。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-kill-server](/man/adb-kill-server)(1), [adb-devices](/man/adb-devices)(1), [adb-connect](/man/adb-connect)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/packages/modules/adb/)```

```[Documentation](https://developer.android.com/tools/adb)```

<!-- verified: 2026-06-11 -->
