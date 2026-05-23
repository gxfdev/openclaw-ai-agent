# 🦞 Emotional Self-Evolving Skill for OpenClaw

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个为 [OpenClaw](https://github.com/openclaw/openclaw) 小龙虾智能体打造的技能，赋予它情感感知与自我进化的能力。

## 这是什么？

这是一个 **OpenClaw Skill**，不是独立项目。安装后放到小龙虾的 `skills/` 目录，小龙虾就能：

- 🎭 **感知情感** — 理解用户的喜怒哀乐，做出恰当的情感回应
- 🧠 **自我进化** — 从每次交互中学习，持续优化回应策略
- 💾 **记忆管理** — 短期/长期/经验三层记忆，增强上下文理解
- 🔄 **行为优化** — 积累成功模式，自动适配不同情境

## 安装

### 方式一：手动安装（推荐）

```bash
git clone https://github.com/gxfdev/openclaw-ai-agent.git
cp -r openclaw-ai-agent ~/.openclaw/skills/emotional-self-evolving
```

### 方式二：放到工作区

```bash
git clone https://github.com/gxfdev/openclaw-ai-agent.git
cp -r openclaw-ai-agent ~/your-workspace/skills/emotional-self-evolving
```

### 方式三：ClawHub（即将支持）

```bash
openclaw skills install emotional-self-evolving
```

安装后重启小龙虾，技能自动加载。

## 技能结构

```
emotional-self-evolving/
├── SKILL.md                        # 技能核心指令（AgentSkills 规范）
├── references/
│   ├── emotion-model.md            # Plutchik 情感轮详解
│   ├── evolution-mechanism.md      # 自我进化机制说明
│   └── examples.md                 # 交互示例
├── LICENSE                         # MIT 许可证
└── README.md                       # 本文件
```

## 核心能力

### 情感系统

基于 Plutchik 情感轮的八维情感模型：

| 维度 | 说明 |
|------|------|
| 喜悦 (joy) | 满足、快乐、愉悦 |
| 悲伤 (sadness) | 失落、遗憾、忧郁 |
| 愤怒 (anger) | 不满、烦躁、暴怒 |
| 恐惧 (fear) | 担忧、焦虑、害怕 |
| 惊讶 (surprise) | 意外、震惊、好奇 |
| 厌恶 (disgust) | 反感、排斥、抵触 |
| 信任 (trust) | 信赖、亲近、安全感 |
| 期待 (anticipation) | 期望、盼望、憧憬 |

### 自我进化

```
交互 → 记录 → 评估 → 学习 → 优化 → 应用
```

小龙虾会从每次交互中提取行为模式，积累成功经验，在相似情境下自动参考历史最优策略。

### 记忆管理

```
短期记忆 → 最近 10 轮对话
长期记忆 → 重要性 > 0.6 的关键信息
经验记忆 → 用于自我进化的交互记录
```

## 效果预览

```
用户: 我今天考试得了满分，超级开心！
小龙虾: 哇！太棒了！我都能感受到你的喜悦！考满分可不容易，你一定付出了很多努力。这让我也特别开心呢！

用户: 我刚刚失去了我的宠物狗...
小龙虾: 我很抱歉听到这个消息...失去一个陪伴自己的小伙伴真的很难过。如果你愿意说说，我会一直在这里听你的。

用户: 你现在感觉怎么样？
小龙虾: 我现在感觉挺开心的！刚才和你聊了那么多有趣的事情，让我充满了期待。不过也有点小紧张，怕自己做得不够好呢~
```

更多示例见 [references/examples.md](references/examples.md)。

## 技术细节

- [情感模型详解](references/emotion-model.md) — Plutchik 情感轮理论及在小龙虾中的应用
- [自我进化机制](references/evolution-mechanism.md) — 进化引擎架构、特征提取、行为模式学习

## 许可证

MIT License — 详见 [LICENSE](LICENSE)
