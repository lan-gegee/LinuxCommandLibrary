# TAGLINE

校验 TLDR 页面格式

# TLDR

**检查单个文件**

```tldr-lint [page.md]```

**检查目录**

```tldr-lint [pages/]```

**详细输出**

```tldr-lint -v [page.md]```

**格式化输出**

```tldr-lint -f [json] [page.md]```

**忽略规则**

```tldr-lint -I [TLDR001] [page.md]```

# SYNOPSIS

**tldr-lint** [_-v_] [_-f format_] [_-I rules_] _files_

# PARAMETERS

**-v**
> 详细输出。

**-f** _FORMAT_
> 输出格式。

**-I** _RULES_
> 忽略指定规则。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# DESCRIPTION

**tldr-lint** 根据 tldr 项目的格式规范校验 TLDR 页面，检查结构正确性、Markdown 语法规范和风格一致性。每条规则都有一个代码（例如 TLDR001），可通过 **-I** 选项有选择地忽略。

该工具可以检查单个文件，也可以扫描整个目录进行批量校验，因此适合在 CI 流水线中强制 tldr-pages 仓库各页面保持一致的格式。输出格式包括纯文本和 JSON，便于与其他工具集成。

# CAVEATS

仅针对 TLDR 格式。需要 Node.js。面向 tldr 贡献者。

# HISTORY

**tldr-lint** 为 **tldr-pages** 项目而创建，用于校验页面格式的一致性。

# INSTALL

```apt: sudo apt install tealdeer```

```dnf: sudo dnf install tldr```

```pacman: sudo pacman -S tealdeer```

```zypper: sudo zypper install tealdeer```

```brew: brew install tealdeer```

```nix: nix profile install nixpkgs#tealdeer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tldr](/man/tldr)(1), [markdownlint](/man/markdownlint)(1)
