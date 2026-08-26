# TAGLINE

管理 OpenStack Glance 中的虚拟机镜像

# TLDR

**列出镜像**

```openstack image list```

**查看镜像详情**

```openstack image show [ubuntu-22.04]```

**从文件创建镜像**

```openstack image create --file [image.qcow2] --disk-format qcow2 [image_name]```

**删除镜像**

```openstack image delete [image_name]```

# SYNOPSIS

**openstack image** _command_ [_options_]

# PARAMETERS

**list**
> 列出镜像。

**show** _name_
> 显示镜像详情。

**create** _name_
> 创建/上传镜像。

**delete** _name_
> 删除镜像。

**--file** _path_
> 要上传的镜像文件。

**--disk-format** _format_
> 磁盘格式（qcow2、raw、vmdk 等）。

**--container-format** _format_
> 容器格式（bare、ovf 等）。

**--public**
> 将镜像设为公开。

# DESCRIPTION

**openstack image** 管理 OpenStack Glance 中的虚拟机镜像，可用于上传、下载和管理实例的启动镜像。属于 OpenStack 统一 CLI。

# SEE ALSO

[openstack-server](/man/openstack-server)(1), [openstack](/man/openstack)(1)
