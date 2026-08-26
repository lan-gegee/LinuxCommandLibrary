# TAGLINE

导入和转换 3D 模型文件格式

# TLDR

在不同格式间**转换** 3D 模型

```assimp export [input.fbx] [output.obj]```

**显示**模型信息和统计数据

```assimp info [model.fbx]```

列出所有支持的**导入**文件扩展名

```assimp listext```

列出所有支持的**导出**格式

```assimp listexport```

检查文件**扩展名**是否受支持

```assimp knowext [fbx]```

提取模型中的**内嵌纹理**

```assimp extract [model.fbx]```

将模型结构**导出**为文本以便调试

```assimp dump [model.fbx] [output.assxml]```

显示特定子命令的**帮助**信息

```assimp [export] --help```

# SYNOPSIS

**assimp** _command_ [_parameters_]

# DESCRIPTION

**assimp** 是 Open Asset Import Library 的命令行界面。它支持众多 3D 文件格式的导入与导出，包括 OBJ、FBX、COLLADA（.dae）、glTF/glTF2（.gltf、.glb）、STL、3DS、PLY、X3D 等等。

该工具可以在不同格式之间转换、显示模型信息、提取内嵌纹理，以及导出模型结构以便调试。使用 `assimp <verb> --help` 可查看各子命令的详细帮助。

# PARAMETERS

**export** _input_ _output_
> 在文件格式之间转换 3D 模型。

**info** _file_
> 显示 3D 模型的统计信息和结构。

**listext**
> 列出所有已知的导入文件扩展名。

**listexport**
> 列出所有支持的导出格式。

**knowext** _extension_
> 检查某个文件扩展名是否能被 Assimp 识别。

**extract** _file_
> 从模型中提取内嵌纹理。

**dump** _file_ [_output_]
> 将模型转换为二进制或 XML 转储（ASSBIN/ASSXML）。

**cmpdump** _file1_ _file2_
> 比较由 assimp dump 生成的两个转储文件。

**version**
> 显示 Assimp 版本信息。

**help**
> 显示帮助消息。

# CAVEATS

转换质量因格式而异。某些特性可能在转换过程中丢失。复杂材质可能无法完美转换。大型模型会占用大量内存。

# HISTORY

**Open Asset Import Library** 大约创建于 **2008** 年，旨在为游戏引擎和图形应用程序提供统一的 3D 模型加载接口。

# INSTALL

```apt: sudo apt install assimp-utils```

```dnf: sudo dnf install assimp```

```pacman: sudo pacman -S assimp```

```apk: sudo apk add assimp```

```brew: brew install assimp```

```nix: nix profile install nixpkgs#assimp```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[blender](/man/blender)(1), [meshlab](/man/meshlab)(1), [meshlabserver](/man/meshlabserver)(1)
