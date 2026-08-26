# TAGLINE

基于命令行的 Markdown 演示工具

# TLDR

**将 markdown 文件作为幻灯片演示**

```mdp [presentation.md]```

**从 stdin 读取演示内容**

```cat [presentation.md] | mdp```

**禁用颜色渐隐进行演示**

```mdp -f [presentation.md]```

**以反色模式演示**

```mdp -i [presentation.md]```

**启用字符实体展开进行演示**

```mdp -e [presentation.md]```

**禁用透明效果进行演示**

```mdp -t [presentation.md]```

# SYNOPSIS

**mdp** [_options_] [_FILE_]

# PARAMETERS

_FILE_
> Markdown 演示文件。未指定文件或文件名为 - 时，从标准输入读取。

**-e**, **--expand**
> 启用字符实体展开（例如 '&gt;' 变成 '>'）。

**-f**, **--nofade**
> 在 256 色模式下禁用颜色渐隐。

**-i**, **--invert**
> 交换黑白颜色。

**-t**, **--notrans**
> 在支持透明的终端中禁用透明效果。

**-d**, **--debug**
> 在 stderr 上启用调试消息。多次指定可提高调试级别。

**-h**, **--help**
> 显示用法消息并退出。

**-v**, **--version**
> 显示版本和许可信息。

# DESCRIPTION

**mdp** 是一个基于命令行的 Markdown 演示工具。它使用标准 markdown 语法在终端中渲染演示文稿。

水平分隔线用作幻灯片分隔符。以 **@** 为前缀的标题会在顶部和底部栏中显示为标题和作者。支持的格式包括标题、代码块、引用块、无序列表、粗体文本、下划线文本和行内代码。

使用方向键、h/j/k/l、Space、Enter、Page Up/Down 进行导航。按 **g** 或 **Home** 跳到第一张幻灯片，按 **G** 或 **End** 跳到最后一张。数字键 **1-9** 跳转到指定幻灯片。按 **r** 重新加载，按 **q** 退出。

# CAVEATS

仅限终端环境。与图形化演示工具相比格式有限。UTF-8 支持因终端而异。

# HISTORY

mdp 由 **Michael Göhler** 创建，是一个基于终端的演示工具，用 markdown 作为幻灯片内容。

# INSTALL

```apt: sudo apt install mdp```

```pacman: sudo pacman -S mdp```

```brew: brew install mdp```

```nix: nix profile install nixpkgs#mdp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[presenterm](/man/presenterm)(1), [slides](/man/slides)(1)
