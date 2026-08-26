# TAGLINE

将软件包上传到 npm registry

# TLDR

**发布当前目录中的软件包**

```npm publish```

**以发行标签（如 beta、next）发布**

```npm publish --tag [beta]```

**公开发布带作用域的软件包**

```npm publish --access public```

**模拟发布而不实际上传**

```npm publish --dry-run```

**发布指定的 tarball 或文件夹**

```npm publish [./package.tgz]```

**附带 2FA 一次性密码发布**

```npm publish --otp=[123456]```

**附带供应链来源证明发布（仅限 CI）**

```npm publish --provenance --access public```

# SYNOPSIS

**npm** **publish** [_package-spec_] [_options_]

# PARAMETERS

_package-spec_
> 要发布的文件夹或 tarball 的路径。默认为当前目录。

**--tag** _TAG_
> 将发布的版本注册到给定的 dist-tag 下，而不是 `latest`。

**--access** _restricted_|_public_
> 为带作用域的软件包设置初始访问级别。新的 scoped 软件包或使用 `--provenance` 时必须设为 `public`。

**--dry-run**
> 报告将要发布的内容而不上传任何东西。

**--otp** _CODE_
> 提供来自 2FA 认证器的一次性密码。

**--provenance**
> 生成并附加供应链来源证明（npm >= 9.5.0，仅限受支持的 CI）。

**--provenance-file** _FILE_
> 附加预先生成的来源证明文件，而不是新建一份。

**-w**, **--workspace** _NAME_
> 发布指定工作区的软件包。

**--workspaces**
> 发布所有已配置的工作区。

**--include-workspace-root**
> 使用 `--workspaces` 时同时包含工作区根目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm publish** 打包当前项目（或给定的文件夹/tarball）并上传到所配置的 registry，使新版本可供他人安装。

tarball 中包含的文件遵循 `.npmignore`、`package.json` 的 `files` 字段以及 npm 标准默认规则。`name` 和 `version` 字段合在一起必须在 registry 上唯一；不允许重复发布已发布的版本。

对于带作用域的软件包（`@scope/name`），npm 默认将其视为私有；首次发布时传入 `--access public` 即可将其公开。

# CAVEATS

发布需要经过身份验证的 npm 账户（`npm login` 或通过 `NPM_TOKEN` 提供令牌）。版本不能被覆盖；重新发布前请用 `npm version` 升版本号。72 小时后取消发布受到严格限制——请谨慎规划发布。`--provenance` 只能在受支持的 CI 环境中使用，且需在 `package.json` 中正确设置 `repository` 字段。

# HISTORY

自 npm 早期版本起，**npm publish** 就一直是共享 JavaScript 软件包的主要机制。基于 Sigstore 的供应链来源证明于 **npm 9.5.0（2023 年）** 加入，而可信发布（基于 OIDC、无需令牌）则在后续版本中为 npm 推出。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-version](/man/npm-version)(1), [npm-unpublish](/man/npm-unpublish)(1)
