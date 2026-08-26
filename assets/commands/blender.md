# TAGLINE

集建模、动画和渲染于一体的 3D 创作套件

# TLDR

**启动** Blender 图形界面

```blender```

**打开**文件

```blender [model.blend]```

**在后台渲染**

```blender -b [scene.blend] -a```

**渲染**指定帧

```blender -b [scene.blend] -f [10]```

**执行** Python 脚本

```blender --python [script.py]```

# SYNOPSIS

**blender** [_options_] [_file_]

# DESCRIPTION

**blender** 是一套免费开源的 3D 创作套件。它覆盖完整的 3D 流程：建模、绑定、动画、模拟、渲染、合成、运动跟踪以及视频剪辑。

该软件被用于制作动画电影、视觉特效、游戏和 3D 打印模型。

# PARAMETERS

**-b**, **--background**
> 在后台运行（无 GUI）

**-a**, **--render-anim**
> 渲染动画

**-f**, **--render-frame** _n_
> 渲染指定帧

**-s** _n_ **-e** _n_
> 设置起始帧和结束帧

**-o** _path_
> 设置渲染输出路径

**--python** _file_
> 执行 Python 脚本

**--python-expr** _expr_
> 执行 Python 表达式

**-x** _0|1_
> 是否为渲染输出名添加文件格式扩展名（use-extension）

**-E** _engine_
> 渲染引擎：CYCLES、BLENDER_EEVEE 或 BLENDER_WORKBENCH（运行 `blender -E help` 可列出）

**-P** _file_
> 运行指定的 Python 脚本文件（与 --python 相同）

**--factory-startup**
> 跳过读取用户配置和启动文件，以获得干净的会话

**--version**
> 打印 Blender 版本并退出

# BACKGROUND RENDERING

```bash
# 渲染动画
blender -b scene.blend -a

# 渲染第 1-100 帧
blender -b scene.blend -s 1 -e 100 -a

# 将单帧渲染为 PNG
blender -b scene.blend -o //output_#### -f 1

# 使用 Cycles 引擎
blender -b scene.blend -E CYCLES -a
```

# PYTHON SCRIPTING

```python
# script.py
import bpy

# 创建立方体
bpy.ops.mesh.primitive_cube_add()

# 渲染
bpy.ops.render.render(write_still=True)
```

# CAVEATS

资源占用高。学习曲线陡峭。后台渲染需要所有依赖项。GPU 渲染需要兼容的驱动程序。Python API 与版本相关。

# HISTORY

**Blender** 由 Ton Roosendaal 于 **1995 年**作为公司内部软件创建，**2002 年**以 GPL 许可证开源，此后已成为最受欢迎的 3D 创作工具之一。

注意参数顺序很重要：参数从左到右依次求值，因此 .blend 文件必须写在作用于它的渲染标志之前。

# INSTALL

```apt: sudo apt install blender```

```dnf: sudo dnf install blender```

```pacman: sudo pacman -S blender```

```apk: sudo apk add blender```

```zypper: sudo zypper install blender```

```nix: nix profile install nixpkgs#blender```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gimp](/man/gimp)(1), [inkscape](/man/inkscape)(1), [krita](/man/krita)(1), [ffmpeg](/man/ffmpeg)(1)

# RESOURCES

```[Source code](https://projects.blender.org/blender/blender)```

```[Homepage](https://www.blender.org/)```

```[Documentation](https://docs.blender.org/manual/en/latest/advanced/command_line/index.html)```

<!-- verified: 2026-06-19 -->
