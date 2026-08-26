# TAGLINE

创建 GRUB 键盘布局文件

# TLDR

**创建键盘布局**

```grub-mklayout -o [layout.gkb] < [layout.ckb]```

**从控制台布局转换**

```ckbcomp [us] | grub-mklayout -o [us.gkb]```

**详细输出**

```grub-mklayout -v -o [layout.gkb] < [input]```

# SYNOPSIS

**grub-mklayout** [_options_]

# PARAMETERS

**-o**, **--output** _FILE_
> 输出的 GKB 文件。

**-v**, **--verbose**
> 详细模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grub-mklayout** 通过将控制台键盘映射转换为 GRUB 的 GKB 格式来创建键盘布局文件。它从 stdin 读取输入，并生成供启动过程使用的二进制布局文件。

借助该工具，GRUB 可以使用非美式键盘布局，让用户能在启动菜单中用自己的母语键盘布局输入密码和命令。

# CAVEATS

属于 GRUB 软件包的一部分。处理控制台布局需要 ckbcomp。可用的布局选项有限。

# HISTORY

grub-mklayout 作为 **GNU GRUB 2** 的一部分开发，用于在启动菜单中支持国际化键盘布局。

# INSTALL

```apt: sudo apt install grub-common```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub](/man/grub)(8), [loadkeys](/man/loadkeys)(1)
