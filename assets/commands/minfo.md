# TAGLINE

打印 MS-DOS 文件系统的参数

# TLDR

**显示文件系统信息**（针对已配置的 mtools 驱动器）

```minfo [a:]```

**显示详细信息**，包括引导扇区的十六进制转储

```minfo -v [a:]```

**显示磁盘镜像文件的信息**

```minfo -i [path/to/image.img] ::```

# SYNOPSIS

**minfo** [**-v**] _drive_

**minfo** **-i** _imagefile_ **::**

# PARAMETERS

**-v**
> 详细模式：同时打印引导扇区的十六进制转储。

**-i** _imagefile_
> 从指定的镜像文件读取，而非已配置的驱动器。

# DESCRIPTION

**minfo** 打印 MS-DOS 文件系统的参数，例如扇区数、磁头数和柱面数。它还会打印一条 **mformat** 命令行，可用于在另一个设备上创建类似的 MS-DOS 文件系统。

**minfo** 是 **mtools** 工具集的一部分，该工具集用于在 Unix 上访问 MS-DOS 磁盘而无需挂载。它支持 FAT12、FAT16 和 FAT32 文件系统。

# CAVEATS

不支持 2m 或 XDF 介质格式，也不支持 MS-DOS 1.0 文件系统。需要为目标驱动器配置好 mtools，或通过 **-i** 提供镜像文件。

# HISTORY

**minfo** 属于 **mtools**，这是一套最初由 Emmet P. Gray 编写的工具集合，用于在 Unix 系统上访问 MS-DOS 磁盘，后来由 Alain Knaff 维护。

# INSTALL

```apt: sudo apt install mtools```

```dnf: sudo dnf install mtools```

```pacman: sudo pacman -S mtools```

```apk: sudo apk add mtools```

```zypper: sudo zypper install mtools```

```brew: brew install mtools```

```nix: nix profile install nixpkgs#mtools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mcopy](/man/mcopy)(1)
