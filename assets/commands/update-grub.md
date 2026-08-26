# TAGLINE

重新生成 GRUB 引导加载程序配置

# TLDR

该命令是 **grub-mkconfig --output /boot/grub/grub.cfg** 的别名。

**查看**原始命令的文档

```tldr grub-mkconfig```

# SYNOPSIS

**update-grub**

# DESCRIPTION

**update-grub** 是一个便捷封装命令，用于生成新的 GRUB 配置文件。它等同于运行 **grub-mkconfig -o /boot/grub/grub.cfg**，常见于基于 Debian 的发行版。

该命令从 **/etc/default/grub** 和 **/etc/grub.d/** 中的脚本读取配置，进而生成引导加载程序配置。

# CAVEATS

需要 root 权限。实际路径可能有所不同（某些系统上是 **/boot/grub2/grub.cfg**）。务必仔细检查对 GRUB 配置所做的更改。

# INSTALL

```apt: sudo apt install grub2-common```

```dnf: sudo dnf install grub2-common```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

```zypper: sudo zypper install grub2-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-mkconfig](/man/grub-mkconfig)(8), [grub-install](/man/grub-install)(8)
