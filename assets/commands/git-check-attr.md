# TAGLINE

显示文件的 gitattributes 信息

# TLDR

**检查文件的属性**

```git check-attr [attribute] [file]```

**检查所有属性**

```git check-attr -a [file]```

**检查多个文件**

```git check-attr [attribute] [file1] [file2]```

**从标准输入读取并检查**

```echo "[file]" | git check-attr --stdin [attribute]```

# SYNOPSIS

**git** **check-attr** [_options_] _attribute_... _pathname_...

# PARAMETERS

**-a**, **--all**
> 检查所有属性。

**--stdin**
> 从标准输入读取路径名。

**-z**
> 以 NUL 字符结尾输出。

# DESCRIPTION

**git check-attr** 显示指定路径的 gitattributes 信息，揭示 Git 将如何根据 .gitattributes 配置处理文件。这一调试工具展示的是应用所有 gitattributes 规则之后生效的属性值。

Gitattributes 控制多种行为，包括换行符转换（text/eol）、diff 驱动、合并策略、导出处理和语言检测。该命令会综合工作区、索引和仓库中的 .gitattributes 文件来解析属性值。

输出会列出每个路径及其属性值，状态为 "set"、"unset" 或 "unspecified"。这有助于调试与文件处理相关的意外 Git 行为，例如不正确的换行符转换或生成文件中的合并冲突。

# CONFIGURATION

**.gitattributes**
> 文件属性模式文件，控制换行符、diff 行为、合并策略以及其他针对特定文件的 Git 操作。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-check-ignore](/man/git-check-ignore)(1)
