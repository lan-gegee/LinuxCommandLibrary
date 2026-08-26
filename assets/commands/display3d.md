# TAGLINE

在终端中渲染 3D 模型并制作动画

# TLDR

**显示帮助**

```display3d --help```

**渲染**一个 OBJ 模型并应用平移

```display3d [model.obj] -t [0,0,5.5]```

**渲染**示例鲨鱼模型（来自仓库资源）

```display3d blahaj.obj -t 0,0,5.5```

# SYNOPSIS

**display3d** [*options*] *model-file*

# DESCRIPTION

**display3d** 是一个命令行工具，使用 ANSI 转义码在终端中渲染 3D 物体并制作动画。它用 Rust 编写，基于 **gemini-engine** crate。

支持的格式：

- **.obj**（可选配 **.mtl** 定义颜色；从 Blender 导出时，将 forward 轴设为 +Z、up 轴设为 +Y）
- **.stl**

安装方式：**cargo install display3d**、AUR 软件包 **display3d**、nixpkgs（**pkgs.display3d** / **nix run nixpkgs#display3d**），或从源码构建（**cargo build --release**）。

# PARAMETERS

完整的相机、变换、动画和显示选项请运行 **display3d --help** 查看你已安装版本的说明。常见用法是传入模型路径和可选的变换标志，例如用于平移的 **-t**。

# CAVEATS

需要能可靠支持 ANSI 转义码的终端（在 Windows 上常常不可靠）。OBJ 的彩色渲染需要 **.obj** 旁有配套的 **.mtl** 文件。性能取决于模型复杂度和终端大小。

# INSTALL

```nix: nix profile install nixpkgs#display3d```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chafa](/man/chafa)(1), [timg](/man/timg)(1), [ascii-image-converter](/man/ascii-image-converter)(1)

# RESOURCES

```[Source code](https://github.com/renpenguin/display3d)```

<!-- verified: 2026-07-19 -->
