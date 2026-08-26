# TAGLINE

Microsoft 365 租户安全评估

# TLDR

**运行 Microsoft 365 安全评估**

```prowler m365```

**运行特定检查项**

```prowler m365 --checks [conditional_access_policies]```

**按合规框架运行**

```prowler m365 --compliance [cis_2.0_m365]```

# SYNOPSIS

**prowler m365** [_options_]

# PARAMETERS

**--checks** _checks_
> 要运行的特定检查项。

**--services** _services_
> 要检查的服务。

**--compliance** _framework_
> 合规框架。

**-M**, **--output-modes** _format_
> 输出格式。

**-o**, **--output-directory** _dir_
> 输出目录。

# DESCRIPTION

**prowler m365** 对 Microsoft 365 租户执行安全评估。它依据安全最佳实践检查 Entra ID、Exchange、SharePoint 和 Teams 的配置。

# INSTALL

```brew: brew install prowler```

```nix: nix profile install nixpkgs#prowler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[prowler](/man/prowler)(1)
