# TAGLINE

移动 VirtualBox 虚拟机文件

# TLDR

**将虚拟机移动到新文件夹**

```VBoxManage movevm [vmname] --type basic --folder [/path/to/new/location]```

**通过 UUID 移动虚拟机**

```VBoxManage movevm [uuid] --type basic --folder [/path/to/new/location]```

# SYNOPSIS

**VBoxManage** **movevm** _vm_ **--type** basic [**--folder** _path_]

# PARAMETERS

**--type** basic
> 指定移动操作的类型。目前仅支持 "basic"。

**--folder** _path_
> 主机文件系统上的目标文件夹。可以是相对路径或绝对路径。

# DESCRIPTION

**VBoxManage movevm** 将虚拟机移动到主机上的新位置。虚拟机的所有关联文件（包括设置文件和磁盘镜像文件）都会被移动到新位置，Oracle VM VirtualBox 的配置会自动更新。可以通过名称或 UUID 标识虚拟机。包含空格的虚拟机名称必须用双引号括起来。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [vboxmanage-clonevm](/man/vboxmanage-clonevm)(1)
