# TAGLINE

自动内核 EFI stub 管理器

# TLDR

**打印当前配置**

```sudo kernelstub -p```

**复制内核和 initrd 到 ESP** 并设置 NVRAM 启动项

```sudo kernelstub```

**设置内核启动选项**

```sudo kernelstub -o "quiet splash"```

**添加内核启动选项**而不替换现有选项

```sudo kernelstub -a "nomodeset"```

**移除内核启动选项**

```sudo kernelstub -d "quiet"```

**模拟操作**而不实际更改（试运行）

```sudo kernelstub -c```

# SYNOPSIS

**kernelstub** [**-h**] [**-c**] [**-p**] [**-e** _ESP_PATH_] [**-r** _ROOT_PATH_] [**-k** _KERNEL_PATH_] [**-i** _INITRD_PATH_] [**-o** _OPTIONS_] [**-a** _OPTIONS_] [**-d** _OPTIONS_] [**-g** _LOG_FILE_] [**-l**] [**-n**] [**-s**] [**-m**] [**-f**] [**-v**]

# PARAMETERS

**-h**, **--help**
> 显示帮助文本并退出。

**-c**, **--dry-run**
> 模拟所有操作而不实际执行。

**-p**, **--print-config**
> 打印当前配置并退出。

**-e** _PATH_, **--esp-path** _PATH_
> 手动指定 EFI 系统分区（ESP）的路径（默认：/boot/efi）。

**-r** _PATH_, **--root-path** _PATH_
> 要使用的根文件系统所在挂载点的路径。

**-k** _PATH_, **--kernel-path** _PATH_
> 内核镜像的路径。

**-i** _PATH_, **--initrd-path** _PATH_
> initrd 镜像的路径。

**-o** _OPTIONS_, **--options** _OPTIONS_
> 设置完整的内核启动选项（保存到配置文件）。

**-a** _OPTIONS_, **--add-options** _OPTIONS_
> 向配置中添加尚不存在的启动选项。

**-d** _OPTIONS_, **--delete-options** _OPTIONS_
> 从配置中移除已存在的启动选项。

**-g** _FILE_, **--log-file** _FILE_
> 日志文件的路径（默认：/var/log/kernelstub.log）。

**-l**, **--loader**
> 创建 systemd-boot 兼容的 loader 配置（保存到配置文件）。

**-n**, **--no-loader**
> 关闭创建 loader 配置的功能。

**-s**, **--stub**
> 为已复制的内核设置 NVRAM 条目（保存到配置文件）。

**-m**, **--manage-only**
> 仅将条目复制到 ESP，不设置 NVRAM 条目（保存到配置文件）。

**-f**, **--force-update**
> 强制更新 loader.conf，将新条目设为默认启动项。

**-v**, **--verbose**
> 提高输出详细程度。使用 **-vv** 可获得调试输出。

# DESCRIPTION

**kernelstub** 是一个用于在 UEFI 系统上引导 Linux 的自动 EFI 系统分区（ESP）管理器。它将当前的内核和 initramfs 镜像复制到 ESP，使 EFI 固件和引导加载程序能够发现它们，并为直接引导内核（EFI stub 引导）设置 NVRAM 启动菜单条目。

该工具会在安装新内核版本时自动更新这些条目。它可以创建 systemd-boot 兼容的 loader 配置，并通过配置文件持久地管理内核启动参数。它主要用于 Pop!_OS，该发行版默认使用 systemd-boot 而非 GRUB 作为引导加载程序。

# CONFIGURATION

配置存储在 **/etc/kernelstub/configuration** 中（若缺失则自动创建）。发行版模板位于 **/etc/default/kernelstub**（只读）。示例配置位于 **/etc/kernelstub/SAMPLE**。**-o**、**-l**、**-s** 和 **-m** 选项会将其值持久化到配置文件中，影响后续调用。

# CAVEATS

必须以 **root** 身份运行（否则退出码为 176）。仅支持 UEFI —— 在传统 BIOS 系统上没有用途。在双系统环境中，**-f** 选项可能覆盖其他操作系统的启动配置。命令行选项会覆盖配置文件的设置，且部分选项（**-o**、**-l**、**-s**、**-m**）会将更改持久化到配置文件。

# HISTORY

**kernelstub** 由 **Ian Santopietro** 于 **2017 年** 创建，旨在简化和自动化 Linux 上的 EFI stub 引导。它以 **Python 3** 编写，是 **System76** 在开发 **Pop!_OS** 过程中的产物，Pop!_OS 使用 systemd-boot 作为默认引导加载程序。该项目目前在 GitHub 的 pop-os 组织下维护。

# SEE ALSO

[bootctl](/man/bootctl)(1), [efibootmgr](/man/efibootmgr)(8), [update-initramfs](/man/update-initramfs)(8)
