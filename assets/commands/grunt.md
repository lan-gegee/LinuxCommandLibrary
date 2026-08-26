# TAGLINE

用于自动化的 JavaScript 任务运行器

# TLDR

**运行默认任务**

```grunt```

**运行特定任务**

```grunt [task-name]```

**按顺序运行多个任务**

```grunt [task-one] [task-two]```

**列出可用任务和选项**

```grunt --help```

**以详细输出运行**

```grunt --verbose```

**忽略警告强制执行**

```grunt --force```

**使用备用的 Gruntfile**

```grunt --gruntfile [path/to/Gruntfile.js] [task-name]```

**执行试运行，不写入文件**

```grunt --no-write```

# SYNOPSIS

**grunt** [_options_] [_tasks_]

# PARAMETERS

_TASKS_
> 要按顺序执行的任务。未指定时运行 **default** 任务。

**-f**, **--force**
> 遇到警告时继续执行而不是中止。

**-v**, **--verbose**
> 详细模式，输出更多关于 Grunt 正在执行操作的信息。

**-b**, **--base** _PATH_
> 备用的基准路径；文件路径默认相对于 Gruntfile。

**--no-color**
> 禁用彩色输出。

**--gruntfile** _FILE_
> 指定备用的 Gruntfile。

**--no-write**
> 禁用文件写入（试运行）。

**-d**, **--debug**
> 为支持调试的任务启用调试模式。

**--stack**
> 因警告或致命错误退出时打印堆栈跟踪。

**-V**, **--version**
> 打印 Grunt 版本；与 --verbose 组合可同时显示插件版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Grunt** 是一款 JavaScript 任务运行器，用于自动化重复性任务。它通过插件生态处理压缩、编译、测试和代码检查等工作。

该工具从 Gruntfile.js 读取配置。全局安装的 **grunt-cli** 软件包提供 **grunt** 命令本身；它只是定位并运行项目本地安装的 Grunt 版本，实际加载 Gruntfile 和插件的正是本地版本。在 npm scripts 以及 Gulp、webpack 等更新的构建工具流行之前，Grunt 曾被广泛使用。

# CONFIGURATION

**Gruntfile.js**
> 项目级配置文件，定义任务、任务选项及执行顺序。

**package.json**
> 将 Grunt 插件列为 devDependencies。

# CAVEATS

需要 Node.js。配置可能较为繁琐。已有更新的替代方案（Gulp、npm scripts）。

# HISTORY

Grunt 由 **Ben Alman** 于 **2012 年**创建，是最早的 JavaScript 任务运行器之一。

# INSTALL

```brew: brew install grunt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gulp](/man/gulp)(1), [npm](/man/npm)(1), [webpack](/man/webpack)(1)

# RESOURCES

```[Source code](https://github.com/gruntjs/grunt)```

```[Homepage](https://gruntjs.com/)```

```[Documentation](https://gruntjs.com/getting-started)```

<!-- verified: 2026-07-17 -->
