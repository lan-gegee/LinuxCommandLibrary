# TAGLINE

安全地将磁盘镜像写入 USB 驱动器

# TLDR

将 ISO **烧录**到驱动器

```caligula burn [path/to/image.iso]```

以**预先指定的哈希值**烧录 ISO

```caligula burn [path/to/image.iso] -s [hash]```

# SYNOPSIS

**caligula** _command_ [_options_] _image_

# DESCRIPTION

**caligula** 是一款易用的 TUI（文本用户界面）应用，用于将磁盘镜像写入 USB 驱动器和其他存储设备。相比 dd，它为制作启动介质提供了更安全、更具交互性的选择。

该工具通过哈希校验来验证镜像完整性，并要求确认目标设备的选择，以防止意外的数据丢失。

# SUBCOMMANDS

**burn**
> 将镜像写入设备

# PARAMETERS

**-s, --hash** _hash_
> 用指定的哈希值校验镜像

# CAVEATS

写入设备需要 root 权限。写入前务必确认目标设备。目标设备上的所有数据都将被销毁。

# INSTALL

```pacman: sudo pacman -S caligula```

```zypper: sudo zypper install caligula```

```nix: nix profile install nixpkgs#caligula```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [pv](/man/pv)(1), [balena-etcher](/man/balena-etcher)(1)

# RESOURCES

```[Source code](https://github.com/ifd3f/caligula)```

<!-- verified: 2026-06-22 -->
