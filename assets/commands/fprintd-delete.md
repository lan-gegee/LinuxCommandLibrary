# TAGLINE

删除已录入的指纹数据

# TLDR

删除特定用户的**所有指纹**

```fprintd-delete [username]```

删除特定用户的一枚**指定指纹**

```fprintd-delete [username] -f [left-thumb|left-index-finger|right-thumb|...]```

显示**帮助**

```fprintd-delete```

# SYNOPSIS

**fprintd-delete** [_options_] _username_

# PARAMETERS

**-f**, **--finger** _FINGER_
> 指定要删除的手指：left-thumb、left-index-finger、left-middle-finger、left-ring-finger、left-little-finger、right-thumb、right-index-finger、right-middle-finger、right-ring-finger、right-little-finger。

# DESCRIPTION

**fprintd-delete** 从 fprintd 数据库中删除已录入的指纹数据。若不使用 **--finger** 选项，则删除指定用户的全部指纹。

该命令通过 D-Bus 与 fprintd 守护进程通信来执行删除操作。指纹数据存储在 **/var/lib/fprint** 中，修改时需要相应的权限。

# CAVEATS

删除指纹的操作无法撤销。如有需要，用户必须使用 **fprintd-enroll** 重新录入指纹。删除其他用户的指纹可能需要 root 权限。

# INSTALL

```apt: sudo apt install fprintd```

```dnf: sudo dnf install fprintd```

```pacman: sudo pacman -S fprintd```

```apk: sudo apk add fprintd```

```zypper: sudo zypper install fprintd```

```nix: nix profile install nixpkgs#fprintd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fprintd](/man/fprintd)(1), [fprintd-enroll](/man/fprintd-enroll)(1), [fprintd-list](/man/fprintd-list)(1), [fprintd-verify](/man/fprintd-verify)(1)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/libfprint/fprintd)```

<!-- verified: 2026-07-15 -->
