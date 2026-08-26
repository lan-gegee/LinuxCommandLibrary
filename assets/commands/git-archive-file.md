# TAGLINE

将 git 仓库的当前 HEAD 导出为 zip 归档

# TLDR

**创建当前分支的归档**

```git archive-file```

# SYNOPSIS

**git** **archive-file**

# DESCRIPTION

**git archive-file** 是一个 git-extras 工具，将仓库的当前 HEAD 导出为文件名具有描述性的 zip 归档。生成的文件名包含仓库名和分支名（例如 "project.main.zip"）；在分离 HEAD 状态下（如处于某个标签时），则使用标签名（例如 "project.1.0.0.zip"）。

该命令不接受任何参数或选项。它始终归档当前 HEAD，并将 zip 文件写到当前目录。

自 git-extras 6.4 起，假定的默认分支名从 master 改为 main。

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

[git-archive](/man/git-archive)(1), [git-extras](/man/git-extras)(1)
