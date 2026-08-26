# TAGLINE

Node.js 进程守护与监控工具

# TLDR

**以守护进程方式启动脚本**

```forever start [app.js]```

**停止守护进程**

```forever stop [app.js]```

**停止所有守护进程**

```forever stopall```

**列出运行中的进程**

```forever list```

**重启脚本**

```forever restart [app.js]```

**启动时指定日志文件**

```forever start -l [forever.log] -o [out.log] -e [err.log] [app.js]```

# SYNOPSIS

**forever** [_options_] _command_ [_script_] [_args_]

# PARAMETERS

**start** _script_
> 以守护进程方式启动脚本。

**stop** _script|pid|index_
> 停止运行中的进程。

**stopall**
> 停止所有进程。

**restart** _script|pid|index_
> 重启进程。

**restartall**
> 重启所有进程。

**list**
> 列出运行中的进程。

**logs** _script|pid|index_
> 显示日志文件。

**-l** _logfile_
> forever 输出的日志文件。

**-o** _outfile_
> stdout 日志文件。

**-e** _errfile_
> stderr 日志文件。

**-w**, **--watch**
> 监视文件变化。

**-m** _max_
> 最大重启次数。

**-s**, **--silent**
> 运行脚本时静默 stdout 和 stderr。

**-a**, **--append**
> 追加写入日志文件而非覆盖。

**--minUptime** _ms_
> 判定为崩溃前所需的最短运行时间（默认：1000ms）。

**--killTree**
> 停止时杀死整个子进程树。

# CONFIGURATION

**~/.forever/config.json**
> forever 设置与默认行为的全局配置。

# DESCRIPTION

**forever** 持续运行 Node.js 脚本，并在脚本崩溃时自动重启。它专为 Node.js 应用的生产部署设计，确保应用保持运行。

该工具监控进程并在其退出时重启。它支持日志记录、多实例，并可监视文件变化以实现开发时的自动重启。

# CAVEATS

仅支持 Node.js。生产使用可考虑 PM2（功能更多）。日志文件可能变得很大。监视模式可能遗漏部分变化。与其他方案相比进程管理较为基础。

# HISTORY

forever 由 **Charlie Robbins** 和 **Nodejitsu** 团队在 **2010** 年代初创建，是最早的 Node.js 进程管理器之一。虽然 PM2 已在生产用途中基本取代了它，forever 依然简单实用。

# SEE ALSO

[pm2](/man/pm2)(1), [nodemon](/man/nodemon)(1), [node](/man/node)(1), [npm](/man/npm)(1)
