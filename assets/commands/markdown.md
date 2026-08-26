# TAGLINE

将 Markdown 格式的文本转换为 HTML

# TLDR

**将 Markdown 转换为 HTML**

```markdown [file.md]```

**从标准输入转换**

```echo "# Hello" | markdown```

**输出到文件**

```markdown [file.md] > [file.html]```

# SYNOPSIS

**markdown** [_options_] [_file_]

# PARAMETERS

**--html4tags**
> 使用 XHTML 风格的空标签。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# DESCRIPTION

**markdown** 将 Markdown 格式的文本转换为 HTML。它实现的是由 John Gruber 制定的最初版 Markdown 规范。

Markdown 允许用纯文本配合简单的格式标记进行写作，并可转换为结构化的 HTML。

# MARKDOWN SYNTAX

```markdown
# Heading 1
## Heading 2

**bold** and *italic*

- List item
- Another item

[Link](http://example.com)

`code`

```
code block
```
```

# IMPLEMENTATIONS

```
markdown      - Original Perl
python-markdown - Python
marked        - JavaScript
pandoc        - Haskell (multi-format)
```

# CAVEATS

存在许多略有差异的实现。没有单一标准（CommonMark 旨在标准化）。最初的 Markdown 是 Perl 脚本。

# HISTORY

Markdown 由 **John Gruber** 在 **Aaron Swartz** 的参与下于 **2004 年**创建。它已成为 README 文件和文档的事实标准。

# INSTALL

```apt: sudo apt install discount```

```dnf: sudo dnf install discount```

```pacman: sudo pacman -S discount```

```apk: sudo apk add discount```

```zypper: sudo zypper install discount```

```brew: brew install discount```

```nix: nix profile install nixpkgs#discount```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pandoc](/man/pandoc)(1), [cmark](/man/cmark)(1), [grip](/man/grip)(1)
