from CRM.models import Product,Order

def getROP_by_ID(p_id):
    orders = Order.objects.all()
    p_orders = returnOrders_by_TypeId(p_id,orders)
    P_totalDemand = calculate_monthlyDemand(p_orders)
    ROP = P_totalDemand / 12 * (Product.objects.filter(id=p_id).first().order_time)
    return ROP

def create_ROP_string():
    res = '夢幻機 的 ROP 是 {}\n，高階機 的 ROP 是 {}，推薦機 的 ROP 是 {}，文書機 的 ROP 是 {}，電競機 的 ROP 是 {}'.format(int(getROP_by_ID(1)),int(getROP_by_ID(2)),int(getROP_by_ID(3)),int(getROP_by_ID(4)),int(getROP_by_ID(5)))
    return res

#參數為 某一特定品項的id 及 年需求
def getEOQ_by_ID(p_id):
    orders = Order.objects.all()
    p_orders = returnOrders_by_TypeId(p_id,orders)
    p_totalDemand = calculate_monthlyDemand(p_orders)
    p_orderCost = Product.objects.filter(id=p_id).first().order_cost
    p_holding_cost = Product.objects.filter(id=p_id).first().holding_cost
    EOQ = (2* p_totalDemand * p_orderCost / p_holding_cost)**(0.5)
    return EOQ

def create_EOQ_string():
    res = '夢幻機 的 EOQ 是 {}，高階機 的 EOQ 是 {}，推薦機 的 EOQ 是 {}，文書機 的 EOQ 是 {}，電競機 的 EOQ 是 {}'.format(int(getEOQ_by_ID(1)),int(getEOQ_by_ID(2)),int(getEOQ_by_ID(3)),int(getEOQ_by_ID(4)),int(getEOQ_by_ID(5)))
    return res

def get_demandList_by_ID(p_id):
    orders = Order.objects.all()
    p_orders = returnOrders_by_TypeId(p_id,orders)
    monthlyDemandList = []
    for m in range(1,13):
        m_p_orders = returnOrders_by_Month(m,p_orders)
        monthlyDemand = calculate_monthlyDemand(m_p_orders)
        monthlyDemandList.append(monthlyDemand)
    return monthlyDemandList

def create_monthlyDemandList_string():
    res = ''
    for product_id in range(1,6):
        res += '【ID 為 {} 的產品】：'.format(product_id)
        monthlyDemandList = get_demandList_by_ID(product_id)
        for i in range(1,13):
            res += '{}月的 預測需求 為 {}，'.format(i,int(monthlyDemandList[i-1]))
        res += '<br/><br/>'
    return res


#輸出為某一「特定品項」的某月平均需求，參數為 特定品項 特定月份 的query
def calculate_monthlyDemand(order_query):
    demand = 0 
    for order in order_query:
        demand = demand + order.quantity
    return demand / 3

#特定品項的一整年平均需求 為了算EOQ
def calculate_totalDemand(monthlyDemand):
    for demand in monthlyDemand:
        totalDemand = demand + totalDemand
    return totalDemand


def returnOrders_by_Month(m,orders):
    res = []
    for order in orders:
        date = str(order.created_time).split("-")
        month = date[1]
        if int(month) == m:
            res.append(order)
    return res

def returnOrders_by_TypeId(t,orders):
    res = []
    for order in orders:
        orderType = order.product.id
        if orderType == t:
            res.append(order)
    return res

def returnOrders_by_Year(y,orders):
    res = []
    for order in orders:
        date = order.created_time.split("-")
        year = date[0]
        if year == y:
            res.append(order.Customer.id)
    return res

def returnOrders_by_No(o_no):
    orders = Order.objects.filter(order_No=o_no)
    return orders