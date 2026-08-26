# TAGLINE

LibreOffice 的文字处理组件

# TLDR

**启动 Writer**

```lowriter```

**打开文档**

```lowriter [document.odt]```

**转换为 PDF**

```lowriter --convert-to pdf [document.odt]```

**转换为 DOCX**

```lowriter --convert-to docx [document.odt]```

**批量转换多个文件**

```lowriter --convert-to pdf --outdir [output/] [*.odt]```

**打印文档**

```lowriter -p [document.odt]```

# SYNOPSIS

**lowriter** [_options_] [_files_...]

# PARAMETERS

**--convert-to** _format_
> 转换为指定格式。

**--outdir** _dir_
> 转换结果的输出目录。

**-p**
> 打印文档。

**--pt** _printer_
> 用指定的打印机打印。

**--headless**
> 无 GUI 运行。

**--view**
> 以只读模式打开。

# DESCRIPTION

**lowriter** 是 LibreOffice 的文字处理组件，提供与 Microsoft Word 格式兼容的全功能文档编辑、排版和发布能力。

其命令行接口支持批量转换和脚本化操作。

# SUPPORTED FORMATS

```
Input:  ODT, DOC, DOCX, RTF, TXT, HTML
Output: PDF, ODT, DOCX, RTF, TXT, HTML
```

# CAVEATS

GUI 需要图形显示环境（服务器上请使用 --headless）。转换质量取决于格式的复杂程度。大文档可能需要更多内存。

# HISTORY

LibreOffice Writer 由 OpenOffice.org Writer 演变而来，后者源自 **Star Division** 公司的 StarWriter（该公司于 1999 年被 Sun Microsystems 收购）。LibreOffice 于 **2010 年**从 OpenOffice.org 分叉而来。

# INSTALL

```apt: sudo apt install libreoffice-writer```

```dnf: sudo dnf install libreoffice-writer```

```apk: sudo apk add libreoffice-writer```

```zypper: sudo zypper install libreoffice-writer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[libreoffice](/man/libreoffice)(1), [unoconv](/man/unoconv)(1)
