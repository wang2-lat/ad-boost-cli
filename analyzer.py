from models import AdData
from typing import Dict, List

class AdAnalyzer:
    def diagnose(self, ad_data: AdData) -> Dict:
        ctr = (ad_data.clicks / ad_data.impressions * 100) if ad_data.impressions > 0 else 0
        cvr = (ad_data.conversions / ad_data.clicks * 100) if ad_data.clicks > 0 else 0
        cpa = (ad_data.spend / ad_data.conversions) if ad_data.conversions > 0 else float('inf')
        
        issues = []
        recommendations = []
        
        if ctr < 1.0:
            issues.append({
                'metric': 'CTR',
                'status': f'{ctr:.2f}%',
                'description': 'Low click-through rate indicates poor ad creative or targeting'
            })
            recommendations.append('Improve ad creative with UGC content showing real customer experiences')
            recommendations.append('Test different audience segments to find better targeting')
        
        if cvr < 2.0:
            issues.append({
                'metric': 'CVR',
                'status': f'{cvr:.2f}%',
                'description': 'Low conversion rate suggests landing page or offer issues'
            })
            recommendations.append('Add social proof and KOC testimonials to landing page')
            recommendations.append('Simplify conversion funnel and reduce friction points')
        
        if cpa > 50:
            issues.append({
                'metric': 'CPA',
                'status': f'${cpa:.2f}',
                'description': 'High cost per acquisition indicates inefficient spending'
            })
            recommendations.append('Shift budget to UGC/KOC channels with lower acquisition costs')
            recommendations.append('Implement retargeting campaigns to improve conversion efficiency')
        
        if not issues:
            issues.append({
                'metric': 'Overall',
                'status': 'Good',
                'description': 'Performance metrics are within acceptable ranges'
            })
            recommendations.append('Consider scaling successful campaigns gradually')
            recommendations.append('Test new UGC formats to maintain engagement')
        
        return {
            'metrics': {
                'ctr': f'{ctr:.2f}%',
                'cvr': f'{cvr:.2f}%',
                'cpa': f'${cpa:.2f}'
            },
            'issues': issues,
            'recommendations': recommendations
        }
