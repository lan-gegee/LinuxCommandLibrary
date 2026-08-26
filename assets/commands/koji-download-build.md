# TAGLINE

从 Koji 构建系统下载已构建的软件包

# TLDR

从一次构建中下载**所有 RPM**

```koji download-build [build_id|nvr]```

下载**指定架构**的 RPM

```koji download-build [build_id] --arch x86_64```

下载用**指定密钥**签名的 RPM

```koji download-build [build_id] --key [key_id]```

下载**指定的 RPM**

```koji download-build [rpm_name] --rpm```

下载**源码 RPM**

```koji download-build [build_id] --type src```

显示**帮助**

```koji download-build --help```

# SYNOPSIS

**koji download-build** [_options_] _build_id_|_nvr_|_rpm_

# DESCRIPTION

**koji download-build** 从 Koji 构建系统下载已构建的软件包。你可以通过构建 ID 或 NVR（Name-Version-Release）指定一次构建，也可以直接下载某个特定的 RPM。

# PARAMETERS

**build_id|nvr|rpm**
> 构建标识、NVR 字符串或 RPM 名称

**--arch ARCH**
> 只下载指定架构的 RPM（如 x86_64、aarch64、noarch）

**--key KEY**
> 只下载用指定密钥签名的 RPM

**--rpm**
> 将参数解释为 RPM 名称

**--type TYPE**
> 下载指定类型：rpm、src、debuginfo

**--latestfrom TAG**
> 从指定标签下载最新构建

**--topdir DIR**
> 指定下载目录

**-h, --help**
> 显示帮助信息

# CAVEATS

包含大量子包的大型构建可能耗费大量时间和带宽。签名 RPM 要求 Koji 中存在相应的签名密钥。

# SEE ALSO

[koji](/man/koji)(1), [koji-build](/man/koji-build)(1), [dnf](/man/dnf)(8)
