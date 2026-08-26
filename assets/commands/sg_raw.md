# TAGLINE

向设备发送原始 SCSI 命令

# TLDR

**发送 SCSI 命令**

```sg_raw [/dev/sg0] [12 00 00 00 24 00]```

**发送带数据输入的命令**

```sg_raw -r [36] [/dev/sg0] [12 00 00 00 24 00]```

**发送带数据输出的命令**

```sg_raw -s [size] -i [file] [/dev/sg0] [command]```

**详细输出**

```sg_raw -v [/dev/sg0] [command]```

**显示二进制响应**

```sg_raw -b [/dev/sg0] [command]```

# SYNOPSIS

**sg_raw** [_-r len_] [_-s len_] [_-i file_] [_options_] _device_ _cdb_

# PARAMETERS

**-r** _LEN_
> 读取 LEN 字节。

**-s** _LEN_
> 发送 LEN 字节。

**-i** _FILE_
> 输入文件。

**-o** _FILE_
> 输出文件。

**-v**
> 详细输出。

**-b**
> 二进制输出。

**-t** _SEC_
> 超时时间。

# DESCRIPTION

**sg_raw** 向设备发送任意的 SCSI 命令描述符块（CDB）并显示响应。它提供对 SCSI 设备最底层的访问方式，可以直接传输任何命令，而无需经过工具本身的解释或校验。

该工具支持所有 SCSI 数据传输阶段：从设备读取数据的命令（**-r**）、向设备写入数据的命令（**-s** 配合 **-i**），以及无数据传输的命令。响应数据可以十六进制形式显示、保存到文件，或以二进制格式输出以便进一步处理。

作为 **sg3_utils** 软件包的一部分，sg_raw 主要用于设备测试、调试 SCSI 协议问题，以及发送高层 sg3_utils 工具未覆盖的厂商专有命令。

# CAVEATS

需要 root 权限。可能损坏设备。请确保清楚自己在做什么。

# HISTORY

**sg_raw** 是 **sg3_utils** 的一部分，这是一套面向 Linux 上 SCSI 设备的工具集。

# INSTALL

```apt: sudo apt install sg3-utils```

```dnf: sudo dnf install sg3_utils```

```pacman: sudo pacman -S sg3_utils```

```apk: sudo apk add sg3_utils```

```zypper: sudo zypper install sg3_utils```

```nix: nix profile install nixpkgs#sg3_utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sg_inq](/man/sg_inq)(1), [sginfo](/man/sginfo)(1), [lsscsi](/man/lsscsi)(1)
