# TAGLINE

提升软件包版本号

# TLDR

**提升补丁版本号**

```npm version patch```

**提升次版本号**

```npm version minor```

**提升主版本号**

```npm version major```

**设置指定版本号**

```npm version [1.2.3]```

**预发布版本号**

```npm version prerelease```

**不创建 git 标签**

```npm version patch --no-git-tag-version```

# SYNOPSIS

**npm** **version** [_version_] [_options_]

# PARAMETERS

_VERSION_
> 版本号或递增类型。

**patch**
> 递增补丁版本号（0.0.x）。

**minor**
> 递增次版本号（0.x.0）。

**major**
> 递增主版本号（x.0.0）。

**--no-git-tag-version**
> 不创建 git 标签。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm version** 提升软件包版本号，更新 package.json 并创建 git 标签。

该命令管理版本号，遵循 semver 规范。

# CAVEATS

默认会创建 git 提交/标签。工作目录必须干净。

# HISTORY

npm version 结合 git 集成提供 **semver 版本管理**功能。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-publish](/man/npm-publish)(1), [semver](/man/semver)(1)
