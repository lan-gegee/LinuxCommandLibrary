# TAGLINE

从 PFB 中提取 AFM

# TLDR

**将 PFB 转换为 AFM**

```pf2afm [font.pfb] > [font.afm]```

**处理多个字体**

```for f in *.pfb; do pf2afm "$f" > "${f%.pfb}.afm"; done```

# SYNOPSIS

**pf2afm** _font_

# PARAMETERS

_FONT_
> 从中提取度量信息的 PostScript Type 1 字体文件（.pfb 或 .pfa）。

# DESCRIPTION

**pf2afm** 从 PostScript Type 1 字体的二进制（.pfb）或 ASCII（.pfa）文件中提取 Adobe 字体度量（AFM）数据。它把生成的 AFM 内容写入标准输出，通常会将其重定向到 .afm 文件。

该工具是一个小型包装器，内部调用 Ghostscript 并运行其自带的 **pf2afm.ps** 脚本。当只有字体的二进制形式可用，而 TeX、Ghostscript 或其他排版工具又需要 AFM 度量数据时，它非常有用。

# CAVEATS

属于 Ghostscript。针对 PostScript Type 1 字体。仅做度量信息提取。

# HISTORY

pf2afm 属于 **Ghostscript**，用于提取字体度量信息。

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

[gs](/man/gs)(1), [printafm](/man/printafm)(1), [afm2tfm](/man/afm2tfm)(1)
