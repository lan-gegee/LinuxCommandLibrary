# TAGLINE

改写某个提交的作者和提交者

# TLDR

将某个提交**重新归属**给另一位作者

```git blame-someone-else "[Author Name] <email@example.com>" [commit]```

**重新归属**最近一次提交

```git blame-someone-else "[Name] <email@example.com>" HEAD```

按哈希**重新归属**某个提交

```git blame-someone-else "[Name] <email@example.com>" [abc123]```

# SYNOPSIS

**git blame-someone-else** _author_ _commit_

# PARAMETERS

_author_
> 新的身份，格式为 **"Name &lt;email&gt;"**。

_commit_
> 要改写的提交。

# DESCRIPTION

**git blame-someone-else** 改写一个提交，使它看起来像是由别人做出的。它是 **Jay Phelps** 编写的独立脚本，本意是个玩笑，不属于 git-extras 或核心 git。

机制上，它使用 **git filter-branch** 并为该目标提交覆盖 **GIT_AUTHOR_NAME**、**GIT_AUTHOR_EMAIL**、**GIT_COMMITTER_NAME** 和 **GIT_COMMITTER_EMAIL**，然后重写自那之后的每个提交。作者和提交者都会被改变，而不只是作者。

唯一说得过去的用途是修复你自己的归属信息：由于 **user.email** 配置错误或在共用机器上做出的提交，其记录的身份完全是错的。

# CAVEATS

这是一个玩笑工具，作者本人明确如此声明，并请求不要对生产仓库运行它然后在它毁掉一切时抱怨。请相应对待。

它会**重写历史**。从目标提交开始的每个提交都会得到新哈希，因此任何已经拉取过旧提交的人都会面临历史分叉，发布结果还需要强制推送。绝不要在共享分支上运行。

它会同时更改**提交者**和作者，因此它不只是纠正归属，还抹掉了究竟是谁做出这个提交的记录。

把工作归功于并未编写它的真实人物是不诚实的，在你不拥有的仓库上这样做还可能违反项目的贡献条款。签名提交也无法幸存：重写会使所有 GPG 签名失效，而这正是抵御此类行为的少数技术手段之一。

修正你自己的身份并不需要这个工具。**git commit --amend --author="Name <email>"** 可修复最近一次提交，配合 **--reset-author** 的 **git rebase -i** 能以更小的附带损害处理更早的提交。

# HISTORY

**git blame-someone-else** 由 **Jay Phelps** 于 **2016 年**作为玩笑编写。其 README 引用了一段来自 **Linus Torvalds** 的"背书"，而那本身就是用该工具伪造的提交，用以演示它确实有效。

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

[git-blame](/man/git-blame)(1), [git-commit](/man/git-commit)(1), [git-filter-branch](/man/git-filter-branch)(1), [git-rebase](/man/git-rebase)(1)

# RESOURCES

```[Source code](https://github.com/jayphelps/git-blame-someone-else)```

<!-- verified: 2026-07-16 -->
