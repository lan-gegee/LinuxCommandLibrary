# TAGLINE

在内存中定位 MEMDISK 实例

# TLDR

**查找 MEMDISK 并输出参数**供 phram 使用

```memdiskfind```

**通过 phram 加载 MEMDISK 镜像**

```modprobe phram phram=memdisk,$(memdiskfind)```

**将 MEMDISK 镜像暴露为块设备**

```modprobe mtdblock```

# SYNOPSIS

**memdiskfind**

# DESCRIPTION

**memdiskfind** 在物理内存中搜索 MEMDISK 实例（由 SYSLINUX 的 MEMDISK 引导加载程序载入内存的磁盘镜像），如果找到，则以 Linux **phram**（将物理内存用作 MTD）驱动能够理解的格式输出镜像的地址和长度。

典型用法是在 initramfs 中：memdiskfind 定位镜像后，phram 将其暴露为 MTD 设备，mtdblock 再将其转换为可挂载的 /dev/mtdblock0 块设备（例如通过 MEMDISK 引导的 ISO 镜像）。

memdiskfind 是 syslinux-utils 软件包的一部分。也可以用 klibc 编译，生成更小的静态二进制文件，适合放入 initramfs 镜像。

# OUTPUT

输出为单行 _address,size_ 格式（均为十六进制并带 0x 前缀），可直接传给 `modprobe phram`。

# CAVEATS

要求系统是通过 MEMDISK 引导的。通常必须以 root 身份运行才能读取 /proc/iomem 或扫描物理内存。应在根文件系统挂载之前使用，即在 initramfs 中使用。

# HISTORY

**memdiskfind** 是 **SYSLINUX** 项目实用工具的一部分，由 H. Peter Anvin 及贡献者创建，用于辅助引导由 MEMDISK 载入内存的 ISO/软盘镜像。

# INSTALL

```apt: sudo apt install syslinux-utils```

```dnf: sudo dnf install syslinux```

```pacman: sudo pacman -S syslinux```

```apk: sudo apk add syslinux```

```zypper: sudo zypper install syslinux```

```nix: nix profile install nixpkgs#syslinux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[syslinux](/man/syslinux)(1), [modprobe](/man/modprobe)(8), [losetup](/man/losetup)(8)
