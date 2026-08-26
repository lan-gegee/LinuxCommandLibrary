# TAGLINE

UEFI 启动管理器配置工具

# TLDR

**列出**所有启动选项及详细信息

```efibootmgr -v```

**添加**新的 UEFI 启动项

```sudo efibootmgr -c -d [/dev/sda] -p [1] -l "[\EFI\boot\bootx64.efi]" -L "[My Entry]"```

**更改**当前启动顺序

```sudo efibootmgr -o [0002,0008,0001,001A]```

**设置**仅在下次启动时生效的启动项

```sudo efibootmgr -n [0002]```

**删除**启动选项

```sudo efibootmgr -b [0008] -B```

**设置**启动管理器超时时间（秒）

```sudo efibootmgr -t [10]```

**将**某个启动项**设为**非活动

```sudo efibootmgr -b [0002] -A```

# SYNOPSIS

**efibootmgr** [_options_]

# DESCRIPTION

**efibootmgr** 通过修改存储在 NVRAM 中的 EFI 变量来操纵 UEFI 启动管理器。它可以创建、删除和修改启动项，更改启动顺序，并设置下次启动设备。

对于管理双系统以及 UEFI 启动配置至关重要。

# PARAMETERS

**-c, --create**
> 创建新的启动项。

**-d, --disk** _disk_
> 包含加载器的磁盘（默认为 /dev/sda）。

**-p, --part** _part_
> 磁盘上的分区号（默认为 1）。

**-l, --loader** _name_
> EFI 加载器文件名（默认为 \EFI\arch\grub.efi）。

**-L, --label** _label_
> 启动项显示标签（默认为 "Linux"）。

**-o, --bootorder** _order_
> 设置启动顺序（逗号分隔的十六进制启动编号）。

**-b, --bootnum** _num_
> 要操作的启动项编号（十六进制）。

**-B, --delete-bootnum**
> 删除 -b 指定的启动项。

**-n, --bootnext** _num_
> 设置仅在下次启动时使用的启动项。一次启动内优先于 BootOrder。

**-N, --delete-bootnext**
> 删除 BootNext 设置。

**-a, --active**
> 将 -b 指定的启动项设为活动。

**-A, --inactive**
> 将 -b 指定的启动项设为非活动。

**-t, --timeout** _seconds_
> 设置启动管理器超时时间（秒）。

**-T, --delete-timeout**
> 删除启动管理器超时变量。

**-u, --unicode**
> 以 Unicode 传递额外的命令行参数。

**-v, --verbose**
> 打印包括设备路径在内的额外信息。

# CAVEATS

需要 root 权限。会修改 UEFI NVRAM 变量。请谨慎使用，错误的设置可能导致系统无法启动。修改前先备份启动项。只能用于以 UEFI 模式启动的系统，不适用于传统 BIOS。

# INSTALL

```apt: sudo apt install efibootmgr```

```dnf: sudo dnf install efibootmgr```

```pacman: sudo pacman -S efibootmgr```

```apk: sudo apk add efibootmgr```

```zypper: sudo zypper install efibootmgr```

```nix: nix profile install nixpkgs#efibootmgr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[efivar](/man/efivar)(1), [grub-install](/man/grub-install)(8), [mokutil](/man/mokutil)(1)
