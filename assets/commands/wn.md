# TAGLINE

WordNet 词汇数据库的命令行接口

# TLDR

**查询名词的同义词**

```wn [word] -synsn```

**显示名词的上位词树**（更宽泛的类别）

```wn [word] -hypen```

**查找形容词的反义词**

```wn [word] -antsa```

**显示单词所有义项的概览**

```wn [word] -over```

**显示名词的释义**（gloss）

```wn [word] -g -synsn```

**查找名词的下位词**（更具体的类别）

```wn [word] -hypon```

**搜索包含某字符串的复合词**

```wn [word] -grepn```

# SYNOPSIS

**wn** _searchstr_ [_-h_] [_-g_] [_-a_] [_-l_] [_-o_] [_-s_] [_-n#_] _search_option ..._

# PARAMETERS

**-g**
> 显示文本释义（定义）

**-s**
> 在输出中显示义项编号

**-o**
> 显示 synset 偏移量编号

**-a**
> 显示与搜索字符串相关的所有 synset

**-n** _#_
> 将结果限定为特定的义项编号

**-h**
> 显示帮助文本

**-l**
> 显示许可与版权信息

# DESCRIPTION

**wn** 提供 **WordNet** 词汇数据库的命令行接口，以格式化的文本形式显示 synset（同义词集合）和语义关系。对于每个单词，可根据句法类别（名词、动词、形容词、副词）和关系类型进行不同的搜索。

搜索选项以表示词性的字母结尾：**n** 表示名词，**v** 表示动词，**a** 表示形容词，**r** 表示副词。多个搜索可以在一条命令中组合使用。

该工具会自动执行形态学分析，因此屈折变化形式（如 "running"）会被解析为其基本形式。

# SEARCH OPTIONS

**-syns**(n|v|a|r)
> 显示匹配 synset 的同义词及其直接上位词

**-ants**(n|v|a|r)
> 显示直接反义词（对立词）

**-hype**(n|v)
> 递归显示上位词树（更宽泛的类别）

**-hypo**(n|v)
> 显示直接下位词（更具体的类别）

**-tree**(n|v)
> 显示从属层级树

**-deri**(n|v)
> 显示形态上相关的词形

**-over**
> 显示跨所有词性的全部义项概览

**-grep**(n|v|a|r)
> 列出包含搜索字符串的复合词

**-sims**v
> 按语义相似度对动词义项分组

# CAVEATS

WordNet 最后一次普林斯顿官方发布是在 **2011 年**，因此对新词汇的覆盖有限。该数据库仅支持英语。结果按使用频率排序，可能无法反映特定专业领域的用法。

# HISTORY

**WordNet** 于 **1985 年**在**普林斯顿大学**认知科学实验室创建，由心理学家 **George Armitage Miller** 领导。后来在 **Christiane Fellbaum** 的主持下，该项目获得了 **2006 年 Antonio Zampolli 奖**。项目最初由美国海军研究办公室资助，后来由 DARPA 和 NSF 资助。

# INSTALL

```apt: sudo apt install wordnet```

```dnf: sudo dnf install wordnet```

```zypper: sudo zypper install wordnet```

```brew: brew install wordnet```

```nix: nix profile install nixpkgs#wordnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dict](/man/dict)(1), [aspell](/man/aspell)(1), [grep](/man/grep)(1)
