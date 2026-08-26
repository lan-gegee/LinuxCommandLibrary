# TAGLINE

基于提交记录的自动化语义化版本管理

# TLDR

**发布新版本**

```standard-version```

**首次发布**

```standard-version --first-release```

**预发布版本**

```standard-version --prerelease alpha```

**试运行**

```standard-version --dry-run```

**指定版本提升类型**

```standard-version --release-as [major|minor|patch]```

**跳过变更日志**

```standard-version --skip.changelog```

# SYNOPSIS

**standard-version** [_--release-as type_] [_--prerelease tag_] [_options_]

# PARAMETERS

**--first-release**
> 第一个版本。

**--release-as** _TYPE_
> 版本提升类型。

**--prerelease** _TAG_
> 预发布标签。

**--dry-run**
> 仅预览。

**--skip.changelog**
> 跳过变更日志。

**-s**, **--sign**
> 使用 GPG 签署提交和标签。

**-a**, **--commit-all**
> 提交所有已暂存的文件，而不只是 package/changelog。

**-t**, **--tag-prefix** _prefix_
> 自定义标签前缀（默认：v）。

**--no-verify**
> 绕过 pre-commit/commit-msg git 钩子。

# DESCRIPTION

**standard-version** 基于 Conventional Commits 规范，为 Node.js 项目自动执行语义化版本管理和变更日志生成。它分析提交信息（feat、fix、BREAKING CHANGE）来决定是提升 major、minor 还是 patch 版本。

该工具会更新 package.json 中的版本号，根据提交信息生成或更新 CHANGELOG.md，创建一个包含版本提升的 git 提交，并用新版本号打标签。试运行模式可以预览更改而不修改文件。支持预发布标签（alpha、beta、rc）用于阶段性发布。

# CAVEATS

**已弃用**——该项目不再维护。作者推荐 GitHub 用户使用 **release-please**，或使用 fork 版 **commit-and-tag-version** 以获得持续支持。需要 Conventional Commits 提交规范、Node.js 项目和 git 仓库。

# HISTORY

**standard-version** 为基于 Conventional Commits 规范的自动化语义化版本管理而创建。

# INSTALL

```brew: brew install standard```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm-version](/man/npm-version)(1), [semantic-release](/man/semantic-release)(1), [git](/man/git)(1)
