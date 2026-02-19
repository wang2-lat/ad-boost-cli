import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from typing import Optional
import json

from models import AdData, BudgetAllocation, TargetAudience
from analyzer import AdAnalyzer
from recommender import StrategyRecommender
from optimizer import BudgetOptimizer

app = typer.Typer(help="CLI tool to boost ad performance with UGC/KOC strategies")
console = Console()

@app.command()
def diagnose(
    ad_data_file: str = typer.Argument(..., help="Path to ad data JSON file"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path")
):
    """Diagnose ad performance and provide improvement suggestions"""
    try:
        with open(ad_data_file, 'r') as f:
            data = json.load(f)
        
        ad_data = AdData(**data)
        analyzer = AdAnalyzer()
        diagnosis = analyzer.diagnose(ad_data)
        
        console.print(Panel.fit("Ad Performance Diagnosis", style="bold blue"))
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Metric", style="cyan")
        table.add_column("Status", style="yellow")
        table.add_column("Issue", style="red")
        
        for issue in diagnosis['issues']:
            table.add_row(issue['metric'], issue['status'], issue['description'])
        
        console.print(table)
        
        console.print("\n[bold green]Recommendations:[/bold green]")
        for i, rec in enumerate(diagnosis['recommendations'], 1):
            console.print(f"{i}. {rec}")
        
        if output:
            with open(output, 'w') as f:
                json.dump(diagnosis, f, indent=2)
            console.print(f"\n[green]Results saved to {output}[/green]")
            
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)

@app.command()
def recommend(
    industry: str = typer.Option(..., "--industry", "-i", help="Industry type"),
    budget: float = typer.Option(..., "--budget", "-b", help="Monthly budget in USD"),
    audience: str = typer.Option(..., "--audience", "-a", help="Target audience (youth/professional/family)"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path")
):
    """Recommend UGC/KOC strategies based on industry and budget"""
    try:
        target = TargetAudience(
            industry=industry,
            budget=budget,
            audience_type=audience
        )
        
        recommender = StrategyRecommender()
        strategies = recommender.recommend(target)
        
        console.print(Panel.fit("UGC/KOC Strategy Recommendations", style="bold blue"))
        
        for strategy in strategies:
            console.print(f"\n[bold cyan]{strategy['channel']}[/bold cyan]")
            console.print(f"Priority: [yellow]{strategy['priority']}[/yellow]")
            console.print(f"Estimated Cost: [green]${strategy['estimated_cost']:.2f}[/green]")
            console.print(f"Expected ROI: [magenta]{strategy['expected_roi']}[/magenta]")
            console.print(f"Description: {strategy['description']}")
            console.print(f"Action Steps:")
            for step in strategy['action_steps']:
                console.print(f"  - {step}")
        
        if output:
            with open(output, 'w') as f:
                json.dump(strategies, f, indent=2)
            console.print(f"\n[green]Results saved to {output}[/green]")
            
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)

@app.command()
def optimize(
    budget_file: str = typer.Argument(..., help="Path to current budget allocation JSON file"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path")
):
    """Optimize budget allocation across channels"""
    try:
        with open(budget_file, 'r') as f:
            data = json.load(f)
        
        allocation = BudgetAllocation(**data)
        optimizer = BudgetOptimizer()
        optimized = optimizer.optimize(allocation)
        
        console.print(Panel.fit("Budget Optimization Results", style="bold blue"))
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Channel", style="cyan")
        table.add_column("Current", style="yellow")
        table.add_column("Optimized", style="green")
        table.add_column("Change", style="red")
        
        for channel in optimized['channels']:
            change = channel['optimized'] - channel['current']
            change_str = f"+${change:.2f}" if change > 0 else f"-${abs(change):.2f}"
            table.add_row(
                channel['name'],
                f"${channel['current']:.2f}",
                f"${channel['optimized']:.2f}",
                change_str
            )
        
        console.print(table)
        
        console.print(f"\n[bold]Expected Improvement:[/bold]")
        console.print(f"ROI Increase: [green]{optimized['roi_improvement']}[/green]")
        console.print(f"Cost Efficiency: [green]{optimized['efficiency_gain']}[/green]")
        
        console.print(f"\n[bold green]Optimization Rationale:[/bold green]")
        for reason in optimized['rationale']:
            console.print(f"- {reason}")
        
        if output:
            with open(output, 'w') as f:
                json.dump(optimized, f, indent=2)
            console.print(f"\n[green]Results saved to {output}[/green]")
            
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
