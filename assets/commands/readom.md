# TAGLINE

读取或写入光介质数据

# TLDR

从 CD/DVD **创建 ISO 镜像**

```sudo readom dev=/dev/sr0 f=[output.iso]```

以较少的重试次数**创建 ISO** 以加快处理速度

```sudo readom dev=/dev/sr0 f=[output.iso] retries=8```

**从指定的 SCSI 设备读取**

```sudo readom dev=[1,0,0] f=[output.iso]```

**显示驱动器能力**

```sudo readom dev=/dev/sr0 -prcap```

# SYNOPSIS

**readom** **dev=**_device_ **f=**_file_ [_options_]

# PARAMETERS

**dev=**_device_
> 指定光驱设备（如 /dev/sr0、/dev/cdrom 或 SCSI 地址）

**f=**_file_
> ISO 镜像的输出文件名

**retries=**_n_
> 对不可读扇区的重试次数（默认：128）

**speed=**_n_
> 设置读取速度

**-prcap**
> 打印驱动器能力

**-clone**
> 克隆模式，创建包含子通道数据的精确副本

**-noerror**
> 即使出错也继续读取

**-nocorr**
> 禁用错误纠正（用于受损介质恢复）

**-c2scan**
> 扫描音频 CD 上的 C2 错误

# DESCRIPTION

**readom**（read optical media）从 CD、DVD 和蓝光光盘创建 ISO 镜像，内置错误检查与恢复能力。它属于 cdrtools/cdrkit 软件包；处理光介质时比 **dd** 更受青睐，因为它理解光盘结构并能优雅地处理读取错误。

该工具逐扇区读取并进行错误检测，可以自动重试失败的读取。它会报告读取速度、容量以及过程中遇到的错误。

对于损坏或有划痕的光盘，readom 可以对每个扇区尝试多次重试。不过对于严重受损的介质，**ddrescue** 这类专门的恢复工具可能效果更好。

# CAVEATS

**需要 root 权限**：必须以 root 身份运行才能直接访问光驱设备。

**读取前先卸载**：运行 readom 前必须先卸载光盘。必要时用 **mount** 检查并用 **umount /dev/sr0** 卸载。

较高的重试次数（默认 128）可能导致处理受损光盘耗时极长。可用 **retries=8** 之类的设置降低重试次数，换取更快的速度和较少的恢复尝试。

输出是原始 ISO 镜像。音频 CD 需要其他工具（如 **cdparanoia**）才能正确抓取。

# INSTALL

```apt: sudo apt install wodim```

```dnf: sudo dnf install wodim```

```apk: sudo apk add cdrkit```

```nix: nix profile install nixpkgs#cdrkit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wodim](/man/wodim)(1), [cdrecord](/man/cdrecord)(1), [dd](/man/dd)(1), [ddrescue](/man/ddrescue)(1), [cdparanoia](/man/cdparanoia)(1)
