# TAGLINE

依次运行 stop、restart 和 start 脚本

# TLDR

**重启应用**

```npm restart```

# SYNOPSIS

**npm** **restart** [_args_...]

# DESCRIPTION

**npm restart** 依次运行生命周期钩子 **prerestart**、**restart** 和 **postrestart**。如果 **package.json** 中未定义 **restart** 脚本，则回退为先运行 **stop** 再运行 **start**（即执行软件包自身的 **start** 和 **stop** 脚本）。这是重启由 **package.json scripts** 描述的长时间运行的 Node 进程的惯用方式，无需在 shell 中重写命令。

# CAVEATS

与进程管理器（pm2、systemd）不同，**npm restart** 不会把新进程放到后台，也不会在 shell 退出后保持其运行——它只是在前台运行 **start** 脚本。生产环境的进程管理请使用真正的进程管理器。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-start](/man/npm-start)(1), [npm-stop](/man/npm-stop)(1)
