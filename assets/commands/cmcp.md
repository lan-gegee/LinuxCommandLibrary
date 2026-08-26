# TAGLINE

基于 TEE 强制执行策略的机密 MCP 网关

# TLDR

**安装**运行时

```pip install cmcp-runtime```

启动前**校验**配置与策略包

```cmcp validate-config --config cmcp-config.yaml```

```cmcp validate-bundle --bundle-path ./policies --expected-hash sha256:[hex]```

以软件/开发模式启动网关（无硬件 TEE）

```CMCP_DEV_MODE=1 cmcp start --config cmcp-config.yaml```

**验证**已签名的 TRACE 声明文件

```cmcp verify claim.json```

使用固定的策略与目录哈希进行**验证**

```cmcp verify claim.json --policy-hash sha256:[hex] --catalog-hash sha256:[hex]```

# SYNOPSIS

**cmcp** _command_ [_options_]

# PARAMETERS

**start** **--config** _path_
> 使用给定的 YAML 配置启动 cMCP 网关。监听 MCP 风格的工具调用，将每个调用交由 Cedar 策略包评估，并记录由硬件封存（开发模式下为软件签名）的审计链。

**validate-config** **--config** _path_
> 解析并校验 **cmcp-config.yaml**，但不启动服务器。

**validate-bundle** **--bundle-path** _path_ **--expected-hash** **sha256:**_hex_
> 在部署前验证 Cedar 策略包目录是否与预期的 SHA-256 匹配。

**verify** _claim_file_ [**--policy-hash** _h_] [**--catalog-hash** _h_] [**--max-age** _s_] [**--trusted-key** _path_] [**--audit-bundle** _path_] ...
> 对 TRACE / GatewayClaim 进行离线验证：签名、模式、新鲜度、审计链以及可选的固定哈希。不需要信任生成该声明的运营者。

# DESCRIPTION

**cmcp** 是 **cMCP（Confidential MCP Runtime）** 的 CLI，后者是一个位于 AI 智能体与 MCP 工具之间的开源网关。每一次 **tools/call** 都会被拦截，并在一个预期运行于**可信执行环境（TEE）**内的策略引擎中依据 **Cedar** 策略包进行评估，然后被允许、拒绝或脱敏。会话会发出签名的 **TRACE Claim**（GatewayClaim），记录哪些工具运行过、哪个策略决定了每次调用、启动时测量的策略包哈希，以及一条哈希链式审计日志。

支持的证明提供方包括 **TPM 2.0 / vTPM**、**AMD SEV-SNP** 和 **Intel TDX**（NVIDIA GPU 机密计算已在路线图中）。当没有硬件 TEE 时，**CMCP_DEV_MODE=1** 可启用纯软件提供方供本地开发使用；生产环境启动时应省略该标志，这样网关在没有证明硬件的情况下将拒绝运行。

典型配置（**cmcp-config.yaml**）设置 **attestation.provider**（**auto** 或特定提供方）、**enforcement_mode**（**enforcing**、**advisory** 或 **silent**）、**policy_bundle_path**、**catalog_path** 和 **listen_addr**。智能体将 JSON-RPC 工具调用发送到网关的 HTTP 端点，而不是直接发送到上游 MCP 服务器。

# CONFIGURATION

**cmcp-config.yaml**（**start** 和 **validate-config** 所需的路径）。重要键：**attestation.provider**、**attestation.enforcement_mode**、**policy_bundle_path**（**.cedar** 文件加 **manifest.json** 所在目录）、**catalog_path**（已批准工具目录 JSON）、**listen_addr**。

环境变量：

- **CMCP_DEV_MODE=1** — 纯软件 TEE；无需硬件
- **CMCP_BEARER_TOKEN** — 要求入站请求携带此 bearer token（在无 token 设置中，回环地址之外必须配置）
- **OPAQUE_ATTESTATION_URL** — 可选启用的 OPAQUE 托管运行时（占位 / 未完全实现）

# CAVEATS

开发者预览版：API 与声明结构在 1.0 之前可能变化。**CMCP_DEV_MODE** 生成的声明只能验证为 partially_verified（无硬件证明）。强制模式默认为 **enforcing**（拒绝时返回 HTTP 403）。不带 bearer token 运行仅适用于回环地址。需要 **Python 3.11+**。残余风险与范围限制记录在项目的 **LIMITATIONS.md** 中。

# HISTORY

**cMCP** 由 **AgenTrust** 以 MIT 许可证维护。它在机密计算峰会（2026 年）前后作为开发者预览版发布，PyPI 软件包名为 **cmcp-runtime**。

# SEE ALSO

[curl](/man/curl)(1), [pip](/man/pip)(1)

# RESOURCES

```[Source code](https://github.com/agentrust-io/cmcp)```

```[Homepage](https://github.com/agentrust-io/cmcp)```

```[Documentation](https://github.com/agentrust-io/cmcp/tree/main/docs)```

<!-- verified: 2026-08-04 -->
