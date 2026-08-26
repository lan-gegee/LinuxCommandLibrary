# TAGLINE

管理受支持 NVIDIA GPU 上的 Multi-Instance GPU 配置

# TLDR

**列出 MIG 设备**

```nvidia-smi mig -lgip```

**创建 GPU 实例**

```nvidia-smi mig -cgi [profile_id] -C```

**删除 GPU 实例**

```nvidia-smi mig -dci -gi [instance_id]```

**列出 GPU 实例**

```nvidia-smi mig -lgi```

# SYNOPSIS

**nvidia-smi mig** [_options_]

# PARAMETERS

**-lgip**
> 列出 GPU 实例配置文件。

**-lcip**
> 列出计算实例配置文件。

**-lgi**
> 列出 GPU 实例。

**-lci**
> 列出计算实例。

**-cgi** _profile_
> 创建 GPU 实例。

**-cci** _profile_
> 创建计算实例。

**-dgi**
> 删除 GPU 实例。

**-dci**
> 删除计算实例。

**-gi** _id_
> GPU 实例 ID。

**-C**
> 创建默认计算实例。

# DESCRIPTION

**nvidia-smi mig** 管理受支持 NVIDIA GPU 上的 Multi-Instance GPU（MIG）配置。MIG 将单个 GPU 划分为多个隔离的实例，以便在多个用户或工作负载之间共享。

# CAVEATS

仅在启用了 MIG 功能的 NVIDIA A100、A30 和 H100 GPU 上受支持。

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1)
