"""
OpenCLAW 简单测试文件
验证核心功能是否正常工作
"""

from openclaw import OpenCLAW
import json


def test_basic_functionality():
    """测试基本功能"""
    print("测试1: 基本功能")
    print("-" * 30)
    
    # 创建实例
    claw = OpenCLAW(name="TestCLAW")
    
    # 测试基本交互
    response = claw.interact("你好，世界！")
    print(f"输入: 你好，世界！")
    print(f"输出: {response}")
    print(f"情感状态: {claw.get_emotional_state()}")
    print()
    
    return True


def test_emotional_response():
    """测试情感回应"""
    print("测试2: 情感回应")
    print("-" * 30)
    
    claw = OpenCLAW(name="EmotionTestCLAW")
    
    # 测试积极情感
    response1 = claw.interact("我今天赢得了比赛！", user_emotion="happy")
    print(f"输入: 我今天赢得了比赛！")
    print(f"情感: happy")
    print(f"回应: {response1}")
    print(f"当前情感: Joy={claw.get_emotional_state()['joy']:.2f}")
    print()
    
    # 测试消极情感
    response2 = claw.interact("我丢失了重要的文件", user_emotion="sad")
    print(f"输入: 我丢失了重要的文件")
    print(f"情感: sad")
    print(f"回应: {response2}")
    print(f"当前情感: Sadness={claw.get_emotional_state()['sadness']:.2f}")
    print()
    
    return True


def test_evolution_tracking():
    """测试进化追踪"""
    print("测试3: 进化追踪")
    print("-" * 30)
    
    claw = OpenCLAW(name="EvolutionTestCLAW")
    
    # 进行几次交互
    claw.interact("我想知道天气怎么样", feedback=0.8)
    claw.interact("请帮我写一封邮件", feedback=0.6)
    claw.interact("告诉我一个故事", feedback=0.9)
    
    # 检查进化状态
    status = claw.get_evolution_status()
    print(f"交互次数: {status['total_interactions']}")
    print(f"行为模式数: {status['behavior_patterns_count']}")
    print(f"改进建议数: {len(status['improvement_suggestions'])}")
    print()
    
    return True


def test_memory_system():
    """测试记忆系统"""
    print("测试4: 记忆系统")
    print("-" * 30)
    
    claw = OpenCLAW(name="MemoryTestCLAW")
    
    # 进行多次交互
    for i in range(5):
        claw.interact(f"测试消息 #{i+1}", context={"round": i})
    
    # 回忆最近的交互
    recent = claw.memory.recall_recent_interactions(3)
    print(f"最近的 {len(recent)} 次交互:")
    for idx, item in enumerate(recent):
        print(f"  {idx+1}. {item['item'][:30]}...")
    
    print()
    
    return True


def run_all_tests():
    """运行所有测试"""
    print("开始测试 OpenCLAW 功能...")
    print("=" * 50)
    
    tests = [
        test_basic_functionality,
        test_emotional_response,
        test_evolution_tracking,
        test_memory_system
    ]
    
    passed = 0
    total = len(tests)
    
    for test_func in tests:
        try:
            result = test_func()
            if result:
                print(f"✓ {test_func.__name__} 通过")
                passed += 1
            else:
                print(f"✗ {test_func.__name__} 失败")
        except Exception as e:
            print(f"✗ {test_func.__name__} 异常: {str(e)}")
    
    print("=" * 50)
    print(f"测试完成: {passed}/{total} 通过")
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    if success:
        print("\n所有测试通过！OpenCLAW 实现正常工作。")
    else:
        print("\n一些测试失败，请检查实现。")