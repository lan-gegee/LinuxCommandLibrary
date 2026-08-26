# TAGLINE

创建用于撤销先前改动的提交

# TLDR

**撤销一个提交**

```git revert [commit]```

**撤销多个提交**

```git revert [commit1] [commit2]```

**撤销但不创建提交**

```git revert -n [commit]```

**撤销合并提交**

```git revert -m [1] [merge_commit]```

**解决冲突后继续**

```git revert --continue```

**中止撤销**

```git revert --abort```

# SYNOPSIS

**git** **revert** [_options_] _commit_...

# PARAMETERS

**-n**, **--no-commit**
> 将撤销应用到工作树和索引，但不创建提交。

**-e**, **--edit**
> 提交前编辑提交信息（交互式运行时的默认行为）。

**--no-edit**
> 使用默认生成的提交信息。

**-m** _parent-number_, **--mainline** _parent-number_
> 撤销合并提交时指定主线父提交（从 1 开始编号）。

**-s**, **--signoff**
> 在提交信息中添加 `Signed-off-by` 尾注。

**-S**[_keyid_], **--gpg-sign**[=_keyid_]
> 为撤销提交进行 GPG 签名。

**--cleanup=**_mode_
> 控制提交信息的清理方式（见 git-commit）。

**--strategy=**_strategy_
> 使用指定的合并策略。

**-X** _option_, **--strategy-option=**_option_
> 将选项传递给合并策略。

**--continue**
> 解决冲突后继续撤销操作。

**--skip**
> 跳过当前提交并继续处理剩余的提交。

**--abort**
> 取消进行中的撤销操作并恢复到序列开始前的状态。

**--quit**
> 忘记当前操作；索引和工作树保持原样。

# DESCRIPTION

**git revert** 创建新的提交来撤销指定提交所引入的改动。与 `git reset` 不同，它通过添加反向提交来保留历史，而不是移除已有提交。

因此对共享分支而言它是安全的——重写历史在那种场景下会引发问题。撤销合并提交时用 `-m` 指定主线父提交。

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

[git-reset](/man/git-reset)(1), [git-cherry-pick](/man/git-cherry-pick)(1)
