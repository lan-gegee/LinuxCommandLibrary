# TAGLINE

内部工具集成库

# TLDR

**供工具脚本 source 引用**

```. "$(git --exec-path)/git-mergetool--lib"```

# SYNOPSIS

**git-mergetool--lib**

# DESCRIPTION

**git-mergetool--lib** 是 `git-mergetool` 和 `git-difftool` 内部使用的 shell 库。它提供用于工具选择、调用和配置处理的公共函数。

需要合并或 diff 工具功能的脚本会 source 该库。它负责工具检测、路径配置以及特定工具的设置。这属于内部基础设施，不供直接使用。

# CAVEATS

内部库，不是命令。由其他 git 脚本 source 引用。不供直接使用。

# HISTORY

git-mergetool--lib 是 **Git** 内部基础设施的一部分，为合并与 diff 工具集成提供共享代码。

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

[git-mergetool](/man/git-mergetool)(1), [git-difftool](/man/git-difftool)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-mergetool--lib)```

<!-- verified: 2026-07-17 -->
