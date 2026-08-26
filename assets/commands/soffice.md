# TAGLINE

LibreOffice 套件启动器与转换器

# TLDR

**打开 LibreOffice**

```soffice```

**打开文档**

```soffice [document.odt]```

**转换为 PDF**

```soffice --convert-to pdf [document.docx]```

**无界面转换**

```soffice --headless --convert-to pdf [document.docx]```

**启动 Writer**

```soffice --writer```

**启动 Calc**

```soffice --calc```

**以安全模式启动**

```soffice --safe-mode```

# SYNOPSIS

**soffice** [_--headless_] [_--convert-to format_] [_options_] [_files_]

# PARAMETERS

**--headless**
> 无图形界面。

**--convert-to** _FMT_
> 转换格式。

**--writer**
> 启动 Writer。

**--calc**
> 启动 Calc。

**--impress**
> 启动 Impress。

**--safe-mode**
> 以安全模式启动。

**--outdir** _DIR_
> 输出目录。

# DESCRIPTION

**soffice** 是 LibreOffice（开源办公生产力套件）的主启动器。它会根据文件类型或显式指定的模块，在 Writer（文字处理）、Calc（电子表格）、Impress（演示文稿）、Draw（矢量图形）及其他组件中打开文档。

**--headless** 标志让 LibreOffice 在无图形界面的情况下运行，从而支持服务端文档处理和脚本化操作。结合 **--convert-to** 使用时，可以在 PDF、DOCX、XLSX、HTML 等众多格式之间进行强大的批量文档转换。

无界面模式常用于自动化流水线中：转换文档、从模板生成 PDF 或执行邮件合并，全程无需用户交互。单次调用即可处理多个文件，并可通过 **--outdir** 指定输出目录。

# CAVEATS

应用程序较重。转换可能较慢。格式还原度参差不齐。

# HISTORY

**soffice** 是 **LibreOffice**（从 OpenOffice.org 分支而来的免费办公套件）的主启动器。

# INSTALL

```apk: sudo apk add libreoffice-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[libreoffice](/man/libreoffice)(1), [lowriter](/man/lowriter)(1), [unoconv](/man/unoconv)(1)
