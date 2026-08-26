# TAGLINE

1Password CLI（命令行密码管理器与机密管理）

# TLDR

**登录** 1Password 账户

```op signin```

**列出保险库中的所有项目**

```op item list --vault [vault_name]```

**获取特定项目的详细信息**

```op item get "[item_name]"```

**从项目中获取特定字段**

```op item get "[item_name]" --fields label=username,label=password```

**使用机密引用读取机密**

```op read "op://[vault]/[item]/[field]"```

**运行命令**并以环境变量的形式注入机密

```op run --env-file [.env] -- [command]```

**在保险库中创建新项目**

```op item create --category login --title "[title]" --vault [vault_name]```

**列出账户中的所有保险库**

```op vault list```

# SYNOPSIS

**op** [_command_] [_subcommand_] [_flags_]

# PARAMETERS

**account**
> 管理本地配置的 1Password 账户

**item**
> 对保险库项目执行 CRUD 操作（获取、列出、创建、编辑、删除）

**vault**
> 管理保险库及其权限

**document**
> 管理文档类项目（获取、列出、创建、编辑、删除）

**read**
> 解析并获取机密引用

**run**
> 将机密作为环境变量传递给子进程

**inject**
> 将机密插入配置文件或模板

**signin**
> 对 1Password 账户进行身份验证

**signout**
> 结束当前会话

**whoami**
> 显示已登录账户的信息

**completion**
> 生成 Shell 补全脚本

**--format** _json_
> 以 JSON 格式输出结果，便于用 jq 等工具解析

**--fields** _label=field_
> 指定要从项目中检索的特定字段

**--vault** _name_
> 指定操作的目标保险库

**--cache=false**
> 禁用守护进程缓存（在受限环境中很有用）

# DESCRIPTION

**op** 是 1Password 的官方命令行界面（打包为 **1password-cli**）。它让你可以直接在终端中安全地访问密码、凭据和敏感数据。

该 CLI 采用名词-动词的命令结构：第一个参数通常是资源类型（item、vault、user），后接动作（get、list、create）。它同时支持交互式和脚本化工作流，适用于开发自动化和 CI/CD 流水线。

主要能力包括：使用格式为 **op://vault/item/field** 的机密引用检索凭据、将机密注入环境变量供所运行的进程使用，以及以编程方式管理保险库内容。该工具在 Unix 系统上使用基于守护进程的缓存来提升性能并减少 API 调用。

项目可以通过名称或其 26 位字母数字 ID 引用；ID 更加稳定，也更适合自动化。输出可以格式化为 JSON，便于与 **jq** 等工具集成。

# CAVEATS

需要 1Password 账户，且大多数操作前必须完成身份验证。守护进程缓存功能会将加密数据存储在内存中，可能不适合所有安全环境——可使用 **--cache=false** 禁用。服务账户的身份验证流程与个人账户不同。本页面仅介绍 **CLI**（二进制文件 **op** / 软件包 **1password-cli**），不涉及 1Password 桌面 GUI。

# HISTORY

1Password 由 **AgileBits** 于 **2006 年**创立，最初是一款 macOS 密码管理器。命令行界面于 **2017 年**首次发布，用于支持开发者工作流和自动化。**2022 年**发布的 CLI 第 2 版引入了现在的名词-动词命令结构、机密引用，以及面向 CI/CD 集成的改进版服务账户支持。

# INSTALL

```aur: yay -S 1password-cli```

```nix: nix profile install nixpkgs#_1password-cli```

```brew: brew install --cask 1password-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [gopass](/man/gopass)(1), [bitwarden-cli](/man/bitwarden-cli)(1), [bw](/man/bw)(1), [vault](/man/vault)(1), [gpg](/man/gpg)(1)

# RESOURCES

```[Homepage](https://1password.com/)```

```[Documentation](https://developer.1password.com/docs/cli/)```

<!-- verified: 2026-07-22 -->
