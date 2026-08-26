# TAGLINE

管理前端 Web 依赖。

# TLDR

**安装**软件包

```bower install [jquery]```

从 bower.json **安装**

```bower install```

**搜索**软件包

```bower search [bootstrap]```

**更新**软件包

```bower update```

**列出**已安装的软件包

```bower list```

# SYNOPSIS

**bower** _command_ [_options_]

# DESCRIPTION

**bower** 是一款面向 Web 开发的包管理器，管理 JavaScript 库、CSS 框架和 Web 组件等前端依赖。它从 Git 仓库下载并安装软件包。

该工具曾广泛用于前端依赖管理，但现已被弃用，由 npm 和 yarn 取代。

# PARAMETERS

**install** _package_
> 安装软件包。

**update** _package_
> 更新软件包。

**uninstall** _package_
> 移除软件包。

**search** _query_
> 搜索软件包。

**list**
> 列出已安装的软件包。

**info** _package_
> 显示软件包信息。

**init**
> 创建 bower.json。

**--save**
> 加入 dependencies。

**--save-dev**
> 加入 devDependencies。

# CONFIGURATION

bower.json:
```json
{
  "name": "my-project",
  "dependencies": {
    "jquery": "^3.6.0",
    "bootstrap": "^5.1.0"
  }
}
```

# WORKFLOW

```bash
# Initialize project
bower init

# Install package
bower install jquery --save

# Install all dependencies
bower install

# Update all
bower update
```

# CAVEATS

**已弃用**——不再积极维护。新项目请改用 npm 或 yarn。扁平的依赖树可能导致版本冲突。需要 .bowerrc 进行配置。大多数软件包现已迁移至 npm。

# HISTORY

**Bower** 由 Twitter 于 **2012 年**创建，用于管理前端依赖，但随着 npm 具备了类似功能，它在 **2017 年**被正式弃用。

# INSTALL

```pacman: sudo pacman -S bower```

```apk: sudo apk add bower```

```brew: brew install bower```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [yarn](/man/yarn)(1), [pnpm](/man/pnpm)(1)

# RESOURCES

```[Source code](https://github.com/bower/bower)```

```[Homepage](https://bower.io)```

<!-- verified: 2026-06-19 -->
