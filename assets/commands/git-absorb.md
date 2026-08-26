# TAGLINE

为暂存的更改自动创建 fixup 提交

# TLDR

将暂存的更改**吸收**进匹配的提交

```git absorb```

**吸收并自动 rebase**

```git absorb --and-rebase```

用**试运行**查看将会发生什么

```git absorb --dry-run```

为 absorb 栈**指定基准提交**

```git absorb --base [HEAD~5]```

跳过安全检查**强制吸收**

```git absorb --force```

**显示详细输出**

```git absorb --verbose```

# SYNOPSIS

**git absorb** [_options_]

# PARAMETERS

**-r**, **--and-rebase**
> 在创建 fixup 提交后自动运行 git rebase --autosquash。

**-n**, **--dry-run**
> 显示将要执行的操作，但不实际更改。

**-b**, **--base** _commit_
> 使用指定的提交作为 absorb 栈的基准。

**-f**, **--force**
> 创建 fixup 提交时跳过安全检查。

**-v**, **--verbose**
> 执行期间显示额外信息。

**-w**, **--whole-file**
> 将更改匹配到最后修改该文件的提交。

**--one-fixup-per-commit**
> 每个提交只创建一个 fixup；发生冲突时使用第一个 hunk。

**--squash-instead-of-fixup**
> 创建 squash 提交而不是 fixup 提交。

**-h**, **--help**
> 打印帮助信息。

**-V**, **--version**
> 打印版本信息。

# DESCRIPTION

**git-absorb** 会为暂存的更改自动创建 **fixup!** 提交，把每个 hunk 匹配到分支历史中合适的提交上。它是 Facebook 面向 Mercurial 的 **hg absorb** 工具的移植版。

工作流程是：先用 **git add** 暂存更改，再运行 **git absorb** 创建 fixup 提交，然后要么手动运行 **git rebase -i --autosquash**，要么使用 **--and-rebase** 自动完成。默认情况下，absorb 会在最近 10 个提交中搜索。

# CONFIGURATION

**~/.gitconfig**
> 配置 `absorb.maxStack` 控制 absorb 向前搜索多少个提交（默认：10）。

# CAVEATS

只考虑暂存的更改（git 索引）。无法吸收跨越多个原始提交的更改。新代码（不修改现有行的代码）无法被吸收。安全检查在某些情况下会阻止吸收；可使用 **--force** 覆盖。

# HISTORY

Git-absorb 由 **Stephen Jung**（tummychow）创建，是 Facebook 面向 Mercurial 的 **hg absorb** 命令的 Rust 移植版。它在堆叠式 diff（stacked diff）工作流中广受欢迎，因为这类工作流对保持干净的提交历史至关重要。

# INSTALL

```dnf: sudo dnf install git-absorb```

```pacman: sudo pacman -S git-absorb```

```apk: sudo apk add git-absorb```

```zypper: sudo zypper install git-absorb```

```brew: brew install git-absorb```

```nix: nix profile install nixpkgs#git-absorb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-rebase](/man/git-rebase)(1), [git-commit](/man/git-commit)(1), [git-branchless](/man/git-branchless)(1)
