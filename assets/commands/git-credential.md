# TAGLINE

为 Git 检索和存储身份验证凭据

# TLDR

**获取某个 URL 的凭据**

```echo "url=https://github.com" | git credential fill```

**将凭据存储到已配置的助手中**

```git credential approve << EOF
url=https://github.com
username=user
password=token
EOF```

**拒绝（擦除）已存储的凭据**

```git credential reject << EOF
url=https://github.com
username=user
password=token
EOF```

# SYNOPSIS

**git credential** _action_

# PARAMETERS

**fill**
> 从标准输入读取凭据属性，通过已配置的助手查找匹配的凭据，并输出包含用户名和密码的结果。

**approve**
> 将凭据属性发送给所有已配置的助手以进行存储。不产生输出。

**reject**
> 通知所有已配置的助手擦除匹配的凭据。不产生输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git credential** 是一个底层接口，通过 Git 的凭据助手系统存储和检索凭据。它与已配置的助手（cache、store、osxkeychain、manager 等）交互，完成凭据的检索、存储和擦除。

该命令通常在需要身份验证时由 Git 在 push/pull 操作期间自动调用。直接使用主要用于调试凭据问题或编写身份验证工作流脚本。输入和输出在 stdin/stdout 上使用 key=value 格式，属性包括 protocol、host、username 和 password。

凭据助手通过 **git config credential.helper** 配置。

# INPUT ATTRIBUTES

**protocol**
> 凭据将使用的协议（如 https、ssh）。

**host**
> 使用该凭据的远程主机名。

**username**
> 凭据的用户名（如果已知）。

**password**
> 凭据的密码（正在提供或返回时）。

**path**
> 使用该凭据的路径（例如访问远程 https 仓库时）。

# CAVEATS

通常由 Git 内部调用，而非用户直接调用。必须先通过 **git config** 配置好凭据助手，此命令才有用武之地。**reject** 操作需要提供与最初存储时相同的凭据属性。敏感凭据可能经由 stdin/stdout 暴露。

# HISTORY

git credential 子系统于 **Git 1.7.9**（2012 年）引入，用于在各助手之间统一凭据管理，取代了此前临时性的身份验证处理方式。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-config](/man/git-config)(1), [git-credential-store](/man/git-credential-store)(1), [git-credential-cache](/man/git-credential-cache)(1)
