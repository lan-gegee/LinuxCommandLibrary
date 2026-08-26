# TAGLINE

systemd-mount --umount 的别名

# TLDR

按挂载点**卸载**文件系统

```systemd-umount [/mnt/usb]```

按设备路径**卸载**文件系统

```systemd-umount [/dev/sdb1]```

自动发现挂载点后**卸载**

```systemd-umount --discover [/dev/sdb1]```

# SYNOPSIS

**systemd-umount** [_options_] _target_...

# DESCRIPTION

**systemd-umount** 等价于 **systemd-mount --umount**。它通过创建处理卸载操作的临时 systemd `.mount` 单元来卸载文件系统。既可按挂载点路径卸载，也可按设备路径卸载。

选项的完整细节请参阅 **systemd-mount** 文档。

# PARAMETERS

**--discover**
> 自动发现设备的挂载点

**--no-block**
> 不等待卸载操作完成

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-mount](/man/systemd-mount)(1), [umount](/man/umount)(8), [mount](/man/mount)(8)
