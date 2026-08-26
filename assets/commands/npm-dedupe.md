# TAGLINE

通过把依赖上移来减少包树中的重复

# TLDR

**去除重复依赖**

```npm dedupe```

**试运行（显示将要发生的更改）**

```npm dedupe --dry-run```

**包含开发依赖**

```npm dedupe --include=dev```

**以旧版捆绑方式去重**

```npm dedupe --legacy-bundling```

# SYNOPSIS

**npm dedupe** [_options_]

# PARAMETERS

**--dry-run**
> 只显示更改而不实际应用。

**--include** _type_
> 包含某类依赖。

**--omit** _type_
> 省略某类依赖。

**--legacy-bundling**
> 使用旧版算法。

**--strict-peer-deps**
> 遇到 peer 依赖问题时失败。

# DESCRIPTION

**npm dedupe** 通过把依赖移动到包树中更高、可被共享的位置，减少包树中的重复。这可以显著缩小 node_modules 的体积。

该命令只做结构重组，不会更改 package-lock.json 中的版本。

# EXAMPLE

```bash
# Before dedupe
node_modules/
├── a/
│   └── node_modules/lodash@4.0.0
└── b/
    └── node_modules/lodash@4.0.0

# After dedupe
node_modules/
├── a/
├── b/
└── lodash@4.0.0
```

# CAVEATS

若版本范围不同则可能无法缩减体积。在 npm install 之后运行。仅重组目录树。

# HISTORY

npm dedupe 的引入是为了应对 npm 嵌套式 node_modules 结构中常见的依赖重复问题。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-prune](/man/npm-prune)(1), [npm-install](/man/npm-install)(1)
