# TAGLINE

带语法高亮的着色版 cat

# TLDR

**显示文件并进行语法高亮**

```ccat [file.py]```

**显示多个文件**

```ccat [file1.go] [file2.js]```

**输出为 HTML**

```ccat --html [file.rb]```

**深色背景配色**

```ccat --bg=dark [file.c]```

**显示调色板**

```ccat --palette```

# SYNOPSIS

**ccat** [_options_] _file_...

# DESCRIPTION

**ccat** 是 cat 的即插即用替代品，为终端中显示的文件内容添加语法高亮。它根据文件扩展名自动检测编程语言，并对关键字、字符串、注释等语法元素应用颜色编码。

该工具支持多种语言，包括 JavaScript、Python、Go、Ruby、C、C++、Java 和 JSON。它以单个二进制文件发布，没有外部依赖，具备原生执行速度。输出可针对浅色或深色终端背景进行渲染，还支持输出 HTML，便于将高亮代码嵌入网页。

# PARAMETERS

**--html**
> 输出为 HTML

**--bg**=_color_
> 背景颜色：light、dark

**-G** _key=color_
> 设置自定义颜色代码

**--palette**
> 显示调色板

**-C**, **--color**=_mode_
> 颜色模式：always、never、auto

# SUPPORTED LANGUAGES

- JavaScript / TypeScript
- Python
- Go
- Ruby
- C / C++
- Java
- JSON
- 以及更多（通过 Pygments）

# ALIASING

用 ccat 替换 cat：

```bash
alias cat='ccat'
```

添加到 ~/.bashrc 中即可永久生效。

# CAVEATS

有 Go 编写版（owenthereal 版）和 Python 编写版（welbornprod 版）。需要支持颜色的终端。

# INSTALL

```apt: sudo apt install ccrypt```

```brew: brew install ccrypt```

```nix: nix profile install nixpkgs#ccrypt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cat](/man/cat)(1), [bat](/man/bat)(1), [highlight](/man/highlight)(1)

# RESOURCES

```[Source code](https://github.com/owenthereal/ccat)```

<!-- verified: 2026-06-22 -->
