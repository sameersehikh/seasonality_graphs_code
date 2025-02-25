import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.font_manager as fm

# Set Public Sans as the font
font_path = r"C:\Users\HP\Videos\PublicSans Font\Public_Sans\static\PublicSans-Regular.ttf"  # Update this with the actual path on your system
public_sans_font = fm.FontProperties(fname=font_path)

def calculate_comprehensive_metrics(seasonality_df, natural_periods):
    seas_nat = seasonality_df['seasonality'].iloc[natural_periods]
    
    metrics = {
        'seas_start': seasonality_df['seasonality'].iloc[0],
        'nat_mean_seas': seas_nat.mean(),
        'nat_std_seas': seas_nat.std(),
        'min_seas': seasonality_df['seasonality'].min(),
        'final_stable_seas': seasonality_df['seasonality'].iloc[-5:].mean()
    }
    
    return metrics

def plot_enhanced_analysis(seasonality_df):
    plt.figure(figsize=(24, 18))
    gs = plt.GridSpec(12, 1)
    title_ax = plt.subplot(gs[0:2])
    ax1 = plt.subplot(gs[3:])

    # Add title
    title_ax.text(0.5, 0.5, "Weekly Percentage of Teachers' Using Trainings",
                  ha='center', va='center', fontsize=16, fontweight='bold',fontproperties=public_sans_font)
    title_ax.axis('off')

    # Plot seasonality data
    ax1.plot(range(len(seasonality_df)), seasonality_df['seasonality'], 
             label='', marker='o', linestyle='-', color='#28B463', 
             linewidth=2, markersize=6)

    # Define and highlight phases with distinct colors and adjusted durations
    phases = [
        {'name': 'Start of NIETE Program\nand Onboarding', 'range': (0, 4), 'color': '#AED6F1'},
        {'name': 'Initial Natural Behaviour', 'range': (4, 11), 'color': '#D7BDE2'},
        {'name': 'FDE Push for Trainings', 'range': (11, 17), 'color': '#F5B7B1'},
        {'name': 'Natural Behaviour after FDE Push', 'range': (17, 36), 'color': '#F9E79F'},
         {'name': 'Winter \nVacation', 'range': (36, 38), 'color': '#cce6ff'},
         {'name': 'Natural \n Behaviour', 'range': (38, 41), 'color': '#ccffeb'}
    ]

    for phase in phases:
        start, end = phase['range']
        ax1.axvspan(start, end, color=phase['color'], alpha=0.3, edgecolor='gray', linewidth=0.5)
        mid_point = (start + end) / 2
        ax1.text(mid_point, 105, phase['name'], ha='center', va='bottom', fontsize=10, 
                 bbox=dict(facecolor='white', alpha=0.9, edgecolor='none'),fontproperties=public_sans_font)

    # Calculate metrics
    natural_periods = list(range(3, 9)) + list(range(17, 27))
    metrics = calculate_comprehensive_metrics(seasonality_df, natural_periods)

    # Add natural baseline
    # ax1.axhline(y=metrics['nat_mean_seas'], color='#7B7D7D', linestyle=':', 
    #             label=f'Average Natural Behaviour ({metrics["nat_mean_seas"]:.1f}%)')

    # Configure axes
    ax1.set_xticks(range(len(seasonality_df)))
    ax1.set_xticklabels(seasonality_df['week'],rotation=45, ha='right')
    ax1.set_ylim(0, 120)
    ax1.set_ylabel('Engagement Rate (%)', size=12)
    ax1.grid(True, linestyle='--', alpha=0.2, color='gray')

    # Add date labels on top
    ax2 = ax1.twiny()
    ax2.set_xlim(ax1.get_xlim())
    ax2.set_xticks(range(len(seasonality_df)))
    date_labels = [d.strftime('%Y-%m-%d') for d in seasonality_df['date']]
    ax2.set_xticklabels(date_labels, rotation=45, ha='left')

    # Position legend at bottom right
    legend = ax1.legend(bbox_to_anchor=(1.0, -0.15), loc='lower right', frameon=True, fancybox=True, ncol=3)
    legend.get_frame().set_facecolor('white')
    legend.get_frame().set_alpha(0.9)

    # Updated analysis text box
    analysis_text = (
        f"Analysis Overview:\n"
        f"• Duration: 42 weeks (Apr 15 - Jan 27, 2025)\n"
        f"• Starting Engagement: {metrics['seas_start']:.1f}%\n"
        f"• Average Natural Behaviour: {metrics['nat_mean_seas']:.1f}%\n"
        f"• Lowest Engagement: {metrics['min_seas']:.1f}% \n"
        f"• Final Stable Engagement: {metrics['final_stable_seas']:.1f}%\n"
        f"Note: Seasonal patterns observed during the analysis period."
    )
    analysis_box = plt.axes([0.08, 0.08, 0.4, 0.12])
    analysis_box.text(0.05, 0.5, analysis_text, fontsize=10, va='center', 
                      bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
    analysis_box.axis('off')

    # Adjust layout
    plt.subplots_adjust(top=0.90, right=0.95, bottom=0.25, left=0.08, hspace=0.3)
    plt.show()

def main():
    # Create data
    start_date = datetime(2024, 4, 15)
    dates = [start_date + timedelta(weeks=i) for i in range(42)]
    
    seasonality_data = {
        'week': [f'W{i}' for i in range(15, 57)],
        'date': dates,
        'seasonality': [
            28.76, 21.26, 15.81, 12.37, 9.58, 9.04, 6.61, 16.43, 11.40,
            7.45, 10.12, 11.65, 49.35, 59.45, 36.05, 26.28, 17.36, 11.30,
            13.39, 10.36, 15.33, 17.50, 22.19, 21.89, 22.50, 18.73, 23.31, 
            24.5108135942328,
22.1282051282051,
25.9514687100894,
26.0117078136931,
16.7174796747968,
11.9017472777918,
10.0884955752212,
8,
6.17160060210738,
7.46680030067652,
5.05885299273729,
9.51427140711067,
8.5127691537306,
6.97848924462231,
4.4216837371971,
        ]
    }
    
    seasonality_df = pd.DataFrame(seasonality_data)
    
    # Generate visualization
    plot_enhanced_analysis(seasonality_df)

if __name__ == "__main__":
    main()
