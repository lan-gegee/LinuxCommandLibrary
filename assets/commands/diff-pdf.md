# TAGLINE

可视化 PDF 对比工具

# TLDR

**可视化对比**两个 PDF

```diff-pdf [file1.pdf] [file2.pdf]```

**将差异输出**到新 PDF

```diff-pdf --output-diff=[diff.pdf] [file1.pdf] [file2.pdf]```

**显示可视化比较**

```diff-pdf --view [file1.pdf] [file2.pdf]```

在输出中用矩形**标记差异**

```diff-pdf --mark-differences --output-diff=[diff.pdf] [file1.pdf] [file2.pdf]```

**设置每个颜色通道的容差**

```diff-pdf --channel-tolerance=[10] [file1.pdf] [file2.pdf]```

# SYNOPSIS

**diff-pdf** [_options_] _file1.pdf_ _file2.pdf_

# PARAMETERS

**--output-diff** _file_
> 将视觉差异输出到 PDF 文件。

**--view**
> 在交互式查看器窗口中打开比较结果。

**-m**, **--mark-differences**
> 额外用矩形标记左侧页面上的差异。

**-g**, **--grayscale**
> 以灰度渲染页面，使差异部分以彩色呈现。

**--channel-tolerance** _N_
> 每个颜色通道允许最多 N（0-255）的差异，超过才标记该像素。

**--per-page-pixel-tolerance** _N_
> 每页允许最多 N 个差异像素，超过才将该页报告为不同。

**--dpi** _N_
> 光栅化分辨率，单位 DPI（默认：300）。

**-s**, **--skip-identical**
> 在输出的 PDF 中跳过完全相同的页面。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**diff-pdf** 以可视方式比较两个 PDF 文件，渲染每一页并逐像素进行比较。与基于文本的 diff 工具不同，它能捕捉文本比较中不可见的视觉差异，包括格式、字体、图像和布局的变化。

该工具将两个 PDF 的每一页光栅化为图像并进行比较。它可以生成用颜色高亮变化的差异 PDF，也可以打开交互式查看器进行并排对比。--channel-tolerance 和 --per-page-pixel-tolerance 选项可以忽略微小的渲染差异。

它特别适合比较内容相同但视觉呈现不同的文档版本，或用于验证文档生成输出一致性的质量保证流程。文件相同时返回退出码 0，不同时返回 1，因此也适用于自动化测试。

# INSTALL

```apt: sudo apt install diff-pdf-wx```

```dnf: sudo dnf install diff-pdf```

```pacman: sudo pacman -S diff-pdf```

```apk: sudo apk add diff-pdf```

```zypper: sudo zypper install diff-pdf```

```brew: brew install diff-pdf```

```nix: nix profile install nixpkgs#diff-pdf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdftk](/man/pdftk)(1), [diff](/man/diff)(1), [cpdf](/man/cpdf)(1)

# RESOURCES

```[Source code](https://github.com/vslavik/diff-pdf)```

```[Homepage](https://vslavik.github.io/diff-pdf/)```

<!-- verified: 2026-07-11 -->
