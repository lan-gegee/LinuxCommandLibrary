# TAGLINE

为提交生成人类可读的名称

# TLDR

**描述当前提交**

```git describe```

**使用所有标签进行描述**

```git describe --tags```

**描述指定提交**

```git describe [commit]```

**始终使用长格式**

```git describe --long```

**匹配标签模式**

```git describe --match "v*"```

**标记脏工作树**

```git describe --dirty```

# SYNOPSIS

**git describe** [_options_] [_commit_]

# PARAMETERS

_COMMIT_
> 要描述的提交（默认：HEAD）。

**--tags**
> 使用任意标签，不局限于附注标签。

**--long**
> 始终输出长格式。

**--match** _PATTERN_
> 只考虑匹配的标签。

**--abbrev** _N_
> 缩写长度（默认：7，或保证唯一性所需的位数）。

**--always**
> 未找到标签时显示提交缩写。

**--dirty**[=_mark_]
> 工作树有本地改动时追加 **-dirty**。

**--contains**
> 查找位于该提交之后（包含该提交）的标签，而不是最近的前驱标签。隐含 **--tags**。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git describe** 基于可用标签为提交生成一个人类可读的名称。它会找到从该提交可达的最近标签，并描述其间的距离。

输出格式为 标签-距离-gSHA，例如 "v1.0.2-14-g2414721" 表示在 v1.0.2 之后 14 个提交。如果提交正好位于某个标签上，则只返回标签名。这常用于在构建系统中生成版本字符串。

# CAVEATS

需要历史中存在标签。默认优先使用附注标签。距离计算可能较慢。

# HISTORY

git describe 是 **Git** 的核心命令，对于根据仓库状态生成版本字符串至关重要。

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

[git-tag](/man/git-tag)(1), [git-log](/man/git-log)(1), [git-rev-parse](/man/git-rev-parse)(1)
