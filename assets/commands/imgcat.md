# TAGLINE

在终端中内联显示图像

# TLDR

**在终端中显示图像**

```imgcat [path/to/image.png]```

**显示多张图像**

```imgcat [image1.jpg] [image2.png]```

**显示来自 URL 的图像**

```curl -s [https://example.com/image.jpg] | imgcat```

**以指定的字符单元格宽度显示**

```imgcat -w [80] [image.png]```

**以指定的字符单元格高度显示**

```imgcat -H [24] [image.png]```

**从 stdin 读取图像**

```curl -s [https://example.com/image.jpg] | imgcat -```

# SYNOPSIS

**imgcat** [_options_] [_file ..._]

# PARAMETERS

**-w**, **--width** _n_
> 以字符单元格为单位的输出宽度。

**-H**, **--height** _n_
> 以字符单元格为单位的输出高度。

**-R**, **--no-stretch**
> 不将图像拉伸以填满可用空间。

**--version**
> 显示版本信息。

**--help**
> 显示帮助。

# DESCRIPTION

**imgcat** 在终端中内联显示图像。它存在多种实现：最初的 iTerm2 shell 脚本使用 iTerm2 内联图像协议，而独立版本（如 posva 的版本或 iTerm2 自带的版本）支持更多选项。

图像经 base64 编码后通过转义序列发送，与文本输出一起内联渲染。这便于在开发过程中快速预览图像、通过 SSH 会话查看图像，以及将可视化输出集成到命令行工作流中。

注意，有多个名为 "imgcat" 的不同工具，它们的选项集各不相同。此处列出的参数反映的是常见选项，但可能因实现而异。

# CAVEATS

终端必须支持某种内联图像协议（iTerm2、Kitty、Sixel）。不同实现的功能和选项差异很大。大图可能拖慢终端渲染。SSH 会话在未经特殊配置的情况下可能不支持内联图像。

# HISTORY

最初的 **imgcat** 由 George Nachman 于 **2014 年**前后为 iTerm2 创建，首次在终端模拟器中引入了内联图像显示。这一概念启发了其他终端的实现，催生了多个功能各异但同名为 "imgcat" 的工具。Kitty 终端后来推出了自己的图形协议，随之出现了各种支持它的工具。

# INSTALL

```nix: nix profile install nixpkgs#imgcat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timg](/man/timg)(1), [viu](/man/viu)(1), [chafa](/man/chafa)(1), [catimg](/man/catimg)(1), [pixterm](/man/pixterm)(1)
