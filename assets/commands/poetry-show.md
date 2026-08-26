# TAGLINE

显示已安装软件包的信息

# TLDR

**列出所有已安装的软件包**

```poetry show```

**显示特定软件包的详细信息**

```poetry show [package]```

**显示完整的依赖树**

```poetry show --tree```

**仅显示顶层依赖**

```poetry show --top-level```

**显示已过时的软件包及最新版本**

```poetry show --outdated --latest```

**显示某个软件包被依赖的原因**

```poetry show --why [package]```

**以 JSON 格式输出软件包列表**

```poetry show --format json```

# SYNOPSIS

**poetry show** [_options_] [_package_]

# PARAMETERS

_PACKAGE_
> 要显示详情的软件包。

**--tree**
> 显示依赖树。

**--top-level**
> 仅显示顶层依赖。

**--outdated**
> 显示已过时的软件包。

**--latest**
> 显示最新的可用版本。

**--why**
> 显示软件包是直接依赖还是被其他软件包所依赖。

**-a**, **--all**
> 显示所有软件包，包括开发依赖。

**-f**, **--format** _FORMAT_
> 输出格式：text（默认）或 json。不能与 --tree 同时使用。

# DESCRIPTION

**poetry show** 显示项目中已安装软件包的信息。不带参数时，它会列出所有已安装的软件包及其版本和描述。给定软件包名时，会显示详细信息，包括依赖关系和可用版本。

**--tree** 标志以依赖树的形式展示软件包之间的关系。**--outdated** 标志标出有新版本可用的软件包，而 **--top-level** 仅显示项目的直接依赖。

# CAVEATS

需要有效的 lock 文件。显示的是已安装状态。

# HISTORY

poetry show 为 Poetry 项目提供**依赖检查**功能。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-lock](/man/poetry-lock)(1)
