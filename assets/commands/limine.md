# TAGLINE

现代、先进、可移植的多协议引导加载程序和引导管理器

# TLDR

安装到 **MBR** 分区的设备

```limine bios-install [/dev/sdX]```

安装到带有 stage 2 分区的 **GPT** 分区设备

```limine bios-install [/dev/sdX] [partition_number]```

安装到**磁盘镜像**文件

```limine bios-install [path/to/image.iso]```

将配置哈希登记到 **Limine EFI 可执行文件**中以支持 Secure Boot

```limine enroll-config [path/to/BOOTX64.EFI]```

# SYNOPSIS

**limine** _command_ [_arguments_]

# DESCRIPTION

**limine** 是一个现代、先进、可移植的多协议引导加载程序和引导管理器，支持 BIOS 和 UEFI 系统。它可以通过 Limine Boot Protocol、Multiboot 1 和 2、Linux 引导协议以及链式加载来引导操作系统和内核。

对于 BIOS 系统，使用 **limine bios-install** 将引导加载程序写入设备或镜像。引导设备必须在某个分区的 /boot/limine、/boot、/limine 或根目录中包含 limine-bios.sys 和 limine.conf。

对于 UEFI 系统，将相应的 BOOT*.EFI 文件复制到 EFI 系统分区。使用 **limine enroll-config** 登记用于 Secure Boot 验证的配置哈希。

# PARAMETERS

**bios-install** _DEVICE_ [_PARTITION_]
> 将 Limine BIOS 引导加载程序安装到设备或镜像。对于 GPT 磁盘，可选择指定从 1 开始编号的 stage 2 分区号（至少 32 KiB）。在 GPT 上省略时会尝试自动检测。

**enroll-config** _EFI_FILE_
> 将 Limine 配置文件的 BLAKE2B 哈希登记到 Limine EFI 可执行镜像中以供验证（Secure Boot）。

# CAVEATS

对于 GPT BIOS 安装，需要一个至少 32 KiB 的专用分区来存放 stage 2。UEFI Secure Boot 需要用 **limine enroll-config** 登记配置哈希。安装前务必备份现有的引导加载程序。

# INSTALL

```pacman: sudo pacman -S limine```

```apk: sudo apk add limine-tool```

```zypper: sudo zypper install limine```

```brew: brew install limine```

```nix: nix profile install nixpkgs#limine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[limine-enroll-config](/man/limine-enroll-config)(1), [limine-entry-tool](/man/limine-entry-tool)(1), [grub-install](/man/grub-install)(8)
