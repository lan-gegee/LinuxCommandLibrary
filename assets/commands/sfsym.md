# TAGLINE

将 Apple SF Symbols 导出为 SVG、PDF 或 PNG

# TLDR

通过 Homebrew 从项目 tap **安装**

```brew install yapstudios/tap/sfsym```

**将符号导出为 SVG**（格式由扩展名推断）

```sfsym export [heart.fill] -o [heart.svg]```

**导出 PNG**，使用自定义颜色和画布尺寸

```sfsym export [star.fill] --color [#FFD60A] --size [48] -o [star.png]```

**渲染分层调色（palette）符号**

```sfsym export [person.2.fill] --mode [palette] --palette [#4F46E5,#22D3EE] -o [out.svg]```

**列出所有可用符号**（8300+）

```sfsym list```

按关键字**搜索目录**

```sfsym list --search [magnifyingglass]```

**浏览某一类别中的符号**

```sfsym list --category [weather] --limit [10]```

**从 stdin 批量处理多次导出**（约 800 次/秒）

```cat [jobs.txt] | sfsym batch```

# SYNOPSIS

**sfsym** _command_ [_options_]

# COMMANDS

**export** _NAME_ **-o** _FILE_
> 渲染单个 SF Symbol。除非指定 **-f**，否则输出格式（svg/pdf/png）由文件扩展名推断。

**batch**
> 从 stdin 读取重复的 _export_ 调用，每行一条。

**list**
> 枚举符号名称；支持 **--search**、**--category**、**--limit**。

**info** _NAME_
> 以 JSON 形式转储符号的几何信息和图层元数据。

**modes** _NAME_
> 列出符号支持的渲染模式。

**colors**
> 打印 **--color** 接受的所有命名颜色。

**categories**
> 打印 Apple 的符号分类体系。

**schema**
> 面向自动化的机器可读 CLI 描述。

# PARAMETERS

**-f** _FORMAT_
> 强制指定输出格式：_svg_、_pdf_ 或 _png_。

**--mode** _MODE_
> 渲染模式：_monochrome_、_hierarchical_、_palette_、_multicolor_。

**--weight** _WEIGHT_
> 符号的字重：_ultralight_、_thin_、_light_、_regular_、_medium_、_semibold_、_bold_、_heavy_、_black_。

**--size** _N_
> 画布尺寸，单位为点（1–2048）。PNG 输出采用 2× 像素密度。

**--color** _HEX_|_NAME_
> 主颜色。接受短/长十六进制（_#RGB_、_#RRGGBB_、_#RRGGBBAA_）或命名的系统颜色。

**--palette** _C1,C2,..._
> 与 **--mode palette** 配合使用的逗号分隔调色板颜色。

**-o** _PATH_
> 输出文件；**-** 表示写入 stdout。

**--json**
> 为 info/list/schema 生成结构化输出。

# DESCRIPTION

**sfsym** 是一款命令行工具，直接通过操作系统自带的符号渲染器渲染 Apple 的 **SF Symbols**，无需 Xcode。它可以生成任意字重、模式、颜色和尺寸的清晰 SVG、PDF 或 PNG 素材——适用于设计流水线、文档生成、图标构建步骤以及 Web 导出。

该工具捆绑了一个通用二进制文件，可在 Apple Silicon 和 Intel Mac 上运行，因此可以直接放入 CI。对于批量工作流，**batch** 子命令接受 stdin 请求，因为它复用单一渲染上下文，速度可达约 **每秒 800 次导出**。机器可读的元数据可通过 **info**、**modes** 和 **schema** 获得，使 sfsym 易于从脚本和编辑器插件中调用。

# CAVEATS

需要 **macOS 13 (Ventura) 或更高版本**；符号目录取决于宿主操作系统提供的版本，因此较新的符号只能在相应的 macOS 版本上渲染。Apple 的 **SF Symbols 许可证**限制这些字形的再分发——导出结果仅供 Apple 平台内部使用，或需获得相应许可。

# HISTORY

**sfsym** 由 **Yap Studios** 开发，基于 Apple 于 2019 年推出的公开 SF Symbols 渲染 API 构建，以 MIT 许可证发布。

# SEE ALSO

[rsvg-convert](/man/rsvg-convert)(1), [inkscape](/man/inkscape)(1), [svgo](/man/svgo)(1), [imagemagick](/man/imagemagick)(1)
