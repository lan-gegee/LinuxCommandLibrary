# TAGLINE

管理多语言的 git hook 脚本

# TLDR

**将 hook 安装到仓库中**

```pre-commit install```

**手动运行所有 hook**

```pre-commit run --all-files```

**运行特定 hook**

```pre-commit run [hook_id]```

**更新 hook 版本**

```pre-commit autoupdate```

**创建示例配置**

```pre-commit sample-config```

**安装 commit-msg hook**

```pre-commit install --hook-type commit-msg```

**对特定文件运行**

```pre-commit run --files [file1] [file2]```

**清理缓存的 hook 环境**

```pre-commit clean```

# SYNOPSIS

**pre-commit** _command_ [_--all-files_] [_--files files_] [_options_]

# PARAMETERS

**install**
> 安装 git hook。

**uninstall**
> 移除 git hook。

**run** [_hook_id_]
> 手动运行 hook。

**autoupdate**
> 将 hook 更新到最新版本。

**sample-config**
> 生成示例配置。

**clean**
> 清理缓存的环境。

**gc**
> 垃圾回收未使用的环境。

**try-repo** _REPO_
> 试运行仓库中的 hook。

**--all-files**, **-a**
> 对所有文件运行，而不仅是暂存的文件。

**--files** _FILES_
> 对特定文件运行。

**--hook-stage** _STAGE_
> 为指定阶段运行 hook：pre-commit、pre-push、commit-msg、post-commit 等。

**--hook-type** _TYPE_
> 为指定类型安装 hook。

**--color** _WHEN_
> 彩色输出：auto、always、never。

**--verbose**, **-v**
> 详细输出。

# DESCRIPTION

**pre-commit** 以代码质量检查的方式管理和运行 git hook。hook 在提交前自动运行，在问题进入仓库之前将其拦截。

配置位于 .pre-commit-config.yaml 中，列出要使用的仓库和 hook。hook 可以检查格式、lint 代码、验证文件或运行任意自定义命令。

每个 hook 都在隔离的环境中运行，自动安装并缓存。这确保了无论开发者的本地环境如何，行为都保持一致。支持特定语言的环境（Python、Node、Ruby 等）。

常见 hook 包括：trailing-whitespace、end-of-file-fixer、check-yaml、check-json、black、flake8、prettier、eslint。hook 生态系统为大多数需求提供了现成的检查工具。

Autoupdate 从各仓库获取最新的 hook 版本。--all-files 标志针对整个代码库运行，适用于 CI 或初始清理。特定阶段的 hook（commit-msg、pre-push）可启用额外的检查。

# CAVEATS

首次安装 hook 可能较慢。hook 需要在每次 clone 后单独安装。某些 hook 可能相互冲突。大文件会拖慢提交速度。hook 更新可能引入破坏性变更。CI 与本地环境应保持一致。

# HISTORY

**pre-commit** 由 **Anthony Sottile** 于 **2014 年**前后在 Yelp 创建。它解决了跨团队管理 git hook 的问题——此前 hook 往往未被提交或不一致。该框架使 hook 管理标准化，并催生了一个庞大的可共享 hook 生态。

# INSTALL

```dnf: sudo dnf install pre-commit```

```pacman: sudo pacman -S pre-commit```

```apk: sudo apk add pre-commit```

```brew: brew install pre-commit```

```nix: nix profile install nixpkgs#pre-commit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-hooks](/man/git-hooks)(5), [husky](/man/husky)(1), [lefthook](/man/lefthook)(1), [lint-staged](/man/lint-staged)(1)
