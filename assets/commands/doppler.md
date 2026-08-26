# TAGLINE

密钥管理与注入平台

# TLDR

**登录 Doppler**

```doppler login```

**设置项目**配置

```doppler setup```

**列出**当前 config 中的密钥

```doppler secrets```

**运行命令并注入**密钥

```doppler run -- [command]```

将密钥**转储到 stdout**，输出为 dotenv 文件

```doppler secrets download --no-file --format [env]```

针对**指定的**项目和 config 运行

```doppler run -p [backend] -c [prod] -- [command]```

使用服务令牌**在 CI 中完成身份验证**

```echo "[dp.st.prd.xxxx]" | doppler configure set token --scope /```

# SYNOPSIS

**doppler** _command_ [_subcommand_] [_flags_]

# COMMANDS

**login** / **logout**
> 让本机完成 Doppler 身份验证，或者解除绑定。

**setup**
> 以交互方式将当前目录绑定到某个项目和 config，此后的命令便无需再加 **-p**/**-c**。

**run** **--** _command_
> 运行 _command_，并把该 config 的密钥注入其环境。

**secrets**
> 列出、获取、设置、删除、下载、上传密钥，以及在模板中替换密钥。

**projects** / **configs** / **environments**
> 管理项目、config 和环境的层级结构。

**configure**
> 查看和编辑 CLI 自身的配置，包括身份验证令牌以及目录与 config 的映射。

**import**
> 从其他来源把密钥导入某个 config。

**activity**
> 显示近期变更的审计日志。

**me**
> 显示当前令牌对应的身份。

**open**
> 在浏览器中打开当前项目的仪表盘。

**update**
> 把 CLI 自身更新到最新版本。

# PARAMETERS

**-p**, **--project** _NAME_ / **-c**, **--config** _NAME_
> 指定要操作的项目和 config，覆盖 `doppler setup` 为该目录所做的选择。

**--command** _STRING_
> 以单条 shell 字符串的形式把命令传给 **run**，而不是放在 `--` 之后。

**--preserve-env** [_LIST_]
> 就列出的密钥而言，让既有环境变量的取值优先于 Doppler 的。

**--mount** _PATH_
> 将密钥写入临时文件，而不是注入环境中。

**--fallback** _PATH_, **--fallback-only**
> 使用加密的本地后备文件，Doppler 不可达时进程依然能够启动。

**--json**
> 以 JSON 格式打印输出。

# DESCRIPTION

**Doppler** 是一个托管型密钥管理平台，它的 CLI 存在的首要目的就是让密钥远离文件。核心命令是 **doppler run**：取得当前 config 的密钥，并以环境变量的形式注入子进程。全程没有任何内容落盘，因而也就不存在可能泄露、被误提交或逐渐过期的 `.env` 文件。

其模型是一个三层结构：每个服务一个*项目*，每个阶段（dev、staging、production）一个*环境*，以及存放实际键值对的 *config*。`doppler setup` 会记录目录所属的项目和 config，于是开发者只需 `cd` 进入仓库，`doppler run` 就能自动选对密钥。

在 CI 和生产环境中，作用于单一 config 的*服务令牌*取代了交互式登录，因此同一条命令在笔记本电脑上和流水线里都能原样工作。每次成功拉取后还会写入一份加密的**后备文件**，即使 Doppler 自身不可达，部署也照常可以启动。

# CAVEATS

Doppler 是商业 SaaS 产品：需要账号，且密钥在进程启动时经由网络获取，一旦出现故障或缺失令牌，应用就无法启动，除非提前备好后备文件。注入环境中的密钥对子进程及其后代均可见；在 Linux 上，同一用户下任何能读取 `/proc/<pid>/environ` 的进程同样能看到，所以对高价值凭据而言，**--mount** 是更稳妥的选择。用 `secrets download --no-file` 导出会把明文留在终端和 Shell 历史中，这基本抵消了使用这个工具的意义。

# HISTORY

Doppler 创立于 **2018 年**，属于回应 `.env` 文件泛滥的那一波工具——这类文件用着方便、容易误提交，却无法集中轮换。尽管后端服务是专有的，CLI 却是用 Go 编写的开源程序，因此注入机制可以独立于平台接受审查。

# INSTALL

```brew: brew install doppler```

```nix: nix profile install nixpkgs#doppler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doppler-secrets](/man/doppler-secrets)(1), [doppler-projects](/man/doppler-projects)(1), [vault](/man/vault)(1), [aws-vault](/man/aws-vault)(1), [sops](/man/sops)(1), [env](/man/env)(1)

# RESOURCES

```[Source code](https://github.com/DopplerHQ/cli)```

```[Homepage](https://www.doppler.com)```

```[Documentation](https://docs.doppler.com/docs/cli)```

<!-- verified: 2026-07-14 -->
