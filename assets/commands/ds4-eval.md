# TAGLINE

DwarfStar 模型输出的质量评估工具

# TLDR

**运行前 N 道内置评估题**

```ds4-eval --questions [10] --ctx [100000]```

**禁用思考并限制生成长度**

```ds4-eval --plain --nothink --tokens [512]```

**写出完整评估轨迹**

```ds4-eval --questions [10] --trace [eval.trace]```

无需重新加载模型即可**重新评分既有轨迹**

```ds4-eval --regrade-trace [eval.trace]```

对单道题做 **CPU 诊断**

```ds4-eval --cpu --questions [1] --tokens [32]```

按顺序**运行指定的用例编号**

```ds4-eval --case-sequence [1,3,5] --ctx [100000]```

# SYNOPSIS

**ds4-eval** [_options_]

# PARAMETERS

**-m**, **--model** _FILE_
> GGUF 模型路径。默认：**ds4flash.gguf**。

**-c**, **--ctx** _N_
> 分配的上下文长度（以 token 计）。

**-n**, **--tokens** _N_
> 每道题的最大生成 token 数。

**--questions** _N_
> 只运行前 _N_ 道内嵌评估题。

**--case-sequence** _LIST_
> 以逗号分隔的用例编号（从 1 开始），按给定顺序运行。

**--trace** _FILE_
> 写出详细的评估轨迹。

**--regrade-trace** _FILE_
> 对先前的轨迹重新评分，而不再加载模型。

**--plain**
> 禁用分屏 ANSI 界面。

**--think** / **--think-max** / **--nothink**
> 控制回答时的思考/推理模式。

**--metal** | **--cuda** | **--rocm** | **--cpu**
> 显式选择推理后端。

**--power** _N_
> GPU 占空比目标，取值 1 到 100。

**--pause-ms** _N_
> TTY 界面中每条结果后的暂停时间。默认：**350**。

**--self-test-extractors**
> 运行答案抽取器自测后退出。

# DESCRIPTION

**ds4-eval** 是 **DwarfStar**（**ds4**）的质量评估工具。它对已加载的 GGUF 运行一组内置问题，抽取答案并评分，让贡献者在修改内核、量化方案或采样默认值时能够发现回归。

与测速度的 **ds4-bench** 不同，**ds4-eval** 关注正确性与答案质量。轨迹可以保存，之后用 **--regrade-trace** 重新评分——在迭代评分逻辑时不必再付一次完整推理的成本，非常实用。plain 模式去掉 ANSI 界面，便于在 CI 或远程会话中记录日志。

# CAVEATS

需要 DwarfStar 兼容的 GGUF 才能得到有意义的分数。内嵌用例和抽取器是项目专属的，并非通用 LLM 排行榜。CPU 模式很慢，仅用于诊断。思考模式和上下文大小会显著影响质量与运行时间。

# HISTORY

**ds4-eval** 由 **Salvatore Sanfilippo**（**antirez**）及其他贡献者开发的 **DwarfStar** 附带发布，体现了该项目在速度基准之外对官方向量校验和回归测试的重视。

# SEE ALSO

[ds4-bench](/man/ds4-bench)(1), [ds4-server](/man/ds4-server)(1), [ds4-agent](/man/ds4-agent)(1), [llama-cli](/man/llama-cli)(1)

# RESOURCES

```[Source code](https://github.com/antirez/ds4)```

```[Documentation](https://github.com/antirez/ds4/blob/main/docs/ENGINE_REFERENCE.md)```

<!-- verified: 2026-07-18 -->
