# TAGLINE

下载并验证工件证明（gh attestation 的别名）

# TLDR

针对仓库的证明**验证工件**

```gh at verify [example.bin] --repo [owner/repo]```

针对组织的证明**验证工件**

```gh at verify [example.bin] --owner [org-name]```

**验证 OCI 镜像**

```gh at verify [oci://image-uri] --owner [org-name]```

**验证并以完整 JSON 输出**结果

```gh at verify [example.bin] --owner [org-name] --format [json]```

**下载证明**以供离线验证

```gh at download [example.bin] --repo [owner/repo]```

**输出受信任根**用于离线验证

```gh at trusted-root --repo [owner/repo]```

# SYNOPSIS

**gh at** _command_ [_flags_]

# PARAMETERS

**verify** [_file-path_ | _oci://image-uri_]
> 使用关联的证明验证工件的完整性与来源。

**download** [_file-path_ | _oci://image-uri_]
> 下载工件的证明以供离线使用。

**trusted-root**
> 输出 trusted_root.jsonl 内容，用于离线验证。

**-o**, **--owner** _string_
> 用于限定证明查找范围的 GitHub 组织。

**-R**, **--repo** _string_
> 仓库名称，格式为 _owner/repo_。

# VERIFY FLAGS

**-d**, **--digest-alg** _string_
> 计算工件摘要所用的摘要算法：sha256 或 sha512（默认 sha256）。

**--cert-identity** _string_
> 强制要求证书的 SubjectAlternativeName 精确匹配。

**-i**, **--cert-identity-regex** _string_
> 强制要求证书的 SubjectAlternativeName 匹配正则表达式。

**--cert-oidc-issuer** _string_
> 强制指定 OIDC 令牌签发者（默认 https://token.actions.githubusercontent.com）。

**--signer-repo** _string_
> 强制匹配签名工作流所在的仓库。

**--signer-workflow** _string_
> 强制匹配签名工作流的路径。

**-b**, **--bundle** _string_
> 使用磁盘上保存的 bundle 进行验证，而不是从 GitHub 获取。

**--bundle-from-oci**
> 从 OCI 注册表而非 GitHub 获取证明 bundle。

**--format** _string_
> 输出格式；目前仅支持 **json**。

**-L**, **--limit** _int_
> 获取证明的最大数量（默认 30）。

# DESCRIPTION

**gh at** 是 **gh attestation** 的内建别名，属于官方 **GitHub CLI**。它下载并验证构建来源证明——通过 Sigstore 加密签名的记录，把工件与构建它的 GitHub 仓库、提交和工作流关联起来。它用于确认下载的二进制文件、软件包或容器镜像确实来自声称的来源和构建流水线。

# CAVEATS

需要提供 **--owner** 或 **--repo** 来限定查找范围。验证依赖对 GitHub 和 Sigstore 公共实例的网络访问；除非使用 **--custom-trusted-root** 或 **--bundle** 进行完全离线验证。

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

# RESOURCES

```[Manual](https://cli.github.com/manual/gh_attestation)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-17 -->
