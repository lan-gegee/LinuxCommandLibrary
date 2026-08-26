# TAGLINE

Create React App 的构建与开发脚本

# TLDR

**启动开发服务器**

```react-scripts start```

**为生产环境构建**

```react-scripts build```

**运行测试**

```react-scripts test```

**弹出配置**

```react-scripts eject```

# SYNOPSIS

**react-scripts** _command_ [_options_]

# COMMANDS

**start**
> 启动开发服务器。

**build**
> 创建生产构建。

**test**
> 运行测试套件。

**eject**
> 暴露配置文件。

# DESCRIPTION

**react-scripts** 是 Create React App 的构建工具。它以零配置的方式封装了 webpack、Babel、ESLint 等工具，统一处理开发服务器、构建和测试。

# EXAMPLES

```bash
# Start dev server (port 3000)
npm start
# or
react-scripts start

# Production build
npm run build
# Creates build/ directory

# Run tests
npm test

# Run tests with coverage
npm test -- --coverage

# Eject (one-way operation)
npm run eject
```

# ENVIRONMENT VARIABLES

```bash
PORT=3001 npm start              # Custom port
BROWSER=none npm start           # Don't open browser
GENERATE_SOURCEMAP=false npm build  # No sourcemaps
CI=true npm test                 # CI mode
```

# PROXY SETUP

```json
// package.json
{
  "proxy": "http://localhost:5000"
}
```

# CAVEATS

eject 不可逆。不 eject 时可定制性有限。可考虑用 CRACO 覆盖配置。

# HISTORY

react-scripts 由 **Facebook** 作为 Create React App（2016 年）的一部分创建，旨在简化 React 开发环境的搭建。

# SEE ALSO

[npm](/man/npm)(1), [vite](/man/vite)(1)
