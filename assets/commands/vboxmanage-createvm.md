# TAGLINE

创建新的 VirtualBox 虚拟机

# TLDR

**创建虚拟机**

```vboxmanage createvm --name [vmname] --register```

**指定操作系统类型创建**

```vboxmanage createvm --name [vmname] --ostype [Ubuntu_64] --register```

**在文件夹中创建**

```vboxmanage createvm --name [vmname] --basefolder [path] --register```

# SYNOPSIS

**vboxmanage** **createvm** [_options_]

# PARAMETERS

**--name** _name_
> 虚拟机名称。

**--ostype** _type_
> 客户机操作系统类型。

**--register**
> 注册到 VirtualBox。

**--basefolder** _path_
> 虚拟机文件的存放位置。

**--uuid** _uuid_
> 指定 UUID。

**--groups** _groups_
> 虚拟机组。

# DESCRIPTION

**vboxmanage createvm** 创建新的虚拟机定义，只生成虚拟机配置而不包含硬件。使用 modifyvm 配置 CPU、内存和存储。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [vboxmanage-modifyvm](/man/vboxmanage-modifyvm)(1)
