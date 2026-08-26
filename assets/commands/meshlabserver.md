# TAGLINE

MeshLab 三维网格处理的命令行接口

# TLDR

**对网格应用滤镜脚本**

```meshlabserver -i [input.obj] -o [output.obj] -s [script.mlx]```

**转换网格格式**

```meshlabserver -i [input.stl] -o [output.ply]```

**应用脚本并记录日志**

```meshlabserver -i [input.obj] -o [output.obj] -s [script.mlx] -l [log.txt]```

**保存带顶点颜色和法线的输出**

```meshlabserver -i [input.obj] -o [output.ply] -m vc vn```

**处理 MeshLab 项目文件**

```meshlabserver -p [project.mlp] -s [script.mlx] -w [output_project.mlp]```

**导出所有可用滤镜函数的列表**

```meshlabserver -d [filters.txt]```

# SYNOPSIS

**meshlabserver** **-i** _input_ [**-o** _output_] [**-s** _script_] [**-l** _log_] [**-m** _options_]

# PARAMETERS

**-i** _file_
> 要加载的输入网格文件（OBJ、STL、PLY、OFF 等）。

**-o** _file_
> 输出网格文件。格式由扩展名决定。

**-s** _file_
> MeshLab 滤镜脚本文件（.mlx），通过 MeshLab GUI 的 Filters > Show current filter script 创建。必须为 XML 格式。

**-l** _file_
> 用于记录滤镜处理输出的日志文件。

**-p** _file_
> 要加载的 MeshLab 项目文件（.mlp）。

**-w** _file_
> 要保存的输出 MeshLab 项目文件（.mlp）。

**-x**
> 与 **-w** 配合使用。覆盖输入项目中的 3D 模型文件，而不是创建带 _out 后缀的新输出文件。

**-d** _file_
> 将所有可用滤镜函数的列表导出到文本文件。

**-m** _options_
> 要保存的网格属性。顶点：vc（颜色）、vf（标志）、vq（质量）、vn（法线）、vt（纹理坐标）、vr（半径）。面：fc（颜色）、ff（标志）、fq（质量）、fn（法线）。楔：wc（颜色）、wn（法线）、wt（纹理坐标）。格式：mp（多边形）、sa（ASCII）。

# DESCRIPTION

**meshlabserver** 是 MeshLab 的命令行（无界面）接口。它允许使用从 MeshLab GUI 导出的滤镜脚本以非交互方式批量处理三维网格。它支持网格格式转换、项目文件处理以及网格处理工作流的自动化。

# CAVEATS

自 MeshLab 2022.02 起已弃用，由提供同等功能的 Python 库 **PyMeshLab** 取代。滤镜脚本（.mlx）必须在 MeshLab GUI 中创建。输出网格属性选项是 **-m** 而非 **-om**。

# SEE ALSO

[meshlab](/man/meshlab)(1), [blender](/man/blender)(1)
