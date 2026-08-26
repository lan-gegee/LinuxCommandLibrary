# TAGLINE

基于 Pandoc Markdown 的终端演示工具

# TLDR

**放映 Markdown 文件**

```patat [presentation.md]```

**放映并在文件变化时自动重新加载**

```patat --watch [presentation.md]```

**将所有幻灯片转储到 stdout**

```patat --dump [presentation.md]```

# SYNOPSIS

**patat** [_options_] _file_

# PARAMETERS

**-w**, **--watch**
> 监视演示文件的更改并自动重新加载。

**-f**, **--force**
> 即使终端声称 ANSI 支持不足也照常运行。

**-d**, **--dump**
> 将所有幻灯片输出到 stdout 以便调试。

**--version**
> 显示版本信息。

# DESCRIPTION

**patat**（Presentations Atop The ANSI Terminal）是一款基于 Pandoc 构建的功能丰富的终端演示工具。它支持图片、执行代码片段、语法高亮、演讲者备注、主题以及幻灯片渐进显示。幻灯片以 Markdown 标题分隔，配置可以嵌入 YAML front matter 中。

# CAVEATS

要求使用 Pandoc 风格的 Markdown。图片显示等部分功能取决于终端能力。

# HISTORY

**patat** 由 **Jasper Van der Jeugt**（jaspervdj）创建，使用 **Haskell** 编写。

# INSTALL

```apt: sudo apt install patat```

```dnf: sudo dnf install patat```

```brew: brew install patat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[slides](/man/slides)(1), [presenterm](/man/presenterm)(1), [mdp](/man/mdp)(1)
