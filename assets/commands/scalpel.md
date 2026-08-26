# TAGLINE

文件雕刻与数据恢复工具

# TLDR

**从镜像中雕刻文件**

```scalpel -o [output_dir] [disk.img]```

**使用自定义配置**

```scalpel -c [scalpel.conf] -o [output] [disk.img]```

**从设备中雕刻**

```sudo scalpel -o [output] [/dev/sda]```

**仅预览而不提取**

```scalpel -p -o [output] [disk.img]```

# SYNOPSIS

**scalpel** [_options_] _image_

# DESCRIPTION

**scalpel** 是一款文件雕刻工具，它基于文件头、文件尾和数据结构来恢复文件。相比 foremost，它速度更快、内存效率更高。

该工具可以不考虑文件系统状态地从磁盘镜像或设备中提取文件，适用于数据恢复和取证。

# PARAMETERS

**-o** _dir_
> 输出目录。

**-c** _file_
> 配置文件。

**-b** _num_
> 块大小（字节）。

**-p**
> 预览模式（不提取）。

**-e**
> 跳过块对齐。

**-v**
> 详细输出。

**-r**
> 只查找匹配的文件。

# CONFIGURATION

**scalpel.conf**
> 配置文件，通过为每个文件签名指定文件头、文件尾、最大大小和大小写敏感性来定义要雕刻的文件类型。

# CAVEATS

支持的类型由配置定义。碎片化的文件可能无法恢复。需要足够的输出空间。大镜像处理较慢。

# HISTORY

**scalpel** 由 **Golden G. Richard III** 开发，是对 foremost 的重写，专注于性能。它在数字取证领域用于从磁盘镜像恢复已删除的文件。

# INSTALL

```apt: sudo apt install scalpel```

```zypper: sudo zypper install scalpel```

```nix: nix profile install nixpkgs#scalpel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foremost](/man/foremost)(1), [photorec](/man/photorec)(1), [testdisk](/man/testdisk)(1), [dd](/man/dd)(1)
