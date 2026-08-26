# TAGLINE

运行 package 中定义的 "test" 脚本

# TLDR

**运行测试**

```npm test```

**带参数运行测试**

```npm test -- --coverage```

**静默运行测试**

```npm test --silent```

**简写形式**

```npm t```

# SYNOPSIS

**npm test** [-- _args_]

# PARAMETERS

**--**
> 将参数传递给测试脚本。

**--silent**
> 减少输出。

**--ignore-scripts**
> 不运行脚本。

# DESCRIPTION

**npm test** 运行 package.json 中定义的 "test" 脚本。它是 "npm run test" 的别名，也是运行项目测试套件的惯用命令。

退出码 0 表示成功；非零表示测试失败。

# PACKAGE.JSON

```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  }
}
```

# COMMON TEST SCRIPTS

```bash
# Jest
"test": "jest"

# Mocha
"test": "mocha"

# Vitest
"test": "vitest"

# TAP
"test": "tap test/*.js"
```

# CAVEATS

需要先在 package.json 中定义 test 脚本。若没有脚本则默认以错误退出。使用 npm run test:name 运行自定义测试脚本。

# HISTORY

npm test 成为 Node.js 项目的标准测试命令，被普遍集成到 CI/CD 流水线中。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-run-script](/man/npm-run-script)(1), [npm-start](/man/npm-start)(1)
