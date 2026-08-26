# TAGLINE

解析规范化的作者与提交者身份

# TLDR

**检查 mailmap 条目**

```git check-mailmap "[Name] <email@example.com>"```

**映射多个条目**

```git check-mailmap "[Name1] <email1>" "[Name2] <email2>"```

**从标准输入读取**

```echo "[Name] <email>" | git check-mailmap --stdin```

# SYNOPSIS

**git check-mailmap** [_options_] _contact_

# PARAMETERS

_CONTACT_
> "Name <email>" 格式的联系人。

**--stdin**
> 从标准输入读取联系人。

**--mailmap-file** _FILE_
> 额外读取指定的 mailmap 文件，其优先级高于仓库已配置的 mailmap。

**--mailmap-blob** _BLOB_
> 与 **--mailmap-file** 类似，但从仓库中的一个 blob 读取 mailmap。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git check-mailmap** 使用 mailmap 文件查找规范的姓名和邮箱地址。它将作者/提交者身份转换为 .mailmap 中配置的规范化形式。

mailmap 功能用于整合身份的各种变体（拼写错误、改名、多个邮箱），统一为规范形式。该命令可以显示这些身份在 git log 和 shortlog 输出中将如何被映射。

这主要是一个调试工具，用于在报告或统计中依赖 .mailmap 之前，验证其中的条目是否能正确解析贡献者身份。

# CONFIGURATION

**.mailmap**
> 将作者和提交者的姓名/邮箱映射为规范形式，在日志和统计中统一各种身份变体。

# CAVEATS

需要仓库中存在 .mailmap 文件。输入必须是规范的 "Name <email>" 格式。主要用于调试。

# HISTORY

git check-mailmap 被加入 **Git** 是为了支持 mailmap 配置的调试，补充 git shortlog -e 的功能。

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

[git-shortlog](/man/git-shortlog)(1), [git-log](/man/git-log)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-check-mailmap)```

<!-- verified: 2026-07-17 -->
