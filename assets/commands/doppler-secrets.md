# TAGLINE

管理并导出密钥值

# TLDR

**列出所有密钥**

```doppler secrets```

**获取指定密钥**

```doppler secrets get [SECRET_NAME]```

**设置密钥**

```doppler secrets set [KEY]=[value]```

**删除密钥**

```doppler secrets delete [SECRET_NAME]```

**打印单个密钥的原始值**，便于脚本处理

```doppler secrets get [SECRET_NAME] --plain```

将密钥**转储到 stdout**，输出为 dotenv 文件

```doppler secrets download --no-file --format [env]```

把现有 .env 文件**上传到** config

```doppler secrets upload [.env]```

**渲染模板**并替换其中的密钥

```doppler secrets substitute [template.yaml]```

# SYNOPSIS

**doppler secrets** [_subcommand_] [_arguments_] [_flags_]

# SUBCOMMANDS

(none)
> 打印当前项目和 config 中全部密钥的表格。

**get** [_secrets_...]
> 获取一个或多个密钥的值。

**set** [_secrets_...]
> 设置一个或多个密钥的值。只提供名称调用时会交互式提示输入值。

**delete** [_secrets_...]
> 删除一个或多个密钥。

**download** [_filepath_]
> 下载某个 config 的密钥以备后用。不加 **--no-file** 时会写入*加密的*后备文件。

**upload** _filepath_
> 上传一个密钥文件，导入其中的所有内容。

**substitute** _filepath_
> 将密钥替换进模板文件。

# PARAMETERS

**-p**, **--project** _NAME_ / **-c**, **--config** _NAME_
> 指定要操作的项目和 config，覆盖 `doppler setup` 为当前目录所做的选择。

**--plain**
> 打印值时不套用表格格式。在脚本中捕获值时必不可少。

**--only-names**
> 只打印密钥名称，省略所有值。

**--raw**
> 打印存储的原始值，不解析密钥引用。

**--copy**
> 将值复制到剪贴板（配合 **get**）。

**--format** _FORMAT_
> **download** 的输出格式：`json`（默认）、`env`、`yaml`、`docker` 等。

**--no-file**
> 将响应打印到 stdout，而不是写入文件。

**--visibility** _LEVEL_
> 在 **set** 时设置密钥的可见性：`masked`、`unmasked` 或 `restricted`。

**-y**, **--yes**
> 不经确认提示直接执行（配合 **delete**）。

**--fallback** _PATH_, **--fallback-only**, **--no-fallback**
> 控制加密的后备文件，使 Doppler 不可达时仍能读取密钥。

**--json**
> 以 JSON 格式打印结果。

# DESCRIPTION

**doppler secrets** 是读写 Doppler config 中密钥的接口。不带子命令运行时，它会以表格打印 `doppler setup` 所选 config 中的全部条目，值会被遮蔽显示。

**download** 是导出途径。它默认采用 **JSON** 格式，并且在未指定 **--no-file** 时写入的是*加密的*后备文件而非明文文件，这是一项刻意为之的安全选择：要把明文 dotenv 输出到 stdout，常规做法是 `doppler secrets download --no-file --format env`。

密钥之间可以用 `${OTHER_SECRET}` 语法相互引用，CLI 会在打印前解析这些引用。**--raw** 显示的则是存储下来的原始文本，跨 config 复制值时就该用它。

**substitute** 渲染一个 Go 模板文件，并把当前 config 的密钥作为变量提供给模板，正好覆盖生成 Kubernetes 清单或期望真实取值而非环境变量的配置文件这类常见场景。

# CAVEATS

凡是通过 **get --plain** 或 **download --no-file** 打印的内容，都会以明文出现在你的终端和 Shell 历史中；更推荐 `doppler run`，让值完全不落盘。**download** 默认写出的文件是加密的，常让期待可读 `.env` 的人感到意外。**delete** 立即生效且没有撤销功能，不过变更会记入活动日志。写入操作需要具有写权限的令牌，只读的服务令牌在执行 **set** 和 **delete** 时会失败。

# HISTORY

**doppler secrets** 是 Doppler CLI 的核心，从产品首个发布版本起便已存在。最终沉淀下来的设计——不让密钥进入磁盘上的 `.env` 文件，而是在进程启动时注入——正是整套 CLI 其余部分的构建基础；加入加密后备文件之后，即便网络或 API 不可用，这套做法依然安全可靠。

# INSTALL

```brew: brew install doppler```

```nix: nix profile install nixpkgs#doppler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doppler](/man/doppler)(1), [doppler-projects](/man/doppler-projects)(1), [vault](/man/vault)(1), [sops](/man/sops)(1)

# RESOURCES

```[Source code](https://github.com/DopplerHQ/cli)```

```[Homepage](https://www.doppler.com)```

```[Documentation](https://docs.doppler.com/docs/cli)```

<!-- verified: 2026-07-14 -->
