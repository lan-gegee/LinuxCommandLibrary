# TAGLINE

删除本地存储的 Terraform 凭据

# TLDR

从 HCP Terraform **登出**（默认）

```terraform logout```

从指定的 **Terraform Enterprise** 实例**登出**

```terraform logout [hostname]```

# SYNOPSIS

**terraform logout** [_hostname_]

# PARAMETERS

**hostname**
> 要登出的 Terraform 服务主机名。默认为 **app.terraform.io**（HCP Terraform）。对于 Terraform Enterprise，请指定你组织的主机名

# DESCRIPTION

**terraform logout** 删除本地存储的、针对指定远程服务主机的 API 凭据。这些凭据通常是在运行 **terraform login** 后保存的。该命令支持 HCP Terraform、Terraform Enterprise 以及任何提供 Terraform 服务的主机。

使用默认凭据文件时，它会从 **~/.terraform.d/credentials.tfrc.json** 中移除指定主机名的令牌。如果配置了**凭据助手**（credentials helper），Terraform 会调用助手的 **forget** 命令从外部系统中移除凭据。

# CAVEATS

API 令牌**仅从本地存储中移除**。它**不会**在远程服务器上被吊销。令牌在你通过服务的 Web UI 或 API 手动吊销之前仍然有效。出于安全考虑，本地登出后务必在远程服务上吊销令牌。

# HISTORY

于 **2020** 年初随 **Terraform v0.12.21** 与 **terraform login** 一同推出，用于简化 Terraform Cloud 和 Enterprise 连接的凭据管理。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-login](/man/terraform-login)(1)
