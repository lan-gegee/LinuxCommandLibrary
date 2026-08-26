# TAGLINE

Markdown 文件的风格检查器和 linter

# TLDR

**检查 Markdown 文件**

```markdownlint [file.md]```

**检查目录**

```markdownlint [docs/]```

**自动修复问题**

```markdownlint --fix [file.md]```

**使用配置文件**

```markdownlint --config [.markdownlint.json] [file.md]```

**忽略特定规则**

```markdownlint --disable [MD013] [MD033] -- [file.md]```

**以 JSON 格式输出**

```markdownlint --json [file.md]```

# SYNOPSIS

**markdownlint** [_options_] _files_...

# PARAMETERS

**-f**, **--fix**
> 自动修复问题。

**-c**, **--config** _file_
> 配置文件。

**-d**, **--disable** _rules_
> 禁用规则。

**-e**, **--enable** _rules_
> 启用规则。

**-i**, **--ignore** _pattern_
> 忽略文件。

**-o**, **--output** _file_
> 输出文件。

**-j**, **--json**
> JSON 输出。

# DESCRIPTION

**markdownlint** 是 Markdown 文件的风格检查器和 linter。它基于可配置的规则强制 Markdown 格式保持一致。

该工具会检查标题风格不一致、行长、行尾空格以及列表格式等问题。

# CONFIGURATION

```json
// .markdownlint.json
{
  "MD013": { "line_length": 120 },
  "MD033": false,
  "MD041": false
}
```

# COMMON RULES

```
MD001 - Heading increment
MD013 - Line length
MD022 - Heading blank lines
MD033 - Inline HTML
```

# CAVEATS

CLI（markdownlint-cli）与库是分开的。某些规则可能与部分 Markdown 处理器冲突。自动修复仅限于部分规则。

# HISTORY

markdownlint 由 **David Anson** 创建，最初是 Node.js 库，CLI 封装（markdownlint-cli）则是独立开发的。

# INSTALL

```pacman: sudo pacman -S markdownlint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[prettier](/man/prettier)(1), [markdown](/man/markdown)(1), [vale](/man/vale)(1)
