# TAGLINE

用于参数化设计的脚本式 3D CAD 建模器

# TLDR

**在 GUI 中打开文件**

```openscad [model.scad]```

**渲染为 STL**

```openscad -o [output.stl] [model.scad]```

**渲染为 PNG**

```openscad -o [output.png] [model.scad]```

**设置参数**

```openscad -D "[var=value]" -o [output.stl] [model.scad]```

**以预览模式导出图像**

```openscad --preview -o [output.png] [model.scad]```

**使用相机角度和图像尺寸导出**

```openscad -o [output.png] --camera [0,0,0,25,0,35,500] --imgsize [1920,1080] [model.scad]```

**在导出图像中自动居中并适配对象**

```openscad -o [output.png] --autocenter --viewall [model.scad]```

# SYNOPSIS

**openscad** [_options_] [_file_]

# PARAMETERS

_FILE_
> OpenSCAD 源文件。

**-o** _OUTPUT_
> 输出文件。

**-D** _ASSIGNMENT_
> 设置变量值。

**--preview**
> 预览渲染模式。

**--render**
> 完整渲染模式（CGAL）。

**--camera** _params_
> 相机参数：translate_x,y,z,rot_x,y,z,dist 或 eye_x,y,z,center_x,y,z。

**--imgsize** _x,y_
> PNG 图像尺寸。

**--projection** _type_
> 投影类型：ortho 或 perspective。

**--autocenter**
> 调整相机使其对准对象中心。

**--viewall**
> 调整相机以容纳整个对象。

**--colorscheme** _scheme_
> 渲染使用的配色方案。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**openscad** 是一个脚本式 3D CAD 建模器，使用构造实体几何（CSG）创建参数化模型。与交互式 CAD 工具不同，模型通过脚本语言以编程方式定义。它可以导出为 STL、OFF、AMF、3MF、DXF、SVG 和 PNG 格式。

# CAVEATS

对复杂模型进行完整的 CGAL 渲染可能非常慢。-o 的输出格式由文件扩展名决定。预览模式比完整渲染更快但精度较低。

# HISTORY

**OpenSCAD** 由 Marius Kintel 和 Clifford Wolf 创建，于 **2010 年**首次发布，是一款使用构造实体几何进行脚本式 3D CAD 建模的开源工具。

# INSTALL

```apt: sudo apt install openscad```

```dnf: sudo dnf install openscad```

```pacman: sudo pacman -S openscad```

```apk: sudo apk add openscad```

```zypper: sudo zypper install openscad```

```nix: nix profile install nixpkgs#openscad```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[freecad](/man/freecad)(1), [blender](/man/blender)(1), [meshlab](/man/meshlab)(1)
