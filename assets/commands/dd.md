# TAGLINE

在块级别转换和复制文件

# TLDR

从 ISO 制作 **可启动 U 盘**并显示进度

```sudo dd if=[path/to/file.iso] of=[/dev/usb_drive] status=progress```

以 4 MiB 块大小将一块磁盘**克隆**到另一块

```sudo dd bs=4M conv=fsync if=[/dev/source_drive] of=[/dev/dest_drive]```

生成一个由**随机字节**组成的文件

```dd bs=100 count=1 if=/dev/urandom of=[path/to/random_file]```

**测试**磁盘写入性能

```dd bs=1M count=1024 if=/dev/zero of=[path/to/file_1GB]```

创建**系统备份**为 IMG 文件

```sudo dd if=[/dev/drive_device] of=[path/to/file.img] status=progress```

从 IMG 备份**恢复**

```sudo dd if=[path/to/file.img] of=[/dev/drive_device] status=progress```

**跳过**输入开头的字节（例如跳过前 512 字节）

```dd if=[input_file] of=[output_file] bs=512 skip=1```

# SYNOPSIS

**dd** [_OPERAND_]...

# DESCRIPTION

**dd** 在块级别转换和复制文件，因此适用于绕过文件系统结构的底层磁盘操作。它默认从标准输入读取并写入标准输出，但通常配合 if= 和 of= 操作数来指定输入和输出的文件或设备。

该工具以固定块大小（用 bs= 设置）运行，分块读写数据以提高效率。这种面向块的方式让 dd 适合创建精确的磁盘镜像、克隆整块磁盘、从 ISO 文件写入可启动 U 盘，以及生成特定大小的测试文件。

常见用途包括取证磁盘镜像、数据备份与恢复、磁盘基准测试，以及生成填零或随机数据的文件。status=progress 选项（GNU coreutils 8.24 加入）提供实时进度信息。向运行中的 dd 进程发送 USR1 信号（BSD 上为 INFO 信号）会让它把 I/O 统计信息打印到 stderr。

# PARAMETERS

**if=**_FILE_
> 从 FILE 读取而非 stdin。

**of=**_FILE_
> 写入 FILE 而非 stdout。

**bs=**_BYTES_
> 每次最多读写字节数 BYTES（默认：512）。覆盖 ibs 和 obs。

**ibs=**_BYTES_
> 每次最多读取字节数 BYTES（默认：512）。

**obs=**_BYTES_
> 每次写入字节数 BYTES（默认：512）。

**count=**_N_
> 仅复制 N 个输入块。

**skip=**_N_
> 跳过输入开头 N 个 ibs 大小的块。

**seek=**_N_
> 跳过输出开头 N 个 obs 大小的块。

**conv=**_CONVS_
> 逗号分隔的转换选项：ascii、ebcdic、ibm、block、unblock、lcase、ucase、sparse、swab、sync、excl、nocreat、notrunc、noerror、fdatasync、fsync。

**status=**_LEVEL_
> 输出级别：none（除错误外全部抑制）、noxfer（抑制传输统计）、progress（定期显示传输统计）。

**iflag=**_FLAGS_
> 逗号分隔的输入标志：append、direct、directory、dsync、sync、fullblock、nonblock、noatime、nocache、noctty、nofollow、count_bytes、skip_bytes。

**oflag=**_FLAGS_
> 逗号分隔的输出标志：append、direct、directory、dsync、sync、nonblock、noatime、nocache、noctty、nofollow、seek_bytes。

# CAVEATS

**危险**：dd 会毫无警告地覆盖数据。执行前务必反复核对 **of=** 操作数。设备名写错可能毁掉整块磁盘。BYTES 后可跟倍数后缀：c=1、w=2、b=512、kB=1000、K=1024、MB=1000000、M=1048576，G、T、P、E、Z、Y 以此类推。

# HISTORY

**GNU Coreutils** 的组成部分。命令名源自 IBM JCL（Job Control Language），其中 DD 代表 "Data Definition"。自 Version 5 AT&T Unix（1974 年）起可用。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cp](/man/cp)(1), [dcfldd](/man/dcfldd)(1), [pv](/man/pv)(1)
