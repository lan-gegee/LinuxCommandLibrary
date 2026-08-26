# TAGLINE

将 PostScript 转换为 Encapsulated PostScript

# TLDR

**将 PS 转换为 EPSI**

```ps2epsi [input.ps] [output.epsi]```

**转换并生成预览**

```ps2epsi [input.ps]```

# SYNOPSIS

**ps2epsi** _input_ [_output_]

# PARAMETERS

_INPUT_
> 输入的 PostScript 文件。

_OUTPUT_
> 输出的 EPSI 文件。

# DESCRIPTION

**ps2epsi** 通过添加 ASCII 预览图像头，将 PostScript 文件转换为 Encapsulated PostScript Interchange（EPSI）格式。EPSI 格式内嵌了一幅低分辨率位图预览，应用无需 PostScript 解释器即可显示它，因此对于需要显示可视化占位图的文档排版程序非常有用。

该工具是 Ghostscript 套件的一部分，内部使用 Ghostscript 渲染预览图像。如果未指定输出文件名，输出文件将以输入文件命名并使用 **.epsi** 扩展名。

# CAVEATS

Ghostscript 套件的一部分。生成位图预览。

# HISTORY

ps2epsi 是 **Ghostscript** 中负责 EPSI 转换的工具。

# INSTALL

```apt: sudo apt install ghostscript```

```dnf: sudo dnf install ghostscript```

```pacman: sudo pacman -S ghostscript```

```apk: sudo apk add ghostscript```

```zypper: sudo zypper install ghostscript```

```brew: brew install ghostscript```

```nix: nix profile install nixpkgs#ghostscript```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gs](/man/gs)(1), [ps2pdf](/man/ps2pdf)(1), [ps2ps](/man/ps2ps)(1)
