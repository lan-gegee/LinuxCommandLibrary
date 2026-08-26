# TAGLINE

从 ISO 创建多系统启动 U 盘

# TLDR

**安装** Ventoy

```sudo ventoy -i [/dev/sdX]```

以 **GPT** 分区安装

```sudo ventoy -i -g [/dev/sdX]```

带**选项**安装

```sudo ventoy -i -g -S -L [LABEL_NAME] [/dev/sdX]```

在末尾**保留**空间

```sudo ventoy -i -r [SIZE_MB] [/dev/sdX]```

**强制**安装

```sudo ventoy -I [/dev/sdX]```

**更新** Ventoy

```sudo ventoy -u [/dev/sdX]```

显示**信息**

```sudo ventoy -l [/dev/sdX]```

**非破坏性**安装

```sudo ventoy -i -n [/dev/sdX]```

# SYNOPSIS

**ventoy** [_OPTIONS_] _DEVICE_

# PARAMETERS

**-i**
> 将 Ventoy 安装到设备

**-I**
> 强制安装（覆盖已有内容）

**-u**
> 更新已有的 Ventoy 安装

**-l**
> 显示 Ventoy 信息

**-g**
> 使用 GPT 分区样式而非 MBR

**-S**
> 禁用安全启动（secure boot）支持

**-L** _LABEL_
> 设置自定义分区标签

**-r** _SIZE_
> 在磁盘末尾保留空间（MB）

**-n**
> 尝试非破坏性安装

# DESCRIPTION

**ventoy** 创建可启动的 U 盘，可直接引导 ISO 文件而无需解压。只需将 ISO 镜像复制到 U 盘，Ventoy 就会显示一个启动菜单供选择要引导的系统。

它支持 UEFI 和 Legacy BIOS、安全启动、持久化，以及数百种不同的 ISO 镜像。

# CAVEATS

安装会销毁磁盘上的现有数据。某些 ISO 可能不兼容。在部分系统上，安全启动需要额外设置。

# INSTALL

```nix: nix profile install nixpkgs#ventoy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1)
