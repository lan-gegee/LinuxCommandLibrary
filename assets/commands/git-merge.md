# TAGLINE

将开发历史汇合到一起

# TLDR

**将分支合并到当前分支**

```git merge [branch-name]```

**带提交信息合并**

```git merge [branch] -m "[message]"```

**禁止 fast-forward 合并（保留拓扑结构）**

```git merge --no-ff [branch]```

**只允许 fast-forward，否则失败**

```git merge --ff-only [branch]```

**压缩合并（单个暂存变更集，无合并提交）**

```git merge --squash [branch]```

**发生冲突时偏向我方或对方**

```git merge -X ours [branch]```

**中止或继续进行中的合并**

```git merge --abort``` / ```git merge --continue```

# SYNOPSIS

**git merge** [_options_] [_commit_...]

**git merge** (--continue | --abort | --quit)

# PARAMETERS

_COMMIT_
> 要合并进当前分支的分支或提交。

**--no-ff**
> 总是创建合并提交，即使可以 fast-forward。

**--ff-only**
> 若当前 HEAD 无法 fast-forward 则拒绝合并。

**--squash**
> 让工作区/索引呈现为真实合并后的状态，但不创建提交。

**--no-commit**
> 执行合并但在创建提交前停止（便于检查）。

**-m** _MESSAGE_
> 设置合并提交的信息。

**-e**, **--edit**
> 调用编辑器完善自动生成的提交信息。

**--abort**
> 中止当前的冲突解决过程，重建合并前的状态。

**--continue**
> 冲突解决完成后继续本次合并。

**--quit**
> 忘记当前进行中的合并，但不恢复合并前的状态。

**-s** _STRATEGY_, **--strategy=**_STRATEGY_
> 选择合并策略：`ort`（默认）、`resolve`、`octopus`、`ours` 或 `subtree`。

**-X** _OPTION_, **--strategy-option=**_OPTION_
> 传入策略专属选项（例如 `ours`、`theirs`、`ignore-all-space`、`find-renames`）。

**--autostash**
> 在合并前后自动 stash 并恢复本地更改。

**--allow-unrelated-histories**
> 合并不共享共同祖先的历史。

**--verify-signatures**
> 要求被合并分支末端具有有效的 GPG 签名。

**-S**[_KEYID_], **--gpg-sign**[=_KEYID_]
> 为生成的合并提交添加 GPG 签名。

**--log**[=_N_]
> 在合并提交信息中包含被合并提交的单行描述。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git merge** 将指定提交（通常是分支末端）的更改并入当前分支。**git pull** 内部也会调用它来整合抓取到的更改。

fast-forward 合并只是把当前分支指针前移到被合并的提交，不创建新提交；`--no-ff` 强制创建合并提交以保留分支拓扑，而 `--ff-only` 在不是 fast-forward 时拒绝合并。压缩合并（`--squash`）把所有传入更改折叠成单个暂存变更集，不记录合并提交。

发生文本冲突时，冲突标记会被写入受影响的文件；解决冲突后 `git add` 这些文件，再运行 `git merge --continue`（或 `git commit`）。默认策略是 **ort**（"Ostensibly Recursive's Twin"），它在 Git 2.33 中取代了旧的 **recursive** 策略，能够处理带重命名检测的三方合并。

# CAVEATS

出现冲突时必须手动解决，合并才能完成。fast-forward 合约会丢失分支拓扑，除非使用 `--no-ff`。使用 `-X ours`/`-X theirs` 会在冲突时静默丢弃一方的更改。`--strategy=ours` 与 `-X ours` 差异极大：前者只保留当前分支的目录树。

# HISTORY

**git merge** 自 **Git** 最早的发布以来就是核心命令。默认策略在 Git 2.33（2021 年 8 月）中从 **recursive** 更名为 **ort**，以改进正确性和性能。`--autostash` 在 Git 2.27 中加入，`--quit` 在 Git 2.11 中加入。

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

[git-rebase](/man/git-rebase)(1), [git-cherry-pick](/man/git-cherry-pick)(1), [git-mergetool](/man/git-mergetool)(1), [git-pull](/man/git-pull)(1), [git-branch](/man/git-branch)(1)
