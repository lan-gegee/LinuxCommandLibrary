# TAGLINE

面向 Python 的确定性无障碍 PDF 生成工具

# TLDR

**安装**该软件包（提供 **emboss** CLI）

```pip install emboss-pdf```

将多文件 Markdown 目录**构建**为一个 PDF

```emboss build [path/to/docs] -o [handbook.pdf]```

**校验**结构完整性或 PDF/UA / PDF/A 合规性

```emboss verify [report.pdf]```

```emboss verify [report.pdf] --conformance ua1```

将两个 PDF **对比**生成一份带修订标记的 PDF

```emboss diff [old.pdf] [new.pdf] -o [redline.pdf]```

根据内嵌的规格说明**复现**自描述 PDF

```emboss reproduce [report.pdf]```

对外分享前**剥离**内嵌规格与内部 id

```emboss strip [report.pdf] -o [external.pdf]```

# SYNOPSIS

**emboss** _command_ [_options_] [_args_]

# DESCRIPTION

**emboss** 是 Emboss（PyPI 上的 **emboss-pdf**）的命令行界面。Emboss 是一个纯 Python 排版引擎，可将声明式规格或 Markdown 转换为带 PDF/UA 标签的确定性 PDF。同一个语义模型同时驱动版面布局与结构树，因此无障碍标签不会偏离可见内容。当输入相同时，输出被设计为逐字节一致。

库 API（**Document**、Fluent 构建器、**from_markdown** / **from_json**）是主要的创作入口；CLI 则覆盖批量构建、验证（若安装了真正的 **veraPDF** 还可调用它）、文档对比标记、可复现性检查，以及在分发前剥离内嵌来源信息。

可选扩展提供 pydantic LLM 模式、pikepdf 验证辅助、用于签名的 cryptography，以及面向智能体工作流的 MCP 服务器接口。

# COMMANDS

**build** _dir_ **-o** _out.pdf_

> 将 _dir_ 下的 Markdown（及相关源文件）拼接为一个 PDF。可选的 **.order** 文件显式列出文件顺序；数字前缀按字母序排序。

**verify** _file.pdf_ [**--conformance** ua1|2b|3b]

> 结构检查；当 **verapdf** 位于 **PATH** 中（或设置了 **VERAPDF_PATH**）时，可调用 veraPDF 进行 PDF/UA-1 / PDF/A-2b / PDF/A-3b 验证。

**diff** _old.pdf_ _new.pdf_ **-o** _redline.pdf_

> 基于稳定的节点 id，生成一份标出新增/删除/修改块的对比 PDF。

**reproduce** _file.pdf_

> 恢复内嵌的 EmbossSpec（或回退到结构树），重新渲染并报告结构一致性。

**strip** _file.pdf_ **-o** _out.pdf_

> 移除内嵌文件、部分元数据及结构树节点 id，以便对外分享。

# CAVEATS

不支持复杂文字排版（阿拉伯文、印度系文字）以及任意 HTML/CSS 输入。合规性验证模式需要安装真正的 veraPDF。PyPI 上的包名为 **emboss-pdf**；控制台脚本为 **emboss**。

# SEE ALSO

[python](/man/python)(1), [pdftotext](/man/pdftotext)(1), [weasyprint](/man/weasyprint)(1)

# RESOURCES

```[Source code](https://github.com/GGChamp85/Emboss)```

```[Homepage](https://pypi.org/project/emboss-pdf/)```

<!-- verified: 2026-07-30 -->
