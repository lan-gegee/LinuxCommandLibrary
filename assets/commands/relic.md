# TAGLINE

面向开发者的端到端加密密钥管理器

# TLDR

通过浏览器向 Relic 进行**身份验证**

```relic login```

为当前项目**初始化** Relic

```relic init```

**打开交互式 TUI**管理密钥

```relic```

以密钥注入环境变量的方式**运行命令**

```relic run -e [production] -- [npm run deploy]```

使用指定文件夹和作用域中的密钥**运行命令**

```relic run -e [staging] -f [api] -s [server] -- [node server.js]```

**列出所有项目**及其环境和文件夹

```relic projects```

**显示当前已认证的用户**

```relic whoami```

**禁用匿名遥测**

```relic telemetry disable```

# SYNOPSIS

**relic** [_command_] [_options_]

# PARAMETERS

**login**
> 通过浏览器使用设备授权流程向 Relic 进行身份验证。

**logout**
> 清除已存储的认证会话、缓存的密钥和密码。

**init**
> 为当前项目初始化 Relic，包括选择项目并写入 relic.toml 配置文件。

**projects**
> 以树状视图列出所有拥有和共享的项目及其环境与文件夹。

**whoami**
> 显示当前已认证用户的姓名、邮箱和套餐。

**mcp**
> 启动 Relic MCP 服务器，用于 AI 助手集成。

**telemetry** _status|enable|disable_
> 管理匿名使用数据的收集。

**run** **-e** _name_ [**-f** _folder_] [**-s** _scope_] [**-p** _id_] **--** _command..._
> 运行命令，并将解密后的密钥注入为环境变量。

**-e**, **--environment** _name_
> 要从中加载密钥的环境名称（必需）。

**-f**, **--folder** _name_
> 环境内的文件夹（可选）。

**-s**, **--scope** _scope_
> 作用域过滤器：**client**、**server** 或 **shared**（可选）。

**-p**, **--project** _id_
> 项目 ID。默认取自 relic.toml 或 **RELIC_PROJECT_ID** 环境变量。

**--version**
> 显示版本信息。

**--help**
> 显示可用命令与选项。

# DESCRIPTION

**relic** 是一个以 CLI 为先的密钥管理层，在把密钥发送到服务器之前先在设备上进行加密。服务器只存储密文，从而实现零知识安全模型。

运行 **relic run** 时，CLI 会从服务器获取加密的密钥，在本地使用 **AES-256** 和 **Argon2id** 解密，然后通过基于 Rust 的运行器将其注入目标进程，并在使用后清除内存。注入过程中不会向磁盘写入任何密钥。

Relic 支持团队协作，每个成员的密钥都用自己的密钥加密。它也可以在 CI/CD 流水线中使用，只需通过 **RELIC_API_KEY** 和 **RELIC_PASSWORD** 环境变量设置 API 密钥即可。

交互式 TUI（直接运行 **relic** 调用）提供可视化界面，可在项目、环境和文件夹之间创建、编辑和组织密钥。MCP 服务器模式支持与 AI 编程助手集成。

# CONFIGURATION

项目配置保存在项目根目录的 **relic.toml** 中，包含项目 ID：

```
project_id = "your-project-id"
```

relic.toml 旁边会创建一个 **.relic/** 目录用于本地缓存（cache.db）。请将 **.relic/** 加入 .gitignore。

**环境变量：**

**RELIC_API_KEY** — 用于 CI/CD 认证的 API 密钥（跳过交互式登录）
**RELIC_PASSWORD** — API 密钥模式下解密用的密码
**RELIC_PROJECT_ID** — 无需 relic.toml 即可覆盖项目 ID

# CAVEATS

独立二进制安装不提供交互式 TUI，请改用 CLI 命令。获取密钥需要活动的网络连接，不过结果会缓存在本地以加快后续运行。基于 Rust 的运行器与平台相关，每种目标架构都需要预编译的二进制文件。

# HISTORY

Relic 由 **Cupola** 公司的 **Can Vardar** 创建，是云密钥管理器的开源、CLI 优先替代品。它由 **TypeScript**（CLI）编写，并带有用于安全密钥注入的 **Rust** 运行时组件。该项目以 **BSL 1.1**（Business Source License）许可发布，托管在 GitHub 上。

# INSTALL

```nix: nix profile install nixpkgs#relic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doppler](/man/doppler)(1), [vault](/man/vault)(1), [sops](/man/sops)(1), [age](/man/age)(1), [gpg](/man/gpg)(1)
