# TAGLINE

tpm2-tools 工具集的统一分发器

# TLDR

**列出所有可用的** TPM2 子命令

```tpm2 --help```

从 TPM **获取 8 个随机字节**

```tpm2 getrandom 8 | xxd -p```

启动后**初始化 TPM**

```tpm2 startup -c```

读取 SHA-256 bank 的 **PCR 值**

```tpm2 pcrread sha256:all```

用预计算的哈希**扩展 PCR**

```tpm2 pcrextend [index]:sha256=[hexdigest]```

**重置可重置的 PCR**（通常为索引 16 或 23）

```tpm2 pcrreset [index]```

在所有者层级下**创建主密钥**

```tpm2 createprimary -C o -c primary.ctx```

**使用指定的 TCTI**（例如模拟器）

```tpm2 --tcti=mssim getrandom 8```

# SYNOPSIS

**tpm2** _tool_ [_options_] [_arguments_]

**tpm2_**_tool_ [_options_] [_arguments_]

# DESCRIPTION

**tpm2** 是一个 busybox 风格的单体可执行文件，将所有独立的 **tpm2-tools** 工具合并为一个二进制文件。每个历史上的工具（如 **tpm2_getrandom** 或 **tpm2_pcrread**）既可作为 **tpm2** 的子命令使用（调用 **tpm2 getrandom**），也可通过原始名称的符号链接调用。

该分发器的存在主要是为了在空间受限的系统（initramfs 镜像、嵌入式设备、恢复环境）上缩减 **tpm2-tools** 的占用，因为在这些环境中附带数十个独立的二进制文件非常浪费。由于每个 _tpm2_<tool>_ 符号链接都指向同一个二进制文件，两种调用方式的行为完全一致。

这些工具覆盖了完整的 TPM 2.0 命令面：密钥创建与加载、NV 存储、PCR 操作、会话与策略管理、证明（attestation）以及审计。

# COMMON OPTIONS

**-h**, **--help**[=_man_|_no-man_]
> 显示所选工具的帮助页。使用 **=man** 时通过 **man** 渲染手册页；使用 **=no-man** 时打印纯文本摘要。

**-v**, **--version**
> 打印 **tpm2-tools** 的版本信息。

**-V**, **--verbose**
> 增加控制台输出；便于调试。

**-Q**, **--quiet**
> 抑制常规信息输出。

**-Z**, **--enable-errata**
> 对已知的 TPM 缺陷应用勘误规避措施。

**-T** _tcti_, **--tcti=**_tcti_
> 选择用于与 TPM 通信的 TCTI（传输接口配置）。

**-R**, **--autoflush**
> 工具退出时自动从 TPM 中清除（flush）临时对象。

# SUBCOMMAND CATEGORIES

**Entropy / hashing**: getrandom, hash, hmac, stirrandom
**Keys**: create, createprimary, createak, createek, load, loadexternal, import, evictcontrol
**PCRs**: pcrread, pcrextend, pcrevent, pcrreset, pcrallocate
**NV storage**: nvdefine, nvread, nvwrite, nvextend, nvundefine
**Sessions & policy**: startauthsession, policypcr, policysigned, policypassword, policyauthvalue
**Attestation**: quote, certify, activatecredential, makecredential
**Signing / encryption**: sign, verifysignature, rsaencrypt, rsadecrypt, encryptdecrypt
**Hierarchies**: clear, changeauth, dictionarylockout, hierarchycontrol

# TCTI SELECTION

与 TPM 的通信由 **TCTI** 抽象。选择优先级：

1. 命令行上的 **-T** / **--tcti**
2. **TPM2TOOLS_TCTI** 环境变量
3. 编译时默认值

常见的 TCTI：

```
tabrmd   Resource manager (tpm2-abrmd)
device   Direct /dev/tpm0 or /dev/tpmrm0
mssim    Microsoft TPM simulator (TCP)
swtpm    libtpms-based software TPM
none     Offline mode (no TPM required)
```

# EXIT CODES

**0**
> 成功。

**1**
> 一般工具错误。

**2**
> 选项解析错误。

**3**
> 身份验证失败。

**4**
> TCTI 通信错误。

**5**
> 不支持的方案或算法。

# CAVEATS

并非每个 TPM 都向用户空间开放所有层级或 PCR：通常只有 PCR 16 和 23 可以在 locality 0 下重置，且某些操作需要所有者密码或有效会话。在使用 **tpm2-abrmd** 的系统上，资源管理器运行期间会阻止直接访问 **device**。编写脚本时优先使用 **tpm2 _tool_** 形式：即使在没有附带各工具符号链接的最小安装中也能工作。

# HISTORY

**tpm2-tools** 项目由 **tpm2-software** 社区维护，在 **tpm2-tss** 栈之上实现了 **TCG TPM 2.0** 规范的用户空间部分。引入统一的 **tpm2** 分发器是为了简化受限环境下的打包；原始的按工具调用方式（**tpm2_**_tool_）仍然受支持，并且在大多数发行版上仍是主要接口。

# INSTALL

```apt: sudo apt install tpm2-tools```

```dnf: sudo dnf install tpm2-tools```

```pacman: sudo pacman -S tpm2-tools```

```apk: sudo apk add tpm2-tools```

```nix: nix profile install nixpkgs#tpm2-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO
