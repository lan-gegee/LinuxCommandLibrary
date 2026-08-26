# TAGLINE

在 Git 工作流的关键节点触发的脚本

# TLDR

**创建 pre-commit 钩子**

```echo '#!/bin/sh' > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit```

**列出可用的钩子**

```ls .git/hooks/*.sample```

**启用示例钩子**

```mv .git/hooks/pre-commit.sample .git/hooks/pre-commit```

# DESCRIPTION

**Git 钩子（hooks）**是在 Git 工作流的关键节点自动运行的脚本。它们可以实现代码检查、测试和提交信息校验等任务的自动化。

钩子存放在 **.git/hooks/** 中且必须可执行。常见钩子包括 pre-commit（提交之前）、prepare-commit-msg（编辑信息）、commit-msg（校验信息）和 pre-push（推送之前）。

# 钩子类型

**客户端钩子：**
```
pre-commit         Run before commit
prepare-commit-msg Edit commit message template
commit-msg         Validate commit message
post-commit        After commit completes
pre-rebase         Before rebase starts
post-checkout      After checkout or switch
post-merge         After merge completes
pre-push           Before push
```

**服务端钩子：**
```
pre-receive        Before accepting push
update             Per-branch pre-receive
post-receive       After push completes
post-update        After all refs updated
```

# CONFIGURATION

**.git/hooks/**
> 存放仓库钩子脚本的默认目录。脚本必须可执行。

**core.hooksPath**
> 用于覆盖钩子目录的 Git 配置变量（自 Git 2.9 起）。通过 `git config core.hooksPath <path>` 设置。

# CAVEATS

.git/hooks 中的钩子不受版本控制。可使用 Husky 或 pre-commit 等工具共享钩子。钩子可以通过 --no-verify 绕过。请保持钩子执行迅速，以免拖累工作流。

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

[git](/man/git)(1), [git-commit](/man/git-commit)(1), [husky](/man/husky)(1), [pre-commit](/man/pre-commit)(1)
