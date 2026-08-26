# TAGLINE

将操作系统镜像烧录到 SD 卡和 U 盘

# TLDR

**启动 Balena Etcher** 图形界面

```balena-etcher```

以 CLI 模式将镜像**烧录**到指定驱动器

```balena-etcher [image.img] --drive [/dev/sdX] --yes```

同时向多个驱动器**烧录镜像**

```balena-etcher [image.img] --drive [/dev/sdb] --drive [/dev/sdc]```

烧录后进行**校验**

```balena-etcher [image.img] --drive [/dev/sdX] --check --yes```

# SYNOPSIS

**balena-etcher** [_options_] [_image_] [_drive..._]

# DESCRIPTION

**Balena Etcher** 是一款跨平台图形应用，用于将操作系统镜像烧录到 SD 卡和 U 盘。它提供简单的三步流程：选择镜像、选择驱动器、烧录。

不带参数启动时会打开 GUI。当命令行参数指定了镜像和驱动器时，则以 CLI 模式运行。

应用会通过回读数据并比较校验和来验证写入，确保镜像烧录可靠。它支持原始镜像（.img、.iso）、压缩镜像（.zip、.gz、.xz、.bz2），还可以直接从 URL 烧录。

Etcher 会自动检测可移动驱动器，防止误选系统盘。它支持多路写入功能，可同时烧录多个驱动器。

# PARAMETERS

**-d**, **--drive** _device_
> 指定要烧录的目标驱动器（可重复使用以指定多个驱动器）。

**-y**, **--yes**
> 自动确认，无需提示。

**-c**, **--check**
> 烧录后通过回读并比较校验和来验证写入。

**-u**, **--unmount**
> 烧录前卸载驱动器。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本号。

# CAVEATS

Etcher 主要是一款 GUI 应用，命令行功能有限。写入设备需要提升的权限。应用虽会阻止选择系统盘，但用户仍应仔细核对目标选择。大型镜像可能需要较长时间来完成烧录和校验。

# HISTORY

**Etcher** 由 **Balena**（原 Resin.io）创建，于 **2016** 年发布，是一款旨在简化为 IoT 设备和树莓派等单板计算机烧录操作系统镜像流程的开源工具。公司更名时，软件名称也从 "Etcher" 改为 "Balena Etcher"。它已成为最受欢迎的镜像烧录工具之一，以友好的用户界面和跨平台支持著称。

# INSTALL

```aur: yay -S balena-etcher```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[dd](/man/dd)(1), [dcfldd](/man/dcfldd)(1), [ventoy](/man/ventoy)(1), [lsblk](/man/lsblk)(1)
