# TAGLINE

将 GTS 文件转换为 STL 格式

# TLDR

**将 GTS 文件转换为 STL**

```gts2stl < [input.gts] > [output.stl]```

**转换并输出详细信息**

```gts2stl --verbose < [input.gts] > [output.stl]```

**转换并反转面法线**

```gts2stl --revert < [input.gts] > [output.stl]```

# SYNOPSIS

**gts2stl** [_options_] < _input.gts_ > _output.stl_

# PARAMETERS

**-v**, **--verbose**
> 打印曲面的统计信息。

**-r**, **--revert**
> 反转面法线（翻转三角形朝向）。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**gts2stl** 将 GTS（GNU Triangulated Surface）文件转换为 STL（STereoLithography）格式。GTS 是一个用于 3D 表面网格操作的库，此工具将网格导出为广泛使用的 STL 格式。

STL 文件常用于 3D 打印和 CAD 应用。转换会保留三角网格结构。输出为 ASCII STL 格式。

# GTS FORMAT

GTS 文件包含：
- 顶点数、边数、面数
- 顶点坐标
- 边的定义（顶点对）
- 面的定义（边三元组）

# CAVEATS

从 stdin 读取，写入 stdout。大型网格可能需要较长时间。GTS 格式不如 STL 常见。属于 GTS 库软件包的一部分。

# HISTORY

gts2stl 是 **GTS 库**（GNU Triangulated Surface）的一部分，该库面向计算几何操作开发，提供表面网格处理、布尔运算和格式转换等工具。

# INSTALL

```apt: sudo apt install libgts-bin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stl2gts](/man/stl2gts)(1), [meshlab](/man/meshlab)(1), [openscad](/man/openscad)(1)
