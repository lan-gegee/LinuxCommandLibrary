# TAGLINE

用 DVC 跟踪数据文件

# TLDR

**跟踪一个文件**

```dvc add [data.csv]```

**跟踪一个目录**

```dvc add [data/]```

**跟踪外部存储中的文件**

```dvc add --external [/external/data]```

# SYNOPSIS

**dvc** **add** [_options_] _targets_...

# PARAMETERS

**-f**, **--file** _file_
> 指定 .dvc 文件名。

**--external**
> 跟踪仓库外部的文件。

**--no-commit**
> 不自动提交到 git。

**--glob**
> 使用 glob 模式。

# DESCRIPTION

**dvc add** 是把数据文件纳入 DVC 版本控制的基础命令。添加文件时，DVC 会计算其哈希值，把它移入 DVC 缓存，并在原位置创建一个轻量的 .dvc 元数据文件。

.dvc 文件包含从缓存或远程存储取回原文件所需的哈希和路径信息。DVC 会自动把原始文件名加入 .gitignore，这样大的数据文件不会提交进 Git，只有小的 .dvc 元数据文件被提交。

这种双文件方案让 Git 能够跟踪数据版本（通过 .dvc 文件），而无需把实际的大文件存入仓库。缓存的数据随后可以推送到远程存储供团队共享。目录会被递归跟踪，单个 .dvc 文件即可覆盖其全部内容。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

