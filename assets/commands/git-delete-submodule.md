# TAGLINE

从仓库中彻底移除子模块

# TLDR

**删除一个子模块**

```git delete-submodule [path/to/submodule]```

# SYNOPSIS

**git** **delete-submodule** _path_

# DESCRIPTION

**git delete-submodule** 从仓库中彻底移除一个子模块，将 Git 正确删除子模块所需的多步流程自动化。它是 git-extras 的组成部分，用一条命令完成所有必要的清理操作。

手动移除子模块需要先对其执行 deinit，编辑 .gitmodules，删除 .git/config 中的条目，删除 .git/modules/[name]，再移除工作目录。遗漏任何一步都会留下残留配置并引发后续问题。该命令统筹所有必需的操作，确保彻底移除。

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

[git-submodule](/man/git-submodule)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

<!-- verified: 2026-07-17 -->
