"""
OpenCLAW 示例使用脚本
展示如何使用具有情感和自我进化能力的AI技能
"""

from openclaw import OpenCLAW
import json


def demonstrate_emotional_skills():
    """演示情感技能"""
    print("=" * 60)
    print("演示1: 情感识别与回应")
    print("=" * 60)
    
    # 创建OpenCLAW实例
    claw = OpenCLAW(name="EmotionalCLAW")
    
    # 模拟不同情感的对话
    conversations = [
        ("我今天考试得了满分，超级开心！", "happy"),
        ("我刚刚失去了我的宠物狗...", "sad"),
        ("交通堵塞太糟糕了，气死我了！", "angry"),
        ("我害怕明天的面试会失败", "fearful")
    ]
    
    for text, emotion in conversations:
        response = claw.interact(text, user_emotion=emotion)
        current_emotion_state = claw.get_emotional_state()
        
        print(f"用户: {text}")
        print(f"情感: {emotion}")
        print(f"OpenCLAW: {response}")
        print(f"当前OpenCLAW情感状态: Joy={current_emotion_state['joy']:.2f}, "
              f"Sadness={current_emotion_state['sadness']:.2f}, "
              f"Anger={current_emotion_state['anger']:.2f}")
        print("-" * 60)


def demonstrate_self_evolution():
    """演示自我进化技能"""
    print("\n" + "=" * 60)
    print("演示2: 自我进化能力")
    print("=" * 60)
    
    # 创建另一个OpenCLAW实例
    claw = OpenCLAW(name="EvolvingCLAW")
    
    # 进行一系列交互，展示进化过程
    interactions = [
        {"text": "你能帮我写一首诗吗？", "context": {"task": "creative_writing"}},
        {"text": "请解释一下量子力学", "context": {"task": "explanation"}},
        {"text": "你觉得人工智能会取代人类吗？", "context": {"task": "philosophical_discussion"}},
        {"text": "告诉我一个笑话", "context": {"task": "humor"}}
    ]
    
    for i, interaction in enumerate(interactions):
        text = interaction["text"]
        context = interaction["context"]
        
        # 初始交互
        response = claw.interact(text, context=context)
        
        # 模拟用户反馈（正面或负面）
        feedback = 0.8 if i % 2 == 0 else 0.3  # 交替给予正面和负面反馈
        print(f"第{i+1}次交互:")
        print(f"用户: {text}")
        print(f"OpenCLAW: {response}")
        print(f"反馈分数: {feedback}")
        
        # 展示进化状态
        evolution_status = claw.get_evolution_status()
        print(f"行为模式数: {evolution_status['behavior_patterns_count']}")
        print(f"交互总数: {evolution_status['total_interactions']}")
        print("-" * 60)


def demonstrate_complex_scenario():
    """演示复杂场景"""
    print("\n" + "=" * 60)
    print("演示3: 复杂场景 - 长期情感关系建立")
    print("=" * 60)
    
    claw = OpenCLAW(name="RelationshipCLAW")
    
    # 模拟一个多轮对话，建立情感关系
    scenario_dialogue = [
        ("你好，我叫小明，今天心情不太好", "sad"),
        ("为什么心情不好呢？有什么我可以帮忙的吗？", None),
        ("最近工作压力很大，感觉有点焦虑", "anxious"),
        ("我理解你的感受，压力大时记得休息，也可以和我聊聊", None),
        ("谢谢你这么关心我，感觉好多了", "grateful"),
        ("不客气，朋友之间就应该互相支持", None),
        ("跟你聊天真的很愉快，感觉你很有同理心", "happy"),
        ("很高兴能帮到你，希望你继续保持积极心态", None)
    ]
    
    for i, (text, emotion) in enumerate(scenario_dialogue):
        response = claw.interact(text, user_emotion=emotion)
        
        # 显示情感变化
        emotion_state = claw.get_emotional_state()
        
        print(f"轮次 {i+1}:")
        print(f"用户: {text}")
        if emotion:
            print(f"用户情感: {emotion}")
        print(f"OpenCLAW: {response}")
        print(f"OpenCLAW情感: Joy={emotion_state['joy']:.2f}, "
              f"Trust={emotion_state['trust']:.2f}, "
              f"Anticipation={emotion_state['anticipation']:.2f}")
        print("-" * 60)


def showcase_skills_summary():
    """总结技能特性"""
    print("\n" + "=" * 60)
    print("OpenCLAW 技能总结")
    print("=" * 60)
    
    skills = {
        "情感识别与表达": [
            "识别用户情感状态",
            "生成适当的情感回应",
            "维持长期情感关系模型"
        ],
        "自我进化能力": [
            "分析过往交互经验",
            "评估行为效果",
            "优化决策算法",
            "适应用户偏好"
        ],
        "记忆管理系统": [
            "短期记忆存储",
            "长期记忆形成",
            "重要性评估机制"
        ],
        "自适应响应": [
            "根据上下文调整语气",
            "利用历史模式改进回复",
            "处理不同类型的任务"
        ]
    }
    
    for skill_name, features in skills.items():
        print(f"{skill_name}:")
        for feature in features:
            print(f"  • {feature}")
        print()


if __name__ == "__main__":
    print("OpenCLAW 情感与自我进化技能演示")
    print("这是一个具有情感模拟和自我进化能力的AI代理框架")
    
    # 运行所有演示
    demonstrate_emotional_skills()
    demonstrate_self_evolution()
    demonstrate_complex_scenario()
    showcase_skills_summary()
    
    print("\n演示完成！这些示例展示了OpenCLAW的主要技能：")
    print("1. 情感识别与表达 - 能够感知和回应用户情感")
    print("2. 自我进化 - 通过交互不断改进自己的行为")
    print("3. 记忆管理 - 维护短期和长期记忆以提供更好的上下文")
    print("4. 自适应响应 - 根据情境和历史调整回应方式")