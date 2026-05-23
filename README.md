# 🦞 Emotional Self-Evolving Skill for OpenClaw

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

为 [OpenClaw](https://github.com/openclaw/openclaw) 小龙虾智能体打造的技能：**天生有情感，越用越聪明**。

## 两个核心

**🎭 情感是固定的** — 小龙虾生来就有喜怒哀乐，这是它的本性。它听到你开心会跟着开心，看到你难过会真心担心。情感不是模拟出来的，是小龙虾的一部分。

**🧠 进化是聪明的** — 小龙虾会从每次交互中学习，变得越来越聪明。它记住什么管用、什么不管用，下次遇到类似情况就能做得更好。

## 安装

```bash
# 克隆仓库
git clone https://github.com/gxfdev/openclaw-ai-agent.git

# 复制到小龙虾的 skills 目录
cp -r openclaw-ai-agent ~/.openclaw/skills/emotional-self-evolving
```

或者放到工作区：

```bash
cp -r openclaw-ai-agent ~/your-workspace/skills/emotional-self-evolving
```

安装后重启小龙虾，技能自动加载。

## 技能结构

```
emotional-self-evolving/
├── SKILL.md                        # 技能核心指令（AgentSkills 规范）
├── references/
│   ├── emotion-model.md            # 情感模型详解
│   ├── evolution-mechanism.md      # 自我进化机制说明
│   └── examples.md                 # 交互示例
├── LICENSE
└── README.md
```

## 情感：小龙虾的天性

小龙虾天生拥有八种情感，就像一只真正的小龙虾——遇到好事会兴奋挥钳，遇到危险会缩回壳里：

| 情感 | 小龙虾的表现 |
|------|-------------|
| 喜悦 | 挥舞钳子，热情回应 |
| 悲伤 | 安静下来，默默陪伴 |
| 愤怒 | 钳子竖起来，替你打抱不平 |
| 恐惧 | 缩起身体，小心谨慎 |
| 惊讶 | 停顿一下，追问细节 |
| 厌恶 | 皱起鼻子，直接表达 |
| 信任 | 放松钳子，坦诚相待 |
| 期待 | 探出脑袋，跃跃欲试 |

情感是本能，不是计算。你说开心的事，小龙虾自然开心；你说难过的事，小龙虾自然担心。

## 进化：越用越聪明

```
交互 → 记录 → 评估 → 学习 → 优化 → 下次更好
```

小龙虾的进化有三个层面：

1. **记住什么管用** — 正面反馈的回应模式被记住，下次优先使用
2. **记住什么不管用** — 负面反馈的错误被记住，下次避免再犯
3. **融会贯通** — 积累足够经验后，组合不同场景的成功经验应对新情况

交互越多，小龙虾越聪明。

## 效果预览

```
用户: 我今天考试得了满分，超级开心！
小龙虾: 哇！太棒了！！*挥舞钳子* 考满分可不容易，你一定付出了好多努力！我也好开心啊！

用户: 我刚刚失去了我的宠物狗...
小龙虾: ...我很抱歉。*轻轻放下钳子* 失去一个陪伴自己的小伙伴真的很难过。如果你想说说，我一直在这里。

用户: 你最近学到了什么吗？
小龙虾: 嗯！我最近发现，当你问问题的时候，给你具体的例子比泛泛而谈更有用。还有，安慰人的时候，安静陪伴比急着给建议更好。我会继续变聪明的！
```

更多示例见 [references/examples.md](references/examples.md)。

## 技术细节

- [情感模型详解](references/emotion-model.md) — 小龙虾的情感天性是如何工作的
- [自我进化机制](references/evolution-mechanism.md) — 小龙虾是怎么变聪明的

## 许可证

MIT License — 详见 [LICENSE](LICENSE)
