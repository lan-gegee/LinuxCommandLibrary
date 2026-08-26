# TAGLINE

管理 Linode 支持工单

# TLDR

**列出门票**

```linode-cli tickets list```

**查看工单**

```linode-cli tickets view [ticket_id]```

**创建工单**

```linode-cli tickets create --summary "[Issue summary]" --description "[Details]"```

**回复工单**

```linode-cli tickets reply [ticket_id] --description "[Reply text]"```

# SYNOPSIS

**linode-cli tickets** _command_ [_options_]

# PARAMETERS

**list**
> 列出支持工单。

**view** _id_
> 查看工单详情。

**create**
> 创建支持工单。

**reply** _id_
> 回复工单。

**--summary** _text_
> 工单摘要。

**--description** _text_
> 工单描述。

# DESCRIPTION

**linode-cli tickets** 管理 Linode 支持工单。可创建、查看和回复支持请求。是用于云基础设施管理的 Linode CLI 的一部分。

# INSTALL

```brew: brew install linode-cli```

```nix: nix profile install nixpkgs#linode-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[linode-cli](/man/linode-cli)(1)
