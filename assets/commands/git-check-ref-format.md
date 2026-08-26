# TAGLINE

校验并规范化 Git 引用名称

# TLDR

**检查引用名是否有效**

```git check-ref-format [refs/heads/branch]```

**检查分支名**

```git check-ref-format --branch [name]```

**规范化引用名**

```git check-ref-format --normalize [refs/heads/branch]```

# SYNOPSIS

**git** **check-ref-format** [_options_] _refname_

# PARAMETERS

**--branch**
> 作为分支名检查。

**--normalize**
> 规范化引用名。

**--allow-onelevel**
> 允许单级引用（不含多个 `/` 分隔组件的引用名）。

**--no-allow-onelevel**
> 要求分层引用（默认）。

**--refspec-pattern**
> 将引用名解释为 refspec 模式，允许一个 `*` 通配符。

# DESCRIPTION

**git check-ref-format** 按照严格的命名规则校验和规范化 Git 引用名称。这确保分支名和标签名在不同文件系统之间可移植，且不会与 Git 内部机制冲突。

引用名称不得包含空格、波浪号、插入符、冒号、问号、星号或方括号；不能以斜杠开头或结尾，不能包含连续斜杠，也不能以 .lock 结尾；斜杠之间的组件不能以点开头。这些规则可避免文件系统冲突和 shell 解释问题。

创建分支或标签的脚本会以编程方式使用该命令，在尝试操作之前校验用户输入。规范化会移除多余的斜杠并保证格式一致。--branch 选项将名称按分支简写解释，将其展开为 refs/heads/ 形式。

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

[git-branch](/man/git-branch)(1), [git-tag](/man/git-tag)(1)
