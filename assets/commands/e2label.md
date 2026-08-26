# TAGLINE

更改 ext 文件系统标签

# TLDR

**显示**当前卷标

```sudo e2label [/dev/sda1]```

更改**卷标**

```sudo e2label [/dev/sda1] "[label_name]"```

**清除**卷标

```sudo e2label [/dev/sda1] ""```

# SYNOPSIS

**e2label** _device_ [_new-label_]

# DESCRIPTION

**e2label** 更改或显示 ext2/ext3/ext4 文件系统上的标签。标签为文件系统提供人类可读的名称，可用于按标签而非设备名挂载文件系统，这在设备名发生变化时能提升可移植性。

如果不指定标签，则显示当前标签。标签在 /etc/fstab 条目中特别有用，能让系统配置在硬件更换导致设备重命名后仍保持有效。

# PARAMETERS

_device_
> 文件系统设备

_new-label_
> 新标签（最多 16 个字符）

# CAVEATS

标签限制为 16 个字符，超长会被静默截断。e2label 是 **tune2fs -L** 的一个轻量封装，两者可以互换。更改标签时文件系统可以处于挂载状态，但 udev 和 /dev/disk/by-label 要到下次扫描后才会识别新标签。属于 **e2fsprogs** 软件包。

# INSTALL

```apt: sudo apt install e2fsprogs```

```dnf: sudo dnf install e2fsprogs```

```pacman: sudo pacman -S e2fsprogs```

```apk: sudo apk add e2fsprogs-extra```

```zypper: sudo zypper install e2fsprogs```

```brew: brew install e2fsprogs```

```nix: nix profile install nixpkgs#e2fsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tune2fs](/man/tune2fs)(8), [blkid](/man/blkid)(8), [mount](/man/mount)(8), [e2undo](/man/e2undo)(8)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/fs/ext2/e2fsprogs.git)```

```[Homepage](https://e2fsprogs.sourceforge.net/)```

<!-- verified: 2026-07-14 -->
