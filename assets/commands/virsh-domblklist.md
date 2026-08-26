# TAGLINE

列出虚拟机块设备

# TLDR

**列出域的块设备**

```virsh domblklist [domain]```

**显示详细信息**

```virsh domblklist [domain] --details```

# SYNOPSIS

**virsh** **domblklist** _domain_ [_options_]

# PARAMETERS

**--details**
> 包含类型和设备信息。

**--inactive**
> 显示非活动配置。

# DESCRIPTION

**virsh domblklist** 列出挂载到虚拟机上的块设备，显示设备目标和源路径。适合用来识别虚拟机关联的磁盘镜像和 CD-ROM。

# SEE ALSO

[virsh](/man/virsh)(1), [virsh-list](/man/virsh-list)(1)

