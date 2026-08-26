# TAGLINE

运行软件包中定义的 stop 脚本

# TLDR

**停止应用**

```npm stop```

**不存在 stop 脚本时不报错**

```npm stop --if-present```

**向 stop 脚本传递参数**

```npm stop -- [--flag] [value]```

# SYNOPSIS

**npm** **stop** [_args_...]

# DESCRIPTION

**npm stop** 运行 package.json 中定义的 stop 脚本，并会执行 prestop 和 poststop 生命周期脚本。用于停止正在运行的服务进程。

# PARAMETERS

**--if-present**
> 未定义 stop 脚本时不报错。

**--silent**, **--quiet**
> 抑制所启动脚本的输出。

**--ignore-scripts**
> 跳过 pre/post 生命周期脚本。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-start](/man/npm-start)(1), [npm-restart](/man/npm-restart)(1)
