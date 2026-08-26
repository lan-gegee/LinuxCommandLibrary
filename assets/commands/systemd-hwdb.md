# TAGLINE

管理 udev 硬件数据库

# TLDR

**更新**硬件数据库

```systemd-hwdb update```

**查询**数据库中的 modalias

```systemd-hwdb query [modalias]```

以**严格**的错误检查方式更新

```systemd-hwdb -s update```

在 **/usr/lib/udev** 中更新

```systemd-hwdb --usr update```

针对**备用根目录**更新

```systemd-hwdb -r [/path/to/root] update```

# SYNOPSIS

**systemd-hwdb** [_OPTIONS_] _COMMAND_

# COMMANDS

**update**
> 将 hwdb 源文件编译为二进制数据库

**query** _MODALIAS_
> 在数据库中查询特定的 modalias

# PARAMETERS

**-s, --strict**
> 解析出错时返回非零退出码

**--usr**
> 更新 /usr/lib/udev 中的数据库而非 /etc/udev

**-r, --root=** _PATH_
> 在指定的备用根文件系统上操作

# DESCRIPTION

**systemd-hwdb** 管理 udev 硬件数据库，该数据库将硬件标识符（modalias）映射到属性和元数据。数据库由 `/usr/lib/udev/hwdb.d/` 和 `/etc/udev/hwdb.d/` 中的文本文件编译成二进制格式，以便快速查找。

udev 规则使用该数据库来识别硬件并设置相应的属性。

# CAVEATS

修改 hwdb 源文件后必须运行 `systemd-hwdb update`。二进制数据库与体系结构相关。/etc 中的更改会覆盖 /usr/lib 中的条目。

# HISTORY

**systemd-hwdb** 取代了较旧的 udev hwdb 管理机制，提供系统中设备配置所需的硬件识别数据。

# INSTALL

```apt: sudo apt install udev```

```zypper: sudo zypper install udev```

```nix: nix profile install nixpkgs#udev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[udevadm](/man/udevadm)(8), [hwdb](/man/hwdb)(7)
