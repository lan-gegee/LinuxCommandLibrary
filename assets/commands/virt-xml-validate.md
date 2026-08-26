# TAGLINE

校验 libvirt XML 文件

# TLDR

按**指定** schema 校验

```virt-xml-validate [path/to/file.xml] [schema]```

校验 **domain** XML

```virt-xml-validate [path/to/domain.xml] domain```

校验 **network** XML

```virt-xml-validate [path/to/network.xml] network```

校验 **storage pool** XML

```virt-xml-validate [path/to/pool.xml] storagepool```

# SYNOPSIS

**virt-xml-validate** _FILE_ [_SCHEMA_]

# PARAMETERS

**FILE**
> 要校验的 XML 文件

**SCHEMA**
> 用于校验的 schema 名称（省略时从根元素自动检测）。有效的 schema 包括：domain、domainsnapshot、domaincheckpoint、domainbackup、domaincaps、network、networkport、nwfilter、nwfilterbinding、storagepool、storagepoolcaps、storagevol、nodedev、capability、interface、secret、cpu。

**-h**, **--help**
> 显示命令行帮助后退出。

**-V**, **--version**
> 显示版本信息后退出。

# DESCRIPTION

**virt-xml-validate** 根据相应的 schema 校验 libvirt XML 文件。如果未指定 schema，会根据 XML 文件的根元素自动确定。

该工具有助于在将 XML 配置文件用于 libvirt 之前验证其有效性。

# CAVEATS

XML 有效并不保证配置能够正常工作。某些 schema 错误可能无法检出。需要安装 libvirt schema。

# INSTALL

```apt: sudo apt install libvirt-clients```

```dnf: sudo dnf install libvirt-client```

```apk: sudo apk add libvirt-client```

```zypper: sudo zypper install libvirt-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virt-xml](/man/virt-xml)(1), [virsh](/man/virsh)(1)
