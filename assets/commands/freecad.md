# TAGLINE

开源参数化 3D CAD 建模器

# TLDR

**启动 FreeCAD**

```freecad```

**打开文件**

```freecad [model.FCStd]```

**以控制台模式启动**（无 GUI）

```freecad -c```

在控制台模式下**运行 Python 脚本**

```freecad -c [script.py]```

将文件**导入并导出**为其他格式

```freecadcmd [model.FCStd] -o [output.step]```

**添加额外的模块路径**

```freecad -M [path/to/modules] [model.FCStd]```

# SYNOPSIS

**freecad** [_options_] [_file_...]

# PARAMETERS

_file_
> 要打开的文件（.FCStd、.step、.iges 等）。

**-c**, **--console**
> 以无 GUI 的控制台模式启动。可选地在后面跟一个要执行的 Python 脚本。

**-o** _file_
> 输出/导出文件（配合 freecadcmd 进行格式转换）。

**-t**, **--run-test** _module_
> 运行指定的测试模块。

**--write-log**
> 将日志文件写入用户主目录下的 FreeCAD_Std.log。

**-M** _path_
> 添加额外的模块搜索路径。

**-u** _file_
> 使用指定的用户配置文件。

**-v**, **--version**
> 显示版本信息。

# CONFIGURATION

**~/.config/FreeCAD/user.cfg**
> 用户偏好设置，包括工作台设置、外观、单位和默认路径。

**~/.local/share/FreeCAD/Mod/**
> 用户安装的工作台和宏所在目录。

# DESCRIPTION

**FreeCAD** 是一个开源的参数化 3D CAD 建模器。它支持多个面向不同任务的工作台：Part Design 用于机械零件，Sketcher 用于 2D 绘图，Arch 用于建筑设计，等等。

FreeCAD 使用 Python 进行脚本编写和宏录制，支持自动化和自定义工具。它可以导入导出 STEP、IGES、STL、OBJ、DXF 等标准格式。

# WORKBENCHES

- **Part Design**: 参数化实体建模
- **Sketcher**: 基于 2D 约束的草图绘制
- **Draft**: 2D 绘图工具
- **Arch**: 建筑建模
- **FEM**: 有限元分析
- **Path**: CNC 刀具路径生成

# CAVEATS

大型装配体可能运行缓慢。参数化建模有学习曲线。部分导入/导出格式存在限制。稳定性因版本而异。

# HISTORY

FreeCAD 由 **Jürgen Riegel** 于 **2002** 年发起，此后由贡献者社区持续开发。它已成为商业 CAD 软件的重要开源替代品，在机械工程和 3D 打印领域尤其如此。

# INSTALL

```pacman: sudo pacman -S freecad```

```nix: nix profile install nixpkgs#freecad```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openscad](/man/openscad)(1), [blender](/man/blender)(1), [meshlab](/man/meshlab)(1)
