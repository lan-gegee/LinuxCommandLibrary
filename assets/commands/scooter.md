# TAGLINE

终端中的交互式查找替换工具

# TLDR

**在当前目录启动交互式查找替换**

```scooter```

**在指定目录中搜索**

```scooter [path/to/directory]```

**预填搜索和替换字段并立即开始搜索**

```scooter --search-text "[old]" --replace-text "[new]" --immediate-search```

**使用字面字符串而不是正则表达式搜索**

```scooter --fixed-strings```

**在搜索中包含隐藏文件**

```scooter --hidden```

**只搜索特定文件类型**

```scooter --files-to-include "[*.py,*.js]"```

# SYNOPSIS

**scooter** [_options_] [_path_]

# PARAMETERS

**-a**, **--advanced-regex**
> 启用完整的正则特性（较慢）。

**-U**, **--multiline**
> 启用多行搜索。

**-N**, **--no-tui**
> 非交互模式。

**--search-text** _TEXT_
> 预填搜索框。

**--replace-text** _TEXT_
> 预填替换框。

**--fixed-strings**
> 使用字面字符串匹配而不是正则表达式。

**--hidden**
> 在搜索中包含隐藏文件。

**--files-to-include** _GLOB_
> 要包含的 glob 模式（逗号分隔）。

**--files-to-exclude** _GLOB_
> 要排除的 glob 模式（逗号分隔）。

**--immediate-search**
> 与 --search-text 组合时立即开始搜索。

# DESCRIPTION

**scooter** 递归搜索目录中的文件，让你以交互方式逐个决定要替换哪些匹配项。它支持固定字符串和带捕获组的正则表达式，遵循 .gitignore 和 .ignore 文件，并可通过自定义主题提供语法高亮。

# HISTORY

**scooter** 由 **Thomas Schafer**（thomasschafer）创建，使用 **Rust** 编写。

# INSTALL

```apk: sudo apk add scooter```

```brew: brew install scooter```

```nix: nix profile install nixpkgs#scooter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sed](/man/sed)(1), [serpl](/man/serpl)(1), [ripgrep](/man/ripgrep)(1)
