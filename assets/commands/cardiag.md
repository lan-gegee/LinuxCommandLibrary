# TAGLINE

通过声音录音诊断汽车故障的音频机器学习流水线

# TLDR

**检查前置条件**和环境

```cardiag doctor```

**使用内置样例数据训练模型**（无需外部数据）

```cardiag train --fixtures```

**诊断一段音频**并获得故障判定、部位区域和排序后的疑似零件列表

```cardiag diagnose clip.wav```

**运行 Web UI**进行交互式分析

```cardiag serve --model models```

**从嘈杂录音中分离机械声音**（不需要模型）

```cardiag clean clip.wav```

**粗判是发动机还是行走机构的问题**

```cardiag triage clip.wav```

# SYNOPSIS

**cardiag** {doctor,train,diagnose,triage,clean,inspect,ingest,scrape,serve,...} [options] [args]

# DESCRIPTION

**cardiag** 是一条端到端的音频机器学习流水线，用于从音频录音（如手机片段或抓取的社交媒体内容）中初步判断机械故障。它会分离出相关的机械声音片段，用冻结的 CLAP 模型生成嵌入向量，然后应用小型校准过的线性分类器。

该工具报告：

- 声音是否有异常（故障 vs 正常）
- 汽车上大致的位置（6 个区域）
- 排序后的疑似零件候选列表（12+ 个类别）
- 当输入不足以支撑可信判断时给出诚实的 `UNCERTAIN`

它明确是一个**辅助初判工具**，不是安全关键或决定性的诊断手段。所有指标都是诚实统计的（按视频分组的交叉验证），且整条流水线设计为可审查。

# INSTALLATION

从仓库安装：

```bash
git clone https://github.com/adam-s/car-diagnosis
cd car-diagnosis
uv venv && source .venv/bin/activate
uv pip install -e ".[scrape,web,dev,viz]"
```

需要 Python 3.11+，（若要完整使用）还需额外的可选依赖。播放/可视化部分是可选的。

# USAGE

运行 `cardiag --help` 或 `cardiag <subcommand> --help` 查看详情。

处理新录音片段的常见工作流：

1. `cardiag doctor`
2. `cardiag diagnose my-recording.wav --json`
3. `cardiag inspect my-recording.wav -o report.html`（可视化 + 音频区间）

用你自己的数据训练：

- `cardiag ingest ./my_clips --kind fault --cause wheel_bearing`
- `cardiag scrape youtube|tiktok ...`
- `cardiag train`

`serve` 子命令启动本地 Web UI，支持拖拽上传或基于 URL 的分析。在推理命令中添加 `--json` 可获得机器可读的输出。

# CAVEATS

- 对粗糙的手机/社交媒体音频表现有限（受该问题文献中的上限约束）。在诚实的评估下，故障/正常判断约为 ~0.79 AUROC，top-3 零件准确率为 45-65 %。
- 模型是 joblib 工件；只加载你信任的模型。
- 不能替代专业诊断。

# RESOURCES

```[Source code](https://github.com/adam-s/car-diagnosis)```

```[Documentation](https://github.com/adam-s/car-diagnosis/blob/main/docs/MODEL_CARD.md)```

<!-- verified: 2026-07-11 -->
