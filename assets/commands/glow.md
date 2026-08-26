# TAGLINE

终端 markdown 渲染器

# TLDR

**渲染 markdown 文件**

```glow [README.md]```

**使用分页器渲染**

```glow -p [file.md]```

**从 stdin 渲染**

```cat [file.md] | glow```

**设置宽度**

```glow -w [80] [file.md]```

**浏览本地文件**

```glow```

**抓取并渲染 GitHub README**

```glow github.com/charmbracelet/glow```

**从 stdin 读取**

```cat [file.md] | glow -```

**编辑配置文件**

```glow config```

# SYNOPSIS

**glow** [_options_] [_source_]

**glow** **config**

# PARAMETERS

_SOURCE_
> 要渲染的 markdown 文件、目录、GitHub/GitLab 仓库或 HTTP(S) URL。给定为 `-` 时从 stdin 读取。

**-p**, **--pager**
> 在配置的分页器中显示输出（默认为 `less -r`）。

**-w** _WIDTH_, **--width** _WIDTH_
> 自动换行宽度。默认为终端宽度。

**-s** _STYLE_, **--style** _STYLE_
> 样式名称（`auto`、`dark`、`light`）或自定义 JSON 样式文件的路径。

**-a**, **--all**
> 显示系统文件和隐藏目录（仅限 TUI 模式）。

**-l**, **--local**
> 仅显示本地文件，禁用网络来源（仅限 TUI 模式）。

**--config** _FILE_
> 使用其他配置文件。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**glow** 在终端中以语法高亮和格式化的方式渲染 markdown。它让你无需离开命令行就能美观地显示 markdown 文档。

该工具支持多种样式，并可交互式浏览 markdown 文件，包括直接从 GitHub 或 GitLab 仓库以及任意 HTTP(S) URL 抓取 README。它支持 GitHub Flavored Markdown，包括表格和代码块。不带参数运行 **glow** 会启动 TUI 文件浏览器。

# CONFIGURATION

**~/.config/glow/glow.yml**
> 配置文件，保存默认样式、宽度和分页器设置。

# CAVEATS

终端必须支持颜色。部分功能需要真彩色支持。不渲染图片。

# HISTORY

glow 由 **Charm** 创建，是其终端工具套件的一部分，为命令行带来了美观的 markdown 渲染效果。

# INSTALL

```apt: sudo apt install glow```

```dnf: sudo dnf install glow```

```pacman: sudo pacman -S glow```

```zypper: sudo zypper install glow```

```brew: brew install glow```

```nix: nix profile install nixpkgs#glow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mdcat](/man/mdcat)(1), [bat](/man/bat)(1)

# RESOURCES

```[Source code](https://github.com/charmbracelet/glow)```

<!-- verified: 2026-07-17 -->
