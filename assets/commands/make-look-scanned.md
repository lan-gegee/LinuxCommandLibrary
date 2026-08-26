# TAGLINE

让 PDF 看起来像实体扫描件

# TLDR

**处理** PDF，生成一份扫描件外观的副本

```make-look-scanned [input.pdf]```

**指定**输出文件路径

```make-look-scanned [input.pdf] -o [output.pdf]```

**施加重度劣化效果**，获得更破旧的外观

```make-look-scanned [input.pdf] --noise 0.4 --skew 2.5 --jpeg-quality 30```

**使用配置文件中的预设**

```make-look-scanned [input.pdf] --preset [preset_name]```

**设置固定随机种子**以获得可复现的输出

```make-look-scanned [input.pdf] --seed [42]```

# SYNOPSIS

**make-look-scanned** [_flags_] _input.pdf_

# PARAMETERS

**-o** _file_
> 输出文件路径（默认：`<input>.scanned.pdf`）

**--preset** _name_
> 使用 `config.toml` 中定义的命名预设

**--seed** _n_
> 用于可复现性的随机种子（默认：输入 PDF 的内容哈希）

**--force**
> 不提示直接覆盖已存在的输出文件

**--dpi** _n_
> 渲染分辨率，单位 DPI（默认：150）

**--skew** _degrees_
> 页面最大旋转角度，单位度（默认：0.6；0 表示禁用）

**--grayscale**
> 将颜色去饱和以模拟灰度扫描仪（默认：true）

**--paper-tone** _n_
> 暖色纸张色调强度，0-1（默认：0.6）

**--noise** _n_
> 扫描仪颗粒效果强度，0-1（默认：0.08）

**--blur** _sigma_
> 散焦高斯 sigma（默认：0.4）

**--edge-shadow** _n_
> 边缘暗角强度，0-1（默认：0.15）

**--jpeg-quality** _n_
> JPEG 压缩质量，1-100（默认：70；越低伪影越多）

# DESCRIPTION

**make-look-scanned** 以选定的 DPI 渲染 PDF 的每一页，然后应用一条可配置的视觉劣化效果流水线，使其呈现实体扫描件的外观：轻微的页面倾斜、灰度转换、暖色纸张色调、扫描仪颗粒、高斯散焦、边缘暗角以及 JPEG 压缩伪影。

输出默认是确定性的：随机种子由输入文件的内容哈希派生，因此同一份 PDF 总是产生完全相同的输出。可以通过 `--seed` 指定自定义种子来生成不同的变体。

命名预设可以存储在 `config.toml` 文件中，并通过 `--preset` 选用，从而定义并复用多种劣化配置（轻度扫描、重度扫描、老旧文档等）。将任何数值型效果参数设为 0 即可完全禁用该效果。

该工具还提供基于浏览器的 WebAssembly 版本，无需安装即可一次性使用。

# CAVEATS

从源码构建需要 Go 工具链和 C 编译器。以高 DPI 处理大型 PDF 会显著增加内存占用和处理时间。该工具生成新的 PDF 文件，不会修改原始文件。

# SEE ALSO

[gs](/man/gs)(1), [pdftk](/man/pdftk)(1), [convert](/man/convert)(1)

# RESOURCES

```[Source code](https://github.com/overflowy/make-look-scanned)```

<!-- verified: 2026-06-20 -->
