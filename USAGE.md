# OpenCLAW 使用指南

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 基本使用
```python
from openclaw import OpenCLAW

# 创建实例
claw = OpenCLAW(name="MyEmotionalAgent")

# 与用户交互
response = claw.interact("你好，我今天很开心！")

# 获取当前情感状态
emotions = claw.get_emotional_state()
print(f"当前情感: {emotions}")

# 获取进化状态
evolution = claw.get_evolution_status()
print(f"进化状态: {evolution}")
```

## 高级功能

### 带情感标签的交互
```python
# 明确告知用户的情感状态
response = claw.interact("我很难过", user_emotion="sad")

# 提供上下文
context = {
    "user_mood": "anxious",
    "conversation_stage": "early"
}
response = claw.interact("我有点紧张", context=context)
```

### 提供反馈以促进进化
```python
# 在交互后提供反馈
response = claw.interact("我的问题是...")
# 用户评价回应质量（0.0-1.0）
claw.interact("我的问题是...", feedback=0.8)
```

### 检查代理状态
```python
# 检查当前情感状态
emotions = claw.get_emotional_state()

# 检查进化进度
evolution_status = claw.get_evolution_status()

# 查看记忆
recent_memories = claw.memory.recall_recent_interactions(limit=5)
```

## 示例应用

### 情感支持机器人
```python
from openclaw import OpenCLAW

agent = OpenCLAW(name="SupportBot")

while True:
    user_input = input("您: ")
    if user_input.lower() in ['quit', 'exit', '退出']:
        break
    
    response = agent.interact(user_input)
    print(f"{agent.name}: {response}")
```

### 智能助手
```python
from openclaw import OpenCLAW

assistant = OpenCLAW(name="SmartAssistant")

# 长期交互，累积记忆
for conversation_round in range(10):
    user_input = input("用户: ")
    response = assistant.interact(user_input)
    print(f"助手: {response}")
    
    # 可选：用户提供反馈
    feedback = input("满意度 (0-1): ")
    if feedback:
        assistant.interact(user_input, feedback=float(feedback))
```

## 配置选项

### 自定义名称
```python
claw = OpenCLAW(name="MyCustomAgent")
```

### 检查系统状态
```python
# 查看当前情感
emotions = claw.get_emotional_state()

# 查看进化统计
stats = claw.get_evolution_status()
```

## 注意事项

1. 情感识别基于关键词和简单启发式规则，更复杂的实现可集成NLP情感分析模型
2. 自我进化需要足够的交互数据和反馈才能有效工作
3. 长期运行时，可能需要定期清理旧的记忆以节省内存
4. 为了获得最佳效果，建议提供用户反馈以加速学习过程