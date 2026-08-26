# TAGLINE

移除 Azure CLI 的身份验证凭证

# TLDR

**登出**当前用户

```az logout```

登出**特定用户**

```az logout --username [user@example.com]```

# SYNOPSIS

**az logout** [_options_]

# DESCRIPTION

**az logout** 登出并移除对 Azure 订阅的访问。它会从本地凭证缓存中清除该账户的访问令牌和刷新令牌。

在切换账户或保护共享系统时，此命令很有用。

# PARAMETERS

**--username** _user_
> 要登出的账户用户。若未指定，则登出当前活动账户。

# WORKFLOW

```bash
# Logout current account
az logout

# Login with different account
az login
```

# CAVEATS

不会在 Azure 端吊销令牌，只移除本地缓存。环境变量中的服务主体凭证不受影响。托管标识的身份验证仍然保留。

# HISTORY

**az logout** 自 **2017** 年的 Azure CLI 2.0 起可用，作为 az login 的配套命令用于凭证管理。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az-login](/man/az-login)(1), [az-account](/man/az-account)(1), [az](/man/az)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-logout)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

<!-- verified: 2026-06-19 -->
