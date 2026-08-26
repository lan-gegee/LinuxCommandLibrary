# TAGLINE

验证基于 Arch 的系统上已安装软件包的完整性和一致性

# TLDR

**列出并检查**所有已安装的软件包

```paccheck```

**检查**特定软件包

```paccheck [package1] [package2]```

仅在**发现问题**时显示消息

```paccheck --quiet```

检查所有**软件包依赖**是否满足

```paccheck --depends```

显示**帮助**

```paccheck --help```

# SYNOPSIS

**paccheck** [_options_] [_packages_...]

# PARAMETERS

**--quiet**
> 仅在发现问题时才输出

**--depends**
> 检查所有软件包依赖是否满足

**--opt-depends**
> 检查可选依赖

**--files**
> 检查软件包文件是否存在

**--file-properties**
> 对照软件包数据库检查文件属性

**--md5sum**
> 检查文件的 MD5 校验和

**--sha256sum**
> 检查文件的 SHA256 校验和

**--require-mtree**
> 将缺失 MTREE 数据视为错误

**--db-files**
> 将数据库文件纳入检查

**--backup**
> 将备份文件纳入检查

**--noextract**
> 将 NoExtract 文件纳入检查

**--noupgrade**
> 将 NoUpgrade 文件纳入检查

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**paccheck** 验证基于 Arch 的系统上已安装软件包的完整性和一致性。它可以检查依赖关系、验证软件包文件是否存在于磁盘上，并对照软件包数据库记录校验文件校验和。

该工具可用于检测系统损坏、识别被手动修改过的配置文件、查找丢失的文件，以及确保所有软件包依赖都得到正确满足。它从本地 pacman 数据库读取软件包元数据。

# CAVEATS

校验和验证要求软件包中包含 MTREE 数据（并非所有软件包都包含）。某些文件被修改是正常的（用户编辑过的配置文件）。在全量验证选项下运行，在装有大量软件包的系统上会比较慢。

# HISTORY

属于 **pacutils**，由 Andrew Gregory 开发的 pacman 工具集。提供类似 RPM 系统上 **rpm -V** 的功能，让管理员能够验证 Arch Linux 上软件包的完整性。

# SEE ALSO

[pacman](/man/pacman)(8), [pacconf](/man/pacconf)(8), [pacsift](/man/pacsift)(8)
