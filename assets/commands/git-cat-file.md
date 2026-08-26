# TAGLINE

显示仓库对象的内容或元数据

# TLDR

**显示对象类型**

```git cat-file -t [object]```

**显示对象大小**

```git cat-file -s [object]```

**显示对象内容**

```git cat-file -p [object]```

**显示 blob 内容**

```git cat-file blob [hash]```

**显示 commit 内容**

```git cat-file commit [hash]```

**显示 tree 内容**

```git cat-file tree [hash]```

**对标准输入中的对象批量输出信息和内容**

```git cat-file --batch```

**对标准输入中的对象批量检查类型和大小**

```git cat-file --batch-check```

# SYNOPSIS

**git** **cat-file** [_options_] _object_

# PARAMETERS

**-t**
> 显示对象类型。

**-s**
> 显示对象大小。

**-p**
> 以易读格式输出内容。

**-e**
> 如果对象存在且有效则以零状态退出。

**--batch**
> 对从标准输入读取的每个对象 ID 输出对象信息和内容。

**--batch-check**
> 对从标准输入读取的每个对象 ID 输出对象类型和大小。

**--textconv**
> 显示经已配置的 textconv 过滤器转换后的内容。

**blob**
> 显示 blob。

**commit**
> 显示 commit。

**tree**
> 显示 tree。

# DESCRIPTION

**git cat-file** 提供对 Git 对象数据库的直接访问，可用于查看 blob、tree、commit 和 tag。这个底层管道命令（plumbing）揭示了 Git 内容寻址存储系统的内部结构。

该命令作用于对象哈希（SHA-1 或 SHA-256），可以显示对象类型、大小或以易读格式输出内容。它对于调试仓库损坏、理解 Git 内部机制以及仓库历史的取证分析必不可少。

常见用途包括：在不检出的情况下检查文件的特定版本、检查 tree 结构以了解特定提交时的目录布局，以及验证对象完整性。-p 选项以人类可读格式美化输出对象，而 -t 和 -s 只提供元数据而不提取完整内容。

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

[git-show](/man/git-show)(1), [git-hash-object](/man/git-hash-object)(1), [git-ls-tree](/man/git-ls-tree)(1), [git-rev-parse](/man/git-rev-parse)(1), [git-verify-pack](/man/git-verify-pack)(1)
