# TAGLINE

显示或更改交换分区的标签和 UUID

# TLDR

**显示**交换分区当前的标签和 UUID

```swaplabel [path/to/device]```

**设置**交换分区的标签

```swaplabel -L [new_label] [path/to/device]```

**设置**交换分区的 UUID

```swaplabel -U [new_uuid] [path/to/device]```

# SYNOPSIS

**swaplabel** [_options_] _device_

# PARAMETERS

**-L, --label _label_**
> 设置交换分区的标签

**-U, --uuid _uuid_**
> 设置交换分区的 UUID（可用 **uuidgen** 生成）

**-h, --help**
> 显示帮助信息

**-V, --version**
> 显示版本信息

# DESCRIPTION

**swaplabel** 用于打印或更改 Linux 交换分区的标签或 UUID。设备可以是分区，也可以是配置为交换空间的普通文件。

标签和 UUID 可用于在 **/etc/fstab** 中标识交换分区，避免使用可能在重启之间发生变化的设备路径。特别建议使用 UUID 来实现可靠的标识。

# CAVEATS

更改标签或 UUID 时，交换分区必须处于未激活（未使用）状态。需要 root 权限。更改 UUID 后，如果 **/etc/fstab** 引用了旧 UUID，请更新它。属于 util-linux 软件包。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkswap](/man/mkswap)(8), [swapon](/man/swapon)(8), [swapoff](/man/swapoff)(8), [uuidgen](/man/uuidgen)(1)
