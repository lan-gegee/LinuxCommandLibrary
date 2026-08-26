# TAGLINE

阻止机密信息进入 git 提交的快速本地扫描器

# TLDR

**扫描**当前目录中的机密信息

```ripsecrets```

**扫描指定文件**（例如已暂存的更改）

```ripsecrets --strict-ignore $(git diff --cached --name-only --diff-filter=ACM)```

**安装**为 git pre-commit 钩子

```ripsecrets --install-pre-commit```

# SYNOPSIS

**ripsecrets** [*options*] [*path*...]

# DESCRIPTION

**ripsecrets** 在源代码文件中搜索高熵字符串和已知机密模式，以防止意外提交。它专为 pre-commit 速度而设计：仅限本地运行（无云端验证）、相比朴素的正则工具误报率更低，且是单个静态二进制文件。

# PARAMETERS

*path*...

> 要扫描的文件或目录（默认：从当前目录递归）。

**--install-pre-commit**

> 安装一个运行 ripsecrets 的 git pre-commit 钩子。

**--strict-ignore**

> 在扫描显式给定的文件列表时严格遵循忽略规则（典型场景是配合 **git diff --cached** 使用）。

其他选项用于控制允许列表和输出——参见 **ripsecrets --help**。

# CAVEATS

本地模式匹配无法证明某个字符串是仍然有效的凭据，也无法捕获所有类型的机密。请与提交钩子及其他互补扫描器配合使用，实现纵深防御。切勿“仅为了测试”而提交真实的机密。

# INSTALL

```brew: brew install ripsecrets```

```nix: nix profile install nixpkgs#ripsecrets```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [gitleaks](/man/gitleaks)(1), [trufflehog](/man/trufflehog)(1)

# RESOURCES

```[Source code](https://github.com/sirwart/ripsecrets)```

<!-- verified: 2026-07-19 -->
