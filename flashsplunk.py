def generate_query():
    print("Splunk Away !! New User\n")
    
    # Basic inputs
    index = input("Enter the index: ")
    sourcetype = input("Enter the sourcetype: ")
    keyword = input("Enter the keyword to search for (optional): ")
    
    # Time range
    earliest = input("Enter the earliest time (e.g., -24h, -7d, -1m): ")
    latest = input("Enter the latest time (e.g., now, -1h, -1d): ")
    
    # Advanced options
    advanced_option = input("Do you want to add advanced options? (yes/no): ").lower()
    query = f'index={index} sourcetype={sourcetype}'
    
    if keyword:
        query += f' "{keyword}"'
    
    query += f' earliest={earliest} latest={latest}'
    
    if advanced_option == 'yes':
        print("\nAdvanced Options:")
        
        # Field extraction
        fields = input("Enter fields to extract (comma-separated): ")
        if fields:
            query += f' | fields {fields}'
        
        # Statistics and aggregation
        stats_option = input("Do you want to add statistics or aggregation? (yes/no): ").lower()
        if stats_option == 'yes':
            stats_type = input("Enter stats type (count, avg, sum, etc.): ")
            stats_field = input(f"Enter field for {stats_type}: ")
            group_by = input("Enter field to group by (optional): ")
            
            if group_by:
                query += f' | stats {stats_type}({stats_field}) by {group_by}'
            else:
                query += f' | stats {stats_type}({stats_field})'
        
        # Timechart
        timechart_option = input("Do you want to add a timechart? (yes/no): ").lower()
        if timechart_option == 'yes':
            timechart_span = input("Enter time span (e.g., 1h, 1d): ")
            timechart_field = input("Enter field for timechart: ")
            timechart_stat = input("Enter statistic (count, avg, etc.): ")
            
            query += f' | timechart span={timechart_span} {timechart_stat}({timechart_field})'
        
        # Join
        join_option = input("Do you want to add a join? (yes/no): ").lower()
        if join_option == 'yes':
            join_index = input("Enter index for join: ")
            join_sourcetype = input("Enter sourcetype for join: ")
            join_field = input("Enter field to join on: ")
            
            query += f' | join type=inner {join_field} [ search index={join_index} sourcetype={join_sourcetype} ]'
        
        # Transaction
        transaction_option = input("Do you want to add a transaction? (yes/no): ").lower()
        if transaction_option == 'yes':
            start_with = input("Enter start condition: ")
            end_with = input("Enter end condition: ")
            transaction_field = input("Enter field to group by: ")
            
            query += f' | transaction startswith="{start_with}" endswith="{end_with}" by {transaction_field}'
    
    print("\nGenerated Splunk Query:")
    print(query)

if __name__ == "__main__":
    generate_query()
