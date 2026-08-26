# TAGLINE

命令行开源番茄钟计时器

# TLDR

**启动**一个番茄钟

```pomodoro start```

**检查**状态

```pomodoro status```

**提前结束** / 进入休息

```pomodoro finish```

**清除**历史记录 / 设置（见帮助）

```pomodoro --help```

# SYNOPSIS

**pomodoro** *command* [*options*]

# DESCRIPTION

**pomodoro** 是 **openpomodoro-cli** 项目的 CLI，实现了番茄工作法：带休息的定时专注时段、适用于 shell 提示符的状态输出，以及简单的日志。可通过 **go install github.com/open-pomodoro/openpomodoro-cli/cmd/pomodoro@latest** 或可用的发行版软件包安装。

# PARAMETERS

**start** [**-t** *duration*] [**-d** *description*]

> 开始专注会话（标志因版本而异）。

**status**

> 打印番茄钟是否正在运行及剩余时间。

**finish** / **break** / **cancel**

> 完成或中止当前时间段。

配置通常位于 XDG 配置主目录下；**POMODORO_*** 环境变量详见上游 README。

# CAVEATS

存在多个互不相关的同名“pomodoro”工具安装——请确保 PATH 指向 openpomodoro-cli。桌面通知依赖可选的钩子。

# INSTALL

```nix: nix profile install nixpkgs#pomodoro```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sleep](/man/sleep)(1), [timer](/man/timer)(1), [arttime](/man/arttime)(1)

# RESOURCES

```[Source code](https://github.com/open-pomodoro/openpomodoro-cli)```

<!-- verified: 2026-07-19 -->
