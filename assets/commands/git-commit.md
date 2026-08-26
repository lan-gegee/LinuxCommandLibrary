# TAGLINE

将更改记录到仓库

# TLDR

**提交已暂存的更改**

```git commit -m "[message]"```

**提交所有已跟踪文件的更改**

```git commit -am "[message]"```

**修改上一次提交**

```git commit --amend```

**使用编辑器提交**

```git commit```

**空提交**

```git commit --allow-empty -m "[message]"```

**带签署的提交**

```git commit -s -m "[message]"```

**fixup 提交**

```git commit --fixup [commit]```

**squash 提交**

```git commit --squash [commit]```

# SYNOPSIS

**git** **commit** [_options_] [_--_] [_files_...]

# PARAMETERS

**-m**, **--message** _msg_
> 提交信息。

**-a**, **--all**
> 暂存所有已修改的文件。

**--amend**
> 修改上一次提交。

**--no-edit**
> 沿用之前的提交信息。

**-s**, **--signoff**
> 添加 Signed-off-by。

**--allow-empty**
> 允许空提交。

**--fixup** _commit_
> 针对某提交创建 fixup 提交。

**--squash** _commit_
> 待并入某提交的 squash 提交。

**-v**, **--verbose**
> 在编辑器中显示差异。

**--author** _author_
> 覆盖作者。

**--date** _date_
> 覆盖作者日期。

**-C**, **--reuse-message** _commit_
> 复用现有提交的信息（和作者信息）。

**-c**, **--reedit-message** _commit_
> 与 --reuse-message 类似，但会打开编辑器修改提交信息。

**-F**, **--file** _file_
> 从 _file_ 读取提交信息。

**-S**, **--gpg-sign** [_keyid_]
> 对提交进行 GPG 签名。

**-n**, **--no-verify**
> 跳过 pre-commit 和 commit-msg 钩子。

**-e**, **--edit**
> 强制打开编辑器（配合 -m/-F）。

**-p**, **--patch**
> 交互式选择要暂存并提交的代码块。

**--dry-run**
> 显示将要提交的内容，但不实际创建提交。

# DESCRIPTION

**git commit** 通过创建一个新的提交对象将更改记录到仓库中，该对象包含当前暂存的更改、元数据和描述性信息。每个提交代表仓库历史中的一个快照，由唯一的 SHA-1 哈希标识，并与其父提交相连。

标准工作流是先用 git add 暂存更改，然后提交这些已暂存的更改。-a 标志是这一流程的快捷方式：在提交前自动暂存所有已修改的被跟踪文件。提交信息可用 -m 内联给出，也可以打开编辑器撰写包含详细说明的多行信息。

--amend 选项修改最近一次提交而不是新建提交，适用于纠正错误或补充遗漏的更改。由于这会改写历史，除非可以接受强制推送，否则不应将已修改的提交推送到共享分支。

高级选项支持用 GPG 签名提交（--gpg-sign）、添加共同作者或 issue 引用等元数据，以及为变基工作流创建特殊提交。--fixup 和 --squash 选项创建的提交会在交互式变基时与更早的提交合并，有助于整理凌乱的提交历史。

空提交（--allow-empty）有时很有用，可以在没有实际代码改动的情况下触发 CI/CD 流水线或标记里程碑。--verbose 标志会在编辑器中显示完整差异，帮助你审阅要提交的内容并写出准确的提交信息。

# CONFIGURATION

**~/.gitconfig [commit]**
> 与提交相关的设置，包括默认 gpgSign、模板和清理行为。

**.git/hooks/commit-msg**
> 在提交最终确定前校验或修改提交信息的钩子脚本。

**.git/hooks/pre-commit**
> 在允许提交前运行检查的钩子脚本。

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

[git-add](/man/git-add)(1), [git-status](/man/git-status)(1)
