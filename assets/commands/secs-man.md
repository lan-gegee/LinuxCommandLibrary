# TAGLINE

使用可互操作的 age 归档加密并备份机密

# TLDR

**导出**并加密清单中列出的所有机密

```sudo secs-man export [path/to/secrets] [path/to/export/endpoint]```

将最新的加密快照**导入**回机密目录

```sudo secs-man import [path/to/export/endpoint] [path/to/secrets]```

按名称**导入**特定快照

```sudo secs-man import [path/to/export/endpoint]/export-[YYYY-MM-DD_HH-MM-SSZ] [path/to/secrets]```

仅**导入**快照中选定的机密

```sudo secs-man import [path/to/export/endpoint] [path/to/secrets] --pick [ssh/id_ed25519] [wg/wg0.key]```

**验证**所有已导出快照的完整性

```sudo secs-man verify-export [path/to/export/endpoint]```

# SYNOPSIS

**secs-man** _subcommand_ [_options_] [_paths_]

# PARAMETERS

**export** _secrets-dir_ _export-endpoint_
> 使用 **age** 加密 _secrets-dir_ 下 `.secrets-manifest` 中列出的每个文件，并将带时间戳的快照写入 _export-endpoint_。密码通过交互式提示输入。

**import** _export-endpoint_ _secrets-dir_
> 从最新快照（或指定的快照路径）解密并恢复机密到 _secrets-dir_，并按清单应用属主和权限。

**verify-export** _export-endpoint_
> 检查 _export-endpoint_ 下某个或全部快照中每个文件的 SHA-256 校验和。

**--pick** _paths..._
> 导入时只恢复列出的相对于清单的路径。

**--from-plaintext** / **--skip-chown-chmod**
> 由配套脚本 **secs-man-ssh** 在远程工作流中使用的高级标志。

# DESCRIPTION

**secs-man** 是一款专注于**工具无关备份**的命令行机密管理器。文件在导出和导入时用你输入的密码通过 **age** 加密；该工具绝不会从文件、参数或环境变量中读取密码。每次导出都会创建一个带时间戳的快照，包含以 `.age` 为后缀的密文文件以及配套的 **sha256sums** 清单。

机密目录根目录下的明文 **.secrets-manifest** 列出了要管理的路径。每个条目可以指定在导入时应用的 **owner** 和 **mode** 权限。其设计目标是不依赖 secs-man 本身也能恢复：解密和恢复可以只用 **age**、**cp**、**chmod** 和 **chown** 手动复现。

可选的 **secs-man-ssh** shell 脚本（单独随仓库提供）可通过 SSH 从远程主机导出或向其导入，而无需将密码传经远程机器。

# CONFIGURATION

**.secrets-manifest** — 位于机密根目录的明文文件，列出受管理的路径（相对路径）、可选的 owner 和可选的 mode。语法参见上游的 `.secrets-manifest.example`。文件路径不能包含空白字符。

# CAVEATS

未发布到 crates.io、nixpkgs 或发行版仓库；请通过 **cargo install --git**、**nix run** 或 Nix flake 安装。当清单指定的属主不是调用者本人时需要 **sudo**。导出的快照从不自动删除——备份解密所需的机密（磁盘密钥、age 身份）时，请手动轮换或删除旧快照。每次导出时都会自动运行完整性检查；**verify-export** 用于审计较旧的快照。

# HISTORY

**secs-man** 由 **Fran314** 用 **Rust** 编写，以 **secrets-manager-rs** 之名按 **AGPL-3.0** 许可证发布，强调通过标准的 **age** 加密而非专有格式来保证长期可访问性。

# SEE ALSO

[age](/man/age)(1), [sha256sum](/man/sha256sum)(1)

# RESOURCES

```[Source code](https://github.com/Fran314/secrets-manager-rs)```

<!-- verified: 2026-06-28 -->
