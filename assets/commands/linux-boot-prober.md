# TAGLINE

探测分区中可引导的 Linux 操作系统

# TLDR

**探测**分区中的可引导系统

```sudo linux-boot-prober /dev/sdXY```

# SYNOPSIS

**linux-boot-prober** _partition_

# DESCRIPTION

**linux-boot-prober** 探测分区中可引导的 Linux 操作系统。它是 os-prober 的一部分，被 GRUB 等引导加载程序用来检测其他已安装的 Linux 系统，并将它们添加到引导菜单中。

# PARAMETERS

**partition**
> 要探测的分区的设备路径（例如 /dev/sda1）

# CAVEATS

需要 root 权限。只检测 Linux 安装，不检测其他操作系统。需要更广泛的检测请使用 os-prober。

# INSTALL

```apt: sudo apt install os-prober```

```dnf: sudo dnf install os-prober```

```pacman: sudo pacman -S os-prober```

```apk: sudo apk add os-prober```

```zypper: sudo zypper install os-prober```

```nix: nix profile install nixpkgs#os-prober```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-mkconfig](/man/grub-mkconfig)(8), [update-grub](/man/update-grub)(8)
