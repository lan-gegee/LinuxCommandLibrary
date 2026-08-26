# TAGLINE

STL 网格分析、修复与变换工具

# TLDR

**显示**STL 文件的信息

```admesh [path/to/model.stl]```

**修复并输出**修正后的 STL 文件

```admesh --write-binary-stl=[output.stl] [input.stl]```

**将 STL 转换为 ASCII 格式**

```admesh --write-ascii-stl=[output.stl] [input.stl]```

修复 STL 文件中的**全部缺陷**

```admesh --fill-holes --normal-directions --normal-values [input.stl] --write-binary-stl=[output.stl]```

按系数**缩放模型**

```admesh --scale=[2.0] [input.stl] --write-binary-stl=[output.stl]```

沿坐标轴**平移模型**

```admesh --translate=[10,20,30] [input.stl] --write-binary-stl=[output.stl]```

**绕 X 轴旋转**

```admesh --x-rotate=[90] [input.stl] --write-binary-stl=[output.stl]```

# SYNOPSIS

**admesh** [_options_] _input.stl_

# PARAMETERS

**-b** _file_, **--write-binary-stl** _file_
> 以二进制 STL 格式输出修复后的网格。

**-a** _file_, **--write-ascii-stl** _file_
> 以 ASCII STL 格式输出修复后的网格。

**--fill-holes**
> 通过添加三角形填补网格中的孔洞。

**--normal-directions**
> 修正法线方向，使其一致朝外。

**--normal-values**
> 为所有面片重新计算法向量。

**-e**, **--exact**
> 使用精确顶点匹配为网格的每个面片查找其 3 个相邻面。

**-n**, **--nearby**
> 查找并连接因舍入误差而近乎对齐但不完全匹配的面片。

**-t** _tolerance_, **--tolerance** _tolerance_
> **--nearby** 所使用的搜索距离。默认为网格的最短边长。

**-i** _n_, **--iterations** _n_
> 以逐渐增大的容差运行邻近检查的次数（默认：2）。

**-u**, **--remove-unconnected**
> 移除在精确检查和邻近检查之后仍然没有相邻面的面片。

**--scale** _factor_
> 按给定系数缩放模型。

**--translate** _x,y,z_
> 平移网格，使其最小 x、y、z 值落在给定的坐标处。

**--x-rotate**, **--y-rotate**, **--z-rotate** _angle_
> 绕指定轴逆时针旋转模型（单位：度）。

**--xy-mirror**, **--yz-mirror**, **--xz-mirror**
> 在指定平面内镜像网格。

**--merge** _file_
> 将另一个 STL 文件合并进输入文件（不自动平移）。

**-v**, **--verbose**
> 显示详细的处理信息。

# DESCRIPTION

**ADMesh** 是一款处理和修复 STL（立体光刻）文件的工具，这类文件广泛用于 3D 打印和 CAD 应用。它能诊断并修正常见的网格问题，包括缝隙、孔洞、反向法线以及会导致打印失败的孤立面片。

在不带输出选项运行时，ADMesh 会分析输入文件并报告统计信息，包括面片数量、体积、表面积和检测到的错误。其修复算法可以自动解决大多数网格问题，因此是准备 3D 打印模型时的得力工具。

ADMesh 同时支持二进制和 ASCII STL 格式，并可在两者之间转换。它还提供缩放、旋转和平移模型的变换操作，无需动用完整的 CAD 应用。

# CAVEATS

ADMesh 只处理 STL 文件；其他 3D 格式需要先转换。非常复杂的修复可能会改变原始几何形状。**--exact** 与 **--nearby** 算法的结果可能随网格质量而不同。ASCII 格式的大文件处理速度明显慢于二进制格式。

# HISTORY

ADMesh 由 **Anthony D. Martin** 于 **1990** 年代中期开发，最初用于为快速原型制造设备修复 STL 文件。它随后被开源并由社区持续维护。随着 **2010** 年代消费级 3D 打印的兴起，该工具重获关注，如今常与切片软件搭配用于 FDM 打印工作流。

# INSTALL

```apt: sudo apt install admesh```

```dnf: sudo dnf install admesh```

```aur: yay -S admesh```

```brew: brew install admesh```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[meshlab](/man/meshlab)(1), [openscad](/man/openscad)(1), [blender](/man/blender)(1)

# RESOURCES

```[Source code](https://github.com/admesh/admesh)```

```[Documentation](https://admesh.readthedocs.io/)```

<!-- verified: 2026-06-11 -->
