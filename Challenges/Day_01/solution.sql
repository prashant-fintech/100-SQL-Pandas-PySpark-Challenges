WITH product_sales AS (
    SELECT
        product_id,
        SUM(quantity) AS total_units_sold
    FROM marketing_campaign
    GROUP BY product_id
)
SELECT
    product_id,
    total_units_sold,
    CASE
        WHEN total_units_sold >= 30 THEN 'Outstanding'
        WHEN total_units_sold BETWEEN 20 AND 29 THEN 'Satisfactory'
        WHEN total_units_sold BETWEEN 10 AND 19 THEN 'Unsatisfactory'
        WHEN total_units_sold BETWEEN 1 AND 9 THEN 'Poor'
        ELSE 'No Sales'
    END AS ad_performance
FROM product_sales
ORDER BY total_units_sold DESC;
