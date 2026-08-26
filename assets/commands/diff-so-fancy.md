# TAGLINE

人类可读的 git diff 格式化工具

# TLDR

**将 git diff 输出**通过管道交给 diff-so-fancy

```git diff | diff-so-fancy```

**配置 git** 使用 diff-so-fancy

```git config --global core.pager "diff-so-fancy | less --tabs=4 -RFX"```

**用作 git diff 工具**

```git config --global interactive.diffFilter "diff-so-fancy --patch"```

以改进的输出**显示文件变更**

```diff-so-fancy < [changes.diff]```

# SYNOPSIS

**diff-so-fancy** [_options_]

# DESCRIPTION

**diff-so-fancy** 将 git diff 的输出转换为更易读的格式。它通过更好的行内高亮、更简洁的文件头以及移除块标记来改善 diff 的视觉呈现。

该工具充分利用终端颜色来高亮行内的变化，使代码审查更快更轻松。它被设计为 git pager 的替代品。

# PARAMETERS

**--patch**
> 使用与补丁兼容的输出模式。

**--no-colors**
> 禁用彩色输出。

**--colors**
> 启用彩色输出。

**--set-defaults**
> 配置 git 使用 diff-so-fancy。

# CONFIGURATION

**~/.gitconfig**
> 用于将 diff-so-fancy 集成为默认 pager 的 Git 配置。

# GIT CONFIGURATION

```
git config --global core.pager "diff-so-fancy | less --tabs=4 -RFX"
git config --global color.ui true
git config --global color.diff-highlight.oldNormal "red bold"
git config --global color.diff-highlight.oldHighlight "red bold 52"
git config --global color.diff-highlight.newNormal "green bold"
git config --global color.diff-highlight.newHighlight "green bold 22"
```

# CAVEATS

需要 Perl。修改后的输出不适合用于应用补丁。某些主题可能需要调整颜色。大型 diff 可能较慢。

# HISTORY

**diff-so-fancy** 由 **Seth Vargo** 创建，由 **so-fancy** 维护。它源于对终端中更好 diff 可视化的需求，在 git 的 diff-highlight 脚本基础上增加了额外的格式改进。

# INSTALL

```dnf: sudo dnf install diff-so-fancy```

```pacman: sudo pacman -S diff-so-fancy```

```zypper: sudo zypper install diff-so-fancy```

```brew: brew install diff-so-fancy```

```nix: nix profile install nixpkgs#diff-so-fancy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-diff](/man/git-diff)(1), [delta](/man/delta)(1), [colordiff](/man/colordiff)(1), [diff](/man/diff)(1)

# RESOURCES

```[Source code](https://github.com/so-fancy/diff-so-fancy)```

<!-- verified: 2026-07-11 -->
