-- 코드를 입력하세요


# SELECT DATE_FORMAT(onsale.sales_date, '%Y-%m-%d'), onsale.product_id, user_id, onsale.sales_amount
# FROM online_sale AS onsale
# WHERE DATE_FORMAT(sales_date, '%Y-%m') ='2022-03'

# UNION ALL

# SELECT DATE_FORMAT(offsale.sales_date, '%Y-%m-%d'), offsale.product_id, NULL AS user_id, offsale.sales_amount
# FROM offline_sale AS offsale
# WHERE DATE_FORMAT(sales_date, '%Y-%m') = '2022-03'

# ORDER BY 1, 2, 3



SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS SALES_DATE, product_id, user_id, sales_amount
FROM online_sale
WHERE sales_date BETWEEN '2022-03-01' AND '2022-03-31' 

UNION ALL 

SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS SALES_DATE, product_id, NULL AS user_id, sales_amount 
FROM offline_sale 
WHERE sales_date BETWEEN '2022-03-01' AND '2022-03-31'

ORDER BY 1, 2, 3