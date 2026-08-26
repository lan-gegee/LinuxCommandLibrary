# TAGLINE

执行软件包中定义的脚本

# TLDR

**运行 package.json 中的脚本**

```npm run [script-name]```

**列出可用的脚本**

```npm run```

**带参数运行**

```npm run [script] -- [--flag]```

**安静地运行**

```npm run [script] --silent```

**脚本存在时才运行**

```npm run [script] --if-present```

# SYNOPSIS

**npm** **run** [_script_] [-- _args_]

# PARAMETERS

_SCRIPT_
> package.json 中的脚本名称。

_ARGS_
> 传递给脚本的参数。

**--silent**
> 抑制输出。

**--if-present**
> 缺失时不报错。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm run** 执行 package.json 中定义的脚本，是核心工作流命令。

该命令运行 scripts 部分的条目。-- 之后的额外参数会传递给脚本。

# CAVEATS

脚本定义在 package.json 中。向脚本传参用 --。别名：npm run-script。

# HISTORY

npm run 是执行项目自定义脚本的**主要机制**。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-start](/man/npm-start)(1), [npm-test](/man/npm-test)(1)
