# TAGLINE

groff 的封装器，用于解析 mm 文档中的交叉引用

# TLDR

**处理 mm 文档**（默认输出：stdout 上的 PostScript）

```mmroff [document.mm]```

**渲染为 PostScript**（把 -Tps 透传给 groff）

```mmroff -Tps [document.mm] > [document.ps]```

**渲染为 PDF**

```mmroff -Tpdf [document.mm] > [document.pdf]```

**渲染为 HTML 以便预览**

```mmroff -Thtml [document.mm] > [document.html]```

**只构建交叉引用文件**然后退出

```mmroff -x [document.mm]```

# SYNOPSIS

**mmroff** [**-x**] _groff_argument_...

**mmroff** **--help**

**mmroff** **--version**

# PARAMETERS

_GROFF_ARGUMENT_
> **groff** 接受的任何选项或输入文件（例如 **-Tps**、**-Tpdf**、**-Thtml**、输入文件名）。**-mm** 宏包会被自动添加。

**-x**
> 构建或更新交叉引用/索引文件，然后退出，不产生排版输出。

**--help**
> 显示用法并退出。

**--version**
> 显示版本并退出。

# DESCRIPTION

**mmroff** 是围绕 **groff** 的一个小型 shell 封装器，负责处理 mm 的交叉引用和索引。它会调用两次 **groff -mm**：第一次带 **-z -rRef=1** 来填充交叉引用和索引文件，第二次正常执行以完成文档排版。该封装器还会展开 PSPIC 图片包含。

对于不使用交叉引用、索引或内嵌 PostScript 图片的 mm 文档，直接调用 **groff -mm** 是等价的，而且稍快一些。

# CAVEATS

它是 GNU **groff** 的一部分。输出格式用 **-T**_device_ 选择，与 groff 本身完全一致；该封装器不会自创格式选项。PDF 支持需要 groff 1.23 引入的 **-Tpdf** 设备。用旧版 AT&T mm 宏编写的文档与 GNU mm 并非 100% 兼容。

# HISTORY

**mmroff** 由瑞典隆德的 **Jörgen Hägg** 编写，是贡献给 **groff** 的 GNU **mm** 宏包的一部分。

# INSTALL

```apt: sudo apt install groff```

```dnf: sudo dnf install groff```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groff](/man/groff)(1), [nroff](/man/nroff)(1), [troff](/man/troff)(1)
