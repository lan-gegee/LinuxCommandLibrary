# TAGLINE

将 PNM 图像转换为 PCL-XL 打印机格式

# TLDR

**将 PNM 转换为 PCL-XL 格式**

```pnmtopclxl [input.pnm] > [output.pclxl]```

**指定纸张尺寸**（A4）

```pnmtopclxl -format=a4 [input.pnm] > [output.pclxl]```

**高分辨率输出，多份打印**

```pnmtopclxl -dpi=600 -copies=2 [input.pnm] > [output.pclxl]```

**双面打印**

```pnmtopclxl -duplex=vertical [input.pnm] > [output.pclxl]```

# SYNOPSIS

**pnmtopclxl** [_options_] [_pnmfile_]

# PARAMETERS

**-format=**_PAPER_
> 纸张尺寸：**letter**、**legal**、**a3**-**a6**、**jb4**-**jb6**、**exec**、**ledger**、**b5envelope**、**c5envelope**、**com10envelope**、**monarchenvelope**、**dlenvelope**、**jpostcard**、**jdoublepostcard**。

**-dpi=**_N_
> 打印分辨率（每英寸点数）。

**-xoffs=**_N_, **-yoffs=**_N_
> 图像在页面上的水平/垂直偏移量（以点为单位）。

**-center**
> 将图像居中放置在页面上。

**-duplex=**_vertical_|_horizontal_
> 启用双面打印，并按给定方向设置装订边。

**-feeder=**_N_
> 以数字表示的介质来源（进纸盒）。

**-copies=**_N_
> 打印份数。

**-rendergray**
> 强制以灰度渲染。

**-colorok**
> 即使打印机报告不支持彩色，也允许进行彩色输出。

**-jobsetup=**_FILE_
> 将 _FILE_ 的内容作为 PCL-XL 作业设置序言插入开头。

**-embedded**
> 只输出图像流，省略 PCL-XL 作业包装器（用于嵌入到更大的作业中）。

# DESCRIPTION

**pnmtopclxl** 将 PNM 图像转换为 **PCL-XL**（又称 PCL 6）打印机语言——现代 HP LaserJet 打印机的原生格式。属于 **Netpbm** 工具集。各选项既可接受单个也可接受双连字符，并用 **=** 或空格分隔取值。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pbmtolj](/man/pbmtolj)(1), [pnmtops](/man/pnmtops)(1)
