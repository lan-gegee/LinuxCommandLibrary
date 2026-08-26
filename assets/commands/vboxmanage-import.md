# TAGLINE

从 OVF/OVA 文件导入虚拟机

# TLDR

**导入 OVA appliance**

```vboxmanage import [file.ova]```

**以试运行方式导入**

```vboxmanage import [file.ova] --dry-run```

**以新名称导入**

```vboxmanage import [file.ova] --vsys 0 --vmname [newname]```

# SYNOPSIS

**vboxmanage** **import** _file_ [_options_]

# PARAMETERS

**--dry-run**
> 显示将要执行的操作。

**--vsys** _n_
> appliance 中的目标虚拟机。

**--vmname** _name_
> 覆盖虚拟机名称。

**--basefolder** _path_
> 虚拟机的存放位置。

**--cpus** _n_
> 覆盖 CPU 数量。

**--memory** _mb_
> 覆盖内存大小。

# DESCRIPTION

**vboxmanage import** 从 OVF/OVA 文件导入虚拟机，基于导出的 appliance 创建虚拟机，并支持自定义导入设置。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [vboxmanage-export](/man/vboxmanage-export)(1)
