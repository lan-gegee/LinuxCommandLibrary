# TAGLINE

用于创作和部署带 AI NPC 像素小镇的 CLI

# TLDR

**安装** CLI（或不做全局安装直接运行）

```npm install -g @redplanethq/town```

```pnpm dlx @redplanethq/town [login]```

**登录** CORE 并保存个人访问令牌

```town login```

**创建新小镇**并打开聊天创作器

```town new ["My Town"]```

将现有小镇**克隆**到本地文件夹

```town clone --slug [my-town]```

将当前文件夹的小镇定义**部署**到服务器

```town deploy```

部署时**强制完整布局重排**

```town deploy --reflow```

**打印地块目录**（可选的小镇数据）

```town catalog --slug [my-town]```

**生成自定义建筑外观**图像

```town generate exterior ["a cozy bookshop with a green awning"] --out [exterior.png]```

用真实 LLM **测试 NPC 提示词**

```town test npc [npcs/cafe.mdx] -q ["What do you recommend today?"]```

# SYNOPSIS

**town** [_command_] [_options_]

**town** {**login** | **new** | **clone** | **deploy** | **catalog** | **delete** | **generate** | **test** | **init**} [_args_] [_options_]

# DESCRIPTION

**town** 是 **Town**（由 RedPlanetHQ / CORE 开发）的配套命令行工具：这是一种多人像素地图空间，每栋建筑中都有具备个性和工具技能组合的 AI 角色。玩家在浏览器中探索小镇；创作者将小镇编辑为磁盘上的 JSON 和 MDX 文件夹，然后用此 CLI 推送更改。

小镇文件夹通常包含 **town.json**（建筑列表和自定义地块引用）、**npcs/**（每个角色一个 **.mdx** 文件，frontmatter 定义身份，正文作为系统提示词）、可选的 **customPlots/**（用户定义的室内/室外场景），以及目录/清单参考文件。在含有 **town.json** 的文件夹中运行不带子命令的裸 **town** 会启动交互式聊天创作器（需要先执行过 **town login**）。在小镇文件夹之外，裸 **town** 则打印帮助信息。

身份验证使用存储在 **~/.town/config.json**（权限模式 **0600**）中的 CORE 个人访问令牌。API 调用会将该令牌作为 Bearer 凭据发送到所配置的小镇服务器。

# COMMANDS

**login**

> 通过 CORE 进行身份验证（浏览器 OAuth 流程），并将主机 URL 和 PAT 保存在 **~/.town/config.json** 下。

**new** [_name_]

> 创建新小镇（省略名称时会提示输入），生成本地文件夹脚手架，并启动聊天创作器。

**clone**

> 将现有小镇的状态拉取到本地目录。使用 **--slug** 可在不进行交互提示的情况下选择小镇。

**deploy**

> 将 **town.json**、**customPlots/** 和 **npcs/** 上传到服务器。先上传新的本地 PNG，再 POST 地块数据；服务器默认应用增量布局操作。

**catalog**

> 打印全局目录中可用的地块键名；配合 **--slug** 时还会包含该小镇的标签和物品模板。

**delete**

> 永久删除你的某个小镇。**--force** 可跳过输入 slug 确认的步骤。

**generate exterior** _concept_ / **generate interior** _concept_

> 根据简短的文字描述为自定义地块的外观或内部生成像素画 PNG。

**test set-key** _provider_ _key_

> 存储用于本地 NPC 测试的 LLM API 密钥（**anthropic**、**openai** 或 **ollama**）。环境变量始终优先于已保存的密钥。

**test npc** [_mdxPath_]

> 用真实模型运行 NPC 提示词（多轮会话、单次提问或脚本化场景）。

**init**

> 已弃用的别名。退出时提示改用 **town new** 或 **town clone**。

# PARAMETERS

**deploy** 选项：

**-d**, **--dir** _path_

> 包含 **town.json**、**customPlots/** 和 **npcs/** 的文件夹（默认：当前目录）。

**--slug** _slug_

> 目标小镇的 slug（默认先取自 **town.json** 中保存的 id，其次取自文件夹名称）。

**--reflow**

> 应用前清空服务器端的地块，使布局完全从头重新生成。

**clone** / **delete** / **catalog** / **generate**：在注明处使用 **--slug** _slug_。

**delete**：**--force** —— 跳过确认。

**generate exterior**：**--out** _path_（默认 **exterior.png**）、**--tiles** _WxH_、**--category** _cat_、**--slug** _slug_

**generate interior**：**--out** _path_（默认 **interior.png**）、**--category** _cat_、**--slug** _slug_

**test npc**：**-s** / **--session** _file_、**-q** / **--question** _text_、**-f** / **--script** _file_、**--show**、**--reset**、**--speaker** _name_、**--model** _id_

# CONFIGURATION

凭据和可选的 LLM 密钥保存在 **~/.town/config.json**（目录 **~/.town/**，文件权限 **0600**）：

```
{
  "auth": {
    "coreUrl": "https://app.getcore.me",
    "townUrl": "https://town.getcore.me",
    "pat": "<CORE personal access token>"
  },
  "llm": {
    "provider": "anthropic",
    "anthropicKey": "...",
    "openaiKey": "...",
    "ollamaKey": "..."
  }
}
```

Shell 环境变量（**ANTHROPIC_API_KEY**、**OPENAI_API_KEY**、**OLLAMA_API_KEY**、**LLM_PROVIDER**、**OLLAMA_BASE_URL**）优先于 **llm** 下保存的值。使用 **town login** 填充 **auth**；本地 NPC 测试密钥则通过 **town test set-key** 设置。

# CAVEATS

需要 Node.js（发布的软件包面向较新的 Node 版本，通常通过 **npm** / **pnpm** 运行）。大多数修改类命令都需要成功执行 **town login**。**town init** 不再创建或克隆小镇——请改用 **new** 或 **clone**。部署时的精灵图上传仅接受 PNG 格式（内容寻址，服务器有大小上限）。**town test npc** 需要配置好的 LLM 密钥，且可能产生服务商费用。交互式创作 TUI 需要真实终端。

# HISTORY

**Town** 是来自 **RedPlanetHQ** 的开源项目，围绕 **CORE** 智能体/记忆平台构建。小镇是带有会使用工具的 AI NPC 的多人像素地图；**@redplanethq/town** 软件包提供离线创作与部署工作流。早期 CLI 版本用一个 **init** 动词同时承担创建和克隆；后来拆分为 **town new** 和 **town clone**，**init** 仅作为迁移提示保留。

# SEE ALSO

[npm](/man/npm)(1), [pnpm](/man/pnpm)(1), [node](/man/node)(1)

# RESOURCES

```[Source code](https://github.com/RedPlanetHQ/town)```

```[Homepage](https://town.getcore.me/explore)```

```[Documentation](https://github.com/RedPlanetHQ/town#readme)```

<!-- verified: 2026-07-18 -->
