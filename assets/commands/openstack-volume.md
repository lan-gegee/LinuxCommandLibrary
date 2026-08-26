# TAGLINE

管理 OpenStack Cinder 中的块存储卷

# TLDR

**列出卷**

```openstack volume list```

**创建卷**

```openstack volume create --size [10] [volume_name]```

**将卷附加到服务器**

```openstack server add volume [server] [volume]```

**删除卷**

```openstack volume delete [volume_name]```

# SYNOPSIS

**openstack volume** _command_ [_options_]

# PARAMETERS

**list**
> 列出卷。

**create** _name_
> 创建卷。

**delete** _name_
> 删除卷。

**show** _name_
> 显示卷详情。

**--size** _gb_
> 卷大小，单位 GB。

**--image** _image_
> 从镜像创建。

**--snapshot** _snapshot_
> 从快照创建。

**--type** _type_
> 卷类型。

# DESCRIPTION

**openstack volume** 管理 OpenStack Cinder 中的块存储卷。可创建持久化存储卷并附加到实例。属于 OpenStack 统一 CLI。

# SEE ALSO

[openstack-server](/man/openstack-server)(1), [openstack](/man/openstack)(1)
