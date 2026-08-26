# TAGLINE

支持终端渲染的 Markdown cat

# TLDR

**渲染 Markdown 文件**

```mdcat [path/to/file.md]```

**渲染来自 stdin 的 Markdown**

```echo "# Hello" | mdcat```

**分页显示输出**

```mdcat -p [path/to/file.md]```

# SYNOPSIS

**mdcat** [_options_] [_files_...]

# PARAMETERS

**-p**, **--paginate**
> 通过分页器分页显示输出。

**--no-colour**
> 禁用语法高亮和颜色。

# DESCRIPTION

**mdcat** 直接在终端中渲染 Markdown 文档，为代码块提供语法高亮（通过 syntect），在支持的终端中内联显示图片，提供可点击的链接，并在 iTerm2 中支持标题跳转标记。

它与 iTerm2、WezTerm 和 kitty 配合最佳，并支持大多数现代终端模拟器，包括 Windows Terminal 和任何基于 VTE 的终端。未指定文件时，它从 stdin 读取。

# CAVEATS

内联图片支持取决于终端模拟器。某些终端可能只能显示指向图片的链接。

# HISTORY

**mdcat** 由 **swsnr** 创建，用 **Rust** 编写。

# INSTALL

```brew: brew install mdcat```

```nix: nix profile install nixpkgs#mdcat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glow](/man/glow)(1), [bat](/man/bat)(1), [mandown](/man/mandown)(1), [cat](/man/cat)(1)
