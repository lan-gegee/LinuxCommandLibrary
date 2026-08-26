# TAGLINE

将 PDF 内容提取为 JSON 格式

# TLDR

**将 PDF 转换为 JSON**

```pdf2json [input.pdf] [output.json]```

**仅转换第一页**

```pdf2json -f [1] -l [1] [input.pdf] [output.json]```

**包含表单字段**

```pdf2json -form [input.pdf] [output.json]```

**将各页拆分为单独文件**

```pdf2json -split [input.pdf] [output_prefix]```

# SYNOPSIS

**pdf2json** [_options_] _input.pdf_ [_output.json_]

# PARAMETERS

**-f** _num_
> 第一页。

**-l** _num_
> 最后一页。

**-form**
> 包含表单数据。

**-split**
> 每页一个文件。

**-enc** _encoding_
> 文本编码。

# DESCRIPTION

**pdf2json** 将 PDF 内容提取为 JSON 格式。它捕获文本、位置、字体和表单字段，使程序能够访问 PDF 数据。

# OUTPUT STRUCTURE

```json
{
  "pages": [
    {
      "width": 612,
      "height": 792,
      "texts": [
        {"x": 72, "y": 720, "text": "Hello"}
      ]
    }
  ]
}
```

# CAVEATS

文本提取质量参差不齐。复杂版式可能无法保留结构。不提取图像。

# HISTORY

pdf2json 基于 PDF.js 或类似库，为 PDF 处理流水线提供 JSON 导出能力。

# INSTALL

```brew: brew install pdf2json```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdftotext](/man/pdftotext)(1), [pdftohtml](/man/pdftohtml)(1), [poppler-utils](/man/poppler-utils)(1)
