# TAGLINE

验证工件证明与构建来源

# TLDR

**验证工件证明**

```gh attestation verify [artifact] -R [owner/repo]```

**用特定的谓词类型验证**

```gh attestation verify [artifact] -R [owner/repo] --predicate-type [https://example.com/predicate/v1]```

**用指定的 bundle 文件验证**（离线）

```gh attestation verify [artifact] --bundle [attestation.json]```

**验证并拒绝自托管运行器**

```gh attestation verify [artifact] -R [owner/repo] --deny-self-hosted-runners```

**下载证明**

```gh attestation download [artifact] -R [owner/repo]```

**以 JSON 格式下载证明**

```gh attestation download [artifact] -R [owner/repo] --format json```

# SYNOPSIS

**gh** **attestation** _command_ [_options_]

# SUBCOMMANDS

**verify**
> 以加密方式验证工件的证明。

**download**
> 下载证明 bundle 以供离线验证。

# PARAMETERS

**-R**, **--repo** _owner/repo_
> 限定证明查找范围的仓库。

**--bundle** _file_
> 本地证明 bundle 文件的路径。

**--owner** _owner_
> 限定证明查找范围的 GitHub 组织或用户。

**--format** _format_
> 输出格式（json）。

**--predicate-type** _type_
> 验证特定的证明谓词类型（默认：https://slsa.dev/provenance/v1）。

**--signer-repo** _owner/repo_
> 签署证明的可复用工作流所在仓库。

**--signer-workflow** _workflow_
> 签署证明的工作流。

**--deny-self-hosted-runners**
> 对在自托管运行器上生成的证明判定为验证失败。

# DESCRIPTION

**gh attestation** 使用 GitHub 的工件证明功能验证工件证明。它以加密方式校验工件是否由受信任的 GitHub Actions 工作流构建，并带有 SLSA 构建来源信息。证明既可以在线对照 GitHub API 验证，也可以用下载的 bundle 文件离线验证。

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

[gh](/man/gh)(1), [gh-release](/man/gh-release)(1)
