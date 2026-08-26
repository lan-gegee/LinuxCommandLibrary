# TAGLINE

无损 SVG 文件优化器

# TLDR

**清理 SVG**

```svgcleaner [input.svg] [output.svg]```

**最大压缩**

```svgcleaner --preset=maximum [input.svg] [output.svg]```

**保留特定属性**

```svgcleaner --keep-named-ids [input.svg] [output.svg]```

**缩进输出**

```svgcleaner --indent [2] [input.svg] [output.svg]```

**静默模式**

```svgcleaner -q [input.svg] [output.svg]```

# SYNOPSIS

**svgcleaner** [_--preset preset_] [_options_] _input_ _output_

# PARAMETERS

**--preset** _NAME_
> 优化预设。

**--keep-named-ids**
> 保留 ID。

**--indent** _N_
> 缩进空格数。

**-q**
> 静默模式。

**--multipass**
> 多轮优化。

# DESCRIPTION

**svgcleaner** 对 SVG 文件执行无损优化，在不改变外观的前提下减小文件体积。它会移除不必要的元数据、编辑器残留、未使用的定义以及冗余属性——这些正是图形编辑器导出的 SVG 文件臃肿的原因。

该工具简化路径数据、优化几何结构、合并兼容的元素，并删除空的分组和容器。可以应用多轮优化以获得最大的体积缩减。通过优化预设可以在保守和激进的清理级别之间选择。

svgcleaner 用 Rust 编写以保证性能，对清理 Inkscape、Adobe Illustrator 和 Sketch 等编辑器生成的 SVG 特别有效，这些文件通常嵌入大量编辑器专有元数据和冗余样式信息。

# CAVEATS

可能破坏复杂的 SVG。请测试输出结果。用 Rust 编写。

# HISTORY

**svgcleaner** 是一个无损 SVG 优化器，可在不影响外观的情况下减小文件体积。

# INSTALL

```pacman: sudo pacman -S svgcleaner```

```zypper: sudo zypper install svgcleaner```

```nix: nix profile install nixpkgs#svgcleaner```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[svgo](/man/svgo)(1), [inkscape](/man/inkscape)(1), [scour](/man/scour)(1)
