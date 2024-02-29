few_shots = [
    {
    'Question' : "How many orders were placed on 14th August, 2006?",
    'SQLQuery' : "SELECT COUNT(*) as num_orders FROM SalesOrder WHERE DATE(orderDate) = '2006-08-14';",
    'SQLResult': "[(2,)]",
    'Answer' : "[(2,)]"
    },
    {
    'Question' : "Give me the products under Confections category.",
    'SQLQuery' : "SELECT productName FROM Product p JOIN Category c ON p.categoryId = c.categoryId WHERE categoryName = 'Confections';",
    'SQLResult': "[('Product PAFRH',), ('Product XKXDO',), ('Product QHFFP',), ('Product VJZZH',), ('Product LYLNI',), ('Product HLGZA',), ('Product SMIOH',), ('Product EZZPR',), ('Product MYNXN',), ('Product FPYPN',), ('Product BIUDV',), ('Product WUXYK',), ('Product TBTBL',)]",
    'Answer' : "[('Product PAFRH',), ('Product XKXDO',), ('Product QHFFP',), ('Product VJZZH',), ('Product LYLNI',), ('Product HLGZA',), ('Product SMIOH',), ('Product EZZPR',), ('Product MYNXN',), ('Product FPYPN',), ('Product BIUDV',), ('Product WUXYK',), ('Product TBTBL',)]"
    },
    {
    'Question' : "Give me the distribution of products across different categories.",
    'SQLQuery' : "SELECT c.categoryName, count(*) FROM Product p JOIN Category c GROUP BY c.categoryId;",
    'SQLResult': "[('Beverages', 12), ('Condiments', 12), ('Confections', 13), ('Dairy Products', 10), ('Grains/Cereals', 7), ('Meat/Poultry', 6), ('Produce', 5), ('Seafood', 12)]",
    'Answer' : "[('Beverages', 12), ('Condiments', 12), ('Confections', 13), ('Dairy Products', 10), ('Grains/Cereals', 7), ('Meat/Poultry', 6), ('Produce', 5), ('Seafood', 12)]"
    },    
]