# TAGLINE

转换和操作 PDF 文件结构

# TLDR

**解密 PDF**

```qpdf --decrypt [input.pdf] [output.pdf]```

**线性化 PDF**（针对 Web 优化）

```qpdf --linearize [input.pdf] [output.pdf]```

**合并 PDF**

```qpdf --empty --pages [file1.pdf] [file2.pdf] -- [output.pdf]```

**提取指定页面**

```qpdf --empty --pages [input.pdf] [1-5,10] -- [output.pdf]```

**旋转页面**

```qpdf [input.pdf] [output.pdf] --rotate=[+90:1-5]```

**压缩流**

```qpdf --compress-streams=y [input.pdf] [output.pdf]```

**检查 PDF 结构**

```qpdf --check [input.pdf]```

**移除密码**

```qpdf --password=[pass] --decrypt [encrypted.pdf] [output.pdf]```

**原地替换输入文件**

```qpdf --replace-input --linearize [input.pdf]```

**将 PDF 拆分**为单页文件

```qpdf --split-pages [input.pdf] [output_%d.pdf]```

**添加密码保护**

```qpdf --encrypt [user_pass] [owner_pass] 256 -- [input.pdf] [output.pdf]```

# SYNOPSIS

**qpdf** [_--decrypt_] [_--linearize_] [_--pages spec_] [_--rotate spec_] [_options_] _input_ _output_

# PARAMETERS

**--decrypt**
> 移除加密。

**--linearize**
> 针对 Web 查看进行优化。

**--encrypt** _user_ _owner_ _bits_ **--**
> 添加加密（bits：40、128 或 256）。

**--pages** _spec_
> 页面选择规范。

**--collate**[=_n_]
> 对来自多个文件的页面进行整理交错，而非简单拼接。

**--rotate** [_+|-_]_angle_:_pages_
> 旋转页面。

**--empty**
> 使用空 PDF 作为输入基础。

**--replace-input**
> 用输出覆盖输入文件，而不是写入单独的文件。

**--check**
> 检查 PDF 结构。

**--show-encryption**
> 显示加密详情。

**--password** _PASS_
> 输入文件的密码。

**--compress-streams**[=_y|n_]
> 压缩/解压流。

**--object-streams**=_mode_
> 控制对象流：保留、禁用或生成。

**--decode-level** _LEVEL_
> 流解码级别：none、generalized、specialized、all。

**--normalize-content**[=_y|n_]
> 规范化内容流。

**--split-pages**[=_n_]
> 拆分为每 n 页一个文件。

**--overlay** _file_
> 将 file 中的页面叠加在上层。

**--underlay** _file_
> 将 file 中的页面垫在下层。

**--flatten-rotation**
> 使旋转永久生效。

**--flatten-annotations**[=_parameter_]
> 扁平化注释外观。

**--coalesce-contents**
> 将每页的多个内容流合并为一个。

**--optimize-images**
> 对图像使用高效的压缩方式。

**--remove-unreferenced-resources**[=_auto|yes|no_]
> 从页面字典中移除未使用的资源。

**--json**
> 以 JSON 格式输出 PDF 结构。

**--qdf**
> 创建 QDF（可编辑的 PDF 源码）。

**--deterministic-id**
> 根据文件内容生成文档 ID，使输出可复现。

**--verbose**
> 输出所执行操作的额外信息。

**--progress**
> 写入文件时显示进度指示器。

**--is-encrypted**
> 测试文件是否已加密（退出码表示结果）。

**--requires-password**
> 测试是否需要密码（退出码表示结果）。

# DESCRIPTION

**qpdf** 是一款命令行工具，用于对 PDF 文件进行保持内容不变的结构性转换。与栅格化或重新渲染的工具不同，qpdf 直接操作 PDF 结构。

主要用途包括加密管理（解密、加密、更改密码）、线性化（针对 Web 分发优化）以及页面操作（合并、拆分、重排）。

页面指定语法灵活：范围（1-10）、特定页（1,3,5）、逆序（z-1）和旋转（1-5:90）。可以使用 --pages 配合 文件：范围 对从多个文件提取页面。

--check 选项在不修改文件的前提下校验 PDF 结构，可用于识别损坏的文件。JSON 输出会暴露内部结构，便于分析或自定义处理。

QDF 模式生成可用文本编辑器编辑的"规范化"PDF，方便调试和手动修复。流的解压会让内容变得人类可读。

线性化会重组 PDF 以便在 HTTP 上高效地进行字节服务，实现逐页加载而无需下载整个文件。

# CAVEATS

无法编辑文本内容（需使用其他工具）。受密码保护的文件需要密码才能处理。某些格式损坏的 PDF 可能无法处理。大型 PDF 需要大量内存。加密强度受 PDF 规范限制（40、128 或 256 位）。退出码：0 表示成功，2 表示错误，3 表示警告（使用 **--warning-exit-0** 可将警告视为成功）。

# HISTORY

**qpdf** 由 **Jay Berkenbilt** 于 **2005 年**前后在 Apex CoVantage 创建。最初是用于 PDF 处理的内部工具，后来开源，并已成为标准的库和命令行工具。与 PDF 编辑器不同，qpdf 专注于精确保留内容的结构性转换。

# INSTALL

```apt: sudo apt install qpdf```

```dnf: sudo dnf install qpdf```

```pacman: sudo pacman -S qpdf```

```apk: sudo apk add qpdf```

```zypper: sudo zypper install qpdf```

```brew: brew install qpdf```

```nix: nix profile install nixpkgs#qpdf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdftk](/man/pdftk)(1), [poppler-utils](/man/poppler-utils)(1), [ghostscript](/man/ghostscript)(1), [pdfunite](/man/pdfunite)(1)
