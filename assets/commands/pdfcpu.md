# TAGLINE

命令行 PDF 处理工具集

# TLDR

**校验** PDF

```pdfcpu validate [input.pdf]```

将多个 PDF **合并**为一个文件

```pdfcpu merge [out.pdf] [in1.pdf] [in2.pdf]```

将 PDF **拆分**为单页

```pdfcpu split [input.pdf] [out_dir]```

**优化**（压缩）PDF

```pdfcpu optimize [input.pdf] [out.pdf]```

**加密** PDF

```pdfcpu encrypt -upw [user] -opw [owner] [input.pdf]```

**添加水印**文字

```pdfcpu watermark add -mode text -- "[text]" [input.pdf] [out.pdf]```

**提取**页面到新 PDF

```pdfcpu trim -pages [1-3] [input.pdf] [out.pdf]```

# SYNOPSIS

**pdfcpu** *command* [*options*] [*file*...]

# DESCRIPTION

**pdfcpu** 是用 Go 编写的 PDF 工具集。它同时提供 Go API 和丰富的 CLI，可用于校验、合并、拆分、优化、加密、盖章、加水印、旋转、裁剪、提取图像/字体、管理书签等众多 PDF 操作，且无需 Ghostscript 或 Adobe 工具。

每个动词（**validate**、**merge**、**split**、**optimize**、**encrypt**、**watermark**、**stamp**、**pages**、**trim**、**rotate**、**extract** 等）都有自己的标志。运行 **pdfcpu** *command* **help** 或访问 https://pdfcpu.io 查看完整的命令矩阵。

# PARAMETERS

**validate** *file*

> 检查 PDF 完整性 / 相关合规性检查。

**merge** *out* *in*...

> 将输入的 PDF 串联为 *out*。

**split** *file* *out_dir*

> 拆分为页面级 PDF。

**optimize** *in* [*out*]

> 通过资源优化减小体积。

**encrypt** / **decrypt** / **changeopw** / **changeupw**

> 密码与权限管理（**-upw**、**-opw**）。

**watermark** / **stamp**

> 添加文本或图像水印/印章。

**trim** **-pages** *range*

> 保留所选页面。

**rotate**, **resize**, **nup**, **poster**, **booklet**

> 页面几何与拼版辅助命令。

**extract**

> 提取图像、字体、内容、页面等。

**version**, **help**

> 版本与命令帮助。

# CAVEATS

并非所有 PDF 特性（尤其是特殊加密、签名表单或专有结构）都得到完整支持。批量转换前务必保留原件。某些操作会重写文件结构，可能影响高级交互特性。

# INSTALL

```apk: sudo apk add pdfcpu```

```brew: brew install pdfcpu```

```nix: nix profile install nixpkgs#pdfcpu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qpdf](/man/qpdf)(1), [pdftk](/man/pdftk)(1), [gs](/man/gs)(1), [mutool](/man/mutool)(1)

# RESOURCES

```[Source code](https://github.com/pdfcpu/pdfcpu)```

```[Homepage](https://pdfcpu.io)```

```[Documentation](https://pdfcpu.io)```

<!-- verified: 2026-07-19 -->
