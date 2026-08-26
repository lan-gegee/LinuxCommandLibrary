# TAGLINE

复用已记录的合并冲突解决方案

# TLDR

**启用 rerere**

```git config rerere.enabled true```

**显示已记录的解决方案**

```git rerere status```

**显示解决方案的差异**

```git rerere diff```

**清除已记录的解决方案**

```git rerere clear```

**忘记某个解决方案**

```git rerere forget [file]```

# SYNOPSIS

**git rerere** [_command_]

# PARAMETERS

**status**
> 显示已有记录解决方案的路径。

**diff**
> 显示当前解决方案的差异。

**clear**
> 清除已记录的解决方案。

**forget** _PATH_
> 忘记某个路径的解决方案。

**gc**
> 清理旧的记录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git rerere**（reuse recorded resolution，复用已记录的解决方案）会记住你解决合并冲突的方式，并在之后的合并中自动套用这些方案。在反复进行合并和变基时尤其有价值。

启用后，Git 会记录冲突的解决方案。当后续合并出现相同冲突时，之前的解决方案会被自动应用，免去重复解决冲突的工作。

# CONFIGURATION

**rerere.enabled**
> 在 git config 中设为 `true`，即可启用冲突解决方案的自动记录。

# CAVEATS

必须在配置中启用。记录仅保存在本地。若上下文不同，可能会应用错误的解决方案。

# HISTORY

git rerere 被加入 **Git** 是为了解决重复解决同一合并冲突的痛点，尤其是在长期分支和变基场景下。

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

[git-merge](/man/git-merge)(1), [git-rebase](/man/git-rebase)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-rerere)```

<!-- verified: 2026-07-17 -->
