# TAGLINE

MicroStation DGN 文件编译与处理工具

# TLDR

**编译一个 DGN 文件**

```dgn_comp [input.dgn] [output]```

**以详细输出模式**编译

```dgn_comp -v [input.dgn]```

**列出支持的选项**

```dgn_comp --help```

# SYNOPSIS

**dgn_comp** [_options_] _input_ [_output_]

# PARAMETERS

_INPUT_
> 要处理的 DGN（MicroStation 设计）文件。

_OUTPUT_
> 输出文件路径。

**-v**, **--verbose**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dgn_comp** 是一个用于处理和编译 DGN（Design）文件的工具，DGN 是 Bentley MicroStation CAD 软件的原生格式。它可用于设计文件的格式校验、转换或预处理。

DGN 文件包含用于工程、建筑和 GIS 应用的 2D 与 3D 矢量图形数据。dgn_comp 这类工具便于在自动化流程中或不具备完整 CAD 软件的系统上处理这些文件。

具体功能取决于实现，因为存在多种同名工具，分别面向不同的 DGN 处理任务。

# CAVEATS

DGN 格式有多个版本，兼容性各不相同。某些功能可能需要授权许可。复杂的设计可能需要完整 CAD 软件才能准确处理。

# HISTORY

DGN 格式由 **Intergraph** 开发，后来由 **Bentley Systems** 为其 MicroStation 软件维护。在专有生态之外，也出现了各种开源和第三方工具来处理 DGN 文件。

# SEE ALSO

[ogr2ogr](/man/ogr2ogr)(1)
