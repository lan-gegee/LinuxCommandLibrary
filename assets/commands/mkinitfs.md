# TAGLINE

从根文件系统收集文件并创建压缩的

# TLDR

按 /etc/mkinitfs/mkinitfs.conf 中的特性生成 **initramfs**

```mkinitfs```

使用**其他配置文件**

```mkinitfs -c [path/to/config]```

用指定算法**压缩** initramfs

```mkinitfs -C [gzip|xz|zstd|lz4|none]```

**列出**将包含在 initramfs 镜像中的文件

```mkinitfs -l```

列出所有**可用特性**

```mkinitfs -L```

为**特定内核版本**生成 initramfs

```mkinitfs [kernel_version]```

指定**输出文件**路径

```mkinitfs -o [path/to/initramfs.img]```

# SYNOPSIS

**mkinitfs** [**-c** _configfile_] [**-C** _algorithm_] [**-f** _fstab_] [**-F** _features_] [**-o** _outfile_] [**-l**] [**-L**] [_kernelversion_]

# PARAMETERS

**-b _basedir_**
> 使用指定目录代替根文件系统

**-c _configfile_**
> 使用备用配置文件；默认为 /etc/mkinitfs/mkinitfs.conf

**-C _algorithm_**
> 压缩方法：gzip（默认）、xz、zstd、lz4 或 none

**-f _fstab_**
> 指定备用的 fstab 文件

**-F _features_**
> 启用指定的特性

**-i _initfile_**
> 使用自定义的 init 脚本

**-k**
> 完成后保留临时文件

**-K**
> 将主机的 APK 密钥包含进 initramfs

**-l**
> 试运行；列出将要包含的文件

**-L**
> 显示所有可用特性

**-n**
> 排除内核模块和固件

**-o _outfile_**
> 指定输出文件路径

**-P _featuresdir_**
> 向搜索路径添加自定义特性目录

**-q**
> 安静模式；抑制输出消息

**-t _tmpdir_**
> 设置临时目录位置

# DESCRIPTION

**mkinitfs** 从根文件系统收集文件并为 Alpine Linux 创建压缩的 initramfs。initramfs 提供启动期间挂载真实根文件系统所需的早期用户空间工具。

特性（feature）决定包含哪些模块、二进制程序和配置文件。常见特性包括基础系统工具、文件系统支持、加密（cryptsetup）、LVM 以及网络启动（dhcp、nfs）。

# CAVEATS

Alpine Linux 专用工具；与其他发行版不兼容。缺少必要特性会导致无法启动。配置文件必须列出成功启动系统所需的全部特性。

# HISTORY

**mkinitfs** 作为 **Alpine Linux** 的一部分开发，用于创建契合该发行版安全与简洁理念的最小高效 initramfs 镜像。它与 Alpine 的 apk 包管理器集成，并采用基于特性的模块化系统。

# INSTALL

```apk: sudo apk add mkinitfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkinitcpio](/man/mkinitcpio)(8), [dracut](/man/dracut)(8), [update-initramfs](/man/update-initramfs)(8)
