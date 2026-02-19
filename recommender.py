from models import TargetAudience
from typing import List, Dict

class StrategyRecommender:
    def recommend(self, target: TargetAudience) -> List[Dict]:
        strategies = []
        
        if target.budget < 1000:
            strategies.append({
                'channel': 'Micro-Influencer Partnerships',
                'priority': 'High',
                'estimated_cost': target.budget * 0.4,
                'expected_roi': '3-5x',
                'description': 'Partner with 5-10 micro-influencers (1K-10K followers) for authentic content',
                'action_steps': [
                    'Identify niche influencers in your industry using hashtag research',
                    'Reach out with product samples and collaboration proposals',
                    'Request authentic review content and usage rights',
                    'Repurpose UGC across your owned channels'
                ]
            })
            strategies.append({
                'channel': 'User-Generated Content Campaign',
                'priority': 'High',
                'estimated_cost': target.budget * 0.3,
                'expected_roi': '4-6x',
                'description': 'Launch hashtag campaign encouraging customers to share experiences',
                'action_steps': [
                    'Create branded hashtag and incentive program',
                    'Offer discounts or features for best submissions',
                    'Curate and showcase best UGC on social media',
                    'Use UGC in paid ads for higher authenticity'
                ]
            })
        else:
            strategies.append({
                'channel': 'KOC Ambassador Program',
                'priority': 'High',
                'estimated_cost': target.budget * 0.35,
                'expected_roi': '4-7x',
                'description': 'Build long-term relationships with key opinion consumers',
                'action_steps': [
                    'Recruit 20-30 passionate customers as brand ambassadors',
                    'Provide exclusive perks and early access to products',
                    'Enable them to create regular authentic content',
                    'Track and reward top performers with bonuses'
                ]
            })
            strategies.append({
                'channel': 'Professional UGC Production',
                'priority': 'Medium',
                'estimated_cost': target.budget * 0.25,
                'expected_roi': '3-5x',
                'description': 'Commission professional creators to produce UGC-style content',
                'action_steps': [
                    'Hire UGC creators from platforms like Fiverr or Upwork',
                    'Brief them on authentic storytelling approach',
                    'Test multiple creative variations',
                    'Scale winning content across paid channels'
                ]
            })
        
        strategies.append({
            'channel': 'Community Building',
            'priority': 'Medium',
            'estimated_cost': target.budget * 0.2,
            'expected_roi': '5-8x (long-term)',
            'description': 'Build engaged community for organic advocacy',
            'action_steps': [
                'Create Facebook/Discord group for customers',
                'Host regular Q&A sessions and exclusive events',
                'Encourage peer-to-peer recommendations',
                'Feature community members in marketing materials'
            ]
        })
        
        return strategies
