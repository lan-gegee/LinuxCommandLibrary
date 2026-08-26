# TAGLINE

用于处理和编辑三维三角网格的开源系统

# TLDR

**启动 MeshLab 图形界面**

```meshlab```

**打开网格文件**

```meshlab [model.stl]```

**转换网格格式**

```meshlabserver -i [input.obj] -o [output.stl]```

**应用滤镜脚本**

```meshlabserver -i [input.ply] -o [output.ply] -s [filters.mlx]```

**批量处理文件**

```meshlabserver -i [input.stl] -o [output.stl] -s [script.mlx]```

# SYNOPSIS

**meshlab** [_files_...]

**meshlabserver** -i _input_ -o _output_ [_options_]

# PARAMETERS

**-i** _file_
> 输入网格文件。

**-o** _file_
> 输出网格文件。

**-s** _script_
> 滤镜脚本（.mlx）。

**-l** _file_
> 日志文件。

**-om** _mask_
> 输出掩码选项。

# DESCRIPTION

**MeshLab** 是一个用于处理和编辑三维三角网格的开源系统，提供清理、修复、检查、渲染和转换网格的工具。

meshlabserver 是用于批量处理的命令行版本。

# SUPPORTED FORMATS

```
Input:  STL, OBJ, PLY, OFF, 3DS, PTX, PTS
Output: STL, OBJ, PLY, OFF, DXF, U3D
```

# FILTER CAPABILITIES

```
- Mesh cleaning and repair
- Simplification
- Smoothing
- Subdivision
- Boolean operations
- Measurement
```

# CAVEATS

大型网格需要大量 RAM。某些滤镜要求流形网格。滤镜脚本需在 GUI 中创建。

# HISTORY

MeshLab 由 ISTI-CNR 的 **Visual Computing Lab** 开发，自 **2005 年**起由 **Paolo Cignoni** 领导。

# INSTALL

```apt: sudo apt install meshlab```

```dnf: sudo dnf install meshlab```

```zypper: sudo zypper install meshlab```

```nix: nix profile install nixpkgs#meshlab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blender](/man/blender)(1), [openscad](/man/openscad)(1), [freecad](/man/freecad)(1)
