# TAGLINE

依据 package-lock 安装依赖

# TLDR

**从 lockfile 全新安装**

```npm ci```

**仅安装生产依赖**

```npm ci --production```

**使用旧版 peer 依赖处理方式安装**

```npm ci --legacy-peer-deps```

**静默安装**

```npm ci --silent```

# SYNOPSIS

**npm** **ci** [_options_]

# PARAMETERS

**--production**
> 跳过 devDependencies（npm 6；npm 7 及以上请用 --omit=dev）。

**--omit** _TYPE_
> 省略某类依赖（dev、optional、peer）。

**--legacy-peer-deps**
> 忽略 peer 依赖冲突。

**--silent**
> 抑制输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm ci** 完全按照 package-lock.json 文件执行全新的依赖安装。它专为 CI/CD 流水线等对可重现性要求很高的自动化环境设计。

该命令在安装前会删除已存在的 node_modules 目录，确保处于干净状态。与 **npm install** 不同，它从不修改 lockfile——如果 package.json 和 package-lock.json 不同步，它会直接报错，而不是静默更新。

# CAVEATS

需要 package-lock.json。会删除 node_modules。lockfile 不匹配时直接失败。

# HISTORY

npm ci 在 **npm 5.7** 中加入，用于持续集成流水线中的确定性构建。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-install](/man/npm-install)(1), [package-lock.json](/man/package-lock.json)(5)
