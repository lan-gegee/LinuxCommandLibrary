# TAGLINE

通过构建受影响的软件包来测试 Nix 软件包变更

# TLDR

**审查拉取请求**

```nixpkgs-review pr [12345]```

**使用本地检出审查**

```nixpkgs-review rev HEAD```

**审查特定提交**

```nixpkgs-review rev [abc123]```

**审查并在构建后发布报告**

```nixpkgs-review pr [12345] --post-result```

**审查时允许非自由（unfree）软件包**

```nixpkgs-review pr [12345] --allow-unfree```

**审查时指定核心数量**

```nixpkgs-review pr [12345] --build-args "-j [4]"```

**列出构建失败的软件包**

```nixpkgs-review pr [12345] --print-result```

# SYNOPSIS

**nixpkgs-review** [_pr_] [_rev_] [_-p post-result_] [_options_] _target_

# PARAMETERS

**pr** _NUMBER_
> 按编号审查拉取请求。

**rev** _COMMIT_
> 审查特定修订版本。

**wip**
> 审查正在进行的工作。

**--post-result**, **-p**
> 将结果发布到 GitHub。

**--allow-unfree**
> 构建非自由（unfree）软件包。

**--build-args** _ARGS_
> 传给 nix-build 的参数。

**--print-result**
> 打印构建结果。

**--no-shell**
> 构建完成后不启动 Shell。

**-c** _PATH_, **--checkout** _PATH_
> nixpkgs 检出的路径。

**--system** _SYSTEM_
> 目标系统。

**--token** _TOKEN_
> GitHub 令牌。

# DESCRIPTION

**nixpkgs-review** 通过构建受影响的软件包来测试 Nix 软件包的变更。它是审查 nixpkgs 拉取请求的必备工具。

对于拉取请求，该工具会检出 PR、识别发生变化的软件包并进行构建。构建失败即表明存在需要在合并前修复的问题。

审查过程会将 PR 与目标分支进行比较。只有受变更影响的软件包才会被构建，从而在大规模贡献时节省时间。

post-result 模式会在 GitHub PR 上评论构建结果，为贡献者和审查者提供自动化反馈。

构建完成后，会提供一个交互式 Shell 以便手动测试已构建的软件包。环境变量会指向构建成功的软件包。

该工具可通过配置处理非自由软件包、交叉编译目标和并行构建。

# CAVEATS

构建可能耗费大量时间和资源。需要启用 flakes 的 nix 或 nix-build。GitHub 的速率限制可能影响 PR 的获取。某些软件包可能无法在所有系统上构建。

# HISTORY

**nixpkgs-review** 由 **Jörg Thalheim**（Mic92）开发，旨在改进 nixpkgs 的审查流程。它将过去手动检出 PR 并构建软件包的流程自动化，显著提升了审查效率。

# INSTALL

```nix: nix profile install nixpkgs#nixpkgs-review```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix-build](/man/nix-build)(1), [nix-shell](/man/nix-shell)(1), [nixos-rebuild](/man/nixos-rebuild)(1)
