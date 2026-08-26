# TAGLINE

在 registry 中检查已安装软件包是否有更新版本

# TLDR

**检查过时的软件包**

```npm outdated```

**检查全局软件包**

```npm outdated -g```

**以 JSON 格式输出**

```npm outdated --json```

**检查指定软件包**

```npm outdated [package]```

**长格式输出**

```npm outdated --long```

**包含嵌套（传递）依赖**

```npm outdated --all```

**可解析的制表符分隔输出**

```npm outdated --parseable```

# SYNOPSIS

**npm outdated** [_options_] [_packages_...]

# PARAMETERS

**-g**, **--global**
> 检查全局安装的软件包而非本地项目。

**--json**
> 以 JSON 格式输出（便于机器解析）。

**-l**, **--long**
> 扩展输出，包括软件包类型（dependencies、devDependencies、peerDependencies、optionalDependencies）和主页。

**-p**, **--parseable**
> 输出以制表符分隔，适合解析。

**--all**
> 显示所有过时的软件包，包括元依赖（传递/嵌套），而不仅是直接依赖。

**--omit** _type_
> 排除某组依赖（dev、optional、peer）。可多次设置。

**-w**, **--workspace** _name_
> 在指定的工作区中运行该命令。

**-ws**, **--workspaces**
> 在所有已配置的工作区中运行。

**--include-workspace-root**
> 使用 --workspaces 时包含工作区根目录。

# DESCRIPTION

**npm outdated** 在 registry 中检查已安装软件包是否有更新版本。它会报告当前安装的版本、满足 package.json 中 semver 范围的最大版本（**wanted**），以及 registry 中标记为 latest 的最新版本（**latest**）。

终端输出中的颜色含义：**红色**表示 semver 范围内有可用更新（可以放心运行 `npm update`）；**黄色**表示存在超出 semver 范围的新版本（需要手动升级版本号）。

# OUTPUT COLUMNS

```
Package   Current  Wanted  Latest  Location            Depended by
lodash    4.17.0   4.17.21 4.17.21 node_modules/lodash my-app

Current     - Currently installed version
Wanted      - Max version satisfying semver range
Latest      - Version tagged "latest" in the registry
Location    - Location in the dependency tree
Depended by - Package depending on this one
Package type - (with --long) dependencies/devDependencies/peer/optional
```

# EXAMPLE

```bash
$ npm outdated
Package  Current  Wanted  Latest
express  4.17.1   4.18.2  4.18.2
lodash   4.17.0   4.17.21 4.17.21
```

# CAVEATS

默认只显示直接依赖；传入 **--all** 可包含传递依赖。该命令只做报告——从不安装或修改任何东西。semver 范围内的更新请用 **npm update** 应用；大版本升级则需手动修改 package.json 中的版本号。发现过时软件包时以非零状态退出，这可能导致 CI 流水线中断。

# HISTORY

npm outdated 的加入是为了帮助开发者识别需要更新的软件包，与 npm update 相辅相成。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-update](/man/npm-update)(1), [npm-ls](/man/npm-ls)(1)
