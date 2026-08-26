# TAGLINE

从模板创建 .gitignore 文件

# TLDR

为当前目录**创建** .gitignore

```gitnr```

为特定语言**创建** .gitignore

```gitnr rust```

使用多个模板**创建** .gitignore

```gitnr rust python node```

列出可用模板

```gitnr --list```

# SYNOPSIS

**gitnr** [_options_] [_templates_]

# PARAMETERS

**-l, --list**
> 列出所有可用模板

**-s, --search** _QUERY_
> 搜索模板

**-a, --append**
> 追加到已有的 .gitignore

**-o, --output** _FILE_
> 输出到指定文件

**-f, --force**
> 覆盖已有文件

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**gitnr** 使用来自 GitHub gitignore 仓库的模板创建 .gitignore 文件。它支持数百种针对不同语言、框架和工具的模板。

该工具从 GitHub 官方 gitignore 仓库获取模板，并在需要时合并多个模板。

# AVAILABLE TEMPLATES

常见模板包括：
- 语言：rust、python、node、go、java
- IDE：vscode、intellij、vim
- 工具：docker、terraform、ansible
- 操作系统：macos、windows、linux

# CAVEATS

获取模板需要联网。可能受 GitHub API 速率限制。部分模板可能需要根据项目需求进行定制。

# HISTORY

**gitnr** 的创建目的是免去手动浏览 GitHub 仓库，便捷地生成 .gitignore 文件。

# INSTALL

```brew: brew install gitnr```

```nix: nix profile install nixpkgs#gitnr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gitignore](https://git-scm.com/docs/gitignore), [gitignore.io](https://www.toptal.com/developers/gitignore)
