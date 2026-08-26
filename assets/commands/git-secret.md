# TAGLINE

加密并在 Git 仓库中存储机密

# TLDR

**初始化 git-secret**

```git secret init```

**按邮箱添加用户**

```git secret tell [user@email.com]```

**添加要加密的文件**

```git secret add [secret.txt]```

**加密机密**

```git secret hide```

**解密机密**

```git secret reveal```

**列出可访问机密的用户**

```git secret whoknows```

**解密单个文件并输出到 stdout**

```git secret cat [secret.txt]```

# SYNOPSIS

**git secret** _command_ [_options_]

# PARAMETERS

**init**
> 在仓库中初始化 git-secret。

**tell** _EMAIL_
> 添加一个可解密机密的 GPG 密钥持有者。使用 **-m** 表示采用 git config 中的 user.email。

**add** _FILE_
> 添加要加密的文件。明文文件会自动加入 .gitignore。

**hide**
> 加密所有已添加的机密文件。使用 **-m** 可在加密后删除明文。

**reveal**
> 解密所有机密文件。使用 **-p** _PASSWORD_ 可以非交互式地输入密码短语。

**remove** _FILE_
> 从机密文件列表中移除某个文件。

**list**
> 列出所有机密文件。

**whoknows**
> 列出有权访问机密的用户。

**changes** _FILE_
> 显示文件明文与解密版本之间的差异。

**cat** _FILE_
> 解密单个机密文件并打印到 stdout。

**removeperson** _EMAIL_
> 将某人从机密访问列表中移除。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git secret** 对敏感文件进行加密，以便安全地存放在 Git 仓库中。文件会用 GPG 针对指定接收者加密，从而可以安全地对机密做版本控制。

该工具管理加密、解密和接收者列表。被 Git 跟踪的是加密后的文件（`.secret`），而原始明文文件会被自动加入 `.gitignore`。

# CONFIGURATION

**.gitsecret/**
> 存放 git-secret 配置、钥匙环和文件映射的目录。

# ENVIRONMENT

**SECRETS_VERBOSE**
> 设置 verbose 标志，为所有命令显示额外输出。

**SECRETS_GPG_COMMAND**
> 指定 gpg 的替代命令（默认：gpg）。

**SECRETS_GPG_ARMOR**
> 启用 gpg --armor 模式，以 ASCII 封装格式输出。

# CAVEATS

需要 GPG。接收者必须持有 GPG 密钥。它与 **gh secret**（GitHub CLI 的 secrets）是不同的工具。

# HISTORY

git secret 的诞生是为了解决在 git 仓库中存放机密的问题，它用 GPG 加密来保护敏感配置。

# INSTALL

```dnf: sudo dnf install git-secret```

```brew: brew install git-secret```

```nix: nix profile install nixpkgs#git-secret```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [gh-secret](/man/gh-secret)(1), [git](/man/git)(1)
