# TAGLINE

将终端会话录制为 SVG 动画

# TLDR

**开始录制**（退出 shell 或按 Ctrl-D 停止）

```termtosvg```

**录制到指定文件**

```termtosvg [out.svg]```

输出**静态帧**而非动画

```termtosvg --still-frames [outdir]```

**渲染 asciicast**

```termtosvg render [recording.cast]```

# SYNOPSIS

**termtosvg** [*output*] [*options*]
**termtosvg** **render** *castfile* [*options*]

# DESCRIPTION

**termtosvg** 是一款用 Python 编写的 Unix 终端录制工具，可将命令行会话渲染为独立的 SVG 动画（或静态帧）。录制的文件轻量且可嵌入项目页面。通过 SVG 模板可自定义配色主题和 UI 外框。它还能渲染 **asciinema** 的 asciicast 文件。

使用 **pip3 install termtosvg**（Python >= 3.5）安装，也可通过发行版软件包安装。以 **termtosvg** 或 **python3 -m termtosvg** 方式调用。

**维护状态：** 自 2020 年 6 月起上游仓库已只读并停止维护。如果你需要活跃支持，新项目请改用 **asciinema** 及其他渲染器。

# PARAMETERS

*output*

> 实时录制输出的 SVG 路径（可选；默认使用临时/生成的名称，具体取决于版本）。

**--still-frames** [*dir*]

> 在支持的情况下导出静态帧而非动画（或同时导出两者）。

**render** *file.cast*

> 渲染已有的 asciicast。

模板和几何参数因版本而异；参见 **termtosvg --help** 以及仓库中的模板 man 页面。

# CAVEATS

自 2020 年起不再维护。仅支持类 Unix 系统（Linux、macOS、BSD）。SVG 播放效果取决于查看器；非常长的会话会产生很大的文件。如需活跃维护的终端录制工具，可考虑 **asciinema**。

# INSTALL

```nix: nix profile install nixpkgs#termtosvg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[asciinema](/man/asciinema)(1), [script](/man/script)(1), [ttyrec](/man/ttyrec)(1), [vhs](/man/vhs)(1)

# RESOURCES

```[Source code](https://github.com/nbedos/termtosvg)```

```[Homepage](https://nbedos.github.io/termtosvg/)```

<!-- verified: 2026-07-19 -->
