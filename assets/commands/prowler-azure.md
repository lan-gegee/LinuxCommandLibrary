# TAGLINE

Azure 云安全评估

# TLDR

**运行 Azure 安全评估**

```prowler azure```

**运行特定检查项**

```prowler azure --checks [storage_account_public_access]```

**按合规框架运行**

```prowler azure --compliance [cis_2.0_azure]```

**指定订阅**

```prowler azure --subscription-ids [sub-id-1]```

# SYNOPSIS

**prowler azure** [_options_]

# PARAMETERS

**--checks** _checks_
> 要运行的特定检查项。

**--services** _services_
> 要检查的服务。

**--compliance** _framework_
> 合规框架。

**--subscription-ids** _ids_
> Azure 订阅 ID。

**-M**, **--output-modes** _format_
> 输出格式。

**-o**, **--output-directory** _dir_
> 输出目录。

# DESCRIPTION

**prowler azure** 对 Azure 订阅执行安全评估。它依据最佳实践和合规框架检查配置，识别 Azure 资源中的安全问题。

# INSTALL

```brew: brew install prowler```

```nix: nix profile install nixpkgs#prowler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[prowler](/man/prowler)(1), [az](/man/az)(1)
