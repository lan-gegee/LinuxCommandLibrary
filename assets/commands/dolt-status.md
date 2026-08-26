# TAGLINE

显示工作树和暂存区状态

# TLDR

**显示工作树状态**

```dolt status```

# SYNOPSIS

**dolt** **status**

# DESCRIPTION

**dolt status** 显示 Dolt 仓库中工作树和暂存区的当前状态。它把表分为三类：已暂存、等待提交的变更，工作集中未暂存的修改，以及未跟踪的新表。

通过输出可以了解下一次提交会包含哪些内容、工作集中还剩哪些变更。这在提交前尤为重要：既能确认目标表已正确暂存，也能避免误提交无关变更。

与 git status 类似，它清晰地呈现仓库状态，指出哪些表需要注意，以及接下来适合执行哪些操作（add、commit 或 reset）。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt-add](/man/dolt-add)(1)
