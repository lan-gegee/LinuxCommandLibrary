# TAGLINE

准备用于邮件提交的补丁

# TLDR

**为最近 N 个提交创建补丁**

```git format-patch -[n]```

**自某提交以来创建补丁**

```git format-patch [commit]```

**为某个范围创建补丁**

```git format-patch [commit1]..[commit2]```

**输出到目录**

```git format-patch -o [patches/] [commit]```

**创建单个合并补丁**

```git format-patch --stdout [commit] > [combined.patch]```

**包含封面说明**

```git format-patch --cover-letter [commit]```

**创建带编号、线程化的补丁并附带基底信息**

```git format-patch --numbered --thread --base=auto [commit]```

**为补丁添加邮件收件人**

```git format-patch --to=[maintainer@example.com] --cc=[list@example.com] -[3]```

# SYNOPSIS

**git** **format-patch** [_options_] [_since_] | [_revision-range_]

# PARAMETERS

**-n**, **--numbered**
> 以 [PATCH n/m] 格式命名输出文件。

**-N**, **--no-numbered**
> 以不带编号的 [PATCH] 格式命名输出文件。

**-o**, **--output-directory** _dir_
> 补丁文件的输出目录。

**--stdout**
> 将所有补丁输出到 stdout 而不是文件。

**--cover-letter**
> 为补丁系列生成封面说明模板。

**-s**, **--signoff**
> 添加 Signed-off-by 尾注。

**--subject-prefix** _prefix_
> 使用给定的前缀代替 [PATCH]。

**-v**, **--reroll-count** _n_
> 将补丁标记为该系列的第 _n_ 版（如 [PATCH v2]）。

**--thread**[=_style_]
> 生成 In-Reply-To 和 References 头。style 可选 shallow（默认）或 deep。

**--in-reply-to** _message-id_
> 让第一封邮件显示为对指定消息的回复。

**--to** _email_
> 为补丁添加 To: 头。可以多次使用。

**--cc** _email_
> 为补丁添加 Cc: 头。可以多次使用。

**--base**[=_commit_]
> 记录基底树信息。使用 "auto" 表示自动选择。

**--no-stat**
> 生成不带 diffstat 的普通补丁。

**--no-binary**
> 不输出二进制文件的内容，仅注明有变更。

**--interdiff** _previous_
> 在封面说明中插入 interdiff，与上一版本比较。

**--range-diff** _previous_
> 在封面说明中插入 range-diff，与上一版本比较。

**--filename-max-length** _n_
> 将生成的文件名限制在大约 _n_ 字节以内（默认：64）。

# DESCRIPTION

**git format-patch** 以适合基于电子邮件的代码评审和提交工作流的格式从提交生成补丁文件。每个提交被格式化为单独的 .patch 文件，以 mbox 格式包含 diff、提交元数据和提交信息。

该命令是 Linux 内核和 Git 自身等项目所采用的邮件驱动开发流程的基础。生成的补丁可以使用 git send-email 或标准邮件客户端发送，并用 git am 应用，同时完整保留包括作者和日期在内的提交信息。

封面说明（--cover-letter）提供了为补丁系列添加背景说明的方式。-v 的版本号支持迭代的评审周期。signoff 选项会添加 Signed-off-by 尾注，以满足开发者原产地证明（DCO）的要求。

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

[git-am](/man/git-am)(1), [git-send-email](/man/git-send-email)(1), [git-apply](/man/git-apply)(1), [git-diff](/man/git-diff)(1)
