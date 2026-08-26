# TAGLINE

Git 风格的端到端加密密钥管理 CLI

# TLDR

通过 npm **安装**

```npm install -g @capysc/cli```

**同步**密钥（首次运行时初始化项目）

```capy```

在交互式 TUI 中**编辑**密钥

```capy edit```

**运行命令**并注入解密后的密钥

```capy run -- npm run dev```

**邀请**团队成员

```capy invite [teammate@example.com]```

**移除**团队成员（密码学撤销）

```capy kick [teammate@example.com]```

将密钥**部署**到托管平台

```capy deploy```

# SYNOPSIS

**capy** [_subcommand_] [_options_] [_args_]

# DESCRIPTION

**capy** 是一套具备 git 风格原语的密钥工具链——sync、branch、deploy、invite、kick——在数据离开你的机器之前就完成加密。服务端只存储成员记录和密文；解密所需的密钥分片永远不会离开客户端。你的 `.env` 成为团队可提交（`keep.lock`）、可回滚、可在不移除所有应用密钥的情况下完成成员退出的版本化状态。

首次在含有明文 `.env` 的项目中运行时，Capy 会将每个值就地加密为 `capy:{resourceId}:{ciphertext}` 片段，并将原文件备份为 `.env.pre-capy.old`。**capy run** 将密钥解密到进程内存中，然后启动任何需要读取环境变量的命令。**capy kick** 会让被移除用户的本地密钥在密码学上失效，而无需为其余成员轮换主密钥。

分支机制与 git 类似：每个 Capy 分支持有各自的密钥状态和访问列表；git 分支通过已提交的 `keep.lock` 绑定到一个 Capy 分支。首次完成认证同步后，离线的 **capy run** 可基于本地缓存工作。

# PARAMETERS

**（无子命令）**
> 在本地 `.env`、绑定的 `keep.lock` 与远端之间进行三方同步。首次使用时初始化项目。

**run** **--** _command_...
> 在内存中解密密钥，并以环境变量的形式提供给 _command_ 运行。

**edit**
> 变量的交互式表格：显示、编辑、漂移/冲突状态。

**status**
> 显示本地、绑定与远端之间的漂移。

**push**
> 只推送本地更改，不先拉取。

**lock**
> 锁定本地密钥，使下次使用需要口令。

**deploy**
> 生成部署令牌并引导完成平台配置（Vercel、Cloudflare、Docker、Fly、Railway、Render、Heroku、GitHub Actions、AWS Lambda 等）。

**connect** _provider_
> 从已关联的提供方拉取一条凭据到 `.env`。

**rotate** [_var_]
> 轮换某个受管凭据。

**invite** _email_
> 邀请团队成员（邀请码经带外方式传递）。

**redeem** _code_
> 兑换邀请码。

**kick** _email_
> 以密码学撤销的方式移除团队成员。

**users**
> 交互式成员管理。

**org**
> 列出或切换组织。

**branch**, **checkout** _branch_
> 列出/切换 Capy 分支；**checkout -b** 创建新分支。

**grant-branch**, **revoke-branch**
> 受保护分支的访问控制。

**recover**, **end-recover**
> 用恢复短语恢复访问 / 结束恢复模式。

**decrypt**
> 离线解密（仅限所有者）。

**use** _profile_, **profile**
> 切换或管理 CLI 配置档。

**byoc** [_url_]
> 在可用时连接自托管的 Capy 实例。

**info**, **logout**, **cleanup**, **transport**
> 会话信息、清除会话、移除钩子/本地状态、将账户迁移到另一台机器。

# CONFIGURATION

**.env**
> 项目密钥文件；init 之后值会变为 `capy:...` 密文片段。

**keep.lock**
> 已提交的清单文件，固定分支和加密资源状态（类似 lockfile）。

**~/.capy/**
> 本地缓存与密钥，使 **capy run** 在首次同步后可离线工作。

**.env.pre-capy.old**
> 首次迁移时对原始明文 `.env` 的自动备份（已被 gitignore）。

# CAVEATS

托管服务组件并非对所有部署形态都支持完全自托管；按设计，若丢失组织所有者的种子短语且没有其他设备保存 `key.enc`，访问权限将永久丧失。首次同步需要网络；离线操作仅使用本地缓存。CLI 采用 AGPL-3.0 许可证；请为你的团队审查许可证义务。

# HISTORY

**Capy**（npm 包 **@capysc/cli**）是 **Incentv Technologies** / capysc 推出的 AGPL-3.0 密钥管理产品，定位为面向人类和代理的零信任、源头加密的密钥管理方案，与 git 并行使用。

# SEE ALSO

[sops](/man/sops)(1), [age](/man/age)(1), [doppler](/man/doppler)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/capysc/capy-cli)```

```[Homepage](https://capy.sc)```

```[Documentation](https://docs.capy.sc)```

<!-- verified: 2026-08-06 -->
