# TAGLINE

控制 EFI 固件启动设置和 systemd-boot

# TLDR

显示**固件和引导加载程序**信息

```bootctl```

列出可用的**引导加载程序条目**

```bootctl list```

设置下次启动时**进入固件**的标志

```sudo bootctl reboot-to-firmware true```

指定 **EFI 系统分区**路径

```bootctl --esp-path /boot/efi/```

**安装** systemd-boot

```sudo bootctl install```

**更新** systemd-boot

```sudo bootctl update```

**移除** systemd-boot

```sudo bootctl remove```

设置**默认启动条目**

```sudo bootctl set-default entry_id```

# SYNOPSIS

**bootctl** [_OPTIONS_] _COMMAND_

# DESCRIPTION

**bootctl** 控制 EFI 固件启动设置并管理 systemd-boot 引导加载程序。它可以安装、更新和移除 systemd-boot，并控制启动条目和固件设置。

# COMMANDS

**status**
> 显示固件和引导加载程序状态（默认）。

**list**
> 列出可用的启动条目。

**install**
> 将 systemd-boot 安装到 EFI 系统分区。

**update**
> 更新 EFI 系统分区中的 systemd-boot。

**remove**
> 从 EFI 系统分区移除 systemd-boot。

**is-installed**
> 检查 systemd-boot 是否已安装。

**random-seed**
> 在 ESP 中初始化随机种子。

**systemd-efi-options [STRING]**
> 获取/设置 systemd.* EFI 选项。

**reboot-to-firmware [BOOL]**
> 获取/设置重启进入固件的标志。

**set-default ID**
> 设置默认启动条目。

**set-oneshot ID**
> 设置一次性启动条目。

**set-timeout SECS**
> 设置启动菜单超时时间。

**set-timeout-oneshot SECS**
> 设置一次性启动菜单超时时间。

# PARAMETERS

**--esp-path PATH**
> EFI 系统分区的路径。

**--boot-path PATH**
> $BOOT 分区的路径。

**-p, --print-esp-path**
> 打印 ESP 路径并退出。

**-x, --print-boot-path**
> 打印 boot 分区路径并退出。

**--no-variables**
> 不改动 EFI 变量。

**--graceful**
> 忽略操作中的错误。

**--make-entry-directory**
> 安装时创建条目目录。

# CAVEATS

需要 EFI 系统分区。检查的默认 ESP 路径为 /efi/、/boot/ 和 /boot/efi/。在非 EFI 系统上，bootctl 的功能有限。

# HISTORY

**bootctl** 是 **systemd** 的一部分，用于管理 systemd-boot 这个可替代 GRUB 的 EFI 引导加载程序。

# INSTALL

```apt: sudo apt install systemd-boot-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kernel-install](/man/kernel-install)(8)
