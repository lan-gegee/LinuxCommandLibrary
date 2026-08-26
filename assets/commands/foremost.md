# TAGLINE

文件雕刻与数据恢复工具

# TLDR

**从磁盘镜像恢复文件**

```foremost -i [disk.img] -o [output_dir]```

**恢复特定类型的文件**

```foremost -t [jpg,png,pdf] -i [disk.img]```

**从设备恢复**

```sudo foremost -i [/dev/sda1] -o [output_dir]```

**显示所有可恢复的类型**

```foremost -h```

**详细输出**

```foremost -v -i [disk.img] -o [output_dir]```

**使用自定义配置**

```foremost -c [foremost.conf] -i [disk.img]```

# SYNOPSIS

**foremost** [_options_] -i _input_ -o _output_dir_

# DESCRIPTION

**foremost** 是一个从磁盘镜像或设备恢复文件的文件雕刻（file carving）工具。它搜索文件头和文件尾，并提取两者之间的数据，而不管文件系统的状态如何。

该工具适用于数据恢复和取证分析，即使媒体损坏或被部分覆盖也能恢复文件。

# PARAMETERS

**-i** _input_
> 输入文件或设备。

**-o** _directory_
> 输出目录。

**-t** _types_
> 要提取的文件类型。

**-c** _file_
> 配置文件。

**-v**
> 详细输出。

**-V**
> 显示版本。

**-q**
> 快速模式。

**-a**
> 写入所有文件头。

**-w**
> 只写审计文件。

# CONFIGURATION

**/etc/foremost.conf**
> 定义用于恢复的文件签名、文件头和文件尾的配置文件。

# FILE TYPES

常见类型：jpg、gif、png、bmp、avi、exe、mpg、wav、riff、wmv、mov、pdf、ole、doc、zip、rar、htm、cpp

# CAVEATS

碎片化的文件可能无法正确恢复。输出目录必须为空。大容量介质需要大量空间。部分文件类型需要配置。

# HISTORY

**foremost** 由 **美国空军特别调查办公室** 与 **信息系统安全研究与研究中心** 在 **2001** 年前后开发。它为取证式文件恢复而设计，并以开源形式发布。

# INSTALL

```apt: sudo apt install foremost```

```dnf: sudo dnf install foremost```

```pacman: sudo pacman -S foremost```

```brew: brew install foremost```

```nix: nix profile install nixpkgs#foremost```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scalpel](/man/scalpel)(1), [photorec](/man/photorec)(1), [testdisk](/man/testdisk)(1), [dd](/man/dd)(1)

# RESOURCES

```[Homepage](http://foremost.sourceforge.net/)```

<!-- verified: 2026-07-15 -->
