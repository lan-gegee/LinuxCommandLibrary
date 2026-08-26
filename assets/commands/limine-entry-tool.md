# TAGLINE

用于在 UEFI 系统上管理 Limine 引导项的辅助脚本

# TLDR

**扫描活动的 UEFI 引导项并将其添加到 Limine 菜单**

```limine-entry-tool --scan```

**添加一个带 initramfs 和内核文件的新内核引导项**

```limine-entry-tool --add "[kernel_name]" "[path/to/initramfs]" "[path/to/vmlinuz]"```

**添加一个新的统一内核镜像（UKI）引导项**

```limine-entry-tool --add-uki "[kernel_name]" "[path/to/uki.efi]"```

**从 ESP 中移除一个内核引导项及其关联文件**

```limine-entry-tool --remove "[kernel_name]"```

**按名称或 machine ID 移除整个 OS 条目**

```limine-entry-tool --remove-os "[OS_name|machine_id]"```

**为其他引导加载程序（如 Windows）添加 EFI 引导项**

```limine-entry-tool --add-efi "[EFI_entry_name]" "[path/to/loader.efi]"```

# SYNOPSIS

**limine-entry-tool** _--option_ [_arguments_]

# PARAMETERS

**--scan**
> 扫描活动的 UEFI 引导项并将其添加到 Limine 配置中。

**--add** _name_ _initramfs_ _vmlinuz_
> 添加一个具有指定名称、initramfs 和内核文件的新内核引导项。

**--add-uki** _name_ _uki.efi_
> 添加一个统一内核镜像（UKI）引导项。

**--remove** _name_
> 从 EFI 系统分区移除一个内核引导项及其文件。

**--remove-os** _name|machine_id_
> 按名称或 machine ID 移除整个操作系统条目，但保留可引导文件不动。

**--add-efi** _name_ _loader.efi_
> 为另一个引导加载程序添加 EFI 引导项（链式加载）。

# DESCRIPTION

**limine-entry-tool** 是一个用于在 UEFI 系统上管理 Limine 引导项的辅助脚本。它将添加、移除和发现 Limine 配置中引导项的过程自动化。

该工具可以检测现有的 UEFI 引导项（包括 Windows 等其他操作系统），并将它们添加到 Limine 的引导菜单中。它既支持传统的内核/initramfs 组合，也支持现代的统一内核镜像（UKI）。

引导项存储在 EFI 系统分区（ESP）上，该工具同时管理配置和实际的内核文件。当安装或卸载内核时，**limine-mkinitcpio-hook** 也会在后台使用此工具来更新引导项。

# CONFIGURATION

**/etc/limine-entry-tool.conf**
> limine-entry-tool 设置的配置文件。可以选择复制到 /etc/default/limine。

# CAVEATS

需要对 EFI 系统分区的写权限。如果启用了 Secure Boot，修改 Limine 配置后可能需要重新登记配置哈希（见 **limine-enroll-config**）。运行此工具前必须先挂载 ESP。

# INSTALL

```aur: yay -S limine-entry-tool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[limine](/man/limine)(1), [limine-enroll-config](/man/limine-enroll-config)(1), [limine-snapper-sync](/man/limine-snapper-sync)(1), [efibootmgr](/man/efibootmgr)(8), [bootctl](/man/bootctl)(1)
