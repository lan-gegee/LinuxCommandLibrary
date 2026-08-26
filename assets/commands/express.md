# TAGLINE

Node.js Web 应用脚手架工具

# TLDR

**用生成器创建 Express 应用**

```npx express-generator [myapp]```

**指定视图引擎创建**

```npx express-generator --view=[pug] [myapp]```

**指定 CSS 预处理器创建**

```npx express-generator --css=[sass] [myapp]```

**不使用视图引擎创建**

```npx express-generator --no-view [myapp]```

**同时生成 .gitignore 创建**

```npx express-generator --git [myapp]```

# SYNOPSIS

**express-generator** [_options_] [_dir_]

# PARAMETERS

**--view** _engine_
> 视图引擎：pug、ejs、hbs、hjs、twig。

**--css** _engine_
> CSS 预处理器：sass、less、stylus、compass。

**-e**, **--ejs**
> 使用 EJS 模板引擎。

**--pug**
> 使用 Pug 模板引擎。

**--hbs**
> 使用 Handlebars 模板引擎。

**--no-view**
> 不使用视图引擎生成。

**-c** _engine_
> CSS 引擎（等同 --css）。

**--git**
> 添加 .gitignore。

**-f**, **--force**
> 在非空目录上强制执行。

# DESCRIPTION

**express-generator** 用于搭建 Express.js Web 应用的骨架。它会创建基本的目录结构、package.json 以及启动 Express 服务器的样板代码。

Express 是一个精简的 Node.js Web 框架。该生成器提供了一个符合惯例的起点，包含路由、视图（可选）、静态文件和错误处理。

# GENERATED STRUCTURE

```
myapp/
├── app.js          # Main application
├── package.json    # Dependencies
├── bin/www         # Server entry point
├── public/         # Static files
├── routes/         # Route handlers
└── views/          # Templates
```

# CAVEATS

生成器只提供最基础的配置。生产环境需要额外的配置（安全、日志等）。Express 5 尚在开发中，生成器可能滞后。较大的项目可以考虑 Fastify 或 Nest.js 等替代方案。

# HISTORY

Express 由 **TJ Holowaychuk** 于 **2010 年**创建，后来成为最受欢迎的 Node.js Web 框架。express-generator 从主包中分离出来，以便核心框架保持精简。

# INSTALL

```aur: yay -S express```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1), [nodemon](/man/nodemon)(1)

# RESOURCES

```[Source code](https://github.com/expressjs/generator)```

```[Homepage](https://expressjs.com/)```

<!-- verified: 2026-07-15 -->
