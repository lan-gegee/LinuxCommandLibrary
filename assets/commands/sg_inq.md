# TAGLINE

查询 SCSI 设备 INQUIRY 数据

# TLDR

**查询 SCSI 设备**信息

```sudo sg_inq [/dev/sda]```

**获取设备标识**（序列号、WWN）

```sudo sg_inq --id [/dev/sda]```

按页号**显示 VPD 页**

```sudo sg_inq --vpd --page=[0x83] [/dev/sda]```

**以十六进制输出响应**

```sudo sg_inq --hex [/dev/sda]```

**解码版本描述符**

```sudo sg_inq --descriptors [/dev/sda]```

直接**查询 ATA 设备**

```sudo sg_inq --ata [/dev/sda]```

**以 JSON 格式输出**

```sudo sg_inq --json [/dev/sda]```

**从文件解码 INQUIRY 数据**

```sg_inq --inhex=[path/to/file.hex]```

# SYNOPSIS

**sg_inq** [_options_] _DEVICE_

**sg_inq** **--inhex=**_FN_ [_options_]

# PARAMETERS

**-a**, **--ata**
> 将设备视为 ATA/ATAPI，使用 ATA IDENTIFY 命令而非 SCSI INQUIRY。

**-B**, **--block=**_0|1_
> 控制打开设备时的阻塞模式。0 为非阻塞，1 为阻塞。

**-c**, **--cmddt**
> 为操作码查询设置 Command Support Data 位。在 SPC-2 中已废弃。

**-d**, **--descriptors**
> 解码 INQUIRY 响应中的版本描述符。

**-e**, **--vpd**
> 启用 Vital Product Data 位以获取 VPD 页。

**-f**, **--force**
> 访问 VPD 页前跳过健全性检查。

**-H**, **--hex**
> 以十六进制格式输出响应。

**-i**, **--id**
> 解码设备标识 VPD 页（0x83）。

**-I**, **--inhex=**_FN_
> 从文件解码 INQUIRY 响应，而不是查询设备。

**-j**, **--json**[=_JO_]
> 以 JSON 格式输出。

**-l**, **--len=**_LEN_
> 设置响应缓冲区的分配长度。

**-o**, **--only**
> 仅输出标准 INQUIRY 响应，跳过序列号 VPD。

**-p**, **--page=**_PG_
> 指定要获取的 VPD 页编号或缩写。

**-q**, **--quiet**
> 抑制解码输出和错误信息。

**-r**, **--raw**
> 以二进制格式输出响应。

**-s**, **--vendor**
> 以 ASCII 显示厂商专用字段。

**-v**, **--verbose**
> 提高详细程度。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**sg_inq** 向设备发送 SCSI INQUIRY 命令并输出解码后的响应。所有 SCSI 设备都必须对标准 INQUIRY 命令作出响应，返回至少 36 字节的数据，其中包含厂商、产品和版本修订信息。

该工具支持 Vital Product Data（VPD）页，提供诸如设备序列号（0x80 页）、带 WWN 的设备标识（0x83 页）以及块设备特性等附加信息。**--id** 选项专门解码设备标识页，SPC-3 兼容设备必须支持该页。

除 SCSI 之外，sg_inq 还可以使用 **--ata** 选项查询 ATA/ATAPI 设备，以及向 NVMe 设备发送 Identify controller NVMe Admin 命令进行查询。这使它能够用于查询 Linux 系统上的各类存储设备。

# CAVEATS

需要 root 权限才能访问原始设备节点。在 Linux 2.4 内核上只能使用 SCSI 通用设备（/dev/sg*）。Linux 2.6+ 支持直接使用块设备。此工具不再添加新的 VPD 页信息；较新的 VPD 页请使用 **sg_vpd** 或 **sdparm**。

# HISTORY

**sg_inq** 是 **sg3_utils** 软件包的一部分，这是一套面向 Linux 上 SCSI 设备的工具集。sg3_utils 项目旨在提供通过 Linux SCSI 通用（sg）驱动与 SCSI 设备交互的用户态工具。该软件包已逐步演进为通过 SAT（SCSI/ATA Translation）支持 ATA 设备，近期还加入了对 NVMe 设备的支持。

# INSTALL

```apt: sudo apt install sg3-utils```

```dnf: sudo dnf install sg3_utils```

```pacman: sudo pacman -S sg3_utils```

```apk: sudo apk add sg3_utils```

```zypper: sudo zypper install sg3_utils```

```nix: nix profile install nixpkgs#sg3_utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsscsi](/man/lsscsi)(1), [smartctl](/man/smartctl)(8), [hdparm](/man/hdparm)(8)
