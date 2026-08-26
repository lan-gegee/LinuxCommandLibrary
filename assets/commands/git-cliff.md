# TAGLINE

从提交记录生成高度可定制的更新日志

# TLDR

**生成更新日志**

```git cliff```

**从指定标签开始生成**

```git cliff --tag [v1.0.0]```

**输出到文件**

```git cliff -o CHANGELOG.md```

**预览未发布内容**

```git cliff --unreleased```

**自定义配置**

```git cliff --config [cliff.toml]```

# SYNOPSIS

**git cliff** [_options_] [_range_]

# PARAMETERS

**-o** _FILE_, **--output** _FILE_
> 输出文件。

**--tag** _TAG_
> 处理到指定标签为止的提交。

**--unreleased**
> 只处理未发布的提交。

**-l**, **--latest**
> 从最新标签开始处理提交。

**--bump**
> 基于 conventional commits 规范为未发布的更改递增版本号。

**-c** _FILE_, **--config** _FILE_
> 配置文件。

**-w** _DIR_, **--workdir** _DIR_
> 以给定目录作为启动目录运行 git-cliff。

**--prepend** _FILE_
> 追加到现有文件的开头。

**--context**
> 打印模板上下文。

**--init**
> 生成默认配置文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git cliff** 遵循 conventional commit 规范从 git 历史生成更新日志。它解析提交信息以归类变更，并产生格式化的输出。

该工具可通过 TOML 文件高度定制，支持自定义 Tera 模板、提交分组、基于 scope 的过滤以及条件小节。它可以集成到 CI/CD 流水线中自动生成发布文档。

git cliff 支持 conventional commits、Angular 风格的提交以及自定义解析规则，能产出 Markdown、AsciiDoc 或自定义模板格式的专业更新日志。

# CONFIGURATION

**cliff.toml**
> 配置文件，定义提交解析规则、分组逻辑、过滤模式，以及采用 Tera 模板语法的输出模板。

**~/.config/git-cliff/cliff.toml**
> 用户级的 git-cliff 默认配置。

# CAVEATS

配合 conventional commits 使用效果最佳。自定义格式需要配置。模板定制需要了解 Tera 语法。

# HISTORY

git cliff 由 **Orhun Parmaksiz** 创建，是一个高度可定制的更新日志生成器，用 Rust 编写以保证性能。

# INSTALL

```pacman: sudo pacman -S git-cliff```

```apk: sudo apk add git-cliff```

```zypper: sudo zypper install git-cliff```

```brew: brew install git-cliff```

```nix: nix profile install nixpkgs#git-cliff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-changelog](/man/git-changelog)(1), [git-log](/man/git-log)(1)

# RESOURCES

```[Source code](https://github.com/orhun/git-cliff)```

```[Homepage](https://git-cliff.org/)```

```[Documentation](https://git-cliff.org/docs/)```

<!-- verified: 2026-07-17 -->
