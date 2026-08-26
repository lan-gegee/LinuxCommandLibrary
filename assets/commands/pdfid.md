# TAGLINE

扫描 PDF 文件中可能表示恶意内容的关键字

# TLDR

**分析 PDF 结构**

```pdfid.py [file.pdf]```

**扫描多个文件**

```pdfid.py [file1.pdf] [file2.pdf]```

**报告熵与 EOF 统计信息（额外分析）**

```pdfid.py --extra [file.pdf]```

**递归扫描目录中的 PDF**

```pdfid.py --scan [path/to/directory]```

**只显示非零的关键字计数**

```pdfid.py --nozero [file.pdf]```

**创建解除武装的副本（中和 /JS、/JavaScript、/AA、/OpenAction、/Launch）**

```pdfid.py --disarm [file.pdf]```

**报告所有名称，而不只是默认关键字列表**

```pdfid.py --all [file.pdf]```

# SYNOPSIS

**pdfid.py** [_options_] _file_...

# PARAMETERS

**--all**
> 检测 PDF 中的所有名称，而不只是预定义关键字列表。

**--extra**
> 计算熵和 EOF 统计信息。

**--disarm**
> 写出一份危险元素已被中和的解除武装 PDF 副本。

**--force**
> 即使文件缺少有效的 %PDF 头也进行处理。

**--nozero**
> 在输出中隐藏计数为零的关键字。

**--output** _FILE_
> 将结果写入指定文件。

**--scan**
> 递归扫描目录中的 PDF 文件。

**--plugins** _PLUGINS_
> 加载一个或多个插件模块（逗号分隔）以进行扩展分析。

**--pluginoptions** _OPTIONS_
> 向已加载的插件传递选项。

**--select** _EXPR_
> 使用 Python 表达式过滤结果。

**--csv**
> 以逗号分隔值格式化输出。

**--literalfilenames**
> 按字面处理文件名，不做通配符展开。

**--verbose**
> 显示详细的错误消息和堆栈跟踪。

# DESCRIPTION

**pdfid** 扫描 PDF 文件中可能表示恶意内容的关键字。它统计 JavaScript、嵌入文件、启动动作及其他可疑元素的出现次数。

# OUTPUT

```
PDFiD 0.2.7 document.pdf
 PDF Header: %PDF-1.4
 obj                   15
 endobj                15
 stream                 3
 /Page                  2
 /JS                    0
 /JavaScript            0
 /OpenAction            0
 /Launch                0
```

# SUSPICIOUS KEYWORDS

```
/JS, /JavaScript  - Embedded JavaScript
/AA, /OpenAction  - Automatic/additional actions
/Launch           - Launch external programs
/EmbeddedFile     - Embedded files
/AcroForm, /XFA   - Interactive forms
/JBIG2Decode      - JBIG2 filter (historical exploit surface)
/RichMedia        - Flash/rich media content
/ObjStm, /Encrypt - Object streams / encryption
```

混淆变体（十六进制编码的名称）会在明文计数旁以括号形式报告，例如 `/JS 1(1)` 表示出现一次且其中一次为混淆形式。

# CAVEATS

关键字的存在并不能确认恶意意图。建议进一步使用 pdf-parser 分析。属于 PDF 分析工具集。

# HISTORY

pdfid 由 **Didier Stevens** 创建，是其面向安全研究的 PDF 分析工具的一部分。

# INSTALL

```nix: nix profile install nixpkgs#pdfid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdf-parser](/man/pdf-parser)(1), [pdfinfo](/man/pdfinfo)(1)
