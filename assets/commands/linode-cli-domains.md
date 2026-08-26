# TAGLINE

管理 Linode 上的 DNS 域

# TLDR

**列出域**

```linode-cli domains list```

**创建域**

```linode-cli domains create --domain [example.com] --type master --soa_email [admin@example.com]```

**查看域**

```linode-cli domains view [domain_id]```

**删除域**

```linode-cli domains delete [domain_id]```

**列出域记录**

```linode-cli domains records-list [domain_id]```

# SYNOPSIS

**linode-cli domains** _command_ [_options_]

# PARAMETERS

**list**
> 列出所有域。

**create**
> 创建域。

**view** _id_
> 查看域详情。

**delete** _id_
> 删除域。

**records-list** _id_
> 列出 DNS 记录。

**records-create** _id_
> 创建 DNS 记录。

**--domain** _name_
> 域名。

**--type** _type_
> 域类型（master、slave）。

# DESCRIPTION

**linode-cli domains** 管理 Linode 上的 DNS 域。可创建、更新和删除域及 DNS 记录。是用于云基础设施管理的 Linode CLI 的一部分。

# INSTALL

```brew: brew install linode-cli```

```nix: nix profile install nixpkgs#linode-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[linode-cli](/man/linode-cli)(1)
