# TAGLINE

列出本地仓库中的引用

# TLDR

**列出所有引用**

```git show-ref```

**仅显示 heads**

```git show-ref --heads```

**仅显示标签**

```git show-ref --tags```

**验证引用是否存在**

```git show-ref --verify refs/heads/main```

**安静模式**

```git show-ref -q --verify refs/heads/main```

# SYNOPSIS

**git show-ref** [**--head**] [**-d** | **--dereference**] [**-s** | **--hash**[=_N_]] [**--abbrev**[=_N_]] [**--branches**] [**--tags**] [--] [_pattern_...]

**git show-ref** **--verify** [**-q** | **--quiet**] [**-d** | **--dereference**] [**-s** | **--hash**[=_N_]] [**--abbrev**[=_N_]] [--] [_ref_...]

**git show-ref** **--exists** _ref_

**git show-ref** **--exclude-existing**[=_pattern_]

# PARAMETERS

_PATTERN_
> 匹配结尾与该模式一致的引用（按完整片段匹配）。

**--head**
> 包含 HEAD 引用，默认会被过滤掉。

**--branches**
> 仅限本地分支（refs/heads）。取代较旧的 **--heads**，后者仍可作为别名使用。

**--tags**
> 仅限本地标签（refs/tags）。

**--verify**
> 要求参数必须是精确的引用路径（例如 refs/heads/main）。若该引用不存在则报错。

**--exists** _ref_
> 检查某个引用是否存在。退出码 0 = 存在，2 = 不存在，1 = 出错。

**--exclude-existing**[=_pattern_]
> 过滤模式。从 stdin 读取引用，打印其中本地不存在的那些，可选择仅限后缀匹配该模式的引用。

**-q**, **--quiet**
> 抑制输出。仅通过退出码判断结果。

**-s**, **--hash**[=_N_]
> 只打印对象名（可选缩略为 _N_ 位十六进制数字），不打印引用名。

**--abbrev**[=_N_]
> 将打印的对象名缩略为 _N_ 位十六进制数字（默认遵循 **core.abbrev**）。

**-d**, **--dereference**
> 对标签对象，同时打印解引用后的提交，并以 **^{}** 作为后缀。

# DESCRIPTION

**git show-ref** 列出本地仓库中的引用，显示分支、标签及其他引用的 SHA-1 哈希值和引用名。它是一个常用于脚本的底层（plumbing）命令。

验证模式用于检查某个特定引用是否存在，而无需列出所有引用，并返回相应的退出码。

# CAVEATS

底层（plumbing）命令。只显示本地引用。远程引用请用 git ls-remote。

# HISTORY

git show-ref 是用于检查引用的核心 **Git** 底层（plumbing）命令，常见于各类脚本中。

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

[git-ls-remote](/man/git-ls-remote)(1), [git-for-each-ref](/man/git-for-each-ref)(1)
