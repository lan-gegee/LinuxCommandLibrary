# TAGLINE

创建自解压 Shell 归档

# TLDR

创建**基本 shell 归档**

```shar -V [path/to/file1] [path/to/file2] > [archive.sh]```

带**压缩**地创建归档

```shar -C xz [path/to/file1] [path/to/file2] > [archive.sh]```

将所有文件视为**二进制**（全部用 uuencode 编码）

```shar -B [path/to/file1] [path/to/file2] > [archive.sh]```

将所有文件视为**文本**

```shar -T [path/to/file1] [path/to/file2] > [archive.sh]```

包含**归档名称**和切割标记

```shar -n "My Archive" -c [path/to/file1] > [archive.sh]```

将归档**拆分**为多个部分

```shar -L 100K [path/to/file1] [path/to/file2] -o [archive]```

# SYNOPSIS

**shar** [_OPTIONS_] [_file_...]

# PARAMETERS

**-V, --vanilla-operation**
> 只使用 echo、test、sed 创建最小化的归档

**-B, --uuencode**
> 强制对所有文件进行 uuencode 编码（视为二进制）

**-T, --text-files**
> 将所有输入文件视为文本

**-M, --mixed-uuencode**
> 自动检测二进制与文本文件（默认）

**-C, --compactor** _program_
> 使用 gzip、bzip2、xz 或 compress 压缩文件

**-g, --level-of-compression** _num_
> 压缩级别 1-9（默认：9）

**-o, --output-prefix** _str_
> 保存为编号文件（prefix.01、prefix.02 等）

**-L, --split-size-limit** _num_
> 按指定大小拆分归档

**-n, --archive-name** _str_
> 在头部记录归档名称

**-c, --cut-mark**
> 以切割行作为输出的开头

**-a, --net-headers**
> 添加 Submitted-by 和 Archive-name 头部

**-x, --no-check-existing**
> 解压时直接覆盖文件而不提示

**-m, --no-timestamp**
> 跳过文件修改时间的恢复

**-q, --quiet**
> 抑制进度消息

**-h, --help**
> 显示用法信息

# DESCRIPTION

**shar**（shell archive）创建自解压归档文件，只需通过 **/bin/sh** 运行即可解包。归档本身是一个纯文本 shell 脚本，内含编码后的文件数据，因此适合通过电子邮件发送或发布到基于文本的系统。

归档可以包含多个文件和目录，支持压缩、通过 uuencode 进行二进制编码，以及为满足大小限制而拆分为多个部分。解压时，用 **sh archive.sh** 运行归档，或将其设为可执行后直接运行。

# CAVEATS

Shell 归档在解压时会执行 shell 命令，对不可信来源构成安全风险。运行前务必检查 shar 文件。即使经过 uuencode，大型二进制文件也会显著增加归档体积。现代的 tar 加压缩等替代方案通常更适合文件分发。

# HISTORY

**shar** 格式起源于 **20 世纪 80 年代初**的 Unix 社区，当时二进制附件还不普遍，它是一种通过 Usenet 和电子邮件分发源码的方式。包含 **shar** 和 **unshar** 的 GNU sharutils 作为 GNU 项目的一部分开发。虽然在很大程度上已被现代归档格式取代，shar 在分发小型纯文本软件包时仍有用处。

# INSTALL

```apt: sudo apt install sharutils```

```dnf: sudo dnf install sharutils```

```pacman: sudo pacman -S sharutils```

```apk: sudo apk add sharutils```

```zypper: sudo zypper install sharutils```

```nix: nix profile install nixpkgs#sharutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unshar](/man/unshar)(1), [tar](/man/tar)(1), [uuencode](/man/uuencode)(1), [uudecode](/man/uudecode)(1)
