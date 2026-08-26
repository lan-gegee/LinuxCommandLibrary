# TAGLINE

创建数学动画

# TLDR

**渲染场景**

```manim [script.py] [SceneName]```

**以低质量预览**

```manim -pql [script.py] [SceneName]```

**渲染高质量视频**

```manim -pqh [script.py] [SceneName]```

**输出 GIF**

```manim --format gif [script.py] [SceneName]```

**保存最后一帧**

```manim -s [script.py] [SceneName]```

**列出场景**

```manim [script.py]```

# SYNOPSIS

**manim** [_options_] _script_ [_scene_]

# PARAMETERS

_SCRIPT_
> Python 脚本文件。

_SCENE_
> 场景类名。

**-p**
> 渲染后预览。

**-q** _QUALITY_
> 质量（l、m、h、k）。

**-s**
> 仅保存最后一帧。

**--format** _FMT_
> 输出格式（mp4、gif、webm）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**manim** 用于创建数学动画。它将用 Python 定义的场景渲染为视频。

该工具支持 LaTeX，为数学概念制作动画。最初为教学视频而创建。

# CAVEATS

需要 FFmpeg 和 LaTeX。渲染可能较慢。需要具备 Python 知识。

# HISTORY

Manim 由 **Grant Sanderson**（3Blue1Brown）为其 YouTube 数学讲解视频而创建。

# INSTALL

```brew: brew install manim```

```nix: nix profile install nixpkgs#manim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [pdflatex](/man/pdflatex)(1), [python](/man/python)(1)
