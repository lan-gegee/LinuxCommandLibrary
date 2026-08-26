# TAGLINE

在启动过程中切换到新的根文件系统

# TLDR

**切换**到新的根文件系统并启动 init

```switch_root [new_root] [/sbin/init]```

# SYNOPSIS

**switch_root** [_options_] _newroot_ _init_ [_arguments_]

# PARAMETERS

**newroot**
> 新根文件系统的路径

**init**
> 要执行的 init 程序路径（相对于新的根目录）

**-h, --help**
> 显示帮助信息

**-V, --version**
> 显示版本信息

# DESCRIPTION

**switch_root** 将特殊文件系统（**/proc**、**/dev**、**/sys**、**/run**）移动到新的根目录，并将其设为挂载树的新根。然后执行指定的 init 程序。

该命令主要用于 initramfs 中，从初始 RAM 文件系统过渡到真正的根文件系统。旧根会在切换发生前被删除以释放内存。

# CAVEATS

新根必须是某个挂载的根，否则命令会失败；如有需要可用 bind 挂载作为变通。必须以 root 运行。只应在早期引导阶段于 initramfs 中使用。属于 util-linux 软件包的一部分。

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

[chroot](/man/chroot)(1), [pivot_root](/man/pivot_root)(8), [mount](/man/mount)(8), [init](/man/init)(8)
