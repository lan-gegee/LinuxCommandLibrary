# TAGLINE

用于快速目录导航的终端文件浏览器

# TLDR

**交互式导航到某个目录**

```cd "$(tere)"```

**使用过滤模式只显示匹配的条目**

```cd "$(tere --filter-search)"```

**超时后自动进入目录（毫秒）**

```cd "$(tere --autocd-timeout 500)"```

**启用鼠标导航**

```cd "$(tere --mouse=on)"```

**按修改日期排序并使用不区分大小写的搜索**

```cd "$(tere --sort modified --ignore-case)"```

# SYNOPSIS

**tere** [_options_]

# PARAMETERS

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 打印版本。

**-f**, **--filter-search**
> 只显示与当前搜索词匹配的条目。

**-F**, **--no-filter-search**
> 搜索时仍显示全部条目（默认）。

**-S**, **--smart-case**
> 小写时不区分大小写，含大写时区分（默认）。

**-i**, **--ignore-case**
> 搜索始终忽略大小写。

**-s**, **--case-sensitive**
> 始终区分大小写。

**-g**, **--gap-search**
> 允许从名称开头起有间隔的模糊匹配（默认）。

**-G**, **--gap-search-anywhere**
> 允许在名称任意位置有间隔的模糊匹配。

**-n**, **--normal-search**
> 从名称开头匹配连续字符。

**-N**, **--normal-search-anywhere**
> 匹配名称中任意位置的连续字符。

**--files** _MODE_
> 文件显示模式：ignore（默认）、hide 或 match。

**--sort** _ORDER_
> 排序方式：name（默认）、created 或 modified。

**--autocd-timeout** _MS_
> 当只有单个匹配时，在 MS 毫秒后自动进入目录。设为 "off" 可禁用。

**--mouse=on|off**
> 启用或禁用鼠标导航（默认为 off）。

**--history-file** _PATH_
> JSON 历史文件的路径。

**--map** _KEY:ACTION_
> 自定义键盘快捷键映射。

# DESCRIPTION

**tere** 提供一个 TUI 用于快速导航到某个目录，退出时打印所选路径。它不是文件管理器——只能浏览文件夹。导航使用方向键、Enter 和输入即搜索，力求最少按键次数。

# HISTORY

**tere** 由 **Marton Gunyho**（mgunyho）创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S tere```

```brew: brew install tere```

```nix: nix profile install nixpkgs#tere```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[broot](/man/broot)(1), [zoxide](/man/zoxide)(1), [ranger](/man/ranger)(1), [fzf](/man/fzf)(1), [nnn](/man/nnn)(1)
