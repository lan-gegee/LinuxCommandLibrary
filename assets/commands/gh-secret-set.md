# TAGLINE

创建或更新 GitHub Actions 加密 secret

# TLDR

**以交互方式设置 secret**

```gh secret set [SECRET_NAME]```

**从值设置 secret**

```echo "[value]" | gh secret set [SECRET_NAME]```

**从文件设置**

```gh secret set [SECRET_NAME] < [secret.txt]```

**设置环境级 secret**

```gh secret set [SECRET_NAME] --env [production]```

**使用 body 标志设置**

```gh secret set [SECRET_NAME] --body "[value]"```

# SYNOPSIS

**gh secret set** _name_ [_options_]

# PARAMETERS

_NAME_
> Secret 名称。

**--body** _VALUE_
> Secret 值（处理敏感数据时请避免使用）。

**--env** _ENVIRONMENT_
> 目标部署环境。

**--org** _ORGNAME_
> 设置组织级 secret。

**--repos** _REPOS_
> 限定到特定仓库。

**--visibility** _SCOPE_
> Secret 的可见性范围。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh secret set** 为 GitHub Actions 创建或更新加密 secret。以交互方式运行时，它会安全地提示输入 secret 值，而不会回显到终端。

该命令在传输前会使用仓库或组织的公钥对 secret 进行加密。Secret 可以限定到部署工作流所用的特定环境，也可以限定到组织中选定的仓库。通过管道或重定向传入内容，可避免将 secret 暴露在 shell 历史记录中。

# CAVEATS

敏感值请避免使用 --body（会留在历史记录中可见）。Secret 在传输过程中是加密的。组织级 secret 需要管理员权限。

# HISTORY

gh secret set 是 **GitHub CLI** 的 secret 管理命令之一，为 CI/CD 工作流提供安全的 secret 配置。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh-secret](/man/gh-secret)(1), [gh-run](/man/gh-run)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_secret_set)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->
