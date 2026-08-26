# TAGLINE

比较两个提交区间

# TLDR

**比较两个版本区间**

```git range-diff [base1]..[rev1] [base2]..[rev2]```

**与上游比较**

```git range-diff @{u} @{1} @```

**比较 rebase 前后的版本**

```git range-diff [main]..@{1} [main]..@```

**带颜色显示**

```git range-diff --color [range1] [range2]```

# SYNOPSIS

**git** **range-diff** [_options_] _range1_ _range2_

# PARAMETERS

**--creation-factor** _n_
> 提交匹配的阈值。

**--no-dual-color**
> 禁用双色模式。

**--notes** _ref_
> 显示注释（notes）。

# DESCRIPTION

**git range-diff** 比较两个提交区间，显示一系列补丁在版本之间发生了什么变化。它执行"差异的差异"，基于内容相似度在两个区间之间匹配提交，揭示 rebase、amend 或其他历史改写过程中产生的变化。

常见用例包括：比较功能分支 rebase 前后的状态、评审补丁在迭代开发中的演变、或验证 rebase 是否保留了预期的更改。输出使用双色调色来区分两层 diff。

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

[git-diff](/man/git-diff)(1), [git-log](/man/git-log)(1), [git-rebase](/man/git-rebase)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-range-diff)```

<!-- verified: 2026-07-17 -->
