# TAGLINE

HTML 静态代码分析工具

# TLDR

**检查 HTML 文件**

```htmlhint [file.html]```

**检查多个文件**

```htmlhint [*.html]```

**使用配置文件**

```htmlhint -c [.htmlhintrc] [file.html]```

**以 JSON 输出**

```htmlhint --format json [file.html]```

**忽略特定模式**

```htmlhint --ignore [**/vendor/**] [file.html]```

**列出所有可用规则**

```htmlhint --list```

**初始化配置文件**

```htmlhint --init```

# SYNOPSIS

**htmlhint** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要检查的 HTML 文件。

**-c**, **--config** _FILE_
> 配置文件路径。

**-f**, **--format** _FORMAT_
> 输出格式：default、json、unix、sarif、markdown、junit、html、compact、checkstyle。

**-i**, **--ignore** _PATTERN_
> 要忽略的文件或文件夹的 glob 模式。

**-r**, **--rules** _RULES_
> 要启用的规则（逗号分隔，例如 tag-pair,attr-lowercase=true）。

**-R**, **--rulesdir** _PATH_
> 从文件或文件夹加载自定义规则。

**-l**, **--list**
> 显示所有可用规则。

**--init**
> 创建一个包含默认规则的新 .htmlhintrc 配置文件。

**--nocolor**
> 禁用彩色输出。

**--warn**
> 仅警告，以退出码 0 退出。

**-V**, **--version**
> 输出版本号。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**HTMLHint** 是一个 HTML 静态代码分析工具。它检查常见错误、已弃用的元素和最佳实践。

该工具强制一致的 HTML 风格并捕获潜在问题。它支持自定义规则和配置文件。

# CAVEATS

需要 Node.js。规则集可通过 .htmlhintrc 或 CLI 标志配置。某些规则可能与框架特有的 HTML 模式冲突（如 Angular、Vue）。

# HISTORY

HTMLHint 的创建目的是为 HTML 文档提供 ESLint 风格的静态分析。

# INSTALL

```brew: brew install htmlhint```

```nix: nix profile install nixpkgs#htmlhint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[eslint](/man/eslint)(1), [prettier](/man/prettier)(1), [tidy](/man/tidy)(1)
