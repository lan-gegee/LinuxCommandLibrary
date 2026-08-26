# TAGLINE

VS Code 扩展管理器 CLI

# TLDR

将扩展**打包**为 .vsix 文件

```vsce package```

将扩展**发布**到 Marketplace

```vsce publish```

**发布并自动**提升版本号

```vsce publish [patch|minor|major]```

以发布者身份**登录**

```vsce login [publisher_name]```

**验证个人访问令牌**

```vsce verify-pat [publisher_name]```

**显示**扩展的元数据

```vsce show [publisher.extension]```

**列出**将要包含在包中的文件

```vsce ls```

**取消发布**扩展

```vsce unpublish [publisher.extension]```

# SYNOPSIS

**vsce** _command_ [_options_]

# PARAMETERS

**package**
> 将扩展打包为 .vsix 文件。

**publish** [_VERSION_]
> 将扩展发布到 Marketplace。_VERSION_ 可以是 `major`、`minor`、`patch` 或明确的版本号。

**login** _PUBLISHER_
> 保存发布者的凭据。

**logout** _PUBLISHER_
> 删除发布者已保存的凭据。

**verify-pat** [_PUBLISHER_]
> 验证个人访问令牌是否具有发布权限。

**show** _EXTENSION_
> 显示扩展的元数据（下载量、评分、版本）。

**search** _TEXT_
> 在 Marketplace 中搜索扩展。

**ls**
> 列出将被打包或发布的文件。

**ls-publishers**
> 列出已知的发布者。

**delete-publisher** _NAME_
> 删除一个发布者。

**unpublish** [_EXTENSION_]
> 从 Marketplace 中移除扩展。

**-p**, **--pat** _TOKEN_
> 用于身份验证的个人访问令牌。

**-t**, **--target** _TARGET_
> 目标平台（例如 `linux-x64`、`win32-x64`）。

**-o**, **--out** _PATH_
> 打包出的 .vsix 的输出文件或目录。

**--pre-release**
> 将打包或发布的版本标记为预发布版。

**--no-yarn** / **--yarn**
> 强制使用 npm 或 Yarn 安装依赖。

**--skip-duplicate**
> 当相同版本已存在时跳过发布。

# DESCRIPTION

**vsce**（Visual Studio Code Extension Manager）是微软官方的命令行工具，用于在 Visual Studio Marketplace 上打包、发布和管理 VS Code 扩展。它覆盖了从本地打包到公开发布的扩展开发完整生命周期。

`package` 命令将扩展项目打包成 `.vsix` 文件，可以在本地安装或直接分享。`publish` 命令将打包好的扩展上传到 Marketplace，并可选择使用语义化版本递增（major、minor、patch）自动提升版本号。

Marketplace 操作需要发布者身份。身份验证使用 Azure DevOps 个人访问令牌。其他命令用于管理发布者凭据、检查包内容以及查询 Marketplace 元数据。

# CAVEATS

需要 Marketplace 账户以及具有 Marketplace (Manage) 权限范围的 Azure DevOps PAT。扩展必须遵守 Marketplace 发布指南。通常通过 `npm install -g @vscode/vsce` 安装。

# HISTORY

**vsce**（Visual Studio Code Extension Manager）由 **Microsoft** 开发，以 `@vscode/vsce` 为名在 npm 上分发。自 Marketplace 上线以来，它一直是打包和发布 VS Code 扩展的主要工具。

# INSTALL

```brew: brew install vsce```

```nix: nix profile install nixpkgs#vsce```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[code](/man/code)(1), [npm](/man/npm)(1)
