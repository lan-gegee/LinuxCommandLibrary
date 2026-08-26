# TAGLINE

显示 Pulumi 环境诊断信息

# TLDR

**显示 Pulumi 版本和环境信息**

```pulumi about```

**以 JSON 格式输出**

```pulumi about --json```

**包含传递性插件依赖**

```pulumi about --transitive```

**显示指定堆栈的信息**

```pulumi about --stack [org/project/dev]```

# SYNOPSIS

**pulumi** **about** [_options_]

# PARAMETERS

**-j**, **--json**
> 以 JSON 格式输出，便于脚本处理。

**-t**, **--transitive**
> 在输出中包含传递性的语言插件依赖。

**-s**, **--stack** _name_
> 针对指定的堆栈运行（默认为当前选定的堆栈）。

# DESCRIPTION

**pulumi about** 显示本地 Pulumi 环境的诊断信息。输出内容包括 Pulumi CLI 版本、主机操作系统和架构、当前使用的后端（Pulumi Cloud、S3、Azure Blob 等）、当前用户、语言运行时以及已安装的资源插件。

在 Pulumi 项目目录中运行时，还会报告项目名称、运行时和当前选定的堆栈。这些信息主要用于支持工单和 CI 调试——Pulumi 工作人员在排查 bug 报告时经常要求提供此输出。

# CAVEATS

输出中包含路径和堆栈标识符；公开分享前请先隐去敏感信息。某些字段仅在 Pulumi 项目目录内才会填充。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-version](/man/pulumi-version)(1), [pulumi-stack](/man/pulumi-stack)(1)
