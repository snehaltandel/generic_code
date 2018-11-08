'''Window Function to calculate diff between 2 rows'''
select customer_id,current_total, previous_total,
       current_total - previous_total as diff
from (
  select customer_id,
         amount as current_total,
         lead(amount) over (partition by customer_id order by amount desc) as previous_total
  from payment
) total_diff
