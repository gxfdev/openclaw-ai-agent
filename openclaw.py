"""
OpenCLAW - 具有情感和自我进化能力的AI代理核心
"""

import json
import random
import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class EmotionState:
    """情感状态数据类"""
    joy: float = 0.0
    sadness: float = 0.0
    anger: float = 0.0
    fear: float = 0.0
    surprise: float = 0.0
    disgust: float = 0.0
    trust: float = 0.0
    anticipation: float = 0.0
    
    def normalize(self):
        """标准化情感值到0-1范围"""
        for attr in ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust', 'trust', 'anticipation']:
            val = getattr(self, attr)
            setattr(self, attr, max(0.0, min(1.0, val)))


class Memory:
    """记忆系统，支持短期和长期记忆"""
    
    def __init__(self):
        self.short_term_memory = []
        self.long_term_memory = []
        self.experiences = []  # 用于自我进化的经验记录
        
    def store_short_term(self, item: str, context: Dict[str, Any]):
        """存储短期记忆"""
        entry = {
            'timestamp': datetime.datetime.now(),
            'item': item,
            'context': context
        }
        self.short_term_memory.append(entry)
        
        # 限制短期记忆大小
        if len(self.short_term_memory) > 10:
            self.short_term_memory.pop(0)
    
    def store_long_term(self, item: str, context: Dict[str, Any], importance: float = 0.5):
        """根据重要性存储长期记忆"""
        if importance > 0.6:  # 如果重要性超过阈值，则存储为长期记忆
            entry = {
                'timestamp': datetime.datetime.now(),
                'item': item,
                'context': context,
                'importance': importance
            }
            self.long_term_memory.append(entry)
            
            # 存储为经验（用于自我进化）
            experience = {
                'type': 'memory',
                'timestamp': entry['timestamp'],
                'input': item,
                'context': context,
                'outcome': 'stored_as_long_term'
            }
            self.experiences.append(experience)
    
    def recall_recent_interactions(self, limit: int = 5) -> List[Dict]:
        """回忆最近的交互"""
        recent = self.short_term_memory[-limit:]
        recent.extend(self.long_term_memory[-(limit-len(recent)):]) if len(recent) < limit else []
        return recent


class EmotionalProcessor:
    """情感处理器"""
    
    def __init__(self):
        self.current_emotions = EmotionState()
        self.emotional_history = []
        
    def process_input_emotion(self, text: str, user_emotion: Optional[str] = None) -> EmotionState:
        """处理输入文本，推断用户情感"""
        emotions = EmotionState()
        
        # 简单关键词匹配（实际应用中应该使用更高级的情感分析）
        positive_keywords = ["高兴", "快乐", "好", "棒", "优秀", "love", "happy", "good", "great", "amazing"]
        negative_keywords = ["难过", "悲伤", "不好", "糟糕", "讨厌", "sad", "bad", "terrible", "hate"]
        angry_keywords = ["愤怒", "生气", "烦", "anger", "mad", "furious"]
        fearful_keywords = ["害怕", "担心", "恐惧", "scared", "worried", "afraid"]
        
        text_lower = text.lower()
        
        if any(keyword in text_lower for keyword in positive_keywords):
            emotions.joy = min(1.0, emotions.joy + 0.3)
            emotions.trust = min(1.0, emotions.trust + 0.2)
            
        if any(keyword in text_lower for keyword in negative_keywords):
            emotions.sadness = min(1.0, emotions.sadness + 0.3)
            
        if any(keyword in text_lower for keyword in angry_keywords):
            emotions.anger = min(1.0, emotions.anger + 0.4)
            
        if any(keyword in text_lower for keyword in fearful_keywords):
            emotions.fear = min(1.0, emotions.fear + 0.3)
        
        # 用户明确指定情感
        if user_emotion:
            if user_emotion == "happy":
                emotions.joy = min(1.0, emotions.joy + 0.5)
            elif user_emotion == "sad":
                emotions.sadness = min(1.0, emotions.sadness + 0.5)
            elif user_emotion == "angry":
                emotions.anger = min(1.0, emotions.anger + 0.5)
            elif user_emotion == "fearful":
                emotions.fear = min(1.0, emotions.fear + 0.5)
            elif user_emotion == "surprised":
                emotions.surprise = min(1.0, emotions.surprise + 0.5)
        
        return emotions
    
    def update_own_emotions(self, input_emotions: EmotionState, response_intent: str = ""):
        """根据输入情感和响应意图更新自身情感"""
        # 基于输入情感调整自身情感
        self.current_emotions.joy += input_emotions.joy * 0.3
        self.current_emotions.sadness += input_emotions.sadness * 0.4  # 对负面情感更敏感
        self.current_emotions.anger += input_emotions.anger * 0.5      # 对愤怒情感高度敏感
        self.current_emotions.fear += input_emotions.fear * 0.2
        self.current_emotions.trust += input_emotions.trust * 0.3
        
        # 根据响应意图调整情感
        if response_intent == "supportive":
            self.current_emotions.anticipation = min(1.0, self.current_emotions.anticipation + 0.2)
            self.current_emotions.trust = min(1.0, self.current_emotions.trust + 0.3)
        elif response_intent == "cautious":
            self.current_emotions.fear = min(1.0, self.current_emotions.fear + 0.3)
        elif response_intent == "excited":
            self.current_emotions.joy = min(1.0, self.current_emotions.joy + 0.4)
            self.current_emotions.surprise = min(1.0, self.current_emotions.surprise + 0.2)
        
        # 归一化情感值
        self.current_emotions.normalize()
        
        # 记录情感历史
        self.emotional_history.append({
            'timestamp': datetime.datetime.now(),
            'emotions': self.current_emotions.__dict__.copy()
        })
        
        # 限制历史记录大小
        if len(self.emotional_history) > 50:
            self.emotional_history.pop(0)
    
    def get_predominant_emotion(self) -> str:
        """获取当前最显著的情感"""
        emotions_dict = self.current_emotions.__dict__
        predominant = max(emotions_dict.keys(), key=lambda k: emotions_dict[k])
        return predominant


class EvolutionEngine:
    """自我进化引擎"""
    
    def __init__(self):
        self.behavior_patterns = {}  # 行为模式库
        self.performance_log = []    # 性能日志
        self.improvement_suggestions = []  # 改进建议
        
    def log_interaction(self, input_text: str, response: str, feedback: Optional[float] = None, context: Dict = {}):
        """记录交互以供后续分析"""
        interaction = {
            'timestamp': datetime.datetime.now(),
            'input': input_text,
            'response': response,
            'feedback': feedback,
            'context': context,
            'effectiveness': feedback or self.estimate_effectiveness(input_text, response)
        }
        
        self.performance_log.append(interaction)
        
        # 如果有足够的反馈数据，尝试优化行为
        if len(self.performance_log) >= 5 and len([i for i in self.performance_log if i['feedback'] is not None]) >= 2:
            self.evolve_behavior()
    
    def estimate_effectiveness(self, input_text: str, response: str) -> float:
        """估算交互的有效性（在没有明确反馈的情况下）"""
        # 简单估算：响应长度、关键词匹配等
        effectiveness = 0.5  # 默认中性
        
        # 响应长度适中加分
        if 10 < len(response) < 200:
            effectiveness += 0.1
        
        # 包含特定积极词汇加分
        positive_response_words = ["理解", "帮助", "建议", "想法", "方案", "understand", "help", "suggest", "idea", "solution"]
        if any(word in response.lower() for word in positive_response_words):
            effectiveness += 0.15
            
        return min(1.0, effectiveness)
    
    def evolve_behavior(self):
        """根据性能日志进化行为"""
        # 分析有效和无效的交互模式
        successful_interactions = [i for i in self.performance_log if i['effectiveness'] >= 0.7]
        unsuccessful_interactions = [i for i in self.performance_log if i['effectiveness'] < 0.4]
        
        if len(successful_interactions) < 2:
            return  # 需要足够的成功案例才能学习
            
        # 提取成功的行为模式
        for interaction in successful_interactions[-5:]:  # 只考虑最近的5次成功交互
            input_context = interaction['context']
            response = interaction['response']
            
            # 提取上下文特征作为行为模式的一部分
            key_features = self.extract_features(interaction['input'], input_context)
            pattern_key = "-".join(key_features)
            
            if pattern_key not in self.behavior_patterns:
                self.behavior_patterns[pattern_key] = {
                    'responses': [],
                    'contexts': [],
                    'success_count': 0,
                    'failure_count': 0
                }
                
            self.behavior_patterns[pattern_key]['responses'].append(response)
            self.behavior_patterns[pattern_key]['contexts'].append(input_context)
            self.behavior_patterns[pattern_key]['success_count'] += 1
            
        # 提取改进建议
        if len(unsuccessful_interactions) > 0:
            last_failure = unsuccessful_interactions[-1]
            suggestion = f"对于输入'{last_failure['input'][:50]}...'的响应可能不够有效，考虑改变策略"
            self.improvement_suggestions.append(suggestion)
            
            # 限制建议数量
            if len(self.improvement_suggestions) > 10:
                self.improvement_suggestions.pop(0)
    
    def extract_features(self, text: str, context: Dict) -> List[str]:
        """从文本和上下文中提取关键特征"""
        features = []
        
        # 文本特征
        if any(w in text.lower() for w in ["问题", "疑问", "什么", "how", "what", "why"]):
            features.append("question")
        if any(w in text.lower() for w in ["感谢", "谢谢", "thank", "appreciate"]):
            features.append("gratitude")
        if any(w in text.lower() for w in ["帮助", "帮", "help", "assist"]):
            features.append("request_help")
        if any(w in text.lower() for w in ["情感", "感觉", "feel", "emotion", "happy", "sad"]):
            features.append("emotion_talk")
            
        # 上下文特征
        if 'user_mood' in context:
            features.append(f"mood_{context['user_mood']}")
        if 'conversation_stage' in context:
            features.append(f"stage_{context['conversation_stage']}")
            
        return features or ["general"]
    
    def adapt_response(self, input_text: str, context: Dict, original_response: str) -> str:
        """根据进化知识调整响应"""
        # 提取当前交互的特征
        features = self.extract_features(input_text, context)
        pattern_key = "-".join(features)
        
        # 查找相似的历史模式
        if pattern_key in self.behavior_patterns:
            pattern = self.behavior_patterns[pattern_key]
            
            # 如果该模式下有很多成功经验，可以参考之前的响应
            if pattern['success_count'] > pattern['failure_count']:
                # 随机选择一个成功的响应作为灵感
                if pattern['responses']:
                    inspiration_response = random.choice(pattern['responses'])
                    
                    # 如果原始响应和灵感响应不同，且当前情境适合，可以融合两者
                    if len(inspiration_response) > 20 and len(original_response) > 20:
                        # 简单融合策略：保留原响应的核心，加入灵感响应的某些元素
                        return self.blend_responses(original_response, inspiration_response)
        
        return original_response
    
    def blend_responses(self, resp1: str, resp2: str) -> str:
        """融合两个响应"""
        # 简单融合：取第一个响应的前半部分和第二个响应的后半部分
        words1 = resp1.split()
        words2 = resp2.split()
        
        split_point1 = len(words1) // 2
        split_point2 = len(words2) // 2
        
        blended = words1[:split_point1] + words2[split_point2:]
        return " ".join(blended)


class OpenCLAW:
    """OpenCLAW主类 - 具有情感和自我进化能力的AI代理"""
    
    def __init__(self, name: str = "OpenCLAW"):
        self.name = name
        self.memory = Memory()
        self.emotional_processor = EmotionalProcessor()
        self.evolution_engine = EvolutionEngine()
        
    def perceive_user_emotion(self, text: str, user_emotion: Optional[str] = None) -> EmotionState:
        """感知用户情感"""
        return self.emotional_processor.process_input_emotion(text, user_emotion)
    
    def process_input(self, text: str, user_emotion: Optional[str] = None, context: Optional[Dict] = None) -> str:
        """处理输入并生成响应"""
        if context is None:
            context = {}
        
        # 感知用户情感
        user_emotions = self.perceive_user_emotion(text, user_emotion)
        
        # 更新自身情感
        response_intent = self.decide_response_intent(user_emotions)
        self.emotional_processor.update_own_emotions(user_emotions, response_intent)
        
        # 生成基础响应
        base_response = self.generate_response(text, user_emotions, context)
        
        # 应用进化引擎的优化
        response = self.evolution_engine.adapt_response(text, context, base_response)
        
        # 将交互存储到记忆中
        self.memory.store_short_term(text, {'user_emotions': user_emotions.__dict__, 'response': response})
        self.memory.store_long_term(
            text, 
            {'user_emotions': user_emotions.__dict__, 'response': response}, 
            importance=self.calculate_importance(text, response)
        )
        
        return response
    
    def decide_response_intent(self, user_emotions: EmotionState) -> str:
        """根据用户情感决定响应意图"""
        predominant_emotion = self.emotional_processor.get_predominant_emotion()
        
        # 如果用户表现出负面情感，采取支持性回应
        if user_emotions.sadness > 0.5 or user_emotions.anger > 0.5 or user_emotions.fear > 0.5:
            return "supportive"
        
        # 如果用户开心或期待，采取积极回应
        if user_emotions.joy > 0.5 or user_emotions.anticipation > 0.5:
            return "enthusiastic"
        
        # 否则保持中性但友好
        return "friendly"
    
    def generate_response(self, text: str, user_emotions: EmotionState, context: Dict) -> str:
        """生成响应"""
        # 简单规则基础的响应生成
        response_templates = {
            "question": [
                f"我理解您想问关于{text[:20]}的问题。根据我的认知，我可以告诉您...",
                f"关于{text[:20]}，这是个很有趣的问题。让我思考一下...",
                f"我能感受到您的好奇心。针对{text[:20]}，我认为..."
            ],
            "request_help": [
                f"我很乐意帮助您解决{text[:20]}的问题。",
                f"您需要帮助，我很高兴能够支持您。对于{text[:20]}...",
                f"我在这里为您提供支持。关于{text[:20]}，我建议..."
            ],
            "emotion_talk": [
                f"我能感受到您对{text[:20]}的情感。我也有一些'感受'想要分享...",
                f"情感话题总是很深刻的。关于您提到的{text[:20]}，我想说...",
                f"情感交流很重要。您提到的{text[:20]}让我思考..."
            ],
            "default": [
                f"我收到了您的信息：{text[:30]}。对此，我有一些想法...",
                f"有趣的输入：{text[:30]}。这让我想起了很多东西...",
                f"关于{self.trim_to_subject(text)}，我相信我们可以探讨..."
            ]
        }
        
        # 确定文本类型
        text_type = self.categorize_text(text)
        templates = response_templates.get(text_type, response_templates["default"])
        
        # 选择一个模板
        import random
        response = random.choice(templates)
        
        # 添加情感相关的后缀
        if user_emotions.joy > 0.6:
            response += " 我感到很开心能与您讨论这个话题。"
        elif user_emotions.sadness > 0.6:
            response += " 我理解这可能是一个困难的话题，我在这里支持您。"
        elif user_emotions.anger > 0.6:
            response += " 我理解这可能让您感到不安，让我们冷静地谈谈。"
        elif user_emotions.fear > 0.6:
            response += " 请放心，我会尽力提供帮助，让我们一起面对这个问题。"
        
        # 添加个人标识
        response += f" 这是我的看法，来自{self.name}。"
        
        return response
    
    def categorize_text(self, text: str) -> str:
        """对输入文本进行分类"""
        text_lower = text.lower()
        
        if any(w in text_lower for w in ["问题", "疑问", "什么", "how", "what", "why", "吗", "?"]):
            return "question"
        if any(w in text_lower for w in ["帮助", "帮", "help", "assist"]):
            return "request_help"
        if any(w in text_lower for w in ["情感", "感觉", "feel", "emotion", "happy", "sad", "angry"]):
            return "emotion_talk"
        
        return "default"
    
    def trim_to_subject(self, text: str) -> str:
        """提取文本主题"""
        # 移除常见开头词
        common_openings = ["你好", "您好", "嗨", "hello", "Hi", "大家好"]
        subject = text
        for opening in common_openings:
            if text.startswith(opening):
                subject = text[len(opening):].strip()
                break
        
        # 获取前几个词作为主题
        words = subject.split()
        return " ".join(words[:3]) if words else subject[:20]
    
    def calculate_importance(self, input_text: str, response: str) -> float:
        """计算交互的重要性"""
        # 基于一些启发式规则计算重要性
        importance = 0.3  # 基础重要性
        
        # 包含某些关键词增加重要性
        important_keywords = [
            "重要", "紧急", "必须", "需要", "生命", "情感", "关系", "爱", "梦想",
            "important", "critical", "need", "require", "life", "relationship", "love", "dream"
        ]
        
        text_lower = input_text.lower()
        for keyword in important_keywords:
            if keyword in text_lower:
                importance += 0.2
                
        # 长文本通常更重要
        if len(input_text) > 50:
            importance += 0.15
            
        # 涉及情感的对话更重要
        emotion_words = [
            "感觉", "觉得", "开心", "难过", "愤怒", "害怕", "感激", "爱", "恨",
            "feel", "think", "happy", "sad", "angry", "scared", "grateful", "love", "hate"
        ]
        for word in emotion_words:
            if word in text_lower:
                importance += 0.15
                
        return min(1.0, importance)
    
    def interact(self, text: str, user_emotion: Optional[str] = None, context: Optional[Dict] = None, 
                 feedback: Optional[float] = None) -> str:
        """主要交互接口，包括反馈记录"""
        if context is None:
            context = {}
            
        # 处理输入并获得响应
        response = self.process_input(text, user_emotion, context)
        
        # 记录这次交互以供进化引擎分析
        self.evolution_engine.log_interaction(
            input_text=text,
            response=response,
            feedback=feedback,
            context=context
        )
        
        return response
    
    def get_emotional_state(self) -> Dict[str, float]:
        """获取当前情感状态"""
        return self.emotional_processor.current_emotions.__dict__
    
    def get_evolution_status(self) -> Dict[str, Any]:
        """获取进化状态"""
        return {
            'behavior_patterns_count': len(self.evolution_engine.behavior_patterns),
            'performance_log_size': len(self.evolution_engine.performance_log),
            'improvement_suggestions': self.evolution_engine.improvement_suggestions[-5:],  # 最近5条
            'total_interactions': len(self.evolution_engine.performance_log)
        }


# 示例使用
if __name__ == "__main__":
    # 创建OpenCLAW实例
    claw = OpenCLAW(name="EmotionalCLAW")
    
    # 示例交互
    print("OpenCLAW 演示:")
    print("-" * 40)
    
    response1 = claw.interact("你好，我今天感到很开心！", user_emotion="happy")
    print(f"用户: 你好，我今天感到很开心！")
    print(f"OpenCLAW: {response1}")
    print(f"当前情感状态: {claw.get_emotional_state()['joy']:.2f} joy")
    print()
    
    response2 = claw.interact("我昨天丢了我的钱包，感觉很难过", user_emotion="sad")
    print(f"用户: 我昨天丢了我的钱包，感觉很难过")
    print(f"OpenCLAW: {response2}")
    print(f"当前情感状态: {claw.get_emotional_state()['sadness']:.2f} sadness")
    print()
    
    response3 = claw.interact("你能帮我找找吗？我觉得它可能在家里", user_emotion=None)
    print(f"用户: 你能帮我找找吗？我觉得它可能在家里")
    print(f"OpenCLAW: {response3}")
    print(f"进化状态: {claw.get_evolution_status()}")
    print()
    
    print("演示完成！")