# TAGLINE

将 quilt 补丁导入为提交

# TLDR

**导入 quilt 补丁**

```git quiltimport```

**从特定目录导入**

```git quiltimport --patches [patches/]```

**试运行**

```git quiltimport -n```

# SYNOPSIS

**git quiltimport** [_options_]

# PARAMETERS

**--patches** _DIR_
> 补丁目录。默认为 patches 或 $QUILT_PATCHES。

**--series** _FILE_
> series 文件的位置。默认为 <patches>/series 或 $QUILT_SERIES。

**-n**, **--dry-run**
> 显示将要导入的内容。

**--author** _AUTHOR_
> 默认作者。

**--keep-non-patch**
> 向 git mailinfo 传递 -b 标志，以在提交信息中保留非补丁内容。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git quiltimport** 将一个 quilt 补丁集作为一系列提交导入 Git。Quilt 是一套补丁管理系统；该命令读取补丁目录和 series 文件，按顺序每个补丁创建一个提交。

该命令支持从基于 quilt 的开发工作流迁移到 Git——这在 Git 成为标准之前，尤其在 Linux 发行版打包领域相当常见。

# CAVEATS

要求 quilt 补丁格式正确。可能需要指定作者信息。只能单向导入。

# HISTORY

git quiltimport 支持从 **quilt** 迁移。quilt 是 Git 普及之前流行的补丁管理工具，尤其常见于 Linux 发行版开发中。

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

[git-am](/man/git-am)(1), [git-apply](/man/git-apply)(1), [quilt](/man/quilt)(1)
