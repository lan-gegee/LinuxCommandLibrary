# TAGLINE

用于 Longbridge 行情数据与交易的终端客户端

# TLDR

**登录** Longbridge 账户（会打开浏览器进行 OAuth 授权）

```longbridge auth login```

**查看某只证券的实时行情**（采用 CODE.MARKET 记法）

```longbridge quote [NVDA.US]```

**显示某只证券的 K 线图**

```longbridge kline [700.HK]```

**列出当前持仓**

```longbridge positions```

**查看投资组合盈亏**

```longbridge portfolio```

**获取某只证券的最新新闻**

```longbridge news [AAPL.US]```

**输出机器可读的 JSON**，便于脚本处理或管道传入 jq

```longbridge quote [TSLA.US] --format json```

# SYNOPSIS

**longbridge** _command_ [_arguments_] [**--format** _json_]

# DESCRIPTION

**longbridge** 是面向 **Longbridge Securities（长桥证券）** 的命令行客户端，可在终端中调用 Longbridge OpenAPI。它将实时与历史行情、基本面数据、账户与投资组合管理以及下单功能整合进单个二进制文件，提供一百多个子命令，分别映射到底层 API 端点。

证券以 **CODE.MARKET** 记法表示，例如美股 `TSLA.US`、港股 `700.HK`、沪市 A 股 `600519.SH`。大多数命令支持 **--format json**，使输出可以被脚本化、管道传给 `jq` 等工具或交给 AI 智能体处理；不加该选项时，结果以人类可读的表格和图表打印。

身份验证通过 Longbridge SDK 的 OAuth 2.0 完成。运行 `longbridge auth login` 会打开浏览器进行账户授权，随后 SDK 会存储并刷新令牌，因此各条命令无需手动输入凭据。

# COMMANDS

**auth login**

> 通过 OAuth 授权 Longbridge 账户并存储会话令牌。

**quote** _symbol_

> 打印指定证券的实时行情。

**kline** _symbol_

> 显示用于技术分析的 K 线图。

**positions**

> 列出账户当前持仓。

**portfolio**

> 显示投资组合概览及盈亏指标。

**news** _symbol_

> 显示某只证券的近期新闻。

**financial-report** _symbol_

> 获取公司财务报表。

其余命令组涵盖深度行情与公告、期权与权证、IPO、自选股、交易、账单、内部人交易、定投、卖空以及选股筛选等功能。

# PARAMETERS

**--format** _json_

> 以机器可读的 JSON 代替格式化的终端输出。适用于脚本处理和管道传入 `jq`。

# CAVEATS

longbridge 会下达真实订单并访问实盘账户数据，因此交易类子命令涉及真实资金并承担相应的市场风险。使用前需要一个已入金的 Longbridge 账户和 OpenAPI 权限，且仅在 Longbridge 支持的市场和品种类型中有效。行情权限取决于账户订阅的市场数据套餐。

# HISTORY

该工具由金融科技公司 **Longbridge** 开发并以 **Apache License 2.0** 协议开源。它使用 **Rust** 编写，兼具可脚本化的 CLI 与交互式终端界面，定位为 Longbridge OpenAPI 的"AI 原生"前端。

# SEE ALSO

[curl](/man/curl)(1), [jq](/man/jq)(1)

# RESOURCES

```[Source code](https://github.com/longbridge/longbridge-terminal)```

```[Documentation](https://open.longbridge.com/docs/cli)```

<!-- verified: 2026-06-27 -->
