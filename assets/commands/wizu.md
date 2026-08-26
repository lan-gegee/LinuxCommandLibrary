# TAGLINE

快速的交互式目录树查看器

# TLDR

**显示当前目录树**

```wisu```

带文件图标的**交互模式**

```wisu -i --icons```

按大小降序排序并支持 gitignore

```wisu -g --sort size --reverse```

# SYNOPSIS

**wisu** [_path_] [_options_]

# PARAMETERS

_PATH_
> 要显示的根目录（默认为当前目录）。

**-i**, **--interactive**
> 启动交互式 TUI 浏览器。

**--icons**
> 在条目旁渲染文件类型的 emoji 图标。

**-g**, **--gitignore**
> 遍历时遵循 `.gitignore` 文件。

**--sort** _KEY_
> 按 `name`、`size`、`mtime` 等对条目排序。

**--reverse**
> 反转排序顺序。

**--export** _FORMAT_
> 将目录树导出为 `csv`、`xml` 或 `json`。

# DESCRIPTION

**wizu**（二进制名 **wisu**）是一个目录树查看器，既提供经典的树状显示，也提供完全交互式的 TUI。功能包括双显示模式、搜索、基于 LS_COLORS 的主题感知着色、emoji 文件图标、gitignore 支持、多种排序模式、按时间过滤，以及导出为 CSV、XML 和 JSON 格式。

# HISTORY

**wizu** 由 **Andrea Frolli**（sh1zen）创建，使用 **Rust** 编写。

# SEE ALSO

[tree](/man/tree)(1), [eza](/man/eza)(1), [broot](/man/broot)(1)
