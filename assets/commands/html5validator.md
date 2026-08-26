# TAGLINE

使用 Nu Html Checker 的命令行 HTML5 校验工具

# TLDR

**校验一个 HTML 文件**

```html5validator [file.html]```

**校验目录中的所有 HTML**

```html5validator --root [path/to/directory]```

**显示警告**

```html5validator --show-warnings [file.html]```

**匹配自定义文件模式**

```html5validator --root [path] --match "*.html *.php"```

**排除目录**

```html5validator --root [path] --blacklist "node_modules vendor"```

**以 JSON 输出**

```html5validator --format json [file.html]```

**忽略特定错误**

```html5validator --ignore-re 'Attribute "ng-[a-z-]+" not allowed' [file.html]```

# SYNOPSIS

**html5validator** [_options_] [_files_]

# PARAMETERS

**--root** _dir_
> 文件搜索的起始目录。

**--match** _pattern_
> 要匹配的文件模式（默认 *.html）。

**--blacklist** _dirs_
> 要跳过的目录名。

**--show-warnings**
> 将警告视为错误显示。

**--format** _fmt_
> 输出格式：gnu、xml、json、text。

**--ignore-re** _regex_
> 忽略匹配正则表达式的错误。

**--ignore** _message_
> 忽略与给定消息完全一致的错误。

**--also-check-css**
> 同时校验 CSS 文件（默认匹配 *.html 和 *.css）。

**--config** _file_
> 从配置文件读取选项。

# DESCRIPTION

**html5validator** 是一个使用 Nu Html Checker（v.Nu）的命令行 HTML5 校验工具。它为静态站点生成器和持续集成而设计。HTML 有效时返回退出码 0。需要 Python 3.6+ 和 Java 8。

# CAVEATS

需要 **PATH** 上有可用的 **Java** 运行时（OpenJDK 8+），因为它会调用内置的 **vnu.jar** 来执行实际的校验。

# INSTALL

```nix: nix profile install nixpkgs#html5validator```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tidy](/man/tidy)(1)

# RESOURCES

```[Source code](https://github.com/svenkreiss/html5validator)```

<!-- verified: 2026-07-19 -->
