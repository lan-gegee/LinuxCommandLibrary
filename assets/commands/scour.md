# TAGLINE

优化和清理 SVG 文件

# TLDR

**优化 SVG 文件**

```scour -i [input.svg] -o [output.svg]```

**以最大压缩度优化**

```scour -i [input.svg] -o [output.svg] --enable-viewboxing --enable-id-stripping --enable-comment-stripping --shorten-ids --indent=none```

**移除元数据和编辑器数据**

```scour -i [input.svg] -o [output.svg] --remove-metadata```

**为输出添加缩进以提高可读性**

```scour -i [input.svg] -o [output.svg] --indent=space```

**从标准输入处理到标准输出**

```cat [input.svg] | scour > [output.svg]```

**显示优化统计信息**

```scour -i [input.svg] -o [output.svg] -v```

# SYNOPSIS

**scour** [_options_] [_-i input.svg_] [_-o output.svg_]

# PARAMETERS

**-i** _file_, **--input**=_file_
> 输入 SVG 文件（默认：stdin）

**-o** _file_, **--output**=_file_
> 输出 SVG 文件（默认：stdout）

**-p** _digits_, **--set-precision**=_digits_
> 坐标的有效数字位数

**--enable-id-stripping**
> 移除未被引用的 ID 属性

**--enable-comment-stripping**
> 移除所有注释

**--shorten-ids**
> 将 ID 替换为更短的版本

**--remove-metadata**
> 移除 metadata 元素

**--enable-viewboxing**
> 启用从 width/height 自动生成 viewBox

**--keep-editor-data**
> 保留 Inkscape、Sodipodi 或 Adobe Illustrator 数据

**--no-renderer-workaround**
> 禁用针对渲染器缺陷的变通方案

**--indent**=_type_
> 缩进类型：none、space、tab

**-v**, **--verbose**
> 显示优化统计信息

**-q**, **--quiet**
> 抑制非错误输出

# DESCRIPTION

**Scour** 是一款基于 Python 的 SVG 优化器，通过移除不必要的数据和优化结构来减小文件体积。它清理 SVG 编辑器添加的"垃圾"内容，同时保持完全相同的视觉渲染效果。

优化内容包括移除未使用的元素和属性、缩短数值、合并分组以及将形状转换为路径。该工具专为准备用于 Web 部署或进一步处理的 SVG 而设计。

Scour 默认执行无损优化，保留原始文件的视觉效果。更激进的选项可能改变文档结构，但不应影响渲染。

# CAVEATS

切勿覆盖原始文件；Scour 会改变文档结构和语义。手工编辑的 SVG 可能无法获得最佳结果，因为 Scour 是为编辑器生成的文件设计的。某些优化可能导致特定 SVG 查看器或处理器出现问题。

# HISTORY

Scour 最初由 **Jeff Schiller** 和 **Louis Simard** 作为开源 SVG 优化工具创建。它在 Inkscape 社区中广受欢迎，现在由 Tobias Oberstein 和 Patrick Storz 维护。采用 Apache-2.0 许可证。

# INSTALL

```pacman: sudo pacman -S scour```

```brew: brew install scour```

```nix: nix profile install nixpkgs#scour```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[svgo](/man/svgo)(1), [inkscape](/man/inkscape)(1), [convert](/man/convert)(1), [xmllint](/man/xmllint)(1)
