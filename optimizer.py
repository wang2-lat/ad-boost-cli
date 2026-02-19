from models import BudgetAllocation
from typing import Dict
import pandas as pd

class BudgetOptimizer:
    def optimize(self, allocation: BudgetAllocation) -> Dict:
        df = pd.DataFrame([
            {
                'channel': ch['name'],
                'current': ch['amount'],
                'roi': allocation.performance_data.get(ch['name'], {}).get('roi', 1.0),
                'cpa': allocation.performance_data.get(ch['name'], {}).get('cpa', 100.0)
            }
            for ch in allocation.channels
        ])
        
        df['efficiency_score'] = df['roi'] / df['cpa']
        df['efficiency_score'] = df['efficiency_score'] / df['efficiency_score'].sum()
        
        df['optimized'] = allocation.total_budget * df['efficiency_score']
        df['change'] = df['optimized'] - df['current']
        
        optimized_channels = []
        for _, row in df.iterrows():
            optimized_channels.append({
                'name': row['channel'],
                'current': row['current'],
                'optimized': row['optimized'],
                'change': row['change']
            })
        
        avg_roi_current = (df['current'] * df['roi']).sum() / df['current'].sum()
        avg_roi_optimized = (df['optimized'] * df['roi']).sum() / df['optimized'].sum()
        roi_improvement = f"+{((avg_roi_optimized / avg_roi_current - 1) * 100):.1f}%"
        
        avg_cpa_current = (df['current'] * df['cpa']).sum() / df['current'].sum()
        avg_cpa_optimized = (df['optimized'] * df['cpa']).sum() / df['optimized'].sum()
        efficiency_gain = f"+{((avg_cpa_current / avg_cpa_optimized - 1) * 100):.1f}%"
        
        rationale = []
        top_performer = df.loc[df['efficiency_score'].idxmax(), 'channel']
        rationale.append(f"Increased allocation to {top_performer} due to highest efficiency score")
        
        low_performers = df[df['efficiency_score'] < df['efficiency_score'].mean()]['channel'].tolist()
        if low_performers:
            rationale.append(f"Reduced allocation from underperforming channels: {', '.join(low_performers)}")
        
        return {
            'channels': optimized_channels,
            'roi_improvement': roi_improvement,
            'efficiency_gain': efficiency_gain,
            'rationale': rationale
        }
