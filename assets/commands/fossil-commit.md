# TAGLINE

将变更记录到仓库

# TLDR

**带提交信息提交**

```fossil commit -m "[message]"```

**交互式提交**

```fossil commit```

**提交特定文件**

```fossil commit [file1] [file2] -m "[message]"```

**提交到新分支**

```fossil commit --branch [branch_name] -m "[message]"```

**修改最近一次提交**

```fossil amend [checkin] -m "[new message]"```

# SYNOPSIS

**fossil** **commit** [_options_] [_files_...]

# PARAMETERS

**-m**, **--comment** _text_
> 提交信息。

**--branch** _name_
> 创建新分支。

**--tag** _name_
> 添加标签。

**--private**
> 使提交保持私有。

**--allow-empty**
> 允许空提交。

**--close**
> 提交后关闭分支。

# DESCRIPTION

**fossil commit** 将工作副本中的变更记录到仓库，创建一个带有指定注释的新 check-in。所有先前添加或修改过的文件都会包含在提交中。

如果未提供 **-m**，该命令会打开编辑器来输入提交信息。与 Git 不同，Fossil 默认启用 autosync，可能在提交后立即把变更推送到已配置的远程。

提交可以创建新分支、添加标签，并包含时间戳和用户信息等元数据。**--private** 选项创建的提交不会被推送到公共仓库。

# INSTALL

```apt: sudo apt install fossil```

```dnf: sudo dnf install fossil```

```pacman: sudo pacman -S fossil```

```apk: sudo apk add fossil```

```zypper: sudo zypper install fossil```

```brew: brew install fossil```

```nix: nix profile install nixpkgs#fossil```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fossil-add](/man/fossil-add)(1)
