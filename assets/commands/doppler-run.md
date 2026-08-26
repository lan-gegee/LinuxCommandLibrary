# TAGLINE

执行命令并向其注入密钥

# TLDR

**运行命令并注入**密钥

```doppler run -- [node app.js]```

使用指定的 config **运行**

```doppler run --config [dev] -- [command]```

使用指定的项目**运行**

```doppler run --project [myapp] -- [command]```

**透传给 Shell**

```doppler run -- sh -c "[echo \$SECRET_KEY]"```

使用后备文件**运行**

```doppler run --fallback [.env.backup] -- [command]```

将密钥**挂载为**文件

```doppler run --mount [secrets.env] -- [command]```

为 .NET **转换密钥名称**

```doppler run --name-transformer dotnet-env -- [dotnet run]```

# SYNOPSIS

**doppler run** [_options_] **--** _command_ [_args_]

# PARAMETERS

**--** _COMMAND_
> 要以注入密钥方式运行的命令。

**--config** _NAME_
> 要使用的配置环境。

**--project** _NAME_
> 项目名称。

**--fallback** _FILE_
> Doppler 不可用时使用的后备文件。

**--no-fallback**
> 禁用后备行为。

**--preserve-env**
> 保留既有的环境变量。接受以逗号分隔的具体密钥列表（例如 --preserve-env="FOO,BAR"），或传 "true" 表示全部保留。

**--mount** _PATH_
> 把密钥写入临时文件，而不是注入环境变量。格式根据文件扩展名自动检测。

**--mount-format** _FORMAT_
> 挂载密钥文件使用的格式（例如 json、env）。

**--name-transformer** _TRANSFORMER_
> 对 UPPER_SNAKE_CASE 形式的密钥名进行转换（例如 dotnet-env、tf-var、lower-camel、lower-snake）。

**--command** _CMD_
> 要执行的命令（可用来替代 `--` 分隔符）。

**--clean-exit**
> 当命令被中断（SIGINT）时以状态码 0 退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**doppler run** 执行一条命令，并把 Doppler 中的密钥作为环境变量注入。这样应用程序无需改动代码或本地配置文件就能访问密钥。

密钥从 Doppler API 获取，且只对被执行的进程可用。双横线用于分隔 doppler 的选项与要运行的命令。

后备文件在 Doppler 不可达时提供韧性，而 preserve-env 则防止覆盖既有的环境变量。

# CAVEATS

需要已通过身份验证的 doppler CLI。网络延迟会影响启动时间。密钥在进程环境中可见。子进程会继承这些密钥。

# HISTORY

doppler run 是 **Doppler** CLI 中负责密钥注入的主力命令，体现了 Doppler 设计之初追求的零配置密钥访问。

# INSTALL

```brew: brew install doppler```

```nix: nix profile install nixpkgs#doppler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doppler](/man/doppler)(1), [doppler-secrets](/man/doppler-secrets)(1), [env](/man/env)(1)
