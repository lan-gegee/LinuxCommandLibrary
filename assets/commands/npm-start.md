# TAGLINE

运行软件包中定义的 "start" 脚本

# TLDR

**运行 start 脚本**

```npm start```

**带参数启动**

```npm start -- [args]```

**以静默模式启动**

```npm start --silent```

# SYNOPSIS

**npm start** [-- _args_]

# PARAMETERS

**--**
> 向脚本传递参数。

**--silent**
> 减少输出。

**--ignore-scripts**
> 不运行脚本。

**-w, --workspace** _name_
> 为指定工作区运行 start 脚本。

**--workspaces**
> 在所有已配置的工作区中运行 start 脚本。

# DESCRIPTION

**npm start** 运行 package.json 中定义的 "start" 脚本。若未定义 start 脚本，则默认执行 "node server.js"。

它是 "npm run start" 的简写，常用于启动应用。

# PACKAGE.JSON

```json
{
  "scripts": {
    "start": "node app.js",
    "start:dev": "nodemon app.js",
    "start:prod": "NODE_ENV=production node app.js"
  }
}
```

# COMMON START SCRIPTS

```bash
# Node.js
"start": "node index.js"

# React (Create React App)
"start": "react-scripts start"

# Next.js
"start": "next start"

# Express
"start": "node server.js"
```

# CAVEATS

未定义脚本时默认为 "node server.js"。传参请用 --。退出码反映脚本的退出码。

# HISTORY

npm start 被确立为 Node.js 应用的惯用入口，已成为事实上的标准。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-run-script](/man/npm-run-script)(1), [npm-test](/man/npm-test)(1)
