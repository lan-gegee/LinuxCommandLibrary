# TAGLINE

本地 API 密钥保险库与 dotenv 运行器

# TLDR

在当前目录**初始化**项目保险库

```obscura init```

为当前用户**初始化**全局保险库

```obscura init --global```

向活动保险库**添加**一个机密

```obscura add [openai_key]```

将机密**读取**到 stdout

```obscura get [openai_key]```

**列出**保险库中的所有条目

```obscura list```

**移除**单个机密且无需确认

```obscura remove [openai_key] --yes```

将 dotenv 文件**导入**保险库

```obscura import [.env]```

将保险库**导出**为 dotenv 文件

```obscura export --dotenv --output [.env]```

**运行**命令并将保险库中的所有机密作为环境变量注入

```obscura run -- [npm start]```

**缓存**保险库密钥 30 分钟，使后续调用不再提示输入口令

```obscura unlock --timeout [30]```

# SYNOPSIS

**obscura** _command_ [_options_] [_args_]

# PARAMETERS

**init** [**--global**]
> 创建项目保险库；传入 **--global** 时创建全局保险库。

**add** _alias_ [**--global**|**--project**|**--from-global**]
> 在 _alias_ 下存储一个机密，可选从全局保险库获取其值。

**get** _alias_
> 将存储在 _alias_ 下的机密打印到 stdout。

**list**, **ls** [**--json**] [**--global**|**--project**]
> 显示活动保险库的条目。

**remove** _alias_ [**--yes**]
> 删除一个机密。**--yes** 跳过确认提示。

**delete** **--global**|**--project** **--yes**
> 销毁整个保险库。两个标志都必须提供。

**rotate** _alias_
> 替换 _alias_ 下的机密值，同时保留其时间戳。

**import** _file_
> 从 dotenv 文件导入键值对到活动保险库。

**export** **--dotenv** [**--output** _file_]
> 以 dotenv 格式导出机密，输出到 stdout 或 _file_。

**run** **--** _command_ [_args_...]
> 执行 _command_ 并将保险库条目作为环境变量注入。

**unlock** [**--timeout** _MINUTES_]
> 缓存派生的保险库密钥 _MINUTES_ 分钟（默认 60）。

**lock**
> 丢弃所有已缓存的保险库密钥。

# DESCRIPTION

**obscura** 是一款单二进制、跨平台的保险库，用于管理本地开发过程中堆积的 API 密钥、令牌和其他机密。机密在磁盘上使用由用户口令经 Argon2 派生的密钥加密保存，并按需解锁，因此不会在任何 **.env** 文件、shell 历史或进程环境中留下明文。

它支持两种作用域：与代码仓库一同存放的项目保险库，以及面向当前用户的全局保险库。**add --from-global** 标志可在两者之间复制条目，而 **import** / **export --dotenv** 让你能够轻松从现有的 dotenv 工作流迁移过来。**run** 子命令会派生一个子进程，把保险库解密注入其环境并在结束后重新上锁，使 obscura 可以直接替代临时的 **export FOO=...** shell 命令。

# CONFIGURATION

保险库文件存放在各平台约定俗成的位置：

```
macOS    ~/Library/Application Support/Obscura/vault.enc
Linux    $XDG_CONFIG_HOME/obscura/vault.enc (defaults to ~/.config/obscura/vault.enc)
Windows  %APPDATA%\Obscura\vault.enc
```

项目保险库存放在其所属仓库旁边。行为可通过环境变量调节：

> **OBSCURA_PASSPHRASE** — 非交互式口令，适用于 CI。
> **OBSCURA_KDF_MEM_KIB** — Argon2 内存开销（KiB）。
> **OBSCURA_KDF_TIME** — Argon2 迭代次数。

# EXIT CODES

```
0   Success
1   General error
2   Alias not found
```

# CAVEATS

obscura 仅面向**本地开发**：它没有团队共享、审计日志、轮换策略或基于硬件的密钥存储。生产环境的机密应存放在托管式机密存储（Vault、AWS Secrets Manager、GCP Secret Manager、1Password CLI 等）中。保险库的安全性取决于 **init** 时选择的口令强度；一旦丢失口令，机密将无法恢复。

# HISTORY

**obscura** 由 **obscura-os** 项目开发，发布于 **github.com/obscura-os/obscura-cli**。仓库名为 **obscura-cli**，但安装的二进制文件就叫 **obscura**。

# INSTALL

```aur: yay -S obscura```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [pass](/man/pass)(1), [age](/man/age)(1), [vault](/man/vault)(1), [op](/man/op)(1)
