# TAGLINE

获取项目依赖的资助信息

# TLDR

**列出所有寻求资助的依赖**

```npm fund```

**显示特定软件包的资助信息**

```npm fund [package-name]```

**以 JSON 格式输出资助信息**

```npm fund --json```

**存在多个资助来源时打开指定的那个**

```npm fund [package-name] --which [1]```

**列出指定工作区的资助信息**

```npm fund --workspace [workspace-name]```

# SYNOPSIS

**npm** **fund** [_package-spec_]

# PARAMETERS

_package-spec_
> 要获取其资助信息的软件包。

**--json**
> 输出 JSON 数据而非常规输出。

**--which** _NUM_
> 存在多个资助来源时，指定要打开的第几个（从 1 开始计数）来源 URL。

**--browser** _BROWSER_
> 用于打开资助 URL 的浏览器。设为 false 时改为把 URL 打印到终端。

**--unicode**
> 在树形输出中使用 Unicode 字符。为 false 时改用 ASCII 字符。

**--workspace** _WORKSPACE_
> 将结果过滤到指定的工作区。

# DESCRIPTION

**npm fund** 获取如何资助给定项目依赖的信息。若未提供软件包名，它会以树形结构列出所有寻求资助的依赖，并显示资助类型和要访问的 URL。

若提供了软件包名，它会尝试用所配置的浏览器打开该软件包的资助 URL。如果该软件包有多个资助来源，会提示用户使用 **--which** 选项加以区分。

# CAVEATS

需要 package.json 中包含资助元数据。默认会用浏览器打开 URL。资助是对开源维护者的自愿性支持。

# HISTORY

**npm fund** 于 **npm 8** 推出，旨在帮助开源维护者获得用户的经济支持。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-install](/man/npm-install)(1), [npm-docs](/man/npm-docs)(1), [npm-ls](/man/npm-ls)(1), [npm-config](/man/npm-config)(1)
