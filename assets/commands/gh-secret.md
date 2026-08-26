# TAGLINE

管理 GitHub secret

# TLDR

**列出仓库 secret**

```gh secret list```

**设置 secret**

```gh secret set [SECRET_NAME]```

**从值设置 secret**

```gh secret set [SECRET_NAME] --body "[secret_value]"```

**从文件设置 secret**

```gh secret set [SECRET_NAME] < [secret.txt]```

**从 dotenv 文件批量设置 secret**

```gh secret set --env-file [.env]```

**删除 secret**

```gh secret delete [SECRET_NAME]```

**列出组织级 secret**

```gh secret list --org [orgname]```

**为特定应用设置 secret**

```gh secret set [SECRET_NAME] --app [actions|codespaces|dependabot]```

# SYNOPSIS

**gh secret** _command_ [_options_]

# PARAMETERS

**list**
> 列出 secret。

**set** _NAME_
> 创建或更新 secret。

**delete** _NAME_
> 删除 secret。

**--org** _ORGNAME_
> 面向组织级 secret。

**--env** _ENVIRONMENT_
> 面向环境级 secret。

**-a**, **--app** _APP_
> 目标应用：actions、codespaces 或 dependabot。

**-b**, **--body** _STRING_
> 直接提供 secret 值（省略时从标准输入读取）。

**-f**, **--env-file** _FILE_
> 从 dotenv 格式的文件导入 secret 名称和值。

**--visibility** _SCOPE_
> 组织级 secret 的可见性（all、private、selected）。默认：private。

**--repos** _REPOS_
> selected 可见性对应的仓库列表。

**-u**, **--user**
> 为你的用户账户设置或列出 secret（Codespaces）。

**-R**, **--repo** _[HOST/]OWNER/REPO_
> 指定目标仓库。

**--no-store**
> 输出加密并 base64 编码后的值，但不存储到 GitHub。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh secret** 管理 GitHub Actions、Codespaces 和 Dependabot 的加密 secret。Secret 经过加密，只在运行时才暴露给工作流，为 CI/CD 流水线提供安全的凭据存储。

该命令支持仓库级、组织级、环境级和用户级 secret。组织级 secret 可通过 **--visibility** 和 **--repos** 限定到特定仓库。值在传输和存储前都会被加密。**--app** 标志用于选择 secret 所属的应用（actions、codespaces 或 dependabot）。

# CAVEATS

Secret 为只写，其值无法读取。组织级 secret 需要管理员权限。Secret 名称不区分大小写。

# HISTORY

gh secret 被加入 **GitHub CLI** 以支持 GitHub Actions 的 secret 管理，这对安全的 CI/CD 工作流至关重要。

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

[gh](/man/gh)(1), [gh-secret-set](/man/gh-secret-set)(1), [gh-variable](/man/gh-variable)(1), [gh-run](/man/gh-run)(1)
