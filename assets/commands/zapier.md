# TAGLINE

用于构建集成的 Zapier Platform CLI

# TLDR

**向 Zapier 进行身份验证**

```zapier login```

**初始化新的集成项目**

```zapier init [project-name]```

**将集成代码推送到 Zapier**

```zapier push```

**在本地运行集成测试**

```zapier test```

**对照 Zapier 的模式校验集成**

```zapier validate```

**将某个版本提升为公开可用**

```zapier promote [1.0.0] [100]```

**查看集成的日志**

```zapier logs```

**在本地调用触发器或操作进行测试**

```zapier invoke [trigger] [trigger_key]```

# SYNOPSIS

**zapier** _command_ [_options_]

# PARAMETERS

**login**
> 向 Zapier 进行身份验证。

**logout**
> 退出 Zapier 登录。

**init**
> 创建新的集成项目。

**scaffold**
> 搭建新的触发器、操作或搜索脚手架。

**push**
> 将当前集成上传到 Zapier。

**test**
> 在本地运行集成测试。

**validate**
> 对照 Zapier 的模式检查集成。

**promote**
> 将某个版本提升为公开可用。

**describe**
> 描述当前集成。

**logs**
> 查看集成最近的日志。

**env:set**
> 为某个版本设置环境变量。

**env:get**
> 获取某个版本的环境变量。

**invoke**
> 在本地调用触发器、操作或搜索。

**register**
> 在 Zapier 上注册新集成。

**build**
> 从当前目录构建可推送的 zip 包。

**versions**
> 列出当前集成的各版本。

# DESCRIPTION

**zapier** 是 Zapier 自动化平台官方的命令行界面，用于开发集成。它提供创建、测试、校验和部署自定义集成的工具，这些集成用 JavaScript 连接第三方应用。

开发工作流从 **zapier init** 搭建新项目开始，随后用 JavaScript（Node.js v22）定义触发器、操作和搜索。**test** 命令在本地运行集成测试，**invoke** 允许从终端测试触发器和操作，**validate** 在部署前对照 Zapier 的模式要求检查集成。

就绪后，**zapier push** 将集成上传到 Zapier 平台。**promote** 命令使特定版本公开可用。已部署版本的环境变量用 **env:set** 和 **env:get** 管理。

# CAVEATS

需要 Zapier 账户。需要 Node.js（集成运行于 Node.js v22）。通过 `npm install -g zapier-platform-cli` 安装。

# HISTORY

**zapier** CLI 由 **Zapier** 创建，是用于在其自动化平台上构建集成的开发者工具。它取代了早期的可视化构建器方式，为开发者提供了基于代码、使用 JavaScript 和 Node.js 的工作流。

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1)
