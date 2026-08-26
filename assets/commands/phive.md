# TAGLINE

PHAR 安装与验证工具

# TLDR

从默认仓库**安装 PHAR 工具**

```phive install [phpunit]```

使用 `@` 语法**锁定特定版本**

```phive install [phpunit@^9.5]```

通过复制到共享目录实现**系统级安装**

```phive install --copy --target [/usr/local/bin] [phpunit]```

**显示已安装的工具和可用更新**

```phive status```

将所有已安装的工具**更新到最新锁定版本**

```phive update```

**列出哪些工具已过时**

```phive outdated```

**移除某个工具**

```phive remove [phpunit]```

**更新 Phive 自身**

```phive selfupdate```

# SYNOPSIS

**phive** _command_ [_options_]

# COMMANDS

**install** _TOOL_[**@**_VERSION_]
> 安装 PHAR 工具，可选地用版本约束锁定（如 **@^9.5**）。

**update** [_TOOL_...]
> 将一个或多个已安装工具更新到最新的兼容版本。

**remove** _TOOL_
> 卸载工具并删除其 PHAR。

**reset** [_TOOL_]
> 在不改变版本锁定的前提下重新下载工具。

**status**
> 列出已安装的工具以及与锁定版本的偏差。

**outdated**
> 报告有新版本可用的工具。

**list**
> 列出所配置仓库中已知的工具。

**purge**
> 从本地缓存中移除未使用的 PHAR。

**default**
> 显示或更改默认仓库配置。

**selfupdate**
> 将 Phive 工具自身更新到最新版本。

# PARAMETERS

**--copy**
> 将 PHAR 复制到目标位置而不是创建符号链接（共享/系统级安装需要此选项）。

**--target** _DIR_
> 将 PHAR 安装到 _DIR_。全局安装时请与 **--copy** 搭配使用（没有 **--global** 标志）。

**--force-accept-unsigned**
> 接受缺少有效 GPG 签名的 PHAR（不推荐）。

**--trust-gpg-keys** _KEYIDS_
> 预先信任指定的 GPG 密钥 ID，不再询问。

**--prefer-offline**
> 使用缓存的元数据（配合 **update** 很有用）。

**--help**
> 显示帮助。

# DESCRIPTION

**phive**，即 **PHAR Installation and Verification Environment**，管理以 PHAR 归档形式分发的 PHP 命令行工具。它从受信任的仓库下载 PHAR，验证其 GPG 签名，并将锁定的版本记录在项目本地的 **phive.xml** 中，以便可复现地重新安装。

典型用法是项目本地安装：**phive install phpunit** 会把该工具写入当前项目的 **tools/** 目录。系统级安装则需组合 **--copy** 和 **--target** 并指向 **$PATH** 中的目录。

# CAVEATS

需要带 **phar** 扩展的 PHP。GPG 用于校验 PHAR 签名；密钥缺失或不受信任会阻止安装，除非显式覆盖。工具必须发布到 Phive 注册表（或自定义仓库）才能按名称安装。

# HISTORY

Phive 为**安全的 phar 分发**而创建，支持签名验证。

# INSTALL

```brew: brew install phive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[composer](/man/composer)(1), [php](/man/php)(1)
