# TAGLINE

在终端中将 3D 模型渲染为 ASCII 艺术

# TLDR

**查看 OBJ** 模型的 ASCII 终端艺术呈现

```3d-ascii-viewer [path/to/model.obj]```

**查看 STL** 模型

```3d-ascii-viewer [path/to/model.stl]```

利用 OBJ 配套 MTL 文件中引用的材质**启用颜色**

```3d-ascii-viewer --color [model.obj]```

**显示帮助**并列出所有支持的选项

```3d-ascii-viewer --help```

# SYNOPSIS

**3d-ascii-viewer** [_options_] _model_file_

# PARAMETERS

_model_file_
> Wavefront `.obj` 或 `.stl` 模型文件的路径。

**--color**
> 使用配套 MTL 文件中所引用各材质的**漫反射颜色**。需要终端支持颜色重定义并有足够的 ncurses 颜色对。

**--help**
> 打印用法信息并退出。

# DESCRIPTION

**3d-ascii-viewer**（由 autopawn 开发）是一个极简查看器，它仅借助 ncurses、不依赖任何图形库，就能把 3D 模型渲染成动态 ASCII 艺术，直接呈现在终端里。它会持续旋转模型，用不同疏密的字符表现表面明暗和深度。

该查看器支持 Wavefront `.obj` 和 `.stl` 文件。对于 OBJ 文件，可以配合随附的 `.mtl` 材质文件和 **--color** 选项，按每个面的漫反射材质颜色为其着色。

由于输出只是标准终端里的文本，这个查看器非常适合在 SSH 会话、tmux 面板或任何没有完整 3D GUI 的环境中使用。

# CAVEATS

构建需要 ncurses 开发库（Debian 系系统上为 `libncurses-dev`）。复杂的高面数模型可能渲染缓慢或丢失细节。视觉效果在很大程度上取决于终端的字体、宽高比和颜色能力；过小的窗口可能产生难以辨认的输出。**--color** 模式需要终端支持颜色重定义且有足够的颜色对。

# HISTORY

**3d-ascii-viewer** 是 `autopawn` 的开源实验项目，展示了在不借助任何图形库的情况下进行实时 3D 光栅化并输出为 ASCII 字符的技术。它延续了 demo 圈和 ASCII 艺术社区用终端做 3D 渲染的悠久传统。

# INSTALL

```apt: sudo apt install 3d-ascii-viewer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blender](/man/blender)(1), [openscad](/man/openscad)(1), [meshlab](/man/meshlab)(1), [figlet](/man/figlet)(1)
