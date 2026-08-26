# TAGLINE

安装 Slackware 软件包，即包含文件与安装脚本的压缩 tar 归档

# TLDR

**安装** Slackware 软件包

```sudo installpkg [path/to/package.tgz]```

**模拟**安装并将报告输出到 stdout

```installpkg -warn [path/to/package.tgz]```

**从当前目录创建**软件包

```installpkg -m [package_name.tgz]```

**将当前目录内容作为命名软件包安装**

```sudo installpkg -r [package_name.tgz]```

# SYNOPSIS

**installpkg** [_options_] _package_

# PARAMETERS

**-warn**
> 生成安装报告而不实际安装

**-m** _NAME_
> 从当前目录制作软件包

**-r** _NAME_
> 将当前目录内容作为软件包安装

**-menu**
> 交互式软件包浏览器

**-priority** _ORDER_
> 设置软件包的搜索顺序

# DESCRIPTION

**installpkg** 安装 Slackware 软件包。这类包是压缩的 tar 归档，包含文件和安装脚本。它会将包内容解压到文件系统，并运行随附的 doinst.sh 安装脚本（如果有）。

软件包元数据存储在 /var/log/packages 中，便于跟踪已安装的文件，供日后删除或升级使用。该工具支持 .tgz、.txz、.tbz 和 .tlz 软件包格式。

# CAVEATS

Slackware 专用软件包工具。不会自动处理依赖关系。除非使用 -warn 选项，否则会不加警告地覆盖现有文件。

# HISTORY

installpkg 自 **1993 年**早期版本起就是 Slackware Linux 的一部分。Slackware 的软件包管理刻意保持简单，倾向于手动处理依赖关系，让用户拥有完全控制权。

# SEE ALSO

[removepkg](/man/removepkg)(8), [upgradepkg](/man/upgradepkg)(8), [pkgtool](/man/pkgtool)(8)
