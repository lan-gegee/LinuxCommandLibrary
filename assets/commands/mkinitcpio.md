# TAGLINE

为启动 Linux 内核创建初始内存盘环境

# TLDR

执行**试运行**（打印将要进行的操作）

```mkinitcpio```

基于**所有现有预设**生成内存盘环境

```sudo mkinitcpio -P```

基于 **linux 预设**生成内存盘环境

```sudo mkinitcpio -p linux```

基于 **linux-lts 预设**生成内存盘环境

```sudo mkinitcpio -p linux-lts```

使用**其他配置文件**生成 initramfs 镜像

```sudo mkinitcpio -c [path/to/mkinitcpio.conf] -g [path/to/initramfs.img]```

为**不同的内核版本**生成 initramfs 镜像

```sudo mkinitcpio -k [kernel_version] -g [path/to/initramfs.img]```

**列出所有可用的钩子**

```mkinitcpio -L```

显示**特定钩子的帮助**

```mkinitcpio -H [hook_name]```

# SYNOPSIS

**mkinitcpio** [**-p** _preset_] [**-P**] [**-c** _config_] [**-g** _filename_] [**-k** _version_] [**-A** _hooks_] [**-S** _hooks_] [**-L**] [**-H** _hook_] [**-v**]

# PARAMETERS

**-g, --generate _filename_**
> 将 CPIO 镜像输出到指定文件

**-U, --uki _filename_**
> 生成用于 UEFI 启动的统一内核镜像

**-k, --kernel _version_**
> 指定内核版本或路径；默认为当前运行的内核

**-c, --config _file_**
> 使用自定义配置文件；默认为 /etc/mkinitcpio.conf

**-p, --preset _preset_**
> 基于 /etc/mkinitcpio.d/ 中的预设构建

**-P, --allpresets**
> 处理所有可用的预设

**-A, --addhooks _hooks_**
> 添加额外的钩子（逗号分隔）

**-S, --skiphooks _hooks_**
> 构建时跳过指定的钩子

**-L, --listhooks**
> 列出所有可用的钩子

**-H, --hookhelp _hookname_**
> 显示指定钩子的文档

**-d, --generatedir _dir_**
> 设置 initramfs 的构建位置

**-t, --builddir _tmpdir_**
> 构建时使用备用临时目录

**-z, --compress _method_**
> 覆盖压缩程序（gzip、xz、lz4、zstd）

**-s, --save**
> 保留构建目录以便调试

**-v, --verbose**
> 显示详细的构建信息

# DESCRIPTION

**mkinitcpio** 为启动 Linux 内核创建初始内存盘环境。initramfs 在启动过程的早期加载，提供挂载真实根文件系统所需的内核模块和工具。

该工具通过钩子以模块化方式纳入加密支持、LVM、RAID 和文件系统驱动等特性。/etc/mkinitcpio.d/ 中的预设为已安装的内核定义标准的镜像生成参数。

# CAVEATS

钩子配置错误可能导致系统无法启动。请始终保留一个可正常工作的内核和 initramfs 作为后备。大多数操作需要 root 权限。修改 /etc/mkinitcpio.conf 后，需用 -P 标志重新生成镜像。

# HISTORY

**mkinitcpio** 由 **Arch Linux** 开发团队创建，用于取代较旧的 initramfs 生成工具。它采用模块化的基于钩子的架构，自 2006 年起就是 Arch Linux 及其衍生发行版的标准 initramfs 生成器。

# INSTALL

```pacman: sudo pacman -S mkinitcpio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dracut](/man/dracut)(8), [mkinitramfs](/man/mkinitramfs)(8)
