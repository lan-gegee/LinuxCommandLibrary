# TAGLINE

从树对象创建提交对象

# TLDR

**从树对象创建提交**

```echo "[message]" | git commit-tree [tree_hash]```

**带父提交创建**

```echo "[message]" | git commit-tree [tree] -p [parent]```

**从消息文件创建**

```git commit-tree [tree] -F [message.txt]```

**创建合并提交**

```git commit-tree [tree] -p [parent1] -p [parent2] -m "[message]"```

# SYNOPSIS

**git** **commit-tree** _tree_ [_options_]

# PARAMETERS

**-p** _parent_
> 父提交。

**-m** _message_
> 提交日志信息中的一个段落。可以多次给出，每段各成一段。

**-F** _file_
> 从给定文件读取提交日志信息。用 - 表示从标准输入读取。可以多次给出。

**-S**[_keyid_]
> 对提交进行 GPG 签名。keyid 可选，默认为提交者身份；若指定，必须不带空格地紧跟在选项后面。

**--no-gpg-sign**
> 抵消先前的 --gpg-sign 选项。

# DESCRIPTION

**git commit-tree** 是一个底层管道命令（plumbing），直接根据树对象哈希创建新的提交对象。与 git commit（上层瓷器命令）不同，它绕过索引和工作目录，直接操作 Git 内部的对象数据库。

git commit 内部就使用该命令，但它也适用于高级场景，例如仓库修复、历史重建或以编程方式创建提交。它要求提供树哈希（通常由 git write-tree 创建或从现有提交提取），并接受可选的父提交哈希来建立谱系。

多个 -p 选项可创建拥有多个父提交的合并提交。提交信息可以用 -m 内联提供、用 -F 从文件读取，或通过管道送入标准输入。作者和提交者信息来自 git config，除非用环境变量覆盖（GIT_AUTHOR_NAME、GIT_COMMITTER_DATE 等）。

该命令输出新建提交对象的 SHA-1 哈希。要让提交可见，通常需要用 git update-ref 或 git reset 更新分支引用。大多数用户不需要直接使用此命令，但它是理解 Git 内部架构和进行高级仓库操作的基础。

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

[git-commit](/man/git-commit)(1), [git-write-tree](/man/git-write-tree)(1), [git-update-ref](/man/git-update-ref)(1)
