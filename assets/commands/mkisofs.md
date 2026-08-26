# TAGLINE

生成 ISO9660、Joliet 和 HFS 混合镜像的预母版制作工具

# TLDR

从目录创建 **ISO 镜像**

```mkisofs -o [filename.iso] [path/to/source_directory]```

创建 ISO 时设置**光盘卷标**

```mkisofs -o [filename.iso] -V "[label_name]" [path/to/source_directory]```

创建带 **Rock Ridge 扩展**的 ISO 以兼容 Unix

```mkisofs -o [filename.iso] -R [path/to/source_directory]```

创建带 **Joliet 扩展**的 ISO 以兼容 Windows

```mkisofs -o [filename.iso] -J [path/to/source_directory]```

用 El Torito 引导镜像创建**可引导 ISO**

```mkisofs -o [filename.iso] -b [boot_image] [path/to/source_directory]```

**排除**匹配模式的文件

```mkisofs -o [filename.iso] -m "*.bak" [path/to/source_directory]```

# SYNOPSIS

**mkisofs** [**-o** _filename_] [**-V** _volid_] [**-R**] [**-J**] [**-b** _boot_image_] [**-m** _glob_] _pathspec_ [_pathspec_...]

# PARAMETERS

**-o _filename_**
> 指定 ISO 镜像的输出文件位置

**-V _volid_**
> 设置卷标识符；最长 32 个字符

**-R**
> 生成 Rock Ridge SUSP 记录以保存 Unix 文件属性

**-r**
> 类似 -R，但会全局规范化所有权和权限

**-J**
> 添加 Joliet 目录记录以支持 Windows 长文件名

**-l**
> 允许完整的 31 字符文件名（不兼容 MS-DOS）

**-b _boot_image_**
> 指定 El Torito 引导镜像相对于源目录的路径。

**-no-emul-boot**
> 使用无模拟引导模式（引导镜像不是软盘镜像）。

**-boot-info-table**
> 在引导镜像的偏移 8 处插入引导信息表

**-m _glob_**
> 排除匹配 shell 通配符模式的文件

**-graft-points**
> 允许用 path=source 语法自定义目录嫁接

**-hide _glob_**
> 在 ISO9660 和 Rock Ridge 目录树中隐藏文件

**-hide-joliet _glob_**
> 仅在 Joliet 树中隐藏文件

**-udf**
> 除 ISO9660 外再生成 UDF 文件系统。

**-quiet**
> 尽量减少详细输出。

**-print-size**
> 计算并显示文件系统大小（扇区数）。

# DESCRIPTION

**mkisofs**（也称 **genisoimage**）是一个预母版制作（pre-mastering）工具，用于生成 ISO9660、Joliet 和 HFS 混合文件系统镜像。它创建适合写入 CD、DVD 或其他光学介质的二进制镜像。

该工具支持保存 Unix 文件属性的 Rock Ridge 扩展、支持 Windows 长文件名的 Joliet 扩展、用于可引导介质的 El Torito，以及 Apple HFS 混合文件系统。它处理目录树，但不直接与刻录机通信。

# CAVEATS

基本 ISO9660 将文件名限制为 8.3 格式；更长的名称请使用 -R 或 -J。-boot-info-table 选项会直接修改源引导文件；如有需要请使用副本。HFS 和 UDF 支持部分属于实验性功能。字符编码因平台而异，可能需要显式指定字符集选项。

# HISTORY

**mkisofs** 最初由 Eric Youngdale 编写，后来作为 Joerg Schilling 维护的 **cdrtools** 软件包的一部分。**genisoimage** 分叉是为 Debian 及其衍生版本创建的 **cdrkit** 的一部分。ISO9660 标准的历史可追溯到 1988 年。

# INSTALL

```apt: sudo apt install genisoimage```

```dnf: sudo dnf install genisoimage```

```apk: sudo apk add xorriso```

```zypper: sudo zypper install xorriso```

```brew: brew install xorriso```

```nix: nix profile install nixpkgs#xorriso```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[genisoimage](/man/genisoimage)(1), [wodim](/man/wodim)(1), [cdrecord](/man/cdrecord)(1), [isoinfo](/man/isoinfo)(8)
