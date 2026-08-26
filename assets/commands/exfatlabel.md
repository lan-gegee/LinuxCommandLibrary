# TAGLINE

获取或设置 exFAT 文件系统的卷标或序列号

# TLDR

**显示卷标**

```exfatlabel [/dev/sda1]```

**设置卷标**

```exfatlabel [/dev/sda1] "[NEW_LABEL]"```

**显示卷序列号**

```exfatlabel -i [/dev/sda1]```

**设置卷序列号**

```exfatlabel -i [/dev/sda1] [0x12345678]```

# SYNOPSIS

**exfatlabel** [_options_] _device_ [_label_]

# PARAMETERS

**-i**, **--volume-serial**
> 切换到卷序列号模式，用于获取或设置卷序列号。

**-V**
> 打印版本号并退出。

# DESCRIPTION

**exfatlabel** 显示或设置 exFAT 文件系统的卷标或卷序列号。如果未给出 label 参数，则显示当前卷标。卷标最多 15 个字符（若使用了超出 Unicode BMP 的字符则更短，因为卷标内部以 UTF-16 存储）。空卷标（`''`）会移除卷名。

# CAVEATS

更改卷标或序列号前必须先卸载文件系统。成功返回 0，失败返回非零值。

# INSTALL

```apt: sudo apt install exfatprogs```

```dnf: sudo dnf install exfatprogs```

```pacman: sudo pacman -S exfatprogs```

```apk: sudo apk add exfatprogs```

```zypper: sudo zypper install exfatprogs```

```nix: nix profile install nixpkgs#exfatprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs.exfat](/man/mkfs.exfat)(8), [fsck.exfat](/man/fsck.exfat)(8), [e2label](/man/e2label)(8)
