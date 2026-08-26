# TAGLINE

查找提交的符号名称

# TLDR

**查找提交的符号名称**

```git name-rev [commit]```

**为多个提交命名**

```git name-rev [commit1] [commit2]```

**为来自标准输入的提交哈希添加标注**

```git log --oneline | git name-rev --annotate-stdin```

**只用标签为提交命名**

```git name-rev --tags [commit]```

**排除匹配模式的引用**

```git name-rev --exclude="refs/tags/*" [commit]```

**为所有引用可达的全部提交命名**

```git name-rev --all```

# SYNOPSIS

**git** **name-rev** [_options_] _commit_...
**git** **name-rev** [_options_] **--all**
**git** **name-rev** [_options_] **--annotate-stdin**

# PARAMETERS

**--annotate-stdin**
> 转换标准输入，把其中的提交哈希替换为对应的符号名称。取代已弃用的 --stdin。

**--tags**
> 只用标签为提交命名。

**--refs** _pattern_
> 只使用名称匹配给定 shell 模式的引用。

**--exclude** _pattern_
> 不使用任何名称匹配给定 shell 模式的引用。

**--all**
> 列出从所有引用可达的全部提交。

**--name-only**
> 只打印符号名称，不打印 SHA-1。

**--no-undefined**
> 引用未定义时以错误退出，而不是打印 "undefined"。

**--always**
> 找不到名称时退而显示唯一缩写的提交对象。

# DESCRIPTION

**git name-rev** 为给定的提交哈希查找符号名称，使其更易于人类阅读。它会显示最能描述每个提交的最近引用（分支或标签），以及距该引用的提交数（例如 "main~3" 表示 main 之前的第三个提交）。

`--annotate-stdin` 选项可以处理管道中的提交哈希，从而为 `git log` 输出或其他产生提交 ID 的命令添加标注。`--tags` 或 `--refs` 等过滤选项可限制用于命名的引用范围。

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

[git-describe](/man/git-describe)(1), [git-rev-parse](/man/git-rev-parse)(1), [git-log](/man/git-log)(1)
