import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# قراءة البيانات من ملف CSV
file_path = r'C:\\Users\\Hussein soft\\OneDrive\\Desktop\\main\\DatasetForCoffeeSales2.csv'
data = pd.read_csv(file_path)

# عرض أسماء الأعمدة للتحقق منها
print(data.columns)

# توزيع المبيعات حسب المدن
branch_sales_fig = px.bar(data, x='City', title='توزيع المبيعات حسب المدن')

# توزيع المبيعات حسب المنتجات
product_sales_fig = px.bar(data, x='Product', title='توزيع المبيعات حسب المنتجات')

# تحليل المبيعات الشهرية
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.to_period('M')
monthly_sales = data.groupby('Month').size().reset_index(name='Sales')
monthly_sales_fig = px.bar(monthly_sales, x='Month', y='Sales', title='تحليل المبيعات الشهرية')

# تحليل الإيرادات الشهرية
monthly_revenue = data.groupby('Month')['Sales Amount'].sum().reset_index()
monthly_revenue_fig = px.bar(monthly_revenue, x='Month', y='Sales Amount', title='تحليل الإيرادات الشهرية')

# تصميم لوحة التحكم
app.layout = html.Div(children=[
    html.H1(children='لوحة التحكم - حجز تذاكر الطيران'),

    html.Div(children='''
        تحليل البيانات وعرض الرسوم البيانية.
    '''),

    dcc.Graph(
        id='branch-sales-chart',
        figure=branch_sales_fig
    ),

    dcc.Graph(
        id='product-sales-chart',
        figure=product_sales_fig
    ),

    dcc.Graph(
        id='monthly-sales-chart',
        figure=monthly_sales_fig
    ),

    dcc.Graph(
        id='monthly-revenue-chart',
        figure=monthly_revenue_fig
    )
])

# تشغيل التطبيق
if __name__ == '__main__':
    app.run_server(debug=True)
