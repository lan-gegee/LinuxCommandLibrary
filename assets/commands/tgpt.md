# TAGLINE

终端 AI 聊天机器人客户端

# TLDR

**提问**

```tgpt "[What is Linux?]"```

**交互模式**

```tgpt -i```

**代码模式**

```tgpt -c "[Write a Python hello world]"```

**多行输入**

```tgpt -m```

**使用指定提供商**

```tgpt --provider [openai] "[question]"```

**生成图像**

```tgpt -img "[A sunset over mountains]"```

# SYNOPSIS

**tgpt** [_-i_] [_-c_] [_--provider name_] [_options_] [_prompt_]

# PARAMETERS

**-i**
> 交互模式。

**-c**
> 代码生成。

**-m**
> 多行输入。

**--provider** _NAME_
> AI 提供商。

**-img**
> 图像生成。

**-s**
> 静默模式。

# DESCRIPTION

**tgpt** 是一款基于终端的客户端，用于与 OpenAI、Anthropic 等多家提供商的 AI 语言模型交互。它支持一次性提问、交互式对话模式（**-i**），以及专门的代码生成模式（**-c**）。

该工具还可以通过 **-img** 标志使用 DALL-E 等模型生成图像。部分提供商无需 API 密钥即可使用，另一些则需要配置密钥进行身份验证。多行输入模式（**-m**）允许直接在终端中编写较长的提示词。

# CAVEATS

可能需要 API 密钥。需要网络。功能因提供商而异。

# HISTORY

**tgpt** 的创建初衷是为各种 AI 语言模型提供基于终端的界面，且部分提供商无需 API 密钥即可使用。

# INSTALL

```pacman: sudo pacman -S tgpt```

```brew: brew install tgpt```

```nix: nix profile install nixpkgs#tgpt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chatgpt-cli](/man/chatgpt-cli)(1), [sgpt](/man/sgpt)(1)
