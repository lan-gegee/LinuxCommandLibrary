# TAGLINE

修改 XFS 文件系统参数

# TLDR

显示**卷标**

```sudo xfs_admin -l [/dev/sdX]```

设置**卷标**

```sudo xfs_admin -L "[label]" [/dev/sdX]```

显示 **UUID**

```sudo xfs_admin -u [/dev/sdX]```

设置 **UUID**

```sudo xfs_admin -U [uuid] [/dev/sdX]```

**生成**新 UUID

```sudo xfs_admin -U generate [/dev/sdX]```

# SYNOPSIS

**xfs_admin** [_OPTIONS_] _DEVICE_

# PARAMETERS

**-l, --list**
> 显示文件系统卷标

**-L, --Label** _LABEL_
> 设置文件系统卷标

**-u, --uuid**
> 显示文件系统 UUID

**-U, --UUID** _UUID_
> 设置文件系统 UUID（或用 "generate" 生成新的）

**-c** _0|1_
> 启用/禁用延迟计数器

# DESCRIPTION

**xfs_admin** 用于修改 XFS 文件系统的参数。它可以更改未挂载的 XFS 文件系统的卷标和 UUID。

修改参数前必须先卸载文件系统。

# CAVEATS

更改 UUID 可能影响 fstab 和启动配置。需要 root 权限。仅适用于 XFS 文件系统。

# INSTALL

```apt: sudo apt install xfsprogs```

```dnf: sudo dnf install xfsprogs```

```pacman: sudo pacman -S xfsprogs```

```apk: sudo apk add xfsprogs-extra```

```zypper: sudo zypper install xfsprogs```

```nix: nix profile install nixpkgs#xfsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xfs_repair](/man/xfs_repair)(8), [mkfs.xfs](/man/mkfs.xfs)(8), [tune2fs](/man/tune2fs)(8)
