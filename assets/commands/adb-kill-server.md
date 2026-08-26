# TAGLINE

终止正在运行的 adb 服务器进程

# TLDR

**停止** adb 服务器

```adb kill-server```

杀死服务器并立即**重启**

```adb kill-server && adb start-server```

# SYNOPSIS

**adb kill-server**

# DESCRIPTION

**adb kill-server** 终止电脑上正在运行的 adb 服务器进程。adb 服务器是一个后台进程，负责管理 adb 客户端与已连接设备之间的通信。

排查连接问题、释放 USB 资源或服务器失去响应时，杀死服务器很有用。之后运行任何 adb 命令时，服务器都会自动重启。

# CAVEATS

服务器被杀死后，所有活动的 adb 连接都会被终止。所有端口转发、反向转发和无线连接都会丢失。之后运行 adb 命令会自动启动新的服务器。

# HISTORY

adb 的客户端-服务器架构自 **2008** 年 Android SDK 首次发布起就是其组成部分。kill-server 命令提供了一种在排查问题时重置服务器的方式。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-start-server](/man/adb-start-server)(1), [adb-devices](/man/adb-devices)(1), [adb-disconnect](/man/adb-disconnect)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/packages/modules/adb/)```

```[Documentation](https://developer.android.com/tools/adb)```

<!-- verified: 2026-06-11 -->
