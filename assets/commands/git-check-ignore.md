# TAGLINE

调试 gitignore 模式与被忽略的文件

# TLDR

**检查文件是否被忽略**

```git check-ignore [file.txt]```

**显示匹配到的规则**

```git check-ignore -v [file.txt]```

**检查多个文件**

```git check-ignore [file1.txt] [file2.txt]```

**从标准输入读取路径**

```echo "[path]" | git check-ignore --stdin```

**检查所有被忽略的文件**

```git check-ignore *```

# SYNOPSIS

**git check-ignore** [_options_] _pathspec_

# PARAMETERS

_PATHSPEC_
> 要检查的文件路径。

**-v**, **--verbose**
> 显示来源和模式。

**--stdin**
> 从标准输入读取路径。

**-z**
> 以 NUL 字符结尾输出。

**-n**, **--non-matching**
> 显示未匹配的路径。

**-q**, **--quiet**
> 只以退出状态表示结果。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git check-ignore** 用于调试 gitignore 模式。它报告路径是否被忽略，以及是哪条规则导致了忽略，帮助排查 gitignore 规则问题。

详细模式（**-v**）会显示导致路径被忽略的 gitignore 文件、行号和模式。对于在多个目录层级上分布着多个 .gitignore 文件的复杂配置，这一点至关重要。

将 **--non-matching** 选项与 **-v** 结合使用，还可以显示文件为何_没有_被忽略，有助于诊断文件意外出现在 git status 输出中的情况。

# CONFIGURATION

**.gitignore**
> 指定要忽略的、有意不纳入跟踪文件的模式的列表。不同目录层级可以存在多个 .gitignore 文件。

**~/.config/git/ignore**
> 用户级全局忽略模式，作用于所有仓库。

**/etc/gitconfig**
> 系统级的 core.excludesFile 配置，指向全局忽略文件。

# CAVEATS

只检查模式，不检查实际文件。嵌套的 gitignore 文件具有更高优先级。取反（negation）模式可以覆盖忽略规则。

# HISTORY

git check-ignore 被加入 **Git** 是为了帮助调试 gitignore 规则，解决忽略模式行为带来的常见困扰。

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

[git-status](/man/git-status)(1)
