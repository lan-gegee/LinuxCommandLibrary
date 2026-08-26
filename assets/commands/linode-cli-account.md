# TAGLINE

管理 Linode（Akamai）账户信息和账单

# TLDR

**显示账户信息**

```linode-cli account view```

**显示账单明细和付款方式**

```linode-cli account view-billing```

**显示账户设置**

```linode-cli account settings```

**列出最近的事件**

```linode-cli account events-list```

**列出发票**

```linode-cli account invoices-list```

**查看特定发票**

```linode-cli account invoice-view [invoice_id]```

**列出付款记录**

```linode-cli account payments-list```

**查看网络流量池使用情况**

```linode-cli account transfer```

# SYNOPSIS

**linode-cli account** _command_ [_options_]

# COMMANDS

**view**
> 查看账户联系信息、余额和有效促销活动。

**view-billing**
> 查看账单明细，包括付款方式和最近一次付款。

**settings**
> 查看账户设置，包括 network helper 和备份默认值。

**update**
> 更新账户联系信息。

**events-list**
> 列出账户事件（Linode 创建、重启等）。

**invoices-list**
> 列出账单发票。

**invoice-view** _ID_
> 查看特定发票的详细信息。

**invoice-items** _ID_
> 列出特定发票的逐项条目。

**payments-list**
> 列出账户的付款记录。

**transfer**
> 查看当月网络流量池的使用情况。

**logins-list**
> 列出最近的账户登录。

**users-list**
> 列出账户上的用户。

# PARAMETERS

**--json**
> 以 JSON 格式输出。

**--text**
> 以纯文本格式输出。

**--pretty**
> 对 JSON 输出进行美化打印。

# DESCRIPTION

**linode-cli account** 管理 Linode（Akamai Cloud）账户信息，包括账单、发票、付款、事件和用户管理。它通过 Linode API 提供对账户详情和财务历史的只读访问。

# CAVEATS

需要已配置好且带有有效 API 令牌的 Linode CLI。某些账户操作要求令牌具有 read_write 权限范围。account view 会显示余额以及任何未使用的赠金或促销活动。

# INSTALL

```brew: brew install linode-cli```

```nix: nix profile install nixpkgs#linode-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[linode-cli](/man/linode-cli)(1)
