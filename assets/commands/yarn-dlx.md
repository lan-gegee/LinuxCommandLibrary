# TAGLINE

无需安装即可运行软件包

# TLDR

**不安装就运行软件包**

```yarn dlx [create-react-app] [my-app]```

**运行指定的软件包版本**

```yarn dlx [gatsby]@[4.0.0] new [my-site]```

**运行来自其他软件包的命令**

```yarn dlx -p [typescript] tsc --version```

**以静默输出运行**

```yarn dlx -q [cowsay] "Hello"```

**运行带多个软件包依赖的命令**

```yarn dlx -p [typescript] -p [ts-node] ts-node --transpile-only -e "console.log('hello')"```

**搭建 Next.js 应用骨架**

```yarn dlx create-next-app [my-app]```

# SYNOPSIS

**yarn dlx** [_-p package_] [_-q_] _command_ [_args_]

# PARAMETERS

**-p** _package_, **--package** _package_
> 指定执行命令前要安装的软件包。可多次指定以安装多个软件包。

**-q**, **--quiet**
> 抑制详细的安装日志，只报告关键的错误信息。

# DESCRIPTION

**yarn dlx** 在临时环境中运行软件包而不永久安装它。它相当于 Yarn 版的 **npx**，适合项目脚手架工具这类一次性命令。

该命令会将指定的软件包下载到临时位置，在当前工作目录中执行其可执行脚本，随后进行清理。它常与 create-react-app、create-next-app 和 gatsby 等用于创建新项目结构的生成器搭配使用。

默认情况下，yarn dlx 会根据命令名确定要安装哪个软件包。当命令名与软件包名不一致时，使用 **-p** 指定不同的软件包。

# CAVEATS

yarn dlx 仅在 Yarn 2+（Berry）中可用；Yarn 1.x 不包含此命令。不建议对需要反复使用的软件包使用 dlx，因为 Yarn 不跟踪通过 dlx 安装的软件包，这会导致构建结果不确定。对于需要重复使用的场景，请用 **yarn add** 正常安装。

# HISTORY

yarn dlx 于 **2020 年**发布的 **Yarn 2**（Berry）中引入，是现代化 Yarn 架构的一部分。它提供与 npx 类似的功能，但集成了 Yarn 的软件包解析与缓存系统。

# INSTALL

```pacman: sudo pacman -S yarn```

```apk: sudo apk add yarn```

```zypper: sudo zypper install yarn```

```brew: brew install yarn```

```nix: nix profile install nixpkgs#yarn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yarn](/man/yarn)(1), [npx](/man/npx)(1), [npm](/man/npm)(1)
