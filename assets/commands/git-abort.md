# TAGLINE

中止任何进行中的 git 操作（rebase、merge、cherry-pick、revert、am）

# TLDR

**中止当前进行中的操作**

```git abort```

# SYNOPSIS

**git abort**

# DESCRIPTION

**git abort** 是 **git-extras** 套件中的一个便捷命令。它通过检查 `.git` 目录来检测哪个 git 操作正在进行中，并执行相应的中止命令：

- rebase 进行中（`rebase-merge/` 或 `rebase-apply/`）→ `git rebase --abort`
- merge 进行中（`MERGE_HEAD`）→ `git merge --abort`
- cherry-pick 进行中（`CHERRY_PICK_HEAD`）→ `git cherry-pick --abort`
- revert 进行中（`REVERT_HEAD`）→ `git revert --abort`
- `git am` 进行中（`rebase-apply/applying`）→ `git am --abort`

如果没有操作在进行中，它会打印一条消息并以非零状态退出。

# CAVEATS

由 **git-extras** 提供，不是 git 的内置命令。可通过软件包管理器安装（`apt install git-extras`、`brew install git-extras` 等），也可从源码安装。所有中止操作对正在运行的操作而言都是破坏性的——未提交的合并解决方案或 rebase 编辑都会被丢弃。工作树会被重置回该操作开始之前的状态。

# HISTORY

**git-extras** 是 **TJ Holowaychuk** 发起的长期项目，捆绑了数十个面向日常工作流的 git 子命令。加入 `git abort` 是为了把各种操作专用的 `--abort` 标志统一到一个易记的命令之下。

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

[git-rebase](/man/git-rebase)(1), [git-merge](/man/git-merge)(1), [git-cherry-pick](/man/git-cherry-pick)(1), [git-am](/man/git-am)(1), [git-extras](/man/git-extras)(1)
