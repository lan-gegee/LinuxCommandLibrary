# TAGLINE

将 STL 三维网格转换为 GTS 格式

# TLDR

**将 STL 转换为 GTS**

```stl2gts < [input.stl] > [output.gts]```

**带详细输出**

```stl2gts -v < [input.stl] > [output.gts]```

**帮助**

```stl2gts --help```

# SYNOPSIS

**stl2gts** [_-v_] < _input.stl_ > _output.gts_

# PARAMETERS

**-v**, **--verbose**
> 详细输出。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**stl2gts** 将广泛使用的 STL（Stereolithography，光固化成型）格式的三维网格文件转换为 GTS（GNU Triangulated Surface）格式。STL 文件以三角面片的集合表示三维曲面，常用于 CAD 软件、3D 打印和计算几何领域。

GTS 格式专为高效操作和分析三角化曲面而设计。与 STL 不同，GTS 存储顶点和边连接关系的拓扑信息，支持网格细化、布尔运算和曲面分析等操作——这些在原始的"三角形汤"数据上很难实现。

该工具遵循 Unix 管道约定，从标准输入读取 STL 数据，并将 GTS 输出写入标准输出。它是 GTS Library 工具集的一部分，该工具集提供一系列用于三角化曲面网格处理和计算几何的实用程序。

# CAVEATS

仅支持 stdin/stdout。不支持二进制 STL。属于 gts-bin 的一部分。

# HISTORY

**stl2gts** 是 **GTS Library**（GNU Triangulated Surface Library）的一部分，用于网格操作与分析。

# INSTALL

```apt: sudo apt install libgts-bin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gts2stl](/man/gts2stl)(1), [meshlab](/man/meshlab)(1), [admesh](/man/admesh)(1)
