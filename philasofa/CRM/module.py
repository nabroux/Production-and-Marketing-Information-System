from .models import Customer,Order

def returnOrders_by_CustomerName(c_name):
    orders = Order.objects.all()
    res = []
    for order in orders:
        name = order.customer_name.customer_name
        if name == c_name:
            res.append(order)
    return res

def returnID_by_CustomerName(c_name):
    c_id = Customer.objects.filter(customer_name = c_name)
    return c_id

def getMonetary_by_ID(id):
    customerOrders = Order.objects.filter(customer_name = id)
    monetary = 0
    for customerOrder in customerOrders:
        product_price = customerOrder.product.selling_price
        quantity = customerOrder.quantity
        monetary += product_price * quantity
    return monetary

def getRFM_by_ID(id):
    orders = Order.objects.all()
    customerOrders = returnOrders_by_CustomerId(id,orders)
    frequency = len(customerOrders)
    monetary = getMonetary_by_ID(id)
    latest_year = 0
    for customerOrder in customerOrders:
        date = str(customerOrder.created_time).split('-')
        year = int(date[0])
        if year > latest_year:
            latest_year = year
    
    return calculate_RFM(latest_year,frequency,monetary)
    

def calculate_RFM(year,frequency,money):
    score = 0
    if year == 2016:
        score += 1
    elif year == 2017:
        score += 2
    elif year == 2018:
        score += 3
    elif year == 2019:
        score += 4
    
    score = score + frequency
    
    if money < 4000000 :
        score += 1
    elif money < 10000000 and money > 4000000 :
        score += 2
    elif money > 10000000 :
        score += 3
    
    return score


def returnOrders_by_Year(y):
    orders = Order.objects.all()
    res = []
    for order in orders:
        date = str(order.created_time).split("-")
        year = date[0]
        if year == str(y):
            res.append(order.customer_name.id)
    return res

# y = 2017 or 2018, order是全部訂單 ，可能要轉回list
def calculate_retentionrate(y):
    res0 = set(returnOrders_by_Year(y-1))
    res1 = set(returnOrders_by_Year(y))
    res2 = res0.intersection(res1)
    retentionrate = len(res2)/len(res0)
    return retentionrate

# y = 2017 or 2018, order是全部訂單
def calculate_surviverate(y):
    if y == 2017:
        surviverate = calculate_retentionrate(2017)
    elif y == 2018:
        surviverate = calculate_surviverate(2017)*calculate_retentionrate(2018)
    return surviverate

def returnOrders_by_CustomerId(c_id,orders):
    res = []
    for order in orders:
        customer_id = order.customer_name.id
        if customer_id == c_id:
            res.append(order)
    return res

def create_city_string():
    city = []
    res = ''
    customers = Customer.objects.all()
    for customer in customers:
        city.append(customer.city)
    cityset = set(city)
    for c in cityset:
        cityNumber = city.count(c)
        res += '{} , {}個 ｜'.format(c,cityNumber)
    return res 