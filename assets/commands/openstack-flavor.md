# TAGLINE

管理 OpenStack 中的实例规格（flavor）

# TLDR

**列出规格**

```openstack flavor list```

**查看规格详情**

```openstack flavor show [m1.small]```

**以指定资源创建规格**

```openstack flavor create --vcpus [2] --ram [4096] --disk [40] [custom.medium]```

**创建私有规格**

```openstack flavor create --vcpus [4] --ram [8192] --disk [80] --private [custom.large]```

**删除规格**

```openstack flavor delete [custom.medium]```

**为规格设置额外属性**

```openstack flavor set --property [hw:cpu_policy=dedicated] [custom.medium]```

# SYNOPSIS

**openstack flavor** _command_ [_options_]

# PARAMETERS

**list**
> 列出可用的规格。

**show** _name_
> 显示规格详情。

**create** _name_
> 创建规格。

**delete** _name_
> 删除规格。

**set** _name_
> 设置规格属性。

**--vcpus** _num_
> vCPU 数量。

**--ram** _mb_
> 内存大小，单位 MB。

**--disk** _gb_
> 根磁盘大小，单位 GB。

**--ephemeral** _gb_
> 临时磁盘大小，单位 GB（默认：0）。

**--swap** _mb_
> 交换空间大小，单位 MB（默认：0）。

**--id** _id_
> 唯一的规格 ID（'auto' 表示生成 UUID，默认：auto）。

**--public**
> 使所有项目都能访问该规格（默认）。

**--private**
> 使仅特定项目能访问该规格。

**--property** _key=value_
> 为规格设置额外属性。

# DESCRIPTION

**openstack flavor** 管理 OpenStack Nova 中的实例规格（尺寸模板）。规格定义了虚拟机的计算、内存和存储资源。通过 **--property** 设置的属性（即 extra_specs）控制调度器和虚拟化管理程序的行为——常见的键包括 `hw:cpu_policy`、`hw:mem_page_size`、`hw:numa_nodes`、`quota:disk_read_bytes_sec` 和 `aggregate_instance_extra_specs:*`。**set** 命令还可以通过 `--project` / `--project-domain` 为私有规格添加或移除租户访问权限。

它是 OpenStack 统一 CLI（`python-openstackclient`）的组成部分，取代了旧的 `nova flavor-*` 命令。

# CAVEATS

规格无法原地修改：可通过 **set**/**unset** 更改属性，或删除后重建以调整资源大小。已在运行的实例将继续使用原来的规格。创建/删除以及设置大多数属性都需要管理员角色。

# SEE ALSO

[openstack](/man/openstack)(1), [openstack-server](/man/openstack-server)(1), [openstack-image](/man/openstack-image)(1), [openstack-volume](/man/openstack-volume)(1)
