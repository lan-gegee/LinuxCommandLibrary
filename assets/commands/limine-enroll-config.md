# TAGLINE

将 Limine 配置文件的 BLAKE2B 哈希嵌入或重置到

# TLDR

将配置文件的 BLAKE2B 哈希**嵌入** Limine EFI 可执行文件

```limine-enroll-config [path/to/BOOTX64.EFI] [blake2b_hash]```

从可执行文件中**移除**已登记的哈希，禁用配置完整性检查

```limine-enroll-config --reset [path/to/BOOTX64.EFI]```

显示**帮助**

```limine-enroll-config --help```

# SYNOPSIS

**limine-enroll-config** [_--reset_] _EFI_FILE_ [_HASH_]

# PARAMETERS

**--reset**
> 从 EFI 可执行文件中移除已登记的配置哈希

**--help**
> 显示帮助信息

**_EFI_FILE_**
> Limine UEFI 可执行文件的路径（例如 BOOTX64.EFI）

**_HASH_**
> limine.conf 配置文件的 BLAKE2B 哈希

# DESCRIPTION

**limine-enroll-config** 将 Limine 配置文件（limine.conf）的 BLAKE2B 哈希嵌入或重置到 Limine EFI 可执行文件中。这可以在启用 Secure Boot 时确保引导加载程序配置未被篡改。

当 Secure Boot 验证经过签名的 Limine 可执行文件时，会使用内嵌的哈希在应用引导设置之前校验配置文件的完整性。如果哈希不匹配，Limine 将拒绝加载该配置。

# CAVEATS

每当 limine.conf 被修改时，都必须重新生成并重新登记配置哈希。此工具仅与 UEFI Secure Boot 环境相关；BIOS 系统不支持这种验证机制。

# SEE ALSO

[limine](/man/limine)(1), [limine-entry-tool](/man/limine-entry-tool)(1)
