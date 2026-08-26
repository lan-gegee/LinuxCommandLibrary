# TAGLINE

面向人类用户和 AI 智能体的复式记账 CLI

# TLDR

**初始化**本地加密账本存储

```magpie --store .magpie init```

创建带工作流角色的**会计科目**

```magpie --store .magpie --actor owner ledger account create --number 1000 --name Checking --type asset --role bank_account```

从 JSON 导入规范化后的**发票**

```magpie --store .magpie --actor owner invoice import-json --file ./external-invoice.json```

**入账**一张发票（依据记账基础生成日记账）

```magpie --store .magpie --actor owner invoice post --invoice-id inv:...```

将发票标记为**已支付**

```magpie --store .magpie --actor owner invoice mark-paid --invoice-id inv:... --cash-account-id acct:... --paid-date 2026-06-15 --amount-cents 108500```

在执行有风险的智能体操作前创建一个**命名快照**

```magpie --store .magpie --actor owner snapshot create --name before-agent-run```

读取重建的**状态**或**审计**轨迹

```magpie --store .magpie --actor owner state```

# SYNOPSIS

**magpie** [**--store** _DIR_] [**--jaybase-url** _URL_] [**--actor** _USER_ID_] [**--role** _ROLE_] _command_ ...

# PARAMETERS

**--store** _DIR_
> 本地存储目录（默认 **.magpie**）。与托管模式互斥

**--jaybase-url** _URL_
> 托管 Jaybase 的 HTTPS origin（或环境变量 `JAYBASE_URL`）。令牌只能通过 `JAYBASE_TOKEN` 提供

**--actor** _USER_ID_
> 用于 RBAC 的调用者身份（init 后默认为 **owner**）

**--role** _ROLE_
> 可选的角色声明；必须与该 actor 被分配的角色一致

**init**
> 引导创建本地或空的托管账本（`cash` 记账基础，拥有 Owner 角色的 **owner**）

**book settings get**|**set**
> 读取或设置账本级设置（例如 **--accounting-basis** cash|modified_cash|accrual）

**ledger account** ...
> 创建/列出科目，设置科目编号、角色和外部引用

**ledger journal create** **--file** _entry.json_
> 特权手动日记账（需要 **journal:adjust** 权限和 **manual_reason**）

**customer**|**invoice**|**payout** ...
> 一等公民的源单据工作流，按记账基础生成日记账

**note put**|**get**|**list**
> Markdown 格式的运维笔记

**snapshot create --name** _NAME_
> 具名的恢复点根节点

**rbac** ...
> 权限、角色、用户及默认配置修复

**state** / **audit**
> 重建的状态和不可变的审计节点（需要 **audit:read** 权限）

# DESCRIPTION

**magpie** 是一款面向小型团队和 AI 智能体的复式记账 CLI 与领域引擎。每次写入都会检查 RBAC 和会计不变量，然后向 [Jaybase](https://github.com/kyle-visner/jaybase) 追加一条加密且不可变的事件。stdout 默认输出 JSON 供智能体消费；stderr 承载结构化错误。

账本有唯一的**记账基础**（`cash`、`modified_cash` 或 `accrual`）。发票和付款工作流会生成带来源标签、语义正确（区分应收账款与现金）的日记账。通用的 `ledger journal create` 仅限用于手动调整和导入，且必须填写理由——日常经营活动应使用领域命令。

本地模式将对象存储在 `.magpie/` 下，载荷采用 AES-256-GCM 加密。托管模式通过 HTTPS 与 Jaybase 服务通信，具备 bearer 认证、乐观并发控制和幂等写入。智能体应遵循项目中的 `llm.md`：绝不直接编辑存储文件，在工作流判断中使用账户**角色**而非名称，并在大规模变更前先创建快照。

# CAVEATS

尚未发布 1.0 版。`--actor` 并未以密码学方式绑定到 Jaybase 令牌主体——请只在可信的自动化环境中运行，或在能映射已认证调用者的包装层之后运行。没有原生 QuickBooks 解析器；智能体必须把外部数据规范化为 Magpie 的 JSON 契约。托管模式下的全量历史回放开销随账本规模增长。采用 AGPL-3.0-or-later 许可证。从源码构建需要较新的 Go 工具链。

# HISTORY

该项目构建于 Jaybase 只追加加密事件存储之上，作为一个对智能体安全的记账界面，提供明确的工作流来源、RBAC 以及基于记账基础的过账规则。


# SEE ALSO

[jq](/man/jq)(1)

# RESOURCES

```[Source code](https://github.com/kyle-visner/magpie)```

```[Documentation](https://github.com/kyle-visner/magpie/blob/main/README.md)```

<!-- verified: 2026-07-29 -->
