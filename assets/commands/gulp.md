# TAGLINE

用于自动化开发工作流的 JavaScript 任务运行器

# TLDR

**运行默认任务**

```gulp```

**运行指定任务**

```gulp [taskname]```

**列出可用任务**

```gulp --tasks```

**以串行而非并行方式运行多个任务**

```gulp [task1] [task2] --series```

**使用自定义 gulpfile 运行**

```gulp --gulpfile [path/gulpfile.js]```

**以静默模式运行**

```gulp --silent```

**监视文件变化**（需要 gulpfile 中存在 "watch" 任务）

```gulp watch```

# SYNOPSIS

**gulp** [_options_] [_tasks_...]

# DESCRIPTION

**gulp** 是一个用于自动化开发工作流的 JavaScript 任务运行器。它将文件流式传输到处理管道中，处理编译、压缩和测试等任务。

该工具采用"代码优于配置"的理念，通过 gulpfile.js 将任务定义为 JavaScript 函数。其流式架构使文件处理十分高效。在命令行上列出的任务默认并发（并行）执行，就像它们是单个任务的依赖项一样。

# PARAMETERS

**-T**, **--tasks**
> 打印已加载 gulpfile 的任务依赖树。

**--tasks-simple**
> 以纯文本形式打印任务列表，便于脚本化使用。

**-f**, **--gulpfile** _path_
> 手动设置 gulpfile 的路径。

**--cwd** _dir_
> 手动设置工作目录。

**-S**, **--silent**
> 抑制所有 gulp 日志输出。

**--continue**
> 任务失败后继续执行后续任务。

**-L**, **--log-level**
> 设置日志级别；重复使用可提高详细程度（如 -LL）。

**--series**
> 以串行而非并行方式运行命令行上给定的任务。

**--color**, **--no-color**
> 强制启用或禁用彩色输出。

**-v**, **--version**
> 打印全局与本地 gulp 的版本号。

# CAVEATS

需要 Node.js 和 npm。插件生态较为碎片化。Gulp 4 的 API 与 Gulp 3 不同。部分插件已无人维护。

# HISTORY

**gulp** 由 **Eric Schoffstall** 创建，于 **2013 年**发布，作为 Grunt 的替代方案。其流式处理方式和基于代码的配置深受开发者欢迎。虽然更新的打包工具不断涌现，gulp 在任务自动化领域依然流行。

# INSTALL

```pacman: sudo pacman -S gulp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [webpack](/man/webpack)(1), [grunt](/man/grunt)(1), [make](/man/make)(1)

# RESOURCES

```[Homepage](https://gulpjs.com)```

```[Source code](https://github.com/gulpjs/gulp)```

```[Documentation](https://gulpjs.com/docs/en/getting-started/quick-start/)```

<!-- verified: 2026-07-17 -->
