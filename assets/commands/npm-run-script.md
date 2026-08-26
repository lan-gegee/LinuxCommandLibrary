# TAGLINE

运行软件包中定义的脚本

# TLDR

**运行 package.json 中定义的 npm 脚本**

```npm run [script-name]```

**向脚本传参**（放在 `--` 之后）

```npm run [script] -- [--flag] [value]```

**列出可用的脚本**

```npm run```

**在每个工作区中运行脚本**

```npm run [script] --workspaces```

**在某个工作区中运行脚本**

```npm run [script] -w [package-name]```

**静默跳过缺失的脚本**

```npm run [script] --if-present```

**安静地运行**

```npm run [script] --silent```

# SYNOPSIS

**npm run-script** _script_ [_-- args_] [_options_]

别名：**npm run**、**npm rum**、**npm urn**。

# PARAMETERS

**--silent**
> 抑制非错误输出。

**--if-present**
> 当指定的脚本未定义时正常退出（不报错）。

**--ignore-scripts**
> 不运行前置和后置钩子脚本（如 **prestart**、**poststart**）。

**--foreground-scripts**
> 直接输出脚本的 stdout/stderr，而不是捕获它们。

**--script-shell** _SHELL_
> 使用指定的 shell 执行脚本（Unix 上默认 **/bin/sh**，Windows 上默认 **cmd.exe**）。

**-w**, **--workspace** _NAME_
> 在给定的工作区中运行脚本。可重复使用。

**--workspaces**
> 在每个已配置的工作区中运行脚本。

**--include-workspace-root**
> 与 **--workspaces** 结合使用时，也在仓库根目录运行脚本。

**--**
> **--** 之后的所有内容都作为参数传递给脚本本身。

# DESCRIPTION

**npm run-script** 运行 **package.json** 的 **scripts** 字段中定义的脚本。**npm run** 是常用的别名。不带参数时它会列出可用的脚本及其命令。

安装到 **node_modules/.bin** 中的任何可执行文件都会在脚本运行期间加入 **$PATH**，因此可以直接用名称调用依赖提供的可执行文件。**--** 之后的参数会追加到脚本命令后面，但不会转发给 **pre**/**post** 生命周期脚本。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-start](/man/npm-start)(1)
