# TAGLINE

创建新软件包

# TLDR

**初始化新项目**

```npm init```

**使用默认值初始化**

```npm init -y```

**用 initializer 创建**

```npm init [initializer]```

**创建 React 应用**

```npm init react-app [my-app]```

**创建 Vite 项目**

```npm init vite@latest [my-app]```

**设置默认作者**

```npm config set init-author-name "[name]"```

# SYNOPSIS

**npm init** [_options_] [_initializer_]

# PARAMETERS

**-y**, **--yes**
> 接受所有默认值。

**--scope** _scope_
> 创建带作用域的软件包。

**-w**, **--workspace**
> 创建工作区。

**initializer**
> 要运行的软件包（create-*）。

# DESCRIPTION

**npm init** 创建新的 package.json 文件。不带 initializer 时会交互式询问软件包信息；带上 initializer 时则运行该软件包的设置流程。

像 "react-app" 这样的 initializer 是 "create-react-app" 的简写。
# Interactive
npm init
# Answer prompts...

# With defaults
npm init -y

# Using initializer (runs create-react-app)
npm init react-app my-app

# Scoped package
npm init --scope=@myorg
```

# PACKAGE.JSON TEMPLATE

```json
{
  "name": "my-package",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": { "test": "echo \"Error: no test\" && exit 1" },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

# CAVEATS

-y 使用默认值，可能需要后续修改。initializer 会下载软件包。monorepo 可用工作区模式。

# SEE ALSO

[npm](/man/npm)(1), [npm-install](/man/npm-install)(1), [npm-config](/man/npm-config)(1)

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->
