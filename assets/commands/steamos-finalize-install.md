# TAGLINE

完成 SteamOS 安装设置

# TLDR

**完成**安装

```sudo steamos-finalize-install```

不安装**引导加载器**或内核地完成

```sudo steamos-finalize-install --no-bootloaders --no-kernel```

跳过**迁移**步骤

```sudo steamos-finalize-install --no-migrate```

设置指定的**根哈希**

```sudo steamos-finalize-install --roothash [hash]```

无论环境如何都**强制**迁移

```sudo steamos-finalize-install --force```

# SYNOPSIS

**steamos-finalize-install** [_OPTIONS_]

# PARAMETERS

**--no-bootloaders**
> 跳过引导加载器设置

**--no-kernel**
> 跳过内核安装

**--no-migrate**
> 跳过所有迁移步骤

**--roothash** _HASH_
> 在完成安装时设置指定的根哈希

**--force**
> 无论环境如何都强制系统迁移

# DESCRIPTION

**steamos-finalize-install** 通过设置引导加载器、安装内核和应用系统更新来完成 SteamOS 安装。它执行必要的迁移步骤，从不完整的安装过渡到完全可启动的系统。

此命令通常作为安装流程的一部分运行，但也可以手动调用以修复或重新配置启动组件。

# CAVEATS

需要 root 权限。使用不当可能导致系统无法启动。--force 标志会绕过安全检查，应谨慎使用。此命令仅适用于 Steam Deck 及兼容硬件上的 SteamOS 3.x。

# HISTORY

**steamos-finalize-install** 是 **Valve** 开发的 **SteamOS** 工具的一部分。它处理 Steam Deck 上 SteamOS 3.0 所使用的 A/B 分区安装系统的最后阶段。

# SEE ALSO

[steamos-update](/man/steamos-update)(1), [steamos-chroot](/man/steamos-chroot)(1)
