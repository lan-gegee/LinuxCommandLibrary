# TAGLINE

在 Android 设备上运行远程 shell

# TLDR

在设备上**打开**交互式 shell

```adb shell```

**运行**单条命令

```adb shell [ls /sdcard]```

以 **root** 身份运行命令（如可用）

```adb shell su -c "[command]"```

带详情**列出**文件

```adb shell ls -la [/system/]```

# SYNOPSIS

**adb shell** [_-e escape_] [_-n_] [_-T|-t_] [_-x_] [_command_]

# DESCRIPTION

**adb shell** 提供对已连接 Android 设备的 shell 访问。不带参数时，打开交互式 shell 会话；带参数时，执行指定的命令并返回输出。

该 shell 是一个受限的 Unix 环境，可访问 **am**（activity manager）、**pm**（package manager）、**dumpsys**、**content** 等 Android 专用命令。可用命令取决于设备以及是否具有 root 权限。

# PARAMETERS

**-e** _char_
> 设置转义字符（默认：~）

**-n**
> 不从 stdin 读取

**-T**
> 禁用 PTY 分配

**-t**
> 强制 PTY 分配

**-x**
> 禁用远程退出码

# CAVEATS

Shell 命令以权限受限的 "shell" 用户身份运行。root 访问需要已解锁的引导加载程序或已获取 root 的设备。并非所有标准 Unix 命令都可用。shell 环境可能因 Android 版本和厂商而异。

# HISTORY

**adb shell** 自 **2008** 年 Android SDK 首次发布起就是其组成部分。shell 已从最初简单的 Toolbox 实现演变为现代 Android 版本上功能更完善的 Toybox。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-shell-pm](/man/adb-shell-pm)(1), [adb-shell-pm-list-packages](/man/adb-shell-pm-list-packages)(1), [adb-install](/man/adb-install)(1), [toybox](/man/toybox)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/packages/modules/adb/)```

```[Documentation](https://developer.android.com/tools/adb)```

<!-- verified: 2026-06-11 -->
