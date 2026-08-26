# TAGLINE

用自动生成的提交信息提交更改

# TLDR

**提交已暂存的更改**，并使用生成的提交信息

```git magic```

**暂存所有更改**（需确认）并提交

```git magic -a```

**提交并推送**

```git magic -p```

**提交并强制推送**

```git magic -p -f```

**在生成的信息前添加自定义标题**

```git magic -m "[title]"```

**提交前编辑生成的信息**

```git magic -e```

# SYNOPSIS

**git** **magic** [_-a_] [_-m_ _msg_] [_-e_] [_-p_] [_-f_]

# PARAMETERS

**-a**
> 提交前暂存所有更改（需确认）。

**-m** _msg_
> 在前面添加自定义信息；自动生成的摘要会附在其后。

**-e**
> 打开编辑器审阅提交信息，而不是直接以 `--no-edit` 提交。

**-p**
> 提交后推送。

**-f**
> 强制推送；仅在与 `-p` 组合时生效。

**-h**
> 显示用法信息。

# DESCRIPTION

**git magic** 是一个 git-extras 命令，它基于 `git status --porcelain -uno` 自动生成提交信息来完成提交，因此最终的信息会列出发生变更的文件。默认情况下，提交过程不打开编辑器（`--no-edit`）。

传入 `-a` 会先显示 `git status`，请求确认，然后在提交前暂存所有内容。`-m` 允许你在自动生成的摘要前添加一段真实的信息，`-e` 会打开编辑器调整最终信息，而 `-p`（可配合 `-f` 进行强制推送）会在提交后立即推送。

# CAVEATS

必须在 git 工作区内运行；它会自动切换到仓库顶层目录。生成的信息只是变更文件的列表，并非有意义的描述，因此更适合快速 WIP 提交，而不适合希望长期保持可读性的历史。

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

[git-commit](/man/git-commit)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-magic)```

<!-- verified: 2026-07-17 -->
