# TAGLINE

基于 Typst 的零配置 Markdown 转 PDF 文档引擎

# TLDR

**从 README.md 生成 PDF**，零配置

```doc-engine build```

**转换指定文件**并覆盖标题和作者

```doc-engine build CONTRIBUTING.md -o guide.pdf -t "Guide" -a "Team"```

**使用其他模板**和强调色

```doc-engine build --template modern --accent teal```

**检查 Markdown 错误**而不生成 PDF

```doc-engine build --dry-run```

通过 pipx **安装**

```pipx install doc-engine-cli```

# SYNOPSIS

**doc-engine** build [INPUT_FILE] [options]

**doc-engine** info

**doc-engine** --help | --version

# DESCRIPTION

**doc-engine** 是一个 CLI 工具，它以 Typst 作为渲染后端，将 Markdown 文件转换为具有专业排版的 PDF 文档。它能自动检测 README.md、从 Git 提取元数据，并生成高质量的技术或学术报告，包含封面、目录和带语法高亮的代码。

它不需要 LaTeX、Pandoc 或手动配置。该工具内置五种模板并支持自定义强调色。还能对源文件进行错误检查，并给出精确的行/列报告。

# PARAMETERS

**build** [_INPUT_FILE_]

> 将 Markdown 文件转换为 PDF。默认自动检测当前目录中的 README.md。

**-o**, **--output** _file.pdf_

> 输出文件路径。默认：<input>_doc.pdf

**-t**, **--title** _title_

> 文档标题。默认取第一个 # 标题，或由 Git 推导得出。

**-a**, **--author** _name_

> 作者名。默认取 `git config user.name`。

**--template** _name_

> 模板：academic（默认）、modern、minimal、technical、book。

**--accent** _color_

> 强调色（十六进制值或命名颜色：blue、teal、rose 等）。

**--bib** _file.bib_

> 参考文献文件，用于生成 IEEE 风格的参考文献部分。

**--dry-run**

> 校验 Markdown 并报告错误，不生成 PDF。

**--open**

> 在 PDF 生成后打开它。

**--no-branding**

> 在页脚中省略 "doc-engine" 署名。

# EXAMPLES

在项目目录中进行基本的零配置转换：

```doc-engine build```

使用自定义选项生成：

```doc-engine build docs/api.md -o api.pdf --template technical --accent "#7c3aed"```

# CAVEATS

Markdown 中的图片只渲染为替代文本（不下载也不嵌入远程图片）。复杂排版可能需要人工检查输出 PDF。需要 Python 3.10+ 和 Typst 的 Python 绑定（会自动安装）。

# SEE ALSO

[typst](/man/typst)(1), [pandoc](/man/pandoc)(1), [weasyprint](/man/weasyprint)(1)

# RESOURCES

```[Source code](https://github.com/leonardosalasd/doc-engine-cli)```

```[Documentation](https://github.com/leonardosalasd/doc-engine-cli#readme)```

<!-- verified: 2026-07-11 -->
