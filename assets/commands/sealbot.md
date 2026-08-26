# TAGLINE

使用 Let's Seal（SEAL）标准封存并验证文档

# TLDR

**封存**文件（PDF 或其他）

```sealbot seal [contract.pdf]```

离线**验证**已封存的文件

```sealbot verify [contract.sealed.pdf]```

通过 **npm** 安装

```npm i -g sealbot```

通过 **npx** 免安装运行

```npx sealbot seal [file]```

# SYNOPSIS

**sealbot** {_seal_|_verify_|_issue_|_anchor_|_watch_} [_options_] [_file_]

# PARAMETERS

**seal** _file_
> 通过 Let's Seal API 或自托管服务封存 PDF 或其他文件

**verify** _file_
> 离线验证封印（完整性、签发者、时间锚点）

**issue**
> 与签发相关的封存操作（见 `sealbot --help`）

**anchor**
> 锚定相关证明（例如时间锚定工作流）

**watch**
> 用于封存工作流的监视/自动化模式

# DESCRIPTION

**sealbot** 是 **Let's Seal** 的命令行客户端。Let's Seal 是一项开放标准（SEAL — Sealed Evidence Anchored to a Ledger），用于证明文件未被篡改、由已知证书封存、且在某个日期之前就已存在。封印尽可能使用格式原生机制（PDF 用 PAdES，媒体用 C2PA，任意文件用分离式 CMS），并且验证时无需永远信任单一厂商。

使用 `npm i -g sealbot` 安装，或运行 `npx sealbot`。上游 `cli-rs/` 目录中还提供独立的 Rust 构建。托管封存使用组织 API 密钥；验证是免费的，一旦获得信任根和证明即可离线完成。

# CAVEATS

通过托管服务封存需要网络访问和凭据。验证需要固定（pin）的信任根才能给出完整的真实性判定。格式支持程度不一（PDF、图像、XML、电子邮件、分离式签名）。

# HISTORY

属于 **Let's Seal** 开源项目（Apache-2.0），仿照免费公共证书基础设施的模式来保障文档真实性。

# SEE ALSO

[openssl](/man/openssl)(1), [ots](/man/ots)(1)

# RESOURCES

```[Source code](https://github.com/letsseal/letsseal)```

```[Homepage](https://letsseal.org)```

```[Documentation](https://letsseal.org)```

<!-- verified: 2026-07-28 -->
