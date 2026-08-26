# TAGLINE

带 Plaid 同步、分类、标签和 FIRE 追踪功能的个人理财终端 UI

# TLDR

启动 TUI（后台同时启动 MCP 和 REST API）

```fungible```

使用假数据运行演示（无需任何配置）

```fungible --demo```

通过 Plaid 关联新的银行账户

```fungible --setup```

导入 CSV 账单

```fungible import-csv /path/to/statement.csv```

仅为 Claude Desktop 运行 MCP 服务器

```fungible mcp```

# SYNOPSIS

**fungible** [_options_] [_command_]

# DESCRIPTION

**fungible** 是一款以键盘操作为主的个人理财终端应用。它可以从 Plaid 同步交易、导入 CSV，让你编写强大的分类与重命名规则、为交易打标签、追踪净资产变化，并计算包括 FIRE 进度在内的财务健康指标。

所有数据都保存在本地 `~/.fungible/` 目录中。Plaid 令牌在存储时加密。TUI、MCP 服务器（供 Claude 等智能体使用）和 REST API 共享同一个数据库，因此从任一界面做出的更改会立即在其他界面生效。

核心概念：

- **Rules（规则）** — 子字符串或正则表达式规则（可选金额过滤），在导入/同步时自动分类或重命名交易。
- **Flexibility tiers（灵活性分级）** — 将类别标记为固定、弹性或自由支配，以了解消费行为。
- **Tags（标签）** — 与类别无关的横切标签（旅行、项目、客户）。
- **Net worth history（净资产历史）** — 定期记录的资产与负债快照。
- **Financial health（财务健康）** — 可支撑月数、FIRE 目标金额、Coast FIRE 以及可调整的假设条件。

# PARAMETERS

**--demo**  
> 使用预填充的演示数据库启动（安全、隔离）

**--setup**  
> 运行首次使用的 Plaid + 配置向导

子命令：

**mcp**  
> 仅运行 stdio MCP 服务器（用于 Claude Desktop 等）

**api**  
> 仅运行 REST API 服务器

# KEY BINDINGS (TUI)

主屏幕：

`1` 仪表盘、`2` 交易、`3` 趋势、`4` 净资产、`5` 标签、`6` 财务健康、`7` 规则、`8` 账户、`q` 退出。

在 **Transactions（交易）** 界面：`e` 编辑、`g` 打标签、`i` 忽略、`/` 正则搜索。

完整的按键绑定可在应用内按 `?` 查看。

# SEE ALSO

[ledger](/man/ledger)(1), [hledger](/man/hledger)(1)
