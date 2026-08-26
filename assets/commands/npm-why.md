# TAGLINE

显示软件包为何被安装

# TLDR

**解释软件包为何被安装**

```npm why [package-name]```

**解释特定版本**

```npm why [package-name]@[version]```

**JSON 输出**

```npm why [package-name] --json```

**限制依赖树深度**

```npm why [package-name] --long```

**针对特定工作区**

```npm why [package-name] --workspace=[workspace-name]```

# SYNOPSIS

**npm** **why** _package-spec_...

# PARAMETERS

_PACKAGE-SPEC_
> 软件包名称，可选带版本范围（如 lodash@^4）。

**--json**
> 以 JSON 格式输出结果。

**--long**
> 显示扩展信息。

**--workspace** _NAME_
> 仅限于某个具名工作区或路径。

**--include-workspace-root**
> 除工作区外还包括根项目。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm why** 显示软件包为何被安装。它是 npm explain 的别名。

该命令追踪依赖路径，显示通向该软件包的所有路径。

# CAVEATS

是 npm explain 的别名。显示所有依赖路径。要求软件包已安装。

# HISTORY

npm why 提供**依赖追踪**功能，用于理解软件包之间的关系。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-explain](/man/npm-explain)(1), [npm-ls](/man/npm-ls)(1)
