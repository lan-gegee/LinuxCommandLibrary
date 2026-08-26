# TAGLINE

管理 Linode 块存储卷

# TLDR

**列出卷**

```linode-cli volumes list```

**创建卷**

```linode-cli volumes create --label [my-volume] --size [20] --region [us-east]```

**挂载到 Linode**

```linode-cli volumes attach [volume_id] --linode_id [linode_id]```

**卸载卷**

```linode-cli volumes detach [volume_id]```

**查看卷**

```linode-cli volumes view [volume_id]```

**调整卷大小**

```linode-cli volumes resize [volume_id] --size [40]```

**删除卷**

```linode-cli volumes delete [volume_id]```

# SYNOPSIS

**linode-cli volumes** _subcommand_ [_options_]

# PARAMETERS

_SUBCOMMAND_
> 卷操作。

**list**
> 列出所有卷。

**create**
> 创建新卷。

**attach** _ID_
> 挂载到 Linode。

**detach** _ID_
> 从 Linode 卸载。

**view** _ID_
> 查看卷详情。

**resize** _ID_
> 调整卷大小（只能扩大）。

**clone** _ID_
> 将卷克隆为新卷。

**delete** _ID_
> 删除卷。

**--label** _NAME_
> 卷名称。

**--size** _GB_
> 以 GB 为单位的大小（最小：10，最大：10240）。

**--region** _REGION_
> 创建卷的区域（例如 us-east）。

**--linode_id** _ID_
> 创建时将卷挂载到的 Linode。

**--format** _FORMAT_
> 输出格式：json 或 text。

**--help**
> 显示帮助信息。

# DESCRIPTION

**linode-cli volumes** 管理 Linode 块存储卷。卷为实例提供持久化存储。

该工具可创建、挂载和调整块存储的大小，其管理独立于 Linode 的生命周期。

# CAVEATS

需要身份验证。按容量计费。挂载时必须与 Linode 处于同一区域。

# HISTORY

linode-cli volumes 是 **Linode CLI** 的一部分，用于管理 Linode 云上的块存储卷。

# INSTALL

```brew: brew install linode-cli```

```nix: nix profile install nixpkgs#linode-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[linode-cli](/man/linode-cli)(1), [linode-cli-linodes](/man/linode-cli-linodes)(1)
