# TAGLINE

用于分布式 LLM 推理的点对点 MoE 模型集群

# TLDR

在集群上**服务**本地模型目录（tracker + 字节数据 + 可选的专家计算）

```lumabri serve --model [/path/to/model]```

**对话**：连接到 tracker，使用来自本地目录树的 colibri 引擎二进制文件

```lumabri chat --tracker [host:7300] --engines-dir [/path/to/colibri/c]```

以**保存的集群设置**打开交互式前端（不带任何标志）

```lumabri```

为签名集群生成**操作员密钥对**

```lumabri key --out [swarm]```

提供服务并**加入**现有 tracker，同时捐出磁盘空间

```lumabri serve --model [./slice] --join [host:7300] --model-name [model] --donate [GB]```

针对**本地**模型目录对话（无需镜像，也无需第二份副本）

```lumabri chat --local [/path/to/model] --engines-dir [/path/to/colibri/c]```

# SYNOPSIS

**lumabri** [_subcommand_] [_options_]

# DESCRIPTION

**lumabri** 使用 [colibri](https://github.com/JustVugg/colibri) 引擎在对等节点集群上运行超大规模混合专家（MoE）语言模型。纯 C 实现，除引擎二进制所需的 colibri 构建外没有其他运行时依赖。一台机器可以共享模型；其他机器无需预先下载完整权重即可对话。推理实际触及的字节会从对等节点获取、校验，并保存在 **~/.lumabri** 下的本地镜像中，以便后续提示词可以离线从缓存运行。

**serve** 启动一个 tracker（记录谁持有哪些文件的索引）和一个响应字节范围读取的维护进程。启用 phase 2 后，它还可以为其他对等节点执行专家计算。**chat** 针对一个可能只存在于集群上的模型路径启动 colibri 引擎：一个 **LD_PRELOAD** shim 会获取缺失的块，可选的专家卸载会把激活值发送给持有相应专家的对等节点。不带参数时，**lumabri** 只询问一次集群地址和密钥，并将其记住在 **~/.lumabri/config** 中。

完整性模式包括开放集群（逐 MiB 哈希、可选的操作员签名、对专家结果的抽查）和由 **LUMABRI_TOKEN** 把关的私有集群。设计目标强调无论专家在本地还是远程执行，输出都逐字节一致，并且硬件门槛包含纯 CPU 机器。

# SUBCOMMANDS

**serve**

> 共享模型：运行 tracker/维护进程（通常还有专家执行）。标志包括 **--model**、**--port**、**--join**、**--donate**、**--model-name**、**--key**、**--advertise**、**--cache** / **--exec-cache**、**--no-exec**。

**chat**

> 连接到集群或本地模型。标志包括 **--tracker**、**--engines-dir**、**--local**、**--role**、**--donate**、**--model-dir**。聊天内命令包括 **/swarm** 和 **/model**。

**key**

> 创建 Ed25519 操作员密钥对（**--out** 路径），用于签名的集群。

# ENVIRONMENT

**LUMABRI_TOKEN**

> 私有集群的共享邀请密钥；设置后每个节点都必须提供。

**LUMABRI_PUBKEY**

> 用于带外验证已签名模型哈希的操作员公钥（十六进制）。

**LUMABRI_REQUIRE_HASH**

> 设为 1 时，拒绝没有完整性数据的获取请求。

**LUMABRI_VERIFY**

> 对第二副本上 phase-2 专家结果进行抽查的比例。

**LUMABRI_PREFETCH**

> 冷镜像的预读块数量（默认 2）。

# CAVEATS

需要 **Linux**、**gcc**、**GNU make** 以及一个匹配的 **colibri** 源码检出来构建引擎二进制（对等专家执行使用 **make phase2-all ENGINE=...**）。首次冷启动的回答受网络限制，因为工作集正在镜像。配置错误的 **--engines-dir** 或缺失的密钥可能导致巨大的下载量或未验证的模型；交互式默认路径有意比原始标志更安全。多主机集群必须保证 tracker/维护进程/执行器端口可达（通常是 **7300–7302**，外加每个额外模型的偏移量）。目前仍是可工作的原型：投机起草和密钥轮换等特性尚未完成。

# SEE ALSO

[ollama](/man/ollama)(1), [llama.cpp](/man/llama-cli)(1)

# RESOURCES

```[Source code](https://github.com/JustVugg/lumabri)```

<!-- verified: 2026-08-10 -->
